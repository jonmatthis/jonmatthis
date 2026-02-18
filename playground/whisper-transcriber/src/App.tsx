import { useCallback, useEffect, useRef, useState } from "react";
import { invoke } from "@tauri-apps/api/core";
import { listen } from "@tauri-apps/api/event";
import Editor from "@monaco-editor/react";
import Waveform from "./Waveform";
import "./App.css";

interface WaveformPayload {
  samples: number[];
}

interface TranscriptionPayload {
  text: string;
}

export default function App() {
  const [isRecording, setIsRecording] = useState(false);
  const [transcript, setTranscript] = useState("");
  const [waveformSamples, setWaveformSamples] = useState(
    new Float32Array(0)
  );
  const [status, setStatus] = useState("Ready — click Record to begin");
  const editorRef = useRef<ReturnType<
    NonNullable<Parameters<typeof Editor>[0]["onMount"]>
  > | null>(null);

  const handleEditorMount = useCallback(
    (editor: Parameters<NonNullable<Parameters<typeof Editor>[0]["onMount"]>>[0]) => {
      editorRef.current = editor as typeof editorRef.current;
    },
    []
  );

  // Listen for transcription results from the Rust backend
  useEffect(() => {
    const unlistenTranscription = listen<TranscriptionPayload>(
      "transcription-result",
      (event) => {
        setTranscript((prev) => {
          const separator = prev.length > 0 ? " " : "";
          return prev + separator + event.payload.text;
        });
      }
    );

    const unlistenWaveform = listen<WaveformPayload>(
      "audio-waveform",
      (event) => {
        setWaveformSamples(new Float32Array(event.payload.samples));
      }
    );

    return () => {
      unlistenTranscription.then((fn) => fn());
      unlistenWaveform.then((fn) => fn());
    };
  }, []);

  // Scroll editor to bottom when transcript updates
  useEffect(() => {
    if (editorRef.current) {
      const model = editorRef.current.getModel();
      if (model) {
        const lineCount = model.getLineCount();
        editorRef.current.revealLine(lineCount);
      }
    }
  }, [transcript]);

  const toggleRecording = async () => {
    if (isRecording) {
      await invoke("stop_listening");
      setIsRecording(false);
      setStatus("Stopped");
      setWaveformSamples(new Float32Array(0));
    } else {
      setStatus("Loading whisper model & starting mic...");
      setIsRecording(true);
      try {
        await invoke("start_listening");
        setStatus("Recording — speak into your microphone");
      } catch (err) {
        setIsRecording(false);
        setStatus(`Error: ${err}`);
        throw new Error(`Failed to start listening: ${err}`);
      }
    }
  };

  const clearTranscript = () => {
    setTranscript("");
  };

  return (
    <div className="app-container">
      <header className="app-header">
        <div className="title-group">
          <h1 className="app-title">whisper<span className="accent">scribe</span></h1>
          <span className="subtitle">local speech-to-text</span>
        </div>
        <div className="controls">
          <button
            className={`btn-record ${isRecording ? "recording" : ""}`}
            onClick={toggleRecording}
          >
            <span className="record-dot" />
            {isRecording ? "Stop" : "Record"}
          </button>
          <button className="btn-clear" onClick={clearTranscript}>
            Clear
          </button>
        </div>
      </header>

      <div className="status-bar">
        <span className={`status-indicator ${isRecording ? "active" : ""}`} />
        <span className="status-text">{status}</span>
      </div>

      <section className="waveform-section">
        <Waveform samples={waveformSamples} isRecording={isRecording} />
      </section>

      <section className="editor-section">
        <Editor
          height="100%"
          defaultLanguage="plaintext"
          theme="vs-dark"
          value={transcript}
          onChange={(value) => setTranscript(value ?? "")}
          onMount={handleEditorMount}
          options={{
            fontSize: 15,
            lineHeight: 24,
            fontFamily: "'IBM Plex Mono', 'Fira Code', monospace",
            wordWrap: "on",
            minimap: { enabled: false },
            lineNumbers: "off",
            glyphMargin: false,
            folding: false,
            scrollBeyondLastLine: false,
            renderLineHighlight: "none",
            overviewRulerBorder: false,
            hideCursorInOverviewRuler: true,
            padding: { top: 16, bottom: 16 },
            scrollbar: {
              verticalScrollbarSize: 6,
              horizontalScrollbarSize: 6,
            },
          }}
        />
      </section>
    </div>
  );
}
