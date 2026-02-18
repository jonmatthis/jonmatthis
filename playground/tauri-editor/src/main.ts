import * as monaco from "monaco-editor";
import editorWorker from "monaco-editor/esm/vs/editor/editor.worker?worker";
import { invoke } from "@tauri-apps/api/core";
import { open } from "@tauri-apps/plugin-dialog";

// Monaco worker setup
self.MonacoEnvironment = {
  getWorker(): Worker {
    return new editorWorker();
  },
};

interface FileEntry {
  name: string;
  path: string;
  is_dir: boolean;
}

let editor: monaco.editor.IStandaloneCodeEditor | null = null;
let currentDirectory: string | null = null;

function initEditor(): void {
  const container = document.getElementById("editor-container");
  if (!container) {
    throw new Error("Editor container not found");
  }

  editor = monaco.editor.create(container, {
    value: "// Select a file to view its contents",
    language: "plaintext",
    theme: "vs-dark",
    automaticLayout: true,
    readOnly: false,
    minimap: { enabled: true },
    fontSize: 14,
    lineNumbers: "on",
    wordWrap: "on",
  });
}

async function listDirectory(path: string): Promise<FileEntry[]> {
  const entries = await invoke<FileEntry[]>("list_directory", { path });
  return entries;
}

async function readFile(path: string): Promise<string> {
  const content = await invoke<string>("read_file", { path });
  return content;
}

function renderFileList(entries: FileEntry[]): void {
  const fileList = document.getElementById("file-list");
  if (!fileList) {
    throw new Error("File list container not found");
  }

  fileList.innerHTML = "";

  // Sort: directories first, then files, both alphabetically
  const sorted = [...entries].sort((a, b) => {
    if (a.is_dir && !b.is_dir) return -1;
    if (!a.is_dir && b.is_dir) return 1;
    return a.name.localeCompare(b.name);
  });

  for (const entry of sorted) {
    const div = document.createElement("div");
    div.className = `file-item ${entry.is_dir ? "directory" : "file"}`;
    div.textContent = `${entry.is_dir ? "📁" : "📄"} ${entry.name}`;

    div.addEventListener("click", () => {
      void handleFileClick(entry, div);
    });

    fileList.appendChild(div);
  }
}

async function handleFileClick(entry: FileEntry, element: HTMLElement): Promise<void> {
  if (entry.is_dir) {
    currentDirectory = entry.path;
    updateCurrentPath(entry.path);
    const entries = await listDirectory(entry.path);
    renderFileList(entries);
  } else {
    // Remove selection from all items
    document.querySelectorAll(".file-item").forEach((el) => {
      el.classList.remove("selected");
    });
    element.classList.add("selected");

    const content = await readFile(entry.path);
    if (!editor) {
      throw new Error("Editor not initialized");
    }

    editor.setValue(content);

    // Detect language from extension
    const ext = entry.name.split(".").pop()?.toLowerCase() ?? "";
    const languageMap: Record<string, string> = {
      ts: "typescript",
      tsx: "typescript",
      js: "javascript",
      jsx: "javascript",
      json: "json",
      html: "html",
      css: "css",
      md: "markdown",
      py: "python",
      rs: "rust",
      go: "go",
      java: "java",
      c: "c",
      cpp: "cpp",
      h: "c",
      hpp: "cpp",
      sh: "shell",
      bash: "shell",
      yml: "yaml",
      yaml: "yaml",
      xml: "xml",
      sql: "sql",
      toml: "toml",
    };

    const language = languageMap[ext] ?? "plaintext";
    monaco.editor.setModelLanguage(editor.getModel()!, language);

    updateEditorHeader(entry.path);
  }
}

function updateCurrentPath(path: string): void {
  const pathElement = document.getElementById("current-path");
  if (!pathElement) {
    throw new Error("Current path element not found");
  }
  pathElement.textContent = path;
}

function updateEditorHeader(path: string): void {
  const headerElement = document.getElementById("editor-header");
  if (!headerElement) {
    throw new Error("Editor header element not found");
  }
  headerElement.textContent = path;
}

async function openFolderDialog(): Promise<void> {
  const selected = await open({
    directory: true,
    multiple: false,
    title: "Select a folder to open",
  });

  if (selected && typeof selected === "string") {
    currentDirectory = selected;
    updateCurrentPath(selected);
    const entries = await listDirectory(selected);
    renderFileList(entries);
  }
}

function init(): void {
  initEditor();

  const openFolderBtn = document.getElementById("open-folder-btn");
  if (!openFolderBtn) {
    throw new Error("Open folder button not found");
  }

  openFolderBtn.addEventListener("click", () => {
    void openFolderDialog();
  });
}

document.addEventListener("DOMContentLoaded", init);
