# Skelly Soul Docs — Knowledge Extraction Strategy

> **Status:** Design document — not yet implemented
> **Date:** 2026-05-25
> **Purpose:** Define the end-to-end strategy for extracting the philosophy, morality, and conceptual foundations of the FreeMoCap project from years of lecture transcripts, livestreams, and talks, and organizing them into a multi-format, multi-audience knowledge system.

---

## Table of Contents

1. [Context & Purpose](#1-context--purpose)
2. [Current State Audit](#2-current-state-audit)
3. [Research Foundation](#3-research-foundation)
4. [Design Principles](#4-design-principles)
5. [Formal Provenance Model](#5-formal-provenance-model)
6. [Three-Phase Architecture](#6-three-phase-architecture)
7. [Phase 1: Linear Temporal Cleanup](#7-phase-1-linear-temporal-cleanup)
8. [Phase 2: Knowledge Graph Construction](#8-phase-2-knowledge-graph-construction)
9. [Phase 3: Progressive Summarization & Rendered Outputs](#9-phase-3-progressive-summarization--rendered-outputs)
10. [Ontology Design](#10-ontology-design)
11. [Directory Structure & Obsidian Compatibility](#11-directory-structure--obsidian-compatibility)
12. [Anti-Patterns & Guardrails](#12-anti-patterns--guardrails)
13. [Gap Analysis: Missing Sources](#13-gap-analysis-missing-sources)
14. [Implementation Sequence](#14-implementation-sequence)
15. [References](#15-references)

---

## 1. Context & Purpose

### What This Is

This repository is the "soul documentation" for the FreeMoCap project — a structured, multi-layered knowledge system that captures the philosophy, morality, history, motivation, and broader implications of FreeMoCap. The project mascot/logo is Skelly, hence "Skelly Soul Docs."

### What This Is Not

- This is **not** technical documentation for the FreeMoCap software (that lives elsewhere).
- This is **not** a personal brand exercise or a "Jon Matthis show." The focus is on the ideas, the project, and the philosophy — not the individual.
- This is **not** a one-shot document. It is a living knowledge system designed to grow as new content is added.

### Source Material

The raw material consists of ~30 transcripts (and growing) drawn from:

- **HMN Course Lectures** (Fall 2024, Spring 2025): Undergraduate/graduate neuroscience of human movement courses at Northeastern University. These lectures weave together neuroscience, philosophy of science, institutional critique, and FreeMoCap tooling.
- **FreeMoCap Livestreams** (2024–2025): Informal technical streams covering SkellyCam architecture, pipeline planning, project governance, and development philosophy.
- **Podcasts & Talks** (forthcoming): External interviews and presentations about FreeMoCap (BOOM Podcast, VFX Futures, etc.).
- **Additional recordings**: OBS dev sessions, lab recordings, state-of-the-project addresses.

### Target Audiences

The content should serve multiple audiences, with the design principle that **anyone can jump in at any point and navigate**:

| Audience | Needs |
|----------|-------|
| General public | Understand what FreeMoCap is, why it exists, and why its philosophy matters — no prior context required |
| Students / learners | Conceptual scaffolding; accessible explanations of the philosophy, science, and their intersection |
| FreeMoCap devs & users | Deeper context on design decisions, project values, and community norms |
| Peers & collaborators | Academic/philosophical grounding; the intellectual lineage of the project's ideas |

### Output Surfaces

The knowledge system should render to multiple formats from a single source of truth:

1. **Obsidian vault** (primary): Markdown files with YAML frontmatter, `[[wikilinks]]`, and tags — browsable with Obsidian's graph view and backlinks panel.
2. **LLM-queryable corpus**: Clean, condensed, well-structured text that can be loaded into an LLM context window for conversational Q&A.
3. **Structured documentation**: Potentially a "philosophical documentation" document or series — readable linearly but composed of self-contained sections.
4. **Knowledge graph visualization**: A browsable graph of concepts, claims, and their relationships.

---

## 2. Current State Audit

### Transcript Inventory

**Total: 30 transcripts, ~2.1 MB of markdown**

#### HMN Course Lectures — Fall 2024 (10 transcripts)

| # | File | Est. Duration | Size |
|---|------|--------------|------|
| 00 | `2024-09-25-HMN24 - 00 - Intro to class` | ~58 min | 50 KB |
| 01 | `2024-09-25-HMN24 - 01 - Intro to Data Collection` | ~60 min | 56 KB |
| 03 | `2024-10-11-HMN24 - 03 - Intro to Balance` | ~65 min | 61 KB |
| 04 | `2024-10-29-HMN24 - 04 - Intro to the Neuro Motor Hierarchy` | ~70 min | 69 KB |
| 05 | `2024-10-29-HMN24 - 05 - Intro to Eye Tracking` | ~55 min | 50 KB |
| 06 | `2024-11-12-HMN24 - 06 - Intro to Eyeballs` | ~75 min | 70 KB |
| 07 | `2024-11-19-HMN24 - 07 - Human Movement Neuroscience (from scratch)` | ~85 min | 82 KB |
| 08 | `2024-11-23-[HMN24#08] Intro to My Dumb BS` | ~85 min | 83 KB |
| 09 | `2024-12-01-[HMN24#09] Prediction, Trauma, and ANS` | ~90 min | 92 KB |
| 10 | `2024-12-20-[HMN24 #10] Outro and final class report` | ~55 min | 50 KB |

#### HMN Course Lectures — Spring 2025 (10 transcripts)

| # | File | Est. Duration | Size |
|---|------|--------------|------|
| 01 | `2025-01-16-HMN25 - 01 - Human Perceptuomotor Neuroscience Overview` | ~80 min | 76 KB |
| 02 | `2025-02-03-HMN25-02 - SI Units, Space and Empirical Measurement` | ~85 min | 80 KB |
| 03 | `2025-02-03-HMN25-03 - FreeMoCap Data Collection` | ~65 min | 64 KB |
| 04 | `2025-02-06-HMN25-04 - Epistemology, postural control, and FreeMoCap data analysis` | ~80 min | 78 KB |
| 05 | `2025-02-12-HMN25-05 - State spaces, phasic jumping, and FreeMoCap data analysis` | ~80 min | 79 KB |
| 06 | `2025-02-13-HMN25-06 - Scientific Posters and Spinal CPGs` | ~80 min | 80 KB |
| — | `2025-03-10-2025 02 24 14 59_transcript` | ~91 min | 74 KB |
| — | `2025-08-06-2025 03 10 15 02_transcript` | ~75 min | 72 KB |
| — | `2025-08-06-2025 03 17 15 01_transcript` | ~78 min | 76 KB |
| — | `2025-08-06-2025 03 19 14 57_transcript` | ~75 min | 72 KB |
| — | `2025-08-06-2025 03 26 15 04_transcript` | ~78 min | 73 KB |

#### FreeMoCap Livestreams (10 transcripts)

| Date | Topic | Est. Duration | Size |
|------|-------|--------------|------|
| 2024-03-08 | FreeMoCap Pipeline Planning - 0 | ~40 min | 37 KB |
| 2024-03-09 | FreeMoCap Pipeline Planning - 1 | ~60 min | 57 KB |
| 2024-03-12 | FreeMoCap PR Reviews (#562, #552, #536) | ~80 min | 77 KB |
| 2024-03-14 | SkellyCam - bot-made ReactJS camera grid | ~6 min | 6 KB |
| 2024-05-10 | SkellyCam Interim Update | ~35 min | 32 KB |
| 2024-05-23 | In-lab recording - Working on TTS (time-to-skeleton) | ~45 min | 44 KB |
| 2024-08-01 | Blender ferret skull w/ eyes | ~7 min | 6 KB |
| 2024-08-09 | FreeMoCap Architecture Planning | ~25 min | 24 KB |
| 2025-08-08 | Project check-in, Treadmill data, SkellyCam 2.0 updates | ~140 min | 133 KB |
| 2025-08-15 | SkellyCam 2.0 Deep Dive | ~189 min | 150 KB |

### Quality Assessment

**What's working:**
- Timestamps are consistent in `[HH:MM:SS]` format
- 10-minute chunking is uniform across all transcripts
- Source metadata (type, path, URL, video ID) is well-tracked in headers
- Total duration is recorded for each transcript

**Issues identified:**
- **Transcripts are raw verbatim.** They preserve ums, ahs, false starts, self-corrections, and informal speech patterns. This is good for provenance but bad for readability and extraction quality.
- **Filename inconsistency in Spring 2025.** Four files use bare timestamp names (e.g., `2025-03-10-2025 02 24 14 59_transcript_w_timestamps.md`) instead of descriptive lecture titles. This appears to be the timestamp naming bug — the video_eater used the file modification time rather than the lecture date/topic.
- **No speaker diarization.** Single-speaker content (these are mostly monologues), so this is not a major issue, but Q&A segments with students are not labeled.
- **Chunk boundaries sometimes cut mid-sentence.** The 10-minute fixed chunking can split a thought across chunk boundaries.

### Existing PDFs (Prior Attempt)

Four PDFs exist in `freemocap-history-manifesto-and-sources/` from a previous AI-assisted synthesis attempt:

| Volume | Title | Size |
|--------|-------|------|
| Vol 0 | Origin Story | 136 KB |
| Vol 1 | The Manifesto | 134 KB |
| Vol 2 | Theoretical Foundations | 204 KB |
| Vol 3 | Source Documents | 756 KB |

**Assessment:** These were generated by an earlier, less capable AI system. The user has noted they may be "too formalized" and may suffer from tone issues (overly hero-worship-y or self-aggrandizing). They should be treated as reference material — potentially useful for cross-referencing claims — but not as authoritative starting points. The current effort should build from the raw transcripts, not from these PDFs.

---

## 3. Research Foundation

This strategy draws on several active research areas. What follows is a survey of the relevant literature and tools that inform our approach, organized by which phase of the pipeline they influence.

### 3.1 Knowledge Graph Extraction from Transcripts

The dominant trend in 2024–2025 is the shift from traditional NLP pipelines (NER → Entity Linking → Relation Extraction) to **LLM-based end-to-end extraction**. Large language models can now perform triple extraction from raw text with no training data.

**CLARE (Context-Aware, Interactive Knowledge Graph Construction from Transcripts)** — Koschmieder et al., MDPI Information, October 2025 — is the most directly relevant system. CLARE achieves **82.1% mean fact accuracy** on the MINE benchmark, compared to KGGen's 64.8% and GraphRAG's 48.3%. Its key innovations are:
- Tight coupling of transcript editing and live KG regeneration (correct a transcript, the graph updates)
- Human-in-the-loop refinement that improves accuracy by +22.7% on average
- Support for 150+ LLMs with local/private deployment options
- Visual knowledge graph editor

*Relevance to our work:* CLARE validates the overall approach of transcript → extract → graph. Its finding that human review adds ~23% accuracy is the justification for our Phase 1 human review step. Its entity merging approach (dedicated LLM pass for disambiguation) directly informs our ontology design.

**KGGen** (Python package, `pip install kg-gen`) — a simpler, library-based approach with a three-stage pipeline: Extract → Aggregate → Iterative Clustering. It uses GPT-4o or compatible LLMs and introduces the MINE benchmark for graph quality evaluation. Its entity consolidation via clustering is a lighter-weight alternative to CLARE's interactive approach.

*Relevance to our work:* KGGen's clustering-based entity consolidation is well-suited to an automated Phase 2 pipeline where we're processing ~30 transcripts and need to merge duplicate concepts across them.

### 3.2 Scalable LLM Document Processing

**ScaleDoc** (Tsinghua University, September 2025) addresses the cost problem of running LLM predicates over large document collections. It uses a proxy/oracle cascade: an offline phase generates embeddings, and an online phase trains a lightweight proxy model that filters high-confidence documents locally, sending only ambiguous cases to the expensive oracle LLM. Results: **2× speedup, up to 85% reduction in expensive LLM invocations.**

**DocETL** (Stanford/UC Berkeley, 2025) applies database query optimization principles to LLM-powered semantic operators (map, filter, reduce, resolve) over unstructured document collections. Its Monte Carlo Tree Search optimizer finds Pareto-optimal plans on the accuracy–cost frontier, achieving **86% cost reduction** while maintaining target accuracy.

*Relevance to our work:* While our corpus (~2 MB) is small enough that cost optimization is not the primary concern, the architectural pattern of "cheap first pass → expensive refinement" is directly applicable. In Phase 1, we can do a fast cleanup pass and then selectively apply deeper extraction only to content rich in philosophical claims.

### 3.3 Hallucination Reduction & Grounding

**SafePassage** (October 2025) introduces the concept of a "safe passage" — LLM-generated content that is both grounded in the source document and consistent with extracted information. Its three-step pipeline (extract → align → flag) reduces hallucinations by **up to 85%**.

**FAIR to WISE (F2W)** (Lawrence Berkeley National Lab, December 2025) converts unstructured PDFs into structured, queryable knowledge graphs with full provenance capture. It grounds responses in extracted evidence and enforces schema constraints, reducing hallucination risk.

*Relevance to our work:* The grounding strategy is critical for our use case. Every extracted claim must be traceable back to its source transcript and timestamp. This is both a quality mechanism (prevents drift) and a trust mechanism (readers can verify). We adopt F2W's approach of schema-constrained extraction with provenance chains.

### 3.4 Temporal Knowledge Graphs

**Graphiti** (open-source Python library, 2025) builds temporal knowledge graphs with bi-temporal modeling — tracking both when something was said (transaction time) and when it was about (valid time). It supports both sequential processing (with edge invalidation for evolving knowledge) and bulk processing (for batch ingestion). Its podcast processing example is the closest analog to our use case.

*Relevance to our work:* Graphiti's temporal modeling directly supports our goal of preserving the evolution of ideas over time. A concept introduced in Fall 2024 might be refined, contradicted, or deepened in Spring 2025. The graph should capture this trajectory, not flatten it into a single static claim.

### 3.5 Progressive Summarization & Personal Knowledge Management

**Progressive Summarization** (Tiago Forte, *Building a Second Brain*, 2022) is a technique for processing notes in layers of increasing compression:

- **Layer 1:** The original captured text
- **Layer 2:** Bolded passages (the most important parts)
- **Layer 3:** Highlighted passages (the "best of the best")
- **Layer 4:** Executive summary (restated in your own words)
- **Layer 5:** Remix/creation (original output drawing on the source)

*Relevance to our work:* This layered approach is the model for our Phase 3. Each transcript produces a stack of progressively compressed artifacts, and cross-transcript synthesis pages draw from the higher (more compressed) layers. This is also the approach most naturally compatible with Obsidian's linking model.

**Zettelkasten Method** (Niklas Luhmann, elaborated by Sönke Ahrens in *How to Take Smart Notes*, 2017) is the practice of creating atomic, densely linked notes where each note contains one idea, written in your own words, and connected to other notes via explicit links. This is the intellectual ancestor of Obsidian's `[[wikilink]]` model.

*Relevance to our work:* Our knowledge graph's "proposition" nodes are essentially Zettelkasten notes — atomic claims, densely linked. The principle of writing each note as if it will be read in isolation ("jump in anywhere") comes directly from Zettelkasten practice.

### 3.6 Obsidian as a Knowledge Graph Platform

Obsidian's particular strengths that make it our target platform:

- **YAML frontmatter** for structured metadata on every note
- **`[[wikilinks]]`** for bidirectional linking between notes
- **Tags** (`#tag`) and nested tags (`#philosophy/open-source`) for categorization
- **Graph view** that visualizes the link structure as a force-directed graph
- **Backlinks panel** that shows all notes linking to the current note
- **Dataview plugin** that allows querying notes by their frontmatter fields
- **Plain markdown files on disk** — no proprietary format, fully git-friendly

---

### 3.7 Grounded Theory & Qualitative Coding Methodology

While Sections 3.1–3.6 cover the computational/technical side of extraction, there is an equally important academic tradition from the social sciences: **qualitative research methodology** for systematically extracting themes, concepts, and theories from interview or transcript data. This tradition — spanning grounded theory, thematic analysis, and qualitative coding — provides the intellectual backbone for the *interpretive* aspects of our pipeline that pure computation cannot replace.

#### Grounded Theory (Glaser & Strauss, 1967; Charmaz, 2006)

Grounded theory is an **inductive, data-driven methodology** in which theory is built "from the ground up" — meaning directly from the data rather than from pre-existing hypotheses. It originated in sociology (Glaser & Strauss, *The Discovery of Grounded Theory*, 1967) and was later developed into a constructivist form by Kathy Charmaz (*Constructing Grounded Theory*, 2006).

The core commitment of grounded theory is that **the data speaks first**. The researcher approaches the material without predetermined categories, allowing patterns to emerge through systematic engagement with the text. This aligns directly with our goal: we are not imposing a pre-built ontology onto the transcripts, but letting the philosophical positions emerge from what was actually said.

#### The Three-Stage Coding Process

Grounded theory and its methodological cousins (thematic analysis, qualitative content analysis) share a staged approach to extracting meaning from unstructured text. This maps surprisingly well onto our three-phase pipeline:

| Qualitative Research Stage | Our Pipeline Equivalent |
|---|---|
| **Open Coding** — line-by-line assignment of descriptive codes, constant comparison, memoing | **Phase 1 cleanup + first-pass tagging** — reading each transcript, assigning initial theme tags, writing notes on emerging patterns |
| **Axial/Focused Coding** — grouping codes into categories, specifying properties and dimensions, identifying relationships between categories | **Phase 2 knowledge graph construction** — extracting atomic propositions, disambiguating entities, defining typed relationships between claims |
| **Theoretical Coding** — relating core categories to each other, developing theoretical concepts, forming propositions | **Phase 3 synthesis** — cross-transcript synthesis pages, progressive summarization, narrative construction |

This is not a coincidence. The intellectual challenge of "what does this person actually believe, based on what they've said across many hours of spoken material?" is the same challenge that grounded theory was designed to address. Our pipeline is essentially a **computationally-assisted grounded theory analysis** — the LLM accelerates the coding and pattern-recognition, but the methodological rigor (constant comparison, saturation checking, audit trails) comes from the qualitative research tradition.

#### The Codebook

A **codebook** is a structured guide containing each code's name, definition, inclusion/exclusion criteria, and example quotes from the raw data (Saldaña, *The Coding Manual for Qualitative Researchers*, 2016). In our pipeline, the codebook is the combination of:
- The **tag taxonomy** (Phase 1) — the hierarchical tag system applied to transcripts
- The **ontology** (Section 10) — the formal definition of entity types, edge types, and their properties
- The **entity registry** (Phase 2 output) — canonical entities with aliases and linked propositions

The codebook serves as the **audit trail** — the documented record of analytical decisions that makes the extraction process transparent and reviewable. In traditional qualitative research, the codebook is what allows another researcher to understand (and potentially replicate) the coding decisions. In our pipeline, it serves the same function — and additionally allows the knowledge graph to be updated consistently when new transcripts are added.

#### Saturation

**Saturation** is the point at which new data no longer yields new codes or insights (Guest, MacQueen & Namey, *Applied Thematic Analysis*, 2012). In interview-based research, you stop collecting data when saturation is reached. In our context, saturation is a signal about the maturity of the knowledge graph:
- If a new transcript generates primarily links to existing propositions (rather than new propositions), the philosophical landscape is well-mapped
- If a new transcript generates many novel propositions, there are still unexplored areas

This is a useful heuristic for Phase 2 — it tells us when the extraction is "complete enough" and when we need to seek out missing perspectives.

#### Constant Comparison & Memoing

Two practices from grounded theory that directly inform our process:

- **Constant comparison:** Continuously compare data-to-data, data-to-code, code-to-category throughout analysis. In our pipeline, this is operationalized as: every new extracted proposition is compared against existing propositions for redundancy, contradiction, or refinement potential.
- **Memoing:** Write theoretical memos throughout the process to capture emerging thoughts, connections, and ideas. In our pipeline, this translates to maintaining a running `OBSERVATIONS.md` log during Phase 1 and 2 — notes about surprising patterns, emerging themes, and methodological decisions.

#### Key References

- Glaser, B.G. & Strauss, A.L. (1967). *The Discovery of Grounded Theory.* Aldine.
- Charmaz, K. (2006/2014). *Constructing Grounded Theory: A Practical Guide Through Qualitative Analysis.* Sage.
- Saldaña, J. (2016). *The Coding Manual for Qualitative Researchers.* Sage.
- Braun, V. & Clarke, V. (2006). "Using thematic analysis in psychology." *Qualitative Research in Psychology*, 3(2), 77–101.
- Guest, G., MacQueen, K.M. & Namey, E.E. (2012). *Applied Thematic Analysis.* Sage.

### 3.8 Digital Humanities Provenance & Intellectual History Methods

A third academic tradition informs our work: **digital humanities (DH) provenance modeling** and the methods of **intellectual history** for tracing how ideas move, transform, and relate across a corpus.

#### Formal Provenance Modeling: CIDOC-CRM & CorpusTracer

The **CIDOC Conceptual Reference Model (CIDOC-CRM)** is an ISO standard (ISO 21127:2014) ontology developed by the museum and cultural heritage community for modeling events, actors, objects, and their relationships through time. Its extension **FRBRoo** (now **LRMoo**) models the bibliographic dimension — works, expressions, manifestations, and items — making it suitable for tracking how texts derive from, translate, comment on, and annotate each other.

The **CorpusTracer** project at the Max Planck Institute for the History of Science (MPIWG Berlin) applied CIDOC-CRM + FRBRoo to model the genealogy of Johannes de Sacrobosco's *Tractatus de Sphaera* — a 13th-century cosmology textbook used in European universities for over 400 years across 300+ printed editions. Their approach:
- Models text derivations, translations, commentaries, and annotations as formal RDF relationships
- Stores data as Linked Open Data in a Blazegraph triple store
- Supports SPARQL queries for tracing knowledge innovations through editorial history
- Links to external authority data (Wikidata, CERL thesaurus)

*Relevance to our work:* While our corpus is smaller and more recent, the same formal modeling approach applies. A lecture from Fall 2024 introduces a concept; a Spring 2025 lecture refines it; a livestream applies it to a technical decision. These are genealogical relationships between textual "expressions" that can be formally modeled — and CIDOC-CRM provides the vocabulary for doing so.

#### Intertextuality Classification

The 2024 DH paper "Mining Asymmetric Intertextuality" (Li et al.) formalizes a taxonomy of intertextual relationships that maps directly onto our edge types:

| Intertextual Type | Description | Our Edge Type |
|---|---|---|
| **Direct Quotation** | Verbatim reuse with markers | (Captured in proposition provenance as `quote` field) |
| **Indirect Quotation** | Paraphrased content from a source | `refines` — same idea, different words |
| **Background Citation** | Citing for context | `contextualizes` |
| **Thematic Borrowing** | Ideas transcending specific formulations | `derives_from` |

#### Semantic Provenance with Sentence Embeddings

Lucian Li's 2024 work "Tracing the Genealogies of Ideas with Sentence Embeddings" used sentence-level embeddings (SBERT) to index and search a 250,000-text 19th-century nonfiction corpus for idea tracing. The key insight: **paraphrased ideas can be detected through semantic similarity even when they share no vocabulary.** This is particularly relevant for our corpus, where the same philosophical position might be expressed very differently in a formal lecture vs. an informal livestream.

*Relevance to our work:* During Phase 2 entity disambiguation, sentence embeddings provide a computational check on the LLM-based merging — two propositions that the LLM didn't flag as related might show high cosine similarity and warrant human review.

#### Span-Level Edit Tracking

Guo & Wei (2026) argue that typical text processing pipelines silently overwrite intermediate editorial decisions, obscuring how textual transformations affect interpretation. Their provenance schema tracks:
- **Span-level edits** (character offsets into base text)
- **Edit type** (substitution, split, merge)
- **Correction source** (rule-based, model-assisted, human)
- **Confidence scores**
- **Review status**

*Relevance to our work:* This is the formal justification for our "provenance all the way down" principle. When Phase 1 cleans a transcript (removing filler words, converting spoken to written grammar), those edits must be traceable. A reader should be able to ask: "Was this claim present in the original spoken words, or did the cleanup process introduce it?"

#### Key References

- CIDOC-CRM: ISO 21127:2014. [cidoc-crm.org](https://cidoc-crm.org)
- CorpusTracer: MPIWG Berlin. [DH2018 presentation](https://dh2018.adho.org/en/digital-modelling-of-knowledge-innovations-in-sacroboscos-sphere/)
- Li, L. (2024). "Tracing the Genealogies of Ideas with Sentence Embeddings." [Semantic Scholar](https://www.semanticscholar.org/paper/Tracing-the-Genealogies-of-Ideas-with-Sentence-Li/433d34e9bcdeadf13bf26177a114326516d567cd)
- Li et al. (2024). "Mining Asymmetric Intertextuality." [ar5iv](https://ar5iv.labs.arxiv.org/html/2410.15145)
- Guo & Wei (2026). "From OCR to Analysis: Tracking Correction Provenance in Digital Humanities Pipelines." [arXiv](https://arxiv.org/html/2603.00884v4)

---

## 4. Design Principles

These principles guide every decision in the pipeline. They are ordered by priority.

### P1: Ideas Are First-Class Objects

The knowledge graph's nodes are **concepts, claims, and questions** — not people. A statement like "open source science is what academia pretends to be" becomes a `Claim` node about the relationship between `open_source` and `academic_science`. The fact that Jon said it in HMN24 Lecture 00 at timestamp `[00:13:14]` is provenance metadata on the edge, not the identity of the node.

This is the structural answer to the "personality cult" problem. When the graph is browsed, you see webs of ideas. When you drill into a specific claim, you see its source — but the claim's identity and relationships are about the idea, not the speaker.

### P2: Jump-In-Anywhere Coherence

Every page, whether a raw transcript chunk or a high-level synthesis, should be readable on its own. This means:
- No unexplained jargon (or jargon is linked to its definition)
- Context is provided inline or linked
- A reader who arrives via search or a random link can orient themselves

This is the Zettelkasten principle: write each note as if it will be read in isolation.

### P3: Provenance All the Way Down

Every extracted claim, summary, and synthesis links back to its source. The chain looks like:

```
Synthesis page
  → links to Claim nodes
    → links to Cleaned transcript chunks
      → links to Raw transcript with timestamp
```

This is adapted from F2W's provenance model and SafePassage's grounding approach. It means:
- A reader can always verify "where did this come from?"
- If a transcript turns out to have an error, we can trace which claims it affects
- The LLM extraction step can be audited for hallucination

### P4: Temporal Spine

Ideas evolve. The pipeline processes transcripts in chronological order, and the knowledge graph captures when claims were introduced, refined, or contradicted. This is adapted from Graphiti's bi-temporal model.

A `Claim` node might have edges like:
- `introduced_in` → `2024-09-25-HMN24-00` (timestamp `[00:13:14]`)
- `refined_in` → `2025-02-06-HMN25-04` (timestamp `[00:25:30]`)
- `contrasted_with` → another `Claim` node

This temporal dimension is valuable both for understanding the evolution of the project's thinking and for the historical record.

### P5: Multi-Audience, Single Source

Rather than maintaining separate versions for different audiences, we build one knowledge graph and render different "views" of it. A general-public view might show high-level synthesis pages with simple language. A developer view might surface technical architecture claims. An academic view might emphasize the philosophical lineage and citations.

This is achieved through tags, frontmatter, and graph traversal — not duplicate content.

### P6: Local-First, Git-Friendly

All artifacts are plain text files (markdown, YAML, JSON) in a git repository. No databases, no hosted services, no proprietary formats. This means:
- The entire knowledge system can be cloned and browsed offline
- Changes are tracked with git history
- Obsidian can open the vault directly
- LLM context windows can ingest the files directly

This also means we use the DeepSeek API (via Claude Code) as our LLM backend — no additional cloud services, no local model hosting complexity.

---

## 5. Formal Provenance Model

### Why Provenance Must Be a First-Class Architectural Layer

The user has stated this requirement in the strongest possible terms:

> "We have to be deadly deadly certain that we maintain a common thread throughout the entire process. Even as we get more abstracted in our extraction method, everything is always directly reference-backable to actual words that were actually said by the speaker in some grounded place within the transcript."

This is not just a design preference — it is the **central trust mechanism** of the entire system. Without robust provenance, the knowledge graph is just an LLM's plausible-sounding invention. With provenance, every claim can be audited, verified, and traced back to its origin.

This principle has deep roots in multiple academic traditions:
- **Digital Humanities** (CIDOC-CRM, CorpusTracer): provenance is a formal, queryable layer — not an afterthought
- **Qualitative Research** (audit trail, codebook): documented analytical decisions are what make interpretive work trustworthy
- **SafePassage** (2025): grounding LLM output in source text reduces hallucinations by up to 85%
- **FAIR to WISE / F2W** (2025): schema-constrained extraction with full provenance chains
- **Journalism**: the editorial standard that every factual claim is attributable to an identifiable source

### The Provenance Chain

Every artifact in the system must be traceable back through the entire pipeline to the original spoken word. The chain has five levels:

```
L5: SYNTHESIS PAGE
    │   "Open source is a moral stance, not just a practical choice..."
    │
    │   Provenance: cites → L4 propositions
    ▼
L4: PROPOSITION (ATOMIC CLAIM)
    │   "The open source community embodies collaborative ideals that
    │    academic science structurally cannot fulfill"
    │
    │   Provenance: extracted_from → L2 cleaned transcript chunk
    │               verified_against → L1 raw transcript quote
    │               confidence: direct_claim
    ▼
L2: CLEANED TRANSCRIPT CHUNK (Phase 1 output)
    │   Grammatically cleaned version of the original spoken words.
    │   "The open source community is what the scientific community
    │    pretends to be. We pretend as scientists that we are working
    │    in this big global collaborative endeavor, but practically
    │    speaking, you're just not really able to do it."
    │
    │   Provenance: cleaned_from → L1 raw chunk
    │               edit_log: [list of transformations applied]
    ▼
L1: RAW TRANSCRIPT (original, never modified)
    │   Verbatim spoken words with timestamps
    │   Source: 2024-09-25-HMN24-00
    │   Timestamp: [00:13:14]
    │
    │   "The open source community is what the scientific community
    │    pretends to be like. We pretend as scientists that we are
    │    doing that, that we're working in this big sort of global
    │    collaborative endeavor, but it's not."
```

**Every link in this chain is bidirectional.** A reader at L5 must be able to click down to L4 → L2 → L1. A reader at L1 must be able to see what propositions were extracted from it (L1 → L4) and what syntheses those propositions fed into (L4 → L5).

*L0 (original audio/video) and L3 (outline) are omitted from this diagram but are part of the progressive summarization stack defined in Section 3.5.*

### Cardinality Rules

The provenance relationships have specific cardinalities that must be enforced:

| Relationship | Cardinality | Rule |
|---|---|---|
| Raw chunk → Cleaned chunk | **1:1** | Each raw chunk produces exactly one cleaned chunk (no splitting or merging at this level) |
| Cleaned chunk → Proposition | **1:many** | One cleaned chunk can contain multiple atomic propositions |
| Proposition → Cleaned chunk | **many:1** | Each proposition comes from exactly one cleaned chunk (its primary source) |
| Proposition → Proposition | **many:many** | Propositions link to each other via typed edges |
| Proposition → Theme | **many:many** | A proposition can belong to multiple themes |
| Synthesis page → Proposition | **1:many** | A synthesis page draws on multiple propositions |
| Proposition → Synthesis page | **many:many** | A proposition can be cited by multiple synthesis pages |

The critical invariant is: **every Proposition must have exactly one `extracted_from` link to a cleaned transcript chunk, and through it, to a raw transcript timestamp.** This is the non-negotiable grounding constraint. A proposition without a source link is invalid and must be either traced or deleted.

### Provenance Metadata Schema

Every node in the knowledge graph carries provenance metadata in its YAML frontmatter. Here is the canonical schema:

#### For a Proposition node:

```yaml
---
id: "prop-2024-09-25-0014"
type: proposition

# What the claim asserts
subject: "[[entities/open-source-community]]"
predicate: "is_more_collaborative_than"
object: "[[entities/academic-science]]"

# Grounding — THE NON-NEGOTIABLE CORE
provenance:
  # The cleaned transcript chunk this was extracted from
  extracted_from:
    source: "[[2024-09-25-HMN24-00-intro-to-class_cleaned]]"
    chunk: 2
    timestamp_range: "00:13:04 - 00:14:09"

  # The exact words in the raw transcript that support this claim
  raw_quote: |
    "The open source community is what the scientific community
    pretends to be like. We pretend as scientists that we are
    doing that, that we're working in this big sort of global
    collaborative endeavor, but practically speaking, you're
    just not really able to do it."

  # The raw transcript file and exact timestamp
  raw_source: "[[2024-09-25-HMN24-00-intro-to-class]]"
  raw_timestamp: "[00:13:14]"

  # Who or what performed the extraction
  extracted_by: "deepseek-api"
  extraction_date: 2026-05-26

  # How confident are we that the claim is actually present in the source?
  confidence: direct_claim  # direct_claim | implication | speculation

  # Has a human reviewed and verified this grounding?
  human_reviewed: false
  human_review_date: null
  human_review_notes: null

# What transformations happened between raw and this proposition?
transformation_log:
  - step: "cleanup"
    description: "Removed filler words 'like', 'sort of'; normalized 'but it's not' to 'but practically speaking, you're just not really able to do it'"
    performed_by: "deepseek-api"
    date: 2026-05-26

# Classification
tags:
  - philosophy/open-source
  - academia/critique
---
```

#### For a Synthesis page:

```yaml
---
title: "Open Source as Moral Imperative"
type: synthesis
theme: "philosophy/open-source"

# Which propositions does this synthesis draw on?
provenance:
  source_propositions:
    - prop-2024-09-25-0014  # "open source is what science pretends to be"
    - prop-2024-12-01-0047  # "false scarcity drives competition"
    - prop-2025-02-06-0023  # "FreeMoCap as institutional alternative"
    - prop-2025-08-15-0089  # "Blender proves open source works at scale"

  # How was this synthesis generated?
  generated_by: "deepseek-api"
  generation_date: 2026-05-28
  human_reviewed: false
---
```

### The Audit Trail: Tracking Transformations Across Levels

The provenance chain is not just about links — it's about **tracking what changed at each level.** Every transformation from L1 (raw) to L5 (synthesis) must be documented.

#### L1 → L2: Cleanup Transformations

When Phase 1 cleans a transcript, the cleanup pass must produce an **edit log** alongside the cleaned output:

```yaml
# In the cleaned transcript's frontmatter
edit_log:
  total_edits: 247
  edit_types:
    filler_removed: 89       # "um", "uh", "you know", "like"
    grammar_normalized: 53   # run-on → sentences, tense agreement
    repetition_removed: 31   # "and, and, and..." → "and"
    timestamp_adjusted: 12   # moved to natural topic breaks
    content_preserved: 247   # every edit preserved substantive meaning
  performed_by: "deepseek-api"
  date: 2026-05-26
```

This is adapted from Guo & Wei's (2026) span-level edit tracking approach. The key principle: **no transformation is silent.** Every edit is recorded, typed, and attributable.

#### L2 → L4: Extraction Transformations

When Phase 2 extracts a proposition from a cleaned transcript, the proposition's `transformation_log` records:
- What specific passage was interpreted
- How the interpretation maps spoken → propositional form
- The confidence level (not all extractions are equally certain)

#### L4 → L5: Synthesis Transformations

When Phase 3 writes a synthesis page, the page's `source_propositions` list provides the audit trail. A reader can verify: "Does every claim in this synthesis actually trace back to a grounded proposition?"

### Verification Protocol

Before any artifact is considered "complete," it must pass these provenance checks:

1. **The Empty Source Check:** Every Proposition node has a non-null `provenance.extracted_from.source` and `provenance.raw_quote`. Fail = invalid.

2. **The Quote-Verbatim Check:** The `provenance.raw_quote` field contains words that actually appear in the referenced raw transcript at the referenced timestamp. This can be verified by a human spot-check or an automated string search. Fail = the proposition is hallucinated and must be deleted or downgraded to `confidence: speculation`.

3. **The Chain-Integrity Check:** Following `extracted_from` links from any Synthesis page should eventually reach a Raw transcript. Broken links = invalid.

4. **The Confidence Calibration Check:** Propositions tagged `confidence: direct_claim` must have a `raw_quote` that unambiguously supports the claim. If the quote is suggestive but not explicit, the confidence must be `implication`. If the proposition synthesizes across multiple passages, it must be `speculation` or have multiple `raw_quote` entries.

5. **The Human Review Gate:** Before Phase 3 synthesis begins, a sample of propositions (at minimum 20% of the total, stratified by confidence level) must be human-reviewed against their source quotes. If the error rate exceeds 10%, all propositions must be reviewed before synthesis proceeds.

### The Non-Negotiable Rule

> **Every claim, at every level of abstraction, must be traceable back to actual words that were actually spoken by the speaker at an identified point in an identified transcript. If you cannot trace a claim back to its source in the raw transcripts, the claim does not belong in the knowledge system.**

This is the firewall against LLM hallucination becoming "canon." It is also the methodological foundation that allows this work to be taken seriously — by academics, by the FreeMoCap community, by anyone who wants to verify that the ideas being presented are genuinely present in the source material.

---

## 6. Three-Phase Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        RAW TRANSCRIPTS (30+)                         │
│                 10-min chunks, verbatim, timestamps                   │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────┐
│                    PHASE 1: LINEAR TEMPORAL CLEANUP                   │
│                                                                      │
│  Per transcript (chronological order):                                │
│  1. Clean: remove filler, fix grammar, preserve meaning              │
│  2. Structure: add YAML frontmatter (date, source, duration, type)   │
│  3. Tag: assign initial theme tags (first-pass extraction)           │
│  4. Rename: standardize filename format                              │
│                                                                      │
│  Output: cleaned_transcripts/ with standardized metadata             │
└──────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────┐
│                   PHASE 2: KNOWLEDGE GRAPH CONSTRUCTION               │
│                                                                      │
│  Cross-transcript:                                                    │
│  1. Extract: atomic propositions from cleaned transcripts            │
│  2. Disambiguate: merge duplicate entities/concepts                  │
│  3. Relate: define edges between propositions                        │
│  4. Cluster: group propositions into themes                          │
│  5. Build: output graph as markdown + wikilinks                      │
│                                                                      │
│  Output: knowledge_graph/ with nodes, edges, and index               │
└──────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────┐
│              PHASE 3: PROGRESSIVE SUMMARIZATION & OUTPUT              │
│                                                                      │
│  Per theme / concept cluster:                                         │
│  1. Synthesize: cross-transcript synthesis pages                     │
│  2. Layer: progressive summarization (outline → abstract → narrative)│
│  3. Render: Obsidian vault, LLM corpus, structured docs              │
│                                                                      │
│  Output: synthesized/ — the final rendered knowledge system          │
└──────────────────────────────────────────────────────────────────────┘
```

Each phase produces artifacts that are independently valuable:
- After Phase 1: you have clean, searchable, well-tagged transcripts
- After Phase 2: you have a browsable knowledge graph of ideas and their relationships
- After Phase 3: you have synthesized, polished output for each target format

---

## 7. Phase 1: Linear Temporal Cleanup

### Purpose

Transform raw verbatim transcripts into clean, structured, consistently-named markdown files that are ready for extraction — while preserving the temporal order and full provenance back to the raw source.

### Process (Per Transcript)

#### Step 1.1: Establish Temporal Order

Create a master timeline of all transcripts by date. The Fall 2024 lectures have clear dates (e.g., `2024-09-25`). The Spring 2025 files with bare timestamps need to have their actual lecture dates determined (likely from the video_eater source playlist metadata or YouTube publish dates).

**Output:** `TIMELINE.md` — a chronological index of all transcripts.

#### Step 1.2: Clean the Transcript

For each transcript, run a cleanup pass that:
- Removes filler words (um, uh, like, you know) where they don't carry meaning
- Converts run-on spoken sentences into grammatical written sentences
- Preserves all substantive content — never delete a concept or claim
- Maintains paragraph boundaries aligned with topic shifts
- Keeps timestamps at natural break points (not rigid 10-min chunks)
- Does NOT add interpretation, commentary, or synthesis

The cleanup should be conservative. When in doubt, keep the original wording. The goal is readability, not rewriting.

**Output:** `cleaned_transcripts/{date}-{topic}_cleaned.md`

#### Step 1.3: Add Structured Frontmatter

Every cleaned transcript gets YAML frontmatter:

```yaml
---
title: "Intro to Class"
date: 2024-09-25
source_type: youtube  # youtube | local_file | playlist
source_url: "https://www.youtube.com/watch?v=cB6lWKBlEhE"
video_id: "cB6lWKBlEhE"
duration: "00:57:40"
series: "HMN Fall 2024"
lecture_number: 0
speaker: "Jon Matthis"
context: "Undergraduate topics course, Northeastern University"
tags:
  - philosophy/open-source
  - academia/critique
  - freemocap/origin-story
  - morality/institutional-harm
---
```

#### Step 1.4: Assign Initial Theme Tags

The first pass of theme extraction happens here. Tags serve as lightweight, flat categorization that will later inform the knowledge graph's cluster structure.

Tags should be namespaced with a `/` hierarchy for Obsidian compatibility:
- `philosophy/open-source` — claims about the moral imperative of open source
- `philosophy/science-ethics` — claims about how science should be done
- `academia/critique` — critique of academic institutions
- `academia/alternatives` — proposed alternatives to traditional academia
- `freemocap/origin-story` — how and why FreeMoCap started
- `freemocap/design-philosophy` — why FreeMoCap is built the way it is
- `morality/institutional-harm` — the concept of moral harm from institutions
- `morality/community` — claims about community, collaboration, mutual support
- `neuroscience/motor-control` — scientific claims about movement
- `neuroscience/vision` — scientific claims about vision and eye tracking
- `technology/mocap` — claims about motion capture technology
- `technology/open-source-tools` — discussion of specific tools (Blender, etc.)

These tags are provisional — Phase 2 will refine them into the formal ontology.

#### Step 1.5: Standardize Filenames

All cleaned transcripts follow the naming convention:

```
{YYYY-MM-DD}-{series-abbrev}-{lecture-number}-{topic-slug}_cleaned.md
```

Examples:
- `2024-09-25-HMN24-00-intro-to-class_cleaned.md`
- `2025-02-03-HMN25-03-freemocap-data-collection_cleaned.md`
- `2025-08-14-FMLS-skellycam-2-deep-dive_cleaned.md`

The bare timestamp files from Spring 2025 need their actual lecture topics identified and names corrected.

### Phase 1 Artifacts

```
skelly-soul-docs/
├── TIMELINE.md                          # Chronological index of all transcripts
├── cleaned_transcripts/
│   ├── 2024-09-25-HMN24-00-intro-to-class_cleaned.md
│   ├── 2024-09-25-HMN24-01-intro-to-data-collection_cleaned.md
│   ├── ...
│   └── 2025-08-15-FMLS-skellycam-2-deep-dive_cleaned.md
└── raw_transcripts/                     # Original transcripts (moved here, not modified)
    ├── hmn-course-lectures/
    └── freemocap-livestreams/
```

---

## 8. Phase 2: Knowledge Graph Construction

### Purpose

Extract atomic propositions from the cleaned transcripts, disambiguate entities, define relationships, and cluster into themes — producing a densely connected knowledge graph where the nodes are ideas, not people.

### Process

#### Step 2.1: Proposition Extraction

Each cleaned transcript is processed to extract **atomic propositions** — single, self-contained claims that can stand alone and be linked to other claims.

An atomic proposition has:
- A **subject** (the concept or entity the claim is about)
- A **predicate** (the relationship or assertion)
- An **object** (what the claim asserts — could be another concept, a value, a property)
- **Provenance** (source transcript + timestamp)
- **Confidence** (is this a direct claim, an implication, or a tentative speculation?)

Example:
```yaml
---
id: "prop-2024-09-25-0014"
type: claim
subject: "open_source_community"
predicate: "is_more_collaborative_than"
object: "academic_science"
provenance:
  source: "2024-09-25-HMN24-00-intro-to-class_cleaned"
  timestamp: "00:13:14"
  quote: "The open source community is what the scientific community pretends to be."
confidence: direct_claim
tags: ["philosophy/open-source", "academia/critique"]
---
```

The extraction is done by an LLM (DeepSeek API via Claude Code) with the following prompt structure (adapted from KGGen and CLARE's extraction approaches):
- System prompt: "You are extracting atomic propositions from a lecture transcript. Each proposition should be a single, self-contained claim. Include the exact quote that supports the claim. Output as structured JSON."
- Temperature: 0.0 (deterministic, factual output — per CLARE and KGGen best practices)
- Chunking: Semantic (topic-based) boundaries, not fixed-size — because lecture arguments span multiple paragraphs (per CLARE's context-aware extraction findings)

#### Step 2.2: Entity & Concept Disambiguation

After extraction, we have many propositions that may refer to the same concept using different language. For example:
- "free open source software" / "FOSS" / "the open source community" / "Blender's model"
- "academia" / "the university system" / "institutions like this one" / "the ivory tower"
- "moral harm" / "moral injury" / "institutional harm"

This step runs a dedicated LLM pass (per SF-GPT's Entity Alias Generation and CLARE's entity merging approach) that:
- Identifies co-referring expressions across all extracted propositions
- Produces a canonical entity name for each cluster
- Links the canonical entity to the proposition IDs that reference it

**Output:** `knowledge_graph/entities.yaml` — a registry of canonical entities with their aliases and linked propositions.

#### Step 2.3: Relationship Definition

With entities disambiguated and propositions extracted, we define the edge types that connect nodes in the graph. Each edge is a typed, directional relationship.

Proposed edge types (informed by the content we've seen in spot-checks):

| Edge Type | Example |
|-----------|---------|
| `supports` | Proposition A provides evidence/logic for Proposition B |
| `contrasts_with` | Proposition A and B are in tension or opposition |
| `refines` | Proposition B is a more precise/specific version of Proposition A |
| `contextualizes` | Proposition A provides background needed to understand Proposition B |
| `derives_from` | Proposition A is the philosophical source of Proposition B |
| `example_of` | Proposition A is a concrete instance of the abstract concept B |
| `questions` | Proposition A raises a question or challenge to Proposition B |
| `introduced_in` | Proposition was first stated in this source |
| `revisited_in` | Proposition was restated or elaborated in a later source |
| `related_to` | General semantic connection (fallback when no specific relation fits) |

These edge types are drawn from standard knowledge graph ontologies (schema.org's relationship types) and adapted for philosophical/propositional content.

#### Step 2.4: Theme Clustering

With propositions extracted, disambiguated, and related, we cluster them into themes. This is the bridge between the flat proposition graph and the hierarchical navigation structure that users will browse.

The clustering is semi-automated:
1. **LLM pass:** Proposes theme clusters based on proposition similarity and co-occurrence (KGGen's iterative clustering approach)
2. **Human review:** Review and adjust cluster boundaries, split or merge themes
3. **Naming:** Each theme gets a descriptive name and a short (1–2 sentence) definition

Example themes (from spot-checking the intro lecture):
- **"Open Source as Moral Imperative"** — claims about why free/open source software is ethically superior and how it relates to scientific ideals
- **"The Academic Ponzi Scheme"** — critique of academic career structures, publication incentives, and the tenure system
- **"Moral Harm and Institutional Complicity"** — the concept of moral injury from participating in systems you find morally repugnant
- **"FreeMoCap as Alternative Infrastructure"** — how building free tools is a form of institutional resistance

#### Step 2.5: Graph Output as Markdown

The knowledge graph is serialized as a set of interlinked markdown files — not a database. This is a deliberate choice for Obsidian compatibility, git-friendliness, and simplicity.

**Entity nodes** → `knowledge_graph/entities/{entity-slug}.md`
**Proposition nodes** → `knowledge_graph/propositions/{prop-id}.md`
**Theme pages** → `knowledge_graph/themes/{theme-slug}.md`
**Edge index** → `knowledge_graph/edges.json` (machine-readable graph structure)

Each node file uses YAML frontmatter for structured data and `[[wikilinks]]` for connections:

```markdown
---
id: "prop-2024-09-25-0014"
type: proposition
subject: "[[entities/open-source-community]]"
predicate: "is_more_collaborative_than"
object: "[[entities/academic-science]]"
confidence: direct_claim
provenance:
  source: "[[2024-09-25-HMN24-00-intro-to-class_cleaned]]"
  timestamp: "00:13:14"
tags:
  - philosophy/open-source
  - academia/critique
---

# The open source community is what the scientific community pretends to be

**Source:** [[2024-09-25-HMN24-00-intro-to-class_cleaned]] at `[00:13:14]`

> "The open source community is what the scientific community pretends to be.
> We pretend as scientists that we are working in this big global collaborative
> endeavor, but practically speaking, you're just not really able to do it."

## Related Propositions

- [[prop-2024-09-25-0012]] — supports (academia's hyper-competition is structural)
- [[prop-2024-12-01-0047]] — refines (adds the role of false scarcity)
- [[prop-2025-02-06-0023]] — contextualizes (FreeMoCap as institutional alternative)
```

### Phase 2 Artifacts

```
skelly-soul-docs/
├── knowledge_graph/
│   ├── entities/
│   │   ├── open-source-community.md
│   │   ├── academic-science.md
│   │   ├── moral-harm.md
│   │   └── ...
│   ├── propositions/
│   │   ├── prop-2024-09-25-0014.md
│   │   ├── prop-2024-12-01-0047.md
│   │   └── ...
│   ├── themes/
│   │   ├── open-source-as-moral-imperative.md
│   │   ├── academic-ponzi-scheme.md
│   │   └── ...
│   ├── edges.json
│   └── ontology.md                    # Formal ontology definition
└── cleaned_transcripts/               # Phase 1 output (linked from graph)
```

---

## 9. Phase 3: Progressive Summarization & Rendered Outputs

### Purpose

Transform the knowledge graph and cleaned transcripts into polished, multi-audience output formats — while maintaining the layered compression structure of progressive summarization and the full provenance chain back to the sources.

### Process

#### Step 3.1: Cross-Transcript Synthesis Pages

For each theme cluster identified in Phase 2, produce a synthesis page that:
- Introduces the theme in accessible language (readable without prior context)
- Weaves together the relevant propositions from across multiple transcripts
- Shows the evolution of the idea over time (when it was introduced, how it changed)
- Links to the full proposition pages and source transcripts for deep dives
- Is written in a consistent voice that is about the ideas, not the speaker

Example structure for a synthesis page:

```markdown
---
title: "Open Source as Moral Imperative"
type: synthesis
theme: "philosophy/open-source"
summary: "Why FreeMoCap's commitment to free and open source software
is not just a practical choice but a moral stance — and how the open
source community embodies collaborative ideals that academic science
claims to hold but structurally cannot fulfill."
first_introduced: "2024-09-25-HMN24-00"
last_updated: "2025-08-15-FMLS-skellycam-2"
related_themes:
  - "[[themes/academic-ponzi-scheme]]"
  - "[[themes/freemocap-as-alternative-infrastructure]]"
---

# Open Source as Moral Imperative

## Overview
[2–3 paragraphs introducing the theme in plain language]

## Core Claims
[The key propositions that form this theme, with brief explanations]

## Evolution Over Time
[How this idea developed across lectures/livestreams]

## Source Index
[Links to all source propositions and transcripts]

## Related Themes
[Links to connected theme pages]
```

#### Step 3.2: Progressive Summarization Layers

Each transcript gets a compression stack (adapted from Tiago Forte's progressive summarization):

| Layer | Description | Format |
|-------|-------------|--------|
| **L0: Raw** | Original verbatim transcript | 10-min chunks with timestamps |
| **L1: Cleaned** | Grammatical, filler removed (Phase 1 output) | Continuous prose, timestamps at topic breaks |
| **L2: Outline** | Bulleted outline of key points | Hierarchical bullet list with timestamps |
| **L3: Abstract** | 1–2 page summary of main claims | Prose, linking to key propositions |
| **L4: Card** | Index-card-sized distillation (for graph nodes) | 2–3 sentences, the "atomic takeaway" |

Layers L2–L4 are produced in Phase 3. L0 and L1 already exist from Phase 1.

Each layer links downward: L4 → L3 → L2 → L1 → L0. A reader can start at any compression level and drill deeper.

#### Step 3.3: Multi-Format Rendering

From the same source material, render different output views:

**Obsidian Vault (Primary Output)**
- All markdown files with YAML frontmatter and `[[wikilinks]]`
- Tags for faceted browsing
- Graph view shows the knowledge graph visually
- Backlinks panel shows how ideas connect
- Dataview plugin can query by tag, date, type, theme

**LLM-Queryable Corpus**
- A consolidated markdown file or directory that can be ingested into an LLM context window
- Organized by theme, with synthesis pages serving as the primary content
- Includes a "compressed" mode that uses only L3–L4 layers for when context window is limited
- Includes a "full" mode with L1–L4 for deep Q&A

**Structured Documentation (Future)**
- Potentially a "FreeMoCap Philosophy & Practice" document
- Linear narrative structure but composed of self-contained sections
- Could be rendered to PDF, web, or ebook
- This is a lower priority than the Obsidian vault and LLM corpus

### Phase 3 Artifacts

```
skelly-soul-docs/
├── synthesized/
│   ├── themes/
│   │   ├── open-source-as-moral-imperative.md
│   │   ├── academic-ponzi-scheme.md
│   │   ├── moral-harm-and-institutional-complicity.md
│   │   └── ...
│   ├── timeline/
│   │   └── evolution-of-ideas.md          # Narrative of how ideas evolved
│   └── index.md                           # Entry point / happy path
├── llm_corpus/
│   ├── compressed/                         # L3-L4 only, for limited context windows
│   └── full/                               # L1-L4, for deep Q&A
└── knowledge_graph/                        # Phase 2 output
```

---

## 10. Ontology Design

The ontology defines the types of nodes, edges, and properties in the knowledge graph. This is the formal schema that constrains extraction and ensures consistency.

### Node Types

```yaml
Entity:
  description: "A concept, person, organization, tool, or idea that can be the subject or object of a claim"
  examples:
    - "open_source_community"
    - "academic_science"
    - "FreeMoCap"
    - "moral_harm"
    - "Blender"
  properties:
    - name
    - aliases (list of co-referring terms)
    - type (concept | person | organization | tool | event)
    - definition (1–2 sentence description)

Proposition:
  description: "A single, self-contained claim about entities"
  properties:
    - subject (link to Entity)
    - predicate (relationship type)
    - object (link to Entity or literal value)
    - confidence (direct_claim | implication | speculation)
    - provenance (source transcript + timestamp + quote)
    - theme_tags (links to Theme nodes)

Theme:
  description: "A cluster of related propositions forming a coherent topic"
  properties:
    - name
    - definition
    - propositions (list of linked Proposition IDs)
    - parent_theme (optional, for hierarchical themes)
    - first_introduced (earliest source)
    - last_updated (most recent source)

Source:
  description: "A transcript or other source document"
  properties:
    - title
    - date
    - type (lecture | livestream | podcast | talk | dev_session)
    - series
    - url (if available)
    - duration
    - speaker

Question:
  description: "An open question or unresolved tension raised in the content"
  properties:
    - question_text
    - raised_in (source)
    - addressed_by (links to Propositions that attempt to answer)
    - status (open | partially_addressed | resolved)
```

### Edge Types

```yaml
supports:
  description: "A provides evidence, reasoning, or logical support for B"
  domain: Proposition
  range: Proposition

contrasts_with:
  description: "A and B are in tension, contradiction, or present opposing views"
  domain: Proposition
  range: Proposition

refines:
  description: "B is a more specific, precise, or developed version of A"
  domain: Proposition
  range: Proposition
  note: "Typically temporal — B comes after A"

contextualizes:
  description: "A provides background or context needed to understand B"
  domain: Proposition
  range: Proposition

derives_from:
  description: "A is the philosophical, theoretical, or logical source of B"
  domain: Proposition
  range: Proposition | Entity

example_of:
  description: "A is a concrete instance of the abstract concept B"
  domain: Proposition | Entity
  range: Entity | Theme

questions:
  description: "A raises a challenge, doubt, or open question about B"
  domain: Proposition
  range: Proposition

introduced_in:
  description: "Proposition was first stated in this Source"
  domain: Proposition
  range: Source

revisited_in:
  description: "Proposition was restated, elaborated, or refined in this later Source"
  domain: Proposition
  range: Source

related_to:
  description: "General semantic connection (fallback)"
  domain: Proposition | Entity
  range: Proposition | Entity
```

This ontology is adapted from:
- **schema.org** for basic entity/relationship types
- **KGGen's** SPO (Subject-Predicate-Object) triple model
- **CLARE's** relationship typing (especially `supports`, `contrasts_with`, `refines`)
- **Graphiti's** temporal edge types (`introduced_in`, `revisited_in`)

---

## 11. Directory Structure & Obsidian Compatibility

### Proposed Repository Structure

```
skelly-soul-docs/
│
├── README.md                                 # Project overview and quick start
├── STRATEGY.md                               # This document
├── TIMELINE.md                               # Chronological index of all source material
│
├── raw_transcripts/                          # Original transcripts (read-only, never modified)
│   ├── hmn-course-lectures/
│   │   ├── fall-2024/
│   │   └── spring-2025/
│   └── freemocap-livestreams/
│
├── cleaned_transcripts/                      # Phase 1 output
│   ├── 2024-09-25-HMN24-00-intro-to-class_cleaned.md
│   ├── 2024-09-25-HMN24-01-intro-to-data-collection_cleaned.md
│   ├── ...
│   └── 2025-08-15-FMLS-skellycam-2-deep-dive_cleaned.md
│
├── knowledge_graph/                          # Phase 2 output
│   ├── ontology.md                           # Formal ontology definition
│   ├── edges.json                            # Machine-readable graph structure
│   ├── entities/
│   │   ├── _index.md                         # Entity registry
│   │   ├── open-source-community.md
│   │   ├── academic-science.md
│   │   └── ...
│   ├── propositions/
│   │   ├── _index.md                         # Proposition registry
│   │   ├── prop-2024-09-25-0014.md
│   │   └── ...
│   └── themes/
│       ├── _index.md                         # Theme registry
│       ├── open-source-as-moral-imperative.md
│       └── ...
│
├── synthesized/                              # Phase 3 output
│   ├── index.md                              # Main entry point / happy path
│   ├── themes/                               # Cross-transcript synthesis pages
│   └── timeline/
│       └── evolution-of-ideas.md
│
├── llm_corpus/                               # LLM-ingestible exports
│   ├── compressed/                           # L3-L4 summaries
│   └── full/                                 # L1-L4 complete
│
└── archive/                                  # Prior work (PDFs, old attempts)
    └── freemocap-history-manifesto-and-sources/
```

### Obsidian Compatibility

This entire directory is designed to be opened as an Obsidian vault. Key Obsidian features we leverage:

- **`[[wikilinks]]`:** All cross-references use Obsidian's wikilink syntax. This means Obsidian's graph view will automatically visualize the entire knowledge graph.
- **YAML frontmatter:** Every page has structured metadata that Obsidian's Dataview plugin can query.
- **Nested tags:** `#philosophy/open-source` creates a tag hierarchy that Obsidian's tag pane shows as a tree.
- **Backlinks:** Obsidian automatically shows which pages link to the current page — this is how readers navigate from a proposition back to all the themes and syntheses that reference it.
- **Graph view:** The force-directed graph visualization naturally represents the knowledge graph structure. Entities and propositions appear as nodes; wikilinks appear as edges.

No Obsidian-specific features are required for the files to be useful — they are plain markdown and work with any markdown reader. Obsidian just provides the richest browsing experience.

---

## 12. Anti-Patterns & Guardrails

These are the failure modes we are actively designing against.

### A1: The Personality Cult Problem

**Symptom:** The content reads as "The Wisdom of Jon Matthis" rather than "The Philosophy of FreeMoCap."

**Structural guardrails:**
- Knowledge graph nodes are ideas, not people. "Jon Matthis" appears only in provenance metadata, never as a node identity.
- Synthesis pages are written in an impersonal, explanatory voice — like Wikipedia, not a memoir.
- The focus question for any piece of content is: "What is the idea, and why does it matter?" — not "What did Jon say?"
- Quotes are used as evidence for claims, not as oracular pronouncements.

### A2: The Blowhard Problem

**Symptom:** The content feels self-important, grandiose, or takes itself too seriously.

**Structural guardrails:**
- Prefer plain language over academic jargon. If a concept can be explained simply, do it.
- Include the self-deprecating humor and informality from the source material — it's part of the authentic voice.
- Avoid making claims seem more profound than they are. Let the ideas speak for themselves.
- The tone of synthesis pages should be explanatory, not declarative. "Here's an idea and why it matters" rather than "Here is the Truth."

### A3: The Over-Formalization Problem

**Symptom:** The content becomes dry, academic, and loses the energy of the source material.

**Structural guardrails:**
- The progressive summarization layers preserve the raw voice at L0 and progressively formalize — but L2 (outline) should still read as if a human said it out loud.
- Direct quotes are used liberally in proposition nodes to keep the original phrasing alive.
- Synthesis pages can and should use an engaging, accessible voice. This is philosophy for everyone, not a journal article.

### A4: The Hallucination Drift Problem

**Symptom:** The LLM extraction process generates plausible-sounding claims that aren't actually in the source material.

**Structural guardrails:**
- Every proposition includes an exact quote from the source (SafePassage grounding approach).
- Propositions are tagged with confidence levels (`direct_claim` vs `implication` vs `speculation`).
- The human review step in Phase 2 is the primary defense — propositions that can't be verified against the source are removed or downgraded.
- The provenance chain is always intact and auditable.

### A5: The Stale Snapshot Problem

**Symptom:** The knowledge system captures a moment in time and becomes outdated as the project evolves.

**Structural guardrails:**
- The temporal spine and bi-temporal modeling (from Graphiti) means new content can be added without restructuring.
- The Phase 1 pipeline is designed to be re-run for new transcripts.
- The `last_updated` field on themes and entities makes staleness visible.
- The system is designed for incremental updates, not one-shot generation.

---

## 13. Gap Analysis: Missing Sources

Cross-referencing the `video_eater` default inputs against the existing transcripts reveals gaps.

### Sources with Transcripts (30 files)

- HMN Fall 2024: 10 lectures (complete series)
- HMN Spring 2025: 10 lectures (complete series, some with naming issues)
- FreeMoCap Livestreams: 10 transcripts

### Sources Without Transcripts (from video_eater defaults)

| Source | Type | Priority |
|--------|------|----------|
| BOOM FreeMoCap Podcast Interview (`kw3hYndzzac`) | YouTube video | High — external-facing philosophy content |
| VFX Futures — Before & Afters Podcast (`Bqt8ZC5C4h8`) | YouTube video | High — external-facing |
| "This is FreeMoCap" video (`WW_WpMcbzns`) | YouTube video | High — core introductory content |
| 2026 State of the Skelly Address (local file) | Local recording | High — annual project update |
| [2025] FreeMoCap Livestreams playlist | YouTube playlist | Medium — ongoing livestream series |
| [OLD] FreeMoCap Development playlist | YouTube playlist | Low — historical, lower relevance to philosophy |
| 2025-08-07 JSM Livestream (local file) | Local recording | Medium |
| 2025-08-14 JSM Livestream (local file) | Local recording | Medium |
| 2026-03-30 FreeMoCap/SkellyCam Dev Update (local file) | Local recording | Medium |
| 2026-03-31 FreeMoCap UI Dev Planning (local file) | Local recording | Low — more technical |
| 2026-05-15 FreeMoCap v2 Update (local file) | Local recording | High — recent project state |
| DW22 talk (local file) | Local recording | Medium — earlier era perspective |

### Recommended Action

The high-priority missing sources should be processed through video_eater to generate transcripts before Phase 1 begins. The medium-priority sources can be added during or after Phase 1.

---

## 14. Implementation Sequence

This is the proposed order of work. Each step produces a concrete, reviewable artifact.

### Milestone 0: Foundation (current)

- [ ] **M0.1:** Write and review this STRATEGY.md (this document)
- [ ] **M0.2:** Set up directory structure per Section 11
- [ ] **M0.3:** Write `TIMELINE.md` — chronological index of all existing transcripts
- [ ] **M0.4:** Process missing high-priority sources through video_eater

### Milestone 1: Phase 1 — Linear Temporal Cleanup

- [ ] **M1.1:** Define the cleanup prompt template (LLM instructions for transcript cleaning)
- [ ] **M1.2:** Process Fall 2024 HMN lectures (10 transcripts) — clean, tag, rename
- [ ] **M1.3:** Review Fall 2024 output, refine prompt template
- [ ] **M1.4:** Process Spring 2025 HMN lectures (10 transcripts)
- [ ] **M1.5:** Process FreeMoCap Livestreams (10 transcripts)
- [ ] **M1.6:** Process any newly generated transcripts from M0.4
- [ ] **M1.7:** Final review — spot-check cleaned transcripts for quality and consistency

### Milestone 2: Phase 2 — Knowledge Graph Construction

- [ ] **M2.1:** Finalize ontology — review and refine node/edge types from Section 10
- [ ] **M2.2:** Define proposition extraction prompt template
- [ ] **M2.3:** Extract propositions from all cleaned transcripts
- [ ] **M2.4:** Entity disambiguation pass — merge co-referring concepts
- [ ] **M2.5:** Relationship extraction — define edges between propositions
- [ ] **M2.6:** Theme clustering — group propositions into themes
- [ ] **M2.7:** Generate knowledge graph markdown files
- [ ] **M2.8:** Human review of knowledge graph — verify accuracy, adjust clustering

### Milestone 3: Phase 3 — Progressive Summarization & Output

- [ ] **M3.1:** Write progressive summarization prompt templates (L2 outline, L3 abstract, L4 card)
- [ ] **M3.2:** Generate summarization layers for each transcript
- [ ] **M3.3:** Write cross-transcript synthesis pages for each theme
- [ ] **M3.4:** Write `synthesized/index.md` — the main entry point / happy path
- [ ] **M3.5:** Generate LLM corpus (compressed and full)
- [ ] **M3.6:** Final review and polish

### Milestone 4: Ongoing

- [ ] **M4.1:** Define process for adding new transcripts to the pipeline
- [ ] **M4.2:** Regular review cycle — update synthesis pages as the project evolves

---

## 15. References

### Academic Papers & Systems

1. **CLARE** — Koschmieder, L., et al. (2025). "CLARE: Context-Aware, Interactive Knowledge Graph Construction from Transcripts." *MDPI Information, 16*(10), 866. [Link](https://www.mdpi.com/2078-2489/16/10/866/xml)
   - *Key contribution:* 82.1% fact accuracy on MINE benchmark; human-in-the-loop refinement gives +22.7% accuracy improvement; supports 150+ LLMs with local deployment.

2. **KGGen** — "KGGen: LLM-Powered Knowledge Graph Generation." Python package (`pip install kg-gen`). [EmergentMind](https://www.emergentmind.com/topics/kggen)
   - *Key contribution:* Three-stage pipeline (Extract → Aggregate → Iterative Clustering); introduced the MINE benchmark; 66.07% MINE score vs. GraphRAG 47.80%.

3. **SF-GPT** — (2025). "SF-GPT: A Training-Free Method to Enhance Capabilities for Knowledge Graph Construction in LLMs." *Neurocomputing*. [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0925231224014978)
   - *Key contribution:* Entity Extraction Filter (EEF) for hallucination reduction; Entity Alias Generation (EAG) for disambiguation; Self-Fusion Subgraph for multi-pass consistency.

4. **SafePassage** — (2025). "SafePassage: High-Fidelity Information Extraction with Black Box LLMs." arXiv:2510.00276v1.
   - *Key contribution:* "Safe passage" concept — LLM-generated content grounded in source documents; up to 85% hallucination reduction; three-step pipeline (extract → align → flag).

5. **FAIR to WISE (F2W)** — Lawrence Berkeley National Lab (2025). "FAIR to WISE v1.0.0." DOI: 10.11578/dc.20251208.5.
   - *Key contribution:* Schema-driven extraction with full provenance capture; ontology-grounded entity linking; hallucination reduction through evidence grounding and schema constraints.

6. **ScaleDoc** — Tsinghua University (2025). "ScaleDoc: Scaling LLM-based Predicates over Large Document Collections." arXiv:2509.12610v1.
   - *Key contribution:* Proxy/oracle cascade architecture; 2× speedup, up to 85% reduction in expensive LLM invocations.

7. **DocETL** — Stanford/UC Berkeley (2025). "DocETL: Semantic Data Processing at Scale with AI-Powered Query Optimization."
   - *Key contribution:* Monte Carlo Tree Search for Pareto-optimal accuracy–cost plans; 86% cost reduction while maintaining target accuracy.

8. **Graphiti** — Open-source Python library (2025). "Graphiti: Temporal Knowledge Graphs."
   - *Key contribution:* Bi-temporal modeling (transaction time + valid time); podcast processing example directly relevant to our use case; built on Neo4j.

9. **DocIE@XLLM25** — (2025). "In-Context Learning for Information Extraction using Fully Synthetic Demonstrations." *XLLM 2025 (ACL Workshop)*.
   - *Key contribution:* Synthetic data generation for document-level entity and relation extraction; 5,000+ abstracts with ~59k entities and ~30k relation triples, zero manual annotation.

### Methodologies & Frameworks

10. **Progressive Summarization** — Forte, T. (2022). *Building a Second Brain: A Proven Method to Organize Your Digital Life and Unlock Your Creative Potential.* Atria Books.
    - *Key contribution:* Five-layer compression model (raw → bolded → highlighted → summary → remix); designed for personal knowledge management but adaptable to structured extraction.

11. **Zettelkasten Method** — Ahrens, S. (2017). *How to Take Smart Notes: One Simple Technique to Boost Writing, Learning and Thinking.* Sönke Ahrens.
    - *Key contribution:* Atomic notes, each containing one idea; dense bidirectional linking; the intellectual ancestor of Obsidian's wikilink model and our "jump in anywhere" principle.

12. **GraphRAG** — Microsoft Research (2024). "GraphRAG: Unlocking LLM Discovery on Narrative Private Data."
    - *Key contribution:* Community-summary-based retrieval over knowledge graphs; has lower fact accuracy for pure extraction (48.3% on MINE) but is the dominant retrieval paradigm for KG-based Q&A.

### Qualitative Research & Grounded Theory

13. **Grounded Theory** — Glaser, B.G. & Strauss, A.L. (1967). *The Discovery of Grounded Theory: Strategies for Qualitative Research.* Aldine Publishing.
    - *Key contribution:* The original formulation of grounded theory — inductive, data-driven theory building with constant comparison and theoretical sampling.

14. **Constructivist Grounded Theory** — Charmaz, K. (2006/2014). *Constructing Grounded Theory: A Practical Guide Through Qualitative Analysis.* Sage Publications.
    - *Key contribution:* Reframed grounded theory within a constructivist epistemology; emphasized the researcher's role in co-constructing meaning; introduced the three-stage coding process (initial → focused → theoretical) used in our pipeline mapping.

15. **The Coding Manual** — Saldaña, J. (2016). *The Coding Manual for Qualitative Researchers.* Sage Publications.
    - *Key contribution:* The definitive practical guide to qualitative coding; codebook methodology; the concept of "coding as a cyclical act" that informs our iterative extraction approach.

16. **Thematic Analysis** — Braun, V. & Clarke, V. (2006). "Using Thematic Analysis in Psychology." *Qualitative Research in Psychology*, 3(2), 77–101.
    - *Key contribution:* Six-phase thematic analysis process (familiarization → coding → theme generation → review → definition → reporting); the most widely cited methodology for extracting themes from qualitative data.

17. **Applied Thematic Analysis** — Guest, G., MacQueen, K.M. & Namey, E.E. (2012). *Applied Thematic Analysis.* Sage Publications.
    - *Key contribution:* Operationalized thematic analysis for large-scale qualitative projects; introduced the concept of "saturation" as a stopping criterion for data collection/analysis.

### Digital Humanities & Provenance

18. **CIDOC-CRM / LRMoo** — ICOM/CIDOC. ISO 21127:2014. [cidoc-crm.org](https://cidoc-crm.org)
    - *Key contribution:* Formal ontology for cultural heritage information; models events, actors, objects, and their temporal relationships; LRMoo extension models bibliographic entities (works, expressions, manifestations); the standard for formal provenance modeling in the digital humanities.

19. **CorpusTracer** — Max Planck Institute for the History of Science, Berlin. Presented at DH2018.
    - *Key contribution:* Applied CIDOC-CRM + FRBRoo to model the genealogy of a 13th-century textbook across 400+ years and 300+ editions; demonstrated that formal provenance models can trace knowledge innovations through complex editorial histories.

20. **Tracing the Genealogies of Ideas** — Li, L. (2024). "Tracing the Genealogies of Ideas with Sentence Embeddings." [Semantic Scholar](https://www.semanticscholar.org/paper/Tracing-the-Genealogies-of-Ideas-with-Sentence-Li/433d34e9bcdeadf13bf26177a114326516d567cd)
    - *Key contribution:* Used sentence embeddings (SBERT) to trace paraphrased ideas across a 250,000-text 19th-century corpus; demonstrated that semantic search captures idea transmission even when vocabulary differs completely.

21. **Mining Asymmetric Intertextuality** — Li et al. (2024). "Mining Asymmetric Intertextuality." [ar5iv](https://ar5iv.labs.arxiv.org/html/2410.15145)
    - *Key contribution:* Formalized a taxonomy of intertextual relationship types from direct quotation through thematic borrowing; mapped onto our knowledge graph edge types.

22. **Provenance Tracking in DH Pipelines** — Guo, J. & Wei, Z. (2026). "From OCR to Analysis: Tracking Correction Provenance in Digital Humanities Pipelines." [arXiv](https://arxiv.org/html/2603.00884v4)
    - *Key contribution:* Span-level edit tracking with edit type, correction source, confidence scores, and review status; demonstrated that provenance-filtered corrections produce materially different analysis results; the formal justification for our "no silent transformation" rule.

### Tools

23. **Neo4j LLM Knowledge Graph Builder** — Neo4j (2025). First release of 2025. [Blog](https://collabnix.com/neo4j/2025/02/05/llm-knowledge-graph-builder-first-release-of-2025/)
    - *Key contribution:* Document → chunk → entity extraction → relationship extraction → Neo4j graph; supports multiple LLM backends; GraphRAG retrievers; RAGAs evaluation.

24. **brain_dump** — Open-source pipeline (2025). [GitHub](https://github.com/navajonki/brain_dump)
    - *Key contribution:* Audio → ASR → atomic chunking → entity extraction → relationship mapping → Markdown + YAML for Obsidian; the closest existing tool to our full pipeline.

---

*This strategy document is a living artifact. As we work through the phases, we will update it with what we learn — prompt templates that work well, ontology refinements, and process improvements.*
