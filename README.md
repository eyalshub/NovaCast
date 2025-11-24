# NovaCast

## Overview

NovaCast is an **AI-powered media automation engine** designed to transform text-based ideas into fully produced, publish-ready videos — autonomously.

Built as a **multi-agent GenAI system**, NovaCast coordinates LLM-driven agents, a workflow orchestrator, vector memory, TTS engines, video rendering pipelines, and social publishing adapters to deliver an end-to-end content studio that runs entirely in software.

The goal of NovaCast is to provide a **scalable, modular, and production-grade foundation** for generating high-quality media at speed and volume. This includes:

- **Idea → Script → Scene Breakdown → Narration → Video Composition → Publishing**
- **Multi-model LLM routing** (OpenAI / Anthropic / Ollama)
- **Multi-engine TTS** (Coqui / ElevenLabs / Piper)
- **FFmpeg-based video builder** with templates, overlays, and dynamic composition
- **Scheduler + Worker system** for long-running and asynchronous jobs
- **Full API surface** (REST + WebSocket) for chat, media generation, prompts, assets, and scheduling
- **Observability stack**, metrics, structured logs, and safety layers

NovaCast is built with the architecture of a **real production system**, not a toy project:

- **FastAPI backend** with versioned endpoints  
- **MongoDB** for operational state, assets, prompts, schedules, and job logs  
- **Vector store** for contextual memory  
- **Distributed worker queue** for heavy media processing  
- **Telemetry stack** (Prometheus + OpenTelemetry)  
- **Cloud-ready infrastructure** (K8s manifests, Terraform scaffolding, Dockerized services)

Although the system framework is complete, many components are currently implemented as **structured scaffolds**. NovaCast is actively developed toward a full MVP capable of generating both short-form and long-form videos automatically.

This repository demonstrates:

- **Production-grade system architecture**
- **Clean layering** of agents, services, orchestration, and data
- **Forward-looking design** aligned with modern AI engineering practices
- Strong attention to **reliability, modularity, extensibility**, and real-world deployment constraints

NovaCast serves as both a **technical showcase** and a **working foundation** for building AI-driven media workflows at scale.


## Key Features

NovaCast brings together multiple AI-driven components into a unified, production-ready media generation pipeline.  
Below are the core features that define the system:

### 🎬 End-to-End Media Generation Pipeline
A fully automated flow from initial idea to published video:
- **Idea generation**
- **Outline + scene structure**
- **Full script writing**
- **Scene-level visual descriptions**
- **AI narration (TTS)**
- **Automated video assembly (FFmpeg template system)**
- **Optional auto-publishing to social platforms**

---

### 🤖 Multi-Agent GenAI System
A modular agent ecosystem, each with a distinct responsibility:
- `ideation_agent` – creative idea generation and refinement  
- `outline_agent` – narrative structure planning  
- `script_agent` – full scriptwriting with pacing, tone, and storytelling  
- `rewrite_agent` – consistency improvements, SEO tuning, stylistic rewrites  
- `scene_describer_agent` – detailed visual descriptions powering the video builder  

Each agent:
- uses its own **YAML prompt**
- enforces **JSONSchema output validation**
- supports **multi-model routing** via `models.yaml`
- is orchestrated through a unified planning engine

---

### 🧠 Model Routing & LLM Adaptation
NovaCast dynamically selects LLMs depending on the task:
- **OpenAI**
- **Anthropic**
- **Ollama (Local inference)**
- Optional: Perplexity, Mistral, Gemini (extensible)

Features include:
- A/B testing flags  
- Experiment groups  
- Task-based model selection (creative vs. structured vs. rewriting)  
- Graceful fallback logic  

---

### 🔊 Multi-Engine TTS System
Unified access to text-to-speech providers:
- **Coqui TTS** (local/on-prem)
- **ElevenLabs**
- **Piper (fast local TTS)**

Supports:
- Voice profiles  
- Audio normalization  
- SSML-style prosody  
- Sentence-based segmentation  
- Caching layers  

---

### 🎥 Intelligent Video Builder (FFmpeg)
The video builder uses a layered approach:
- Scene-based timeline composition  
- Background footage selection  
- Text overlays & captions  
- Transitions & pacing  
- Audio ducking & mixing  
- Render profiles (TikTok, YouTube, 1080p, 720p, etc.)

---

### 📡 Social Publishing Integrations
Adapters for uploading generated videos to:
- **YouTube**
- **TikTok**
- **Twitter/X**

Each adapter follows:
- Rate-limit aware workflows  
- Retry strategies  
- Dry-run mode for local testing  

---

### 🧩 Workflow Orchestration Engine
A custom DSL-driven orchestration layer:
- `intent.py` – classify user intent  
- `planner.py` – define Plans, Steps, guards, validations  
- `orchestrator.py` – execute plan → dispatch → monitor  

The orchestrator coordinates:
- agents  
- workers  
- vector memory  
- policies  
- media processors  

---

### 🗄 Persistent Storage & Metadata
Backed by MongoDB:
- `assets` – media assets, signed URLs  
- `prompts` – versioned prompt registry  
- `schedules` – advanced recurrence patterns  
- `chat_sessions` – session state + vector memory keys  
- `job_logs` – pipeline execution logs  

Includes:
- Retry logic  
- Connection pooling  
- Strict Pydantic models  

---

### 🧠 Vector Memory Layer
Supports:
- Conversation memory  
- Script consistency tracking  
- Long-form content context  
- Scene continuity enforcement  

Powered by **FAISS/Chroma** with pluggable embeddings.

---

### ⏱ Distributed Workers & Scheduler
NovaCast uses:
- **Dramatiq / RabbitMQ / Kafka** (pluggable queue)
- Idempotent task execution  
- Backoff + jitter policies  
- APScheduler for automated recurring jobs  

Supports background:
- TTS rendering  
- Video generation  
- Uploading and publishing  
- Notifications  

---

### 📊 Observability & Telemetry
Production-grade monitoring:
- **Prometheus** metrics  
- **OpenTelemetry** tracing  
- **Structured JSON logs** with trace IDs  
- Error breadcrumbs  
- Long-job audit trail  

---

### 🔐 Security & Policy Layer
Includes:
- JWT + OAuth2  
- API keys  
- RBAC (role-based access control)  
- MFA-ready design  
- `policy.yaml` for content safety, moderation, and guardrails  
- Rate-limiting middleware  

---

### ☁️ Cloud-Ready Infrastructure
NovaCast ships with:
- **Kubernetes manifests** (Helm-ready)
- **Terraform scaffolding**  
- **Docker images**: API, Worker, E2E Runner  
- **GitHub Actions** for CI/CD (planned)
- Local storage adapters for development  

---

### 🛠 Developer-First Design
The repository is structured for developers:
- Clear layering between agents, services, core flow, and API  
- Strong typing (Pydantic, TypedDicts, JSONSchema)  
- Pre-commit formatting + linting  
- Comprehensive test scaffolding  
- Mock services for deterministic CI  

---

NovaCast is designed not only to *run*, but to *scale* — a modern AI system for real-world creative automation.


## High-Level Architecture

NovaCast is designed as a **modular, cloud-ready, multi-agent AI system** where each layer is cleanly separated and independently scalable.  
At its core, NovaCast orchestrates LLM agents, tool-augmented pipelines, vector memory, TTS engines, and video rendering components to produce complete, publish-ready media.

The architecture is built around the following layers:

---

### 🧠 1. Orchestrator Layer
The orchestrator acts as the **brain** of NovaCast.

Files:
- `core/orchestrator.py`
- `core/flow/intent.py`
- `core/flow/planner.py`

Responsibilities:
- Interpret user intent  
- Build an executable "Plan" (DSL)  
- Dispatch tasks to agents and workers  
- Track progress & retries  
- Guarantee consistent output  

---

### 🤖 2. Multi-Agent Layer
A set of specialized GenAI agents, each responsible for a segment of the pipeline.

Folder: `app/agents/`

Agents include:
- **Ideation Agent** – generate ideas, angles, content directions  
- **Outline Agent** – build structural narrative frameworks  
- **Script Agent** – produce full scripts  
- **Rewrite Agent** – polishing, adaptation, SEO-aware refinement  
- **Scene Describer Agent** – create detailed visual prompts  

Each agent:
- Uses its own **YAML prompt**
- Enforces **JSONSchema contracts**
- Uses model routing from `models.yaml`
- Supports deterministic retries

---

### 🗃 3. Data Layer (MongoDB + Vectorstore)
Folder: `app/db/`

Components:
- MongoDB models: assets, schedules, prompts, chat sessions, job logs  
- CRUD modules with async Motor integration  
- Vectorstore (FAISS/Chroma) for:
  - memory retention  
  - script consistency  
  - long-form contextual retrieval  

---

### 🗣 4. Media Processing Layer
Folder: `app/media/`

Components:
- **TTS Engine** – multi-provider (Coqui, ElevenLabs, Piper)  
- **Video Builder** – FFmpeg-based timeline renderer  
- **Publisher** – adapters for YouTube, TikTok, Twitter/X  

Responsibilities:
- Audio generation  
- Visual assembly  
- Export and upload workflows  

---

### 🌐 5. API Layer (REST + WebSocket)
Folder: `app/api/v1/`

Endpoints for:
- Chatbot (REST + WS streaming)  
- Media generation triggers  
- Prompt CRUD & versioning  
- Asset management  
- Schedules and recurrence rules  
- Model routing (A/B tests)  
- Health + readiness  

The API is secured with:
- OAuth2 / JWT  
- API keys  
- MFA-ready architecture  
- RBAC  

---

### ⚙️ 6. Worker & Scheduler Layer
Folder: `app/services/worker/` + `app/services/scheduler.py`

Workers do the heavy lifting:
- Rendering TTS  
- Building videos  
- Uploading & publishing  
- Encoding, merging, normalizing audio/video  

Features:
- Dramatiq/RabbitMQ/Kafka queue abstraction  
- Idempotent pipelines  
- Backoff + jitter  
- APScheduler for recurring content or publishing flows  

---

### 📈 7. Observability Layer
Folder: `app/services/telemetry/`

Provides:
- **Prometheus metrics**  
- **OpenTelemetry tracing**  
- **Structured JSON logs**  
- Request-scoped trace IDs  
- Pipeline audit logs  

This prepares NovaCast for real production environments.

---

### ☁️ 8. Infrastructure Layer
Folder: `infra/`

Includes:
- Kubernetes manifests (Helm-ready)  
- Terraform scaffolding  
- GitHub Actions templates  
- Dockerfiles for API, Worker, and E2E runner  
- Local development Docker Compose  

---

### 🧩 Architectural Flow Diagram

```text
                 ┌─────────────────────────┐
                 │        FastAPI API      │
                 │  REST | WS | Auth | CRUD│
                 └───────────────┬─────────┘
                                 │
                         (Intent Router)
                                 │
                 ┌───────────────▼───────────────┐
                 │          Orchestrator          │
                 │    Plan → Dispatch → Track     │
                 └───────────────┬───────────────┘
                                 │
           ┌──────────────────┬──┼──┬───────────────────┐
           ▼                  ▼      ▼                   ▼
   Ideation Agent      Outline Agent   Script Agent   Rewrite Agent
           │                  │             │               │
           └───────────────► Scene Describer Agent ◄────────┘
                                 │
                                 ▼
                           TTS Engine
                                 │
                                 ▼
                          Video Builder
                                 │
                                 ▼
                             Publisher(s)
                                 │
                 (YouTube / TikTok / X / Local Export)



## Project Structure

Below is the full directory layout of NovaCast.  
This structure reflects a production-oriented, modular architecture designed for multi-agent orchestration, media generation, scheduling, and cloud deployment.

```
NOVACAST/

├── app/
│   ├── main.py                          # FastAPI app + lifespan (DB/Telemetry/Worker init)
│   │
│   ├── api/
│   │   ├── deps/auth.py                 # JWT/OAuth2 + RBAC + MFA + API keys
│   │   └── v1/
│   │       ├── health.py                # Health + Readiness + Liveness probes
│   │       ├── chatbot.py               # REST/WS Chat + Streaming
│   │       ├── media.py                 # Script→TTS→Video→Publish pipeline trigger
│   │       ├── schedules.py             # CRUD + advanced recurrence rules
│   │       ├── assets.py                # CRUD + signed URLs (S3/GCS)
│   │       ├── prompts.py               # CRUD + version pinning + experiment flags
│   │       └── models_map.py            # Manage models.yaml + A/B model selection
│   │
│   ├── core/
│   │   ├── orchestrator.py              # Main brain: plan→dispatch→monitor
│   │   └── flow/
│   │       ├── intent.py                # User intent classification
│   │       └── planner.py               # DSL for Plans/Steps + validation engine
│   │
│   ├── agents/
│   │   ├── ideation_agent.py
│   │   ├── outline_agent.py
│   │   ├── script_agent.py
│   │   ├── rewrite_agent.py
│   │   └── scene_describer_agent.py
│   │
│   ├── prompt_agent/
│   │   ├── loader.py
│   │   ├── registry.py
│   │   ├── validators.py
│   │   └── types.py                     # JSONSchema enforced prompt contracts
│   │
│   ├── chatbot/
│   │   ├── session.py                   # Session state + vector memory
│   │   ├── middleware.py                # rate-limit + safe-content + policy.yaml
│   │   ├── tools.py                     # wiki/search/YouTube API connectors
│   │   └── pipelines.py
│   │
│   ├── media/
│   │   ├── tts_engine.py                # Multi-engine adapter (Coqui, ElevenLabs, Piper)
│   │   ├── video_builder.py             # FFmpeg/Pydub wrapper + template system
│   │   └── publisher.py                 # YouTube/TikTok/Twitter adapters
│   │
│   ├── db/
│   │   ├── connection.py                # Motor init + retry + connection pool
│   │   ├── models/
│   │   │   ├── asset.py
│   │   │   ├── schedule.py
│   │   │   ├── prompt.py
│   │   │   ├── chat_session.py
│   │   │   └── job_log.py
│   │   └── crud/
│   │       ├── assets.py
│   │       ├── schedules.py
│   │       ├── prompts.py
│   │       ├── chat_sessions.py
│   │       └── job_logs.py
│   │
│   ├── services/
│   │   ├── llm/
│   │   │   ├── base.py
│   │   │   ├── ollama_adapter.py
│   │   │   ├── openai_adapter.py
│   │   │   ├── anthropic_adapter.py      # add redundancy
│   │   │   └── factory.py
│   │   ├── vectorstore/                 # FAISS/Chroma + embeddings utils
│   │   ├── scheduler.py                 # APScheduler + distributed locks
│   │   ├── worker/
│   │   │   ├── queue.py                 # Dramatiq/RabbitMQ/Kafka (idempotent jobs)
│   │   │   └── tasks.py                 # render_tts/render_video/upload/notify
│   │   └── telemetry/
│   │       ├── metrics.py               # Prometheus + custom counters
│   │       └── tracing.py               # OpenTelemetry + context propagation
│   │
│   ├── config/
│   │   ├── settings.py                  # Pydantic Settings + Secrets Manager
│   │   ├── models.yaml
│   │   └── policy.yaml                  # Content Safety + moderation rules
│   │
│   └── utils/
│       ├── schema.py
│       ├── logging.py                   # JSON logs + trace IDs
│       ├── errors.py
│       └── retry.py                     # exponential backoff + jitter
│
├── storage/                             # Local mount / ephemeral
│   ├── assets/
│   ├── tmp/
│   └── logs/
│
├── infra/                               # ✅ IaC for cloud deployment
│   ├── k8s/                             # Helm charts / manifests
│   ├── terraform/                       # Optional infra provisioning
│   └── github-actions/                  # CI/CD workflows
│
├── tests/
│   ├── mocks/                           # Mock LLM/TTS/FFmpeg/Publisher
│   ├── perf/                            # Load/soak tests
│   ├── test_health.py
│   ├── test_crud_assets.py
│   ├── test_crud_schedules.py
│   ├── test_prompt_registry.py
│   ├── test_chatbot_intents.py
│   └── test_end_to_end_pipeline.py
│
├── scripts/
│   └── run_local_pipeline.py
│
├── docker/
│   ├── Dockerfile.api
│   ├── Dockerfile.worker
│   ├── nginx.conf
│   └── Dockerfile.e2e                   # test container
│
├── docker-compose.yml
├── Makefile
├── .env.example
├── .pre-commit-config.yaml
├── README.md
└── requirements.txt
```



## Core Pipeline  
### Idea → Outline → Script → Rewrite → Scenes → TTS → Video → Publish

NovaCast implements a fully automated **end-to-end media generation pipeline**, where each stage is handled by a dedicated AI agent or processing component.  
The pipeline is orchestrated through a DSL-based planning system (`planner.py`) and executed by the main orchestrator (`orchestrator.py`).

Below is a detailed view of each stage in the flow:

---

### 1️⃣ Ideation  
**Goal:** Convert a short user concept or prompt into several refined content ideas.  
**Handled by:** `ideation_agent.py`  
**Output:**  
- Title suggestions  
- Angles & themes  
- Audience framing  
- Variations (short-form, long-form, educational, storytelling, etc.)

This stage seeds the creative direction of the entire pipeline.

---

### 2️⃣ Outline  
**Goal:** Transform an idea into a structured, multi-section outline.  
**Handled by:** `outline_agent.py`  
**Output:**  
- Chapter breakdown  
- Section summaries  
- Key transitions  
- Visual pacing notes  

The outline forms the backbone that downstream agents follow.

---

### 3️⃣ Script Generation  
**Goal:** Produce a full, ready-to-narrate script based on the outline.  
**Handled by:** `script_agent.py`  
**Output:**  
- Narration text  
- Dialogue (if needed)  
- On-screen text cues  
- Scene pacing  
- Emotional and stylistic notes  

The script is delivered in a **structured JSON format**, validated by schema.

---

### 4️⃣ Script Refinement (Rewrite)  
**Goal:** Improve clarity, emotional resonance, pacing, SEO optimization, or stylistic alignment.  
**Handled by:** `rewrite_agent.py`  
**Output:**  
- Polished script  
- Optional variants (engaging, professional, humorous, cinematic)  

This stage ensures consistent tone and quality.

---

### 5️⃣ Scene-Level Visual Descriptions  
**Goal:** Generate detailed visual prompts for each scene.  
**Handled by:** `scene_describer_agent.py`  
**Output:**  
- Scene-by-scene camera notes  
- Visual prompt descriptions  
- Suggestions for background footage  
- Motion/transition recommendations  

These descriptions feed directly into the **video_builder** layer.

---

### 6️⃣ Text-to-Speech (TTS) Rendering  
**Goal:** Convert narration text into audio.  
**Handled by:** `media/tts_engine.py`  
**Engines Supported:**  
- Coqui TTS  
- ElevenLabs  
- Piper  

Features:
- Sentence splitting  
- Prosody control  
- Audio normalization  
- Voice profiles  
- Caching  

Result: a clean narration audio track.

---

### 7️⃣ Video Composition  
**Goal:** Build a cohesive video timeline using script + audio + scene descriptions.  
**Handled by:** `media/video_builder.py`  
**Core Components:**  
- FFmpeg timeline generation  
- Background footage selection  
- Text overlays  
- Transitions (cuts, fades, motion)  
- Audio sync against narration  
- Render presets (TikTok vertical, YouTube wide, etc.)

This stage produces the final video file.

---

### 8️⃣ Publishing  
**Goal:** Upload and distribute the generated video.  
**Handled by:** `media/publisher.py`  
**Supports:**  
- YouTube  
- TikTok  
- Twitter/X  
- Local export for testing  

Includes:
- OAuth flow (YouTube)  
- Retry logic  
- Safety checks  
- Thumbnail and description generation (optional future enhancement)

---

### 🌐 End-to-End Pipeline Diagram

```text
User Input
    │
    ▼
[Ideation Agent]
    │
    ▼
[Outline Agent]
    │
    ▼
[Script Agent] → [Rewrite Agent]
    │
    ▼
[Scene Describer Agent]
    │
    ▼
[TTS Engine]
    │
    ▼
[Video Builder]
    │
    ▼
[Publisher]





## Multi-Agent System

NovaCast uses a **modular, extensible multi-agent architecture** where each agent is responsible for a well-defined part of the media generation process.  
Agents communicate through the Orchestrator and follow strict, schema-validated contracts to ensure predictable, high-quality output.

All agents live under:
app/agents/

Each agent:
- Uses a dedicated **YAML prompt** (loaded by the Prompt Registry)
- Runs behind an **LLM adapter** (OpenAI / Anthropic / Ollama)
- Ensures structured output using **JSONSchema**
- Includes deterministic **retry logic**
- Supports model routing from `models.yaml`
- Is orchestrated via a **Plan** defined in `planner.py`

---

### 🎯 Agent Responsibilities

#### 🧠 Ideation Agent (`ideation_agent.py`)
**Purpose:**  
Generate creative ideas, angles, hooks, and content directions based on a short seed or user request.

**Outputs:**  
- Titles  
- Concepts  
- Themes  
- Target-audience framing  
- Idea variants  

---

#### 📝 Outline Agent (`outline_agent.py`)
**Purpose:**  
Transform a chosen idea into a structured outline that divides the story into logical sections.

**Outputs:**  
- Section list  
- Scene breakdown  
- Core narrative beats  
- Story pacing  

---

#### 🎬 Script Agent (`script_agent.py`)
**Purpose:**  
From a structured outline, generate a full script suitable for narration and video production.

**Outputs:**  
- Narration text  
- Dialogue  
- On-screen cues  
- Scene pacing instructions  
- Structured JSON payload (schema validated)

---

#### ✨ Rewrite Agent (`rewrite_agent.py`)
**Purpose:**  
Improve the script’s clarity, tone, pacing, emotional depth, or SEO/marketing alignment.

**Outputs:**  
- Refined script  
- Style-specific variations  
- More engaging or targeted writing  

---

#### 🎨 Scene Describer Agent (`scene_describer_agent.py`)
**Purpose:**  
Produce detailed scene-level visual descriptions for the video builder.

**Outputs:**  
- Camera instructions  
- Visual style prompts  
- Background suggestions  
- Mood/lighting notes  

This serves as the input for the **video_builder** component.

---

### 🧩 Agent Architecture

Each agent follows a similar internal structure:

## Database & Vector Memory

NovaCast uses a dual-layer storage architecture combining:

1. **MongoDB (via Motor)** — for all operational, metadata, and pipeline state  
2. **Vectorstore (FAISS/Chroma)** — for contextual retrieval, session memory, and long-form reasoning

This architecture supports both **high-throughput media pipelines** and **LLM-aware conversational workflows**.

---

### 🗄 MongoDB (Operational Data Layer)

All document models live under:

app/db/models/

and are managed by async CRUD modules:

app/db/crud/

NovaCast uses MongoDB to persist:

#### **1. Assets (`asset.py`)**
Stores references to:
- uploaded media  
- generated audio/video  
- signed URLs (S3/GCS/local)  
- content metadata (resolution, duration, hashes)  
- pipeline stage provenance  

#### **2. Prompts (`prompt.py`)**
A versioned registry of YAML prompt templates:
- A/B variations  
- experiment flags  
- model-specific tuning  
- schema-bound prompt definitions  

This integrates with the **Prompt Registry**.

#### **3. Schedules (`schedule.py`)**
Used by the scheduler to:
- store CRON/RRule patterns  
- map Jobs → Pipelines  
- track last-run / next-run  
- handle user-configured automation  

#### **4. Chat Sessions (`chat_session.py`)**
Tracks:
- session IDs  
- conversation metadata  
- vector memory keys  
- orchestrator plan UUIDs  

This enables persistent conversational workflows.

#### **5. Job Logs (`job_log.py`)**
A complete audit log for:
- pipeline execution  
- agent responses  
- failures / retries  
- worker lifecycle events  

Essential for debugging long-running media jobs.

---

### ⚙ Connection & Reliability

`app/db/connection.py` implements:

- Async Motor client initialization  
- Connection pooling  
- Exponential retry policies  
- Graceful shutdown on lifespan ending  
- Readiness/liveness probes  

Example:

```python
client = AsyncIOMotorClient(
    settings.MONGO_URI,
    maxPoolSize=settings.DB_POOL_SIZE,
    uuidRepresentation="standard",
)

             ┌─────────────────────┐
             │     Chat Session    │
             │   (chat_session.py) │
             └───────────┬─────────┘
                         │
                 memory_key (UUID)
                         │
             ┌───────────▼───────────┐
             │     Vectorstore        │
             │  (FAISS / Chroma)      │
             └───────────┬───────────┘
                         │
         ┌───────────────┼────────────────┬──────────────┐
         ▼               ▼                ▼               ▼
   Script Embeddings   Scene Memory   User Context   Brand Assets


## Media Engine (TTS, Video Builder, Publisher)

The Media Engine is responsible for converting structured narrative content into **audio**, **visual scenes**, and a fully rendered **video file** ready for publication.  
It is built to be modular, provider-agnostic, and optimized for long-running asynchronous workloads.

All media components live under:

---

# 🎤 Text-to-Speech (TTS) Engine

NovaCast includes a unified TTS engine with pluggable backends.

### Location

### Supported Providers
- **Coqui TTS** (local, GPU/CPU, high-quality)
- **ElevenLabs API**
- **Piper TTS** (fast, lightweight local model)

### Capabilities
- Sentence-level chunking
- Prosody & emphasis controls
- Voice presets (male/female/brand/neutral)
- Audio normalization (dBFS normalization)
- Silence trimming & padding
- Caching layer to avoid re-rendering
- Automatic fallback between providers

### Example TTS Flow

```text
Script JSON → Chunk sentences → Generate audio per chunk → Normalize → Concatenate → Export WAV/MP3
             ┌───────────────────────────┐
             │        Script JSON         │
             └──────────────┬────────────┘
                            │
                 ┌──────────▼──────────┐
                 │    Scene Builder    │
                 │ (scene_describer)   │
                 └──────────┬──────────┘
                            │ Scenes
                 ┌──────────▼──────────┐
                 │     TTS Engine      │
                 └──────────┬──────────┘
                        Audio Track
                            │
                 ┌──────────▼──────────┐
                 │    Video Builder    │
                 │   (FFmpeg engine)   │
                 └──────────┬──────────┘
                      Final Video.mp4
                            │
                 ┌──────────▼──────────┐
                 │     Publisher       │
                 │ YT / TikTok / X     │
                 └─────────────────────┘


## API Layer

NovaCast exposes a fully modular API surface built on **FastAPI**, providing both synchronous REST endpoints and real-time WebSocket streaming capabilities.  
The API layer is designed for:

- Triggering media generation pipelines  
- Managing prompts, assets, and schedules  
- Running chatbot conversations  
- Monitoring system health  
- Managing model routing and experiment flags  

All API routes live under:



---

# 🌐 Overview of API Capabilities

### Supported API Domains
- **Chatbot Interface** (REST + WS)
- **Media Pipeline Triggering**
- **Prompt Registry (CRUD)**
- **Asset Management (CRUD + signed URLs)**
- **Scheduling & Automation**
- **Model Routing & Experiments**
- **System Health & Diagnostics**

---

# 🩺 Health & Diagnostics API

### Location
app/api/v1/health.py

### Endpoints
- `GET /health/live` — Liveness probe  
- `GET /health/ready` — Readiness probe (DB + Worker connectivity)  
- `GET /health/metrics` — Prometheus metrics endpoint (optional)  

Used by:
- Kubernetes  
- Docker Compose  
- CI smoke tests  

---

# 💬 Chatbot API (REST + WebSocket)

### Location
app/api/v1/chatbot.py

### Features
- Real-time WebSocket streaming  
- Structured request/response envelopes  
- Integration with the **Orchestrator**  
- Hybrid tool usage (wiki/search/YouTube API connectors)  
- Memory persistence using `chat_session.py`  
- Rate-limiting + safety middleware  

### Endpoints

#### REST
- `POST /chat/text`  
- `POST /chat/with-tools`  

#### WebSocket
- `WS /chat/ws`  
  - Bi-directional streaming  
  - Token-by-token output  
  - Automatic reconnection support  

Payloads are strongly typed using Pydantic models.

---

# 🎬 Media Pipeline API

### Location
app/api/v1/media.py


### Responsibilities
- Trigger the pipeline: Idea → Script → Scenes → TTS → Video → Publish  
- Return job IDs for long-running tasks  
- Expose job status via `job_logs.py`  
- Allow synchronous or async execution  
- Accept configuration overrides:
  - target platform  
  - render profile  
  - voice  
  - model selection  

### Endpoints
- `POST /media/generate`  
- `GET  /media/job/{job_id}`  
- `POST /media/publish` (optional)

Pipeline execution is delegated to the Worker system.

---

# 🗂 Assets API

### Location
app/api/v1/assets.py


Manages all media files, including:
- Uploaded user assets  
- Generated audio/video  
- Temporary pipeline files  
- Signed URLs for S3/GCS (if enabled)  

### Endpoints
- `POST /assets/upload`
- `GET /assets/{id}`
- `DELETE /assets/{id}`
- `GET /assets/signed-url` (future S3/GCS integration)

---

# 🧩 Prompts API (Versioned Prompt Registry)

### Location
app/api/v1/prompts.py

Allows:
- CRUD operations  
- Version pinning for agent prompts  
- Enabling/disabling A/B variants  
- Managing prompt metadata:
  - schema version  
  - model compatibility  
  - experiment flags  

### Endpoints
- `GET /prompts/{name}`
- `POST /prompts/`
- `PUT /prompts/{name}`
- `DELETE /prompts/{name}`
- `GET /prompts/versions/{name}`

---

# 🧠 Model Map API (A/B Testing & Routing)

### Location
app/api/v1/models_map.py


This API controls:
- Which model each agent uses  
- Feature flags  
- Experimental settings  
- A/B testing strategies  

### Endpoints
- `GET /models-map`
- `PUT /models-map`
- `POST /models-map/refresh`

Backed by `config/models.yaml`.

---

# ⏱ Scheduler API

### Location
app/api/v1/schedules.py


Enables programmatic creation of:
- recurring media generation jobs  
- CRON / RRule schedules  
- per-user or system-wide automation  

### Endpoints
- `POST /schedules/`
- `GET /schedules/{id}`
- `PUT /schedules/{id}`
- `DELETE /schedules/{id}`
- `POST /schedules/trigger/{id}`

Integrates with:
- APScheduler  
- worker queue  
- job logs  

---

# 🔐 Authentication & Security

### Location
app/api/deps/auth.py


Implements:
- OAuth2 Password/JWT  
- API Keys  
- RBAC roles  
- Optional MFA  
- Token expiration / refresh  
- Bearer token enforcement  

Paired with:
config/policy.yaml

for content safety and moderation.

---

# 📑 Summary

The API layer provides a clean, well-structured, production-grade interface for controlling every aspect of NovaCast:

- conversation  
- media generation  
- prompt management  
- automation  
- model routing  
- observability  
- publishing  

It is designed for both **human developers** and **automated agents**, making NovaCast a flexible and scalable platform for AI-driven media workflows.

## Worker System & Scheduler

NovaCast is designed for **long-running, CPU/GPU-heavy operations** such as text-to-speech rendering, FFmpeg video processing, background uploads, and recurring automated jobs.  
To support this, the system includes a dedicated **distributed worker layer** plus a **scheduler** for recurring tasks.

All worker-related code lives under:
app/services/worker/


The scheduler component lives here:
app/services/scheduler.py



---

# ⚙ Worker System

The worker architecture is built for durability, idempotency, and distributed execution across multiple nodes.

### Components

#### **1. Queue Abstraction**
app/services/worker/queue.py



This module provides a unified interface over multiple queue backends:

- **Dramatiq**
- **RabbitMQ**
- **Kafka**
- (future) Redis Streams

It exposes:
- `enqueue(job)`  
- `retry(job)`  
- `ack(job)`  
- `fail(job)`  

allowing NovaCast to run locally (Dramatiq) or in distributed cloud setups (RabbitMQ/Kafka).

---

#### **2. Worker Tasks**
app/services/worker/tasks.py

Tasks include:
- `render_tts` – generate narration audio  
- `render_video` – assemble scenes with FFmpeg  
- `upload_video` – send output to YouTube/TikTok/X  
- `notify_user` – webhook or email notifications  
- `cleanup_job` – remove temp files  

Each task is **idempotent** (safe to retry) and includes:
- metadata attachment  
- backoff + jitter retry logic  
- structured job logging into MongoDB  

---

#### **3. Job Logging**
Backed by the collection:
db/models/job_log.py


Tracks:
- job creation time  
- pipeline stage  
- runtime  
- retries  
- worker hostname  
- final status (success/error)  

This creates a fully auditable media generation history.

---

# ⏱ Scheduler (APScheduler + Distributed Locks)

The scheduler enables **automated content creation**, such as:

- "Publish a video every morning at 09:00"
- "Generate a TikTok summary of market news every hour"
- "Run the entire pipeline nightly with topic X"

### Location
app/services/scheduler.py


### Features
- CRON expressions  
- RRule recurrence (RFC 5545)  
- Distributed locking (to avoid duplicate executions)  
- Coordinated with worker queue  
- Auto-retry on failures  
- Skip logic if job is already running  

### Backing Storage
db/models/schedule.py
and
db/crud/schedules.py


---

# 📡 Scheduler Flow Diagram

```text
 ┌───────────────────────┐
 │   schedule.py (DB)    │
 └───────────┬───────────┘
             │ load rules
 ┌───────────▼───────────┐
 │   scheduler.py        │
 │  (APScheduler loop)   │
 └───────────┬───────────┘
             │ enqueue job
 ┌───────────▼───────────┐
 │     queue.py          │
 └───────────┬───────────┘
             │ dispatched
 ┌───────────▼───────────┐
 │     worker node       │
 │     tasks.py          │
 └────────────────────────┘


## Observability & Telemetry

NovaCast is built with **production-grade observability** to ensure that long-running media pipelines, LLM agent workflows, and asynchronous worker tasks can be monitored, debugged, and optimized effectively.

The system integrates three major observability pillars:

1. **Metrics (Prometheus)**
2. **Distributed Tracing (OpenTelemetry)**
3. **Structured Logging (JSON logs with trace IDs)**

All telemetry modules live under:
app/services/telemetry/

---

# 📊 Metrics (Prometheus)

### Location
app/services/telemetry/metrics.py


NovaCast exposes custom Prometheus metrics for:

### **Pipeline Performance**
- Agent execution time  
- Pipeline duration  
- Time spent per stage (Ideation → Outline → Script → Scenes → TTS → Render → Publish)  
- Number of retries  

### **Media Engine Metrics**
- TTS render time  
- FFmpeg render duration  
- Upload time per platform  

### **API Metrics**
- Request latency  
- Error rate  
- WS message throughput  
- Rate-limit counters  

### **Queue & Worker Metrics**
- Jobs queued  
- Jobs completed  
- Jobs failed  
- Jobs retried  
- Worker uptime  

### Example Metric

```text
novacast_pipeline_duration_seconds{stage="render_video"} 42.3

Observability Architecture Diagram

                    ┌──────────────────────────┐
                    │        FastAPI API        │
                    └────────────┬──────────────┘
                                 │  trace_id
                                 ▼
                    ┌──────────────────────────┐
                    │       Orchestrator        │
                    └────────────┬──────────────┘
                                 │  metrics/logs
                                 ▼
                    ┌──────────────────────────┐
                    │         Workers           │
                    └──────┬───────┬────────────┘
                           │       │
                           │       │
                           ▼       ▼
                   [TTS Engine]  [Video Builder]
                           │       │
                           └───────┘
                            metrics/logs

      ┌───────────────────────────────────────────────────────────┐
      │                Observability Backends                     │
      │  Prometheus   |   OpenTelemetry   |   JSON Log Collector  │
      └───────────────────────────────────────────────────────────┘

## Security & Governance

NovaCast is designed with **production-grade security**, including authentication, authorization, policy enforcement, sensitive-operation protection, and content-level governance for AI agents.  
Security is enforced across the entire stack: API → Orchestrator → Agents → Workers → Storage.

All security components live under:
app/api/deps/auth.py
config/policy.yaml
app/chatbot/middleware.py


---

# 🔐 Authentication

NovaCast implements multiple authentication methods suitable for both internal systems and public API consumers.

### Supported Authentication Methods

### **1. OAuth2 + JWT**
The primary authentication mechanism.

Features:
- Access tokens + refresh tokens  
- Token expiration enforcement  
- User identity claims  
- HMAC or RSA signing (configurable)  

### **2. API Keys**
Suitable for automation and worker-to-worker communication.

Features:
- Per-client API keys  
- Rate-limit tiers  
- Ability to rotate keys without downtime  

### **3. Optional MFA (Design-ready)**
Architecture supports pluggable MFA providers (TOTP, SMS, email).

---

# 👥 Authorization (RBAC)

NovaCast includes **Role-Based Access Control**, mapping users and API keys to roles:

### Default Roles
- `admin` – full access  
- `editor` – can generate content, manage prompts, but not schedules  
- `automation` – worker/job-only permissions  
- `viewer` – read-only access  

RBAC affects:
- Prompt registry access  
- Schedule management  
- Asset deletion  
- Model routing changes  
- Admin-only endpoints  

---

# 📦 Secrets Management

NovaCast supports multiple secrets backends:

- `.env` (development)
- Docker secrets  
- Kubernetes secrets  
- Vault / AWS Secrets Manager / GCP Secret Manager (ready)

All sensitive values come through:
app/config/settings.py


with Pydantic-managed validation/sanitization.

---

# 🛡 API Hardening

NovaCast includes a variety of protections to ensure safe operation in production-scale environments.

### **1. Rate Limiting**
Located in:
app/chatbot/middleware.py


Features:
- per-IP quotas  
- per-token quotas  
- burst vs. sustained thresholds  
- optional Redis-backed distributed rate limiting  

### **2. CORS Policies**
Configurable whitelist for:
- frontend domains  
- mobile clients  
- integrations  

### **3. Request Validation**
Performed via:
- Pydantic schemas  
- JSONSchema for agent outputs  
- Size limits for uploads  
- Strict type enforcement  

---

# 🔏 Content Safety & Moderation (policy.yaml)

Beyond technical security, NovaCast includes **AI safety** and content controls.

### Location
config/policy.yaml


### Capabilities
- Disallowed content categories  
- Safe-mode for LLMs  
- Profanity filtering  
- Sexual/violent content restrictions  
- Metadata tagging for sensitive topics  
- Escalation logic for dangerous outputs  
- Tools disabled when unsafe (e.g., YouTube search toolblock)

These policies are enforced at runtime by:
- Chatbot middleware  
- Orchestrator safety checks  
- Agent-level validation  

---

# 🧾 Governance & Prompt Safety

The Prompt Registry enforces strict governance over agent behavior:

### Governance Features
- Version pinning (deterministic pipelines)  
- Approved/locked prompts  
- Experiment isolation (A/B flags)  
- Schema-validated agent outputs  
- Human override mechanisms  

This ensures:
- reproducibility  
- safety  
- compliance  
- change auditing  

### Prompt Change Audit Trail
Every prompt update writes:
- timestamp  
- user ID  
- old version hash  
- new version hash  
- change summary  

Stored in:
db/models/prompt.py


---

# 🔍 Storage Security

NovaCast secures storage at multiple levels:

### Local Development
- isolated storage under `storage/`  
- file-level permission checks  

### Cloud Deployment
- S3/GCS signed URLs  
- time-limited read/write access  
- MIME validation (avoid harmful uploads)  
- optional object encryption (SSE-S3 / KMS)  

---

# 🔐 Worker Security

Worker nodes authenticate securely using:
- API keys  
- service roles  
- restricted IAM permissions (cloud mode)  
- encrypted environment variables  

Tasks involving external services (e.g., YouTube upload) use:
- scoped OAuth tokens  
- short-lived credentials  
- never store raw tokens in logs  

---

# 🧯 Security Architecture Diagram

```text
                     ┌───────────────────────────────┐
                     │           FastAPI API           │
                     │  OAuth2 / JWT / API Keys / RBAC │
                     └───────────────┬────────────────┘
                                     │
                           (Auth + Policy Checks)
                                     │
                     ┌───────────────▼───────────────┐
                     │         Orchestrator           │
                     │  Safety hooks + validation     │
                     └───────────────┬───────────────┘
                                     │
                      ┌──────────────┼──────────────┐
                      ▼              ▼              ▼
                 Agents         Vectorstore     Media Engine
             (prompt rules)   (safe embeddings)  (safe uploads)
                      │              │              │
                      └─────── Secure Worker Nodes ─┘


## Setup & Installation

NovaCast is a modular, production-grade system composed of:
- A FastAPI backend  
- A distributed worker service  
- A vectorstore  
- MongoDB  
- Optional TTS/FFmpeg dependencies  
- Dockerized runtime environments  

This section explains how to set up NovaCast for local development, testing, and production deployments.

---

# 🧰 Requirements

### **System Requirements**
- **Python 3.10+**
- **FFmpeg** (required for video rendering)
- **MongoDB 6+**
- **Make** (optional but recommended)
- **Docker & Docker Compose** (for full stack)

### **Recommended Hardware**
- 16 GB RAM minimum  
- 4+ CPU cores  
- Optional GPU for Coqui TTS acceleration  

---

# 📦 Install Dependencies

### Clone the repository

```bash
git clone https://github.com/<your-username>/NovaCast.git
cd NovaCast

🧪 Create a Virtual Environment
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.\.venv\Scripts\activate   # Windows

Install Python dependencies:
pip install -r requirements.txt

⚙ Environment Configuration

NovaCast uses a central .env file for all settings.

Copy the example:
cp .env.example .env

Edit the following fields:
MONGO_URI=mongodb://localhost:27017/novacast
JWT_SECRET=your_jwt_secret
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
OLLAMA_HOST=http://localhost:11434

Optional TTS providers:
ELEVENLABS_API_KEY=
COQUI_TTS_MODEL=

Optional cloud settings:
S3_BUCKET=
GCP_BUCKET=

### ▶️ Running NovaCast Locally

NovaCast consists of:

* API server

* Worker process

* Optional scheduler

* MongoDB

* Vectorstore (local folder or Chroma)

Run everything with Docker Compose
docker-compose up --build

Start the API server
uvicorn app.main:app --reload

Start the Worker
python -m app.services.worker.queue

Start the Scheduler
python -m app.services.scheduler

🧬 Initialize Vectorstore

NovaCast supports:

* FAISS

* ChromaDB

By default it uses a local Chroma instance inside storage/.
python scripts/init_vectorstore.py

macOS
brew install ffmpeg

Ubuntu / Debian
sudo apt-get update
sudo apt-get install ffmpeg


## ✅ Completed vs Not Completed (Based on `architecture.text`)

This section summarizes **what is fully scaffolded** vs **what is missing or not yet implemented** across the NovaCast repository.  
It reflects the current state of the project folder (`c:\Users\eyals\MyProjects\NovaCast`).

---

# ✅ Completed (Scaffolded / Present)

The following components **exist in the repository** and represent the full planned architecture.  
Most are **placeholders** and require implementation.

### 📁 Project Structure (Folders + Root Files)
- Full folder hierarchy present:
  - `app/`, `storage/`, `infra/`, `tests/`, `docker/`, `scripts/`
- Root files exist:
  - `Makefile`, `.env.example`, `requirements.txt`, `README.md`, `docker-compose.yml`

### 📦 All Modules & Files Scaffolded
Every planned module has a file present (even if empty or partial):
- `app/main.py`
- `app/api/*`
- `app/core/*`
- `app/agents/*`
- `app/prompt_agent/*`
- `app/chatbot/*`
- `app/media/*`
- `app/db/*`
- `app/services/*`
- `app/config/*`
- `app/utils/*`

### 🧪 Tests & Mocks (Declared)
- Test folders exist under `tests/`
- Mocks folder exists under `tests/mocks/`
- Test files declared but **contain placeholders**

### ☁ Infra + Docker
- `infra/k8s/` manifests exist (scaffold)
- `infra/terraform/` exists (empty skeleton)
- `.github-actions/` folder present (scaffold)
- `docker/` contains Dockerfiles for:
  - API
  - Worker
  - E2E runner
  - Nginx config

### ⚙ Config Templates
- `config/settings.py`
- `config/models.yaml`
- `config/policy.yaml`

All templates exist but are **not implemented**.

---

# ❌ Not Completed (Missing or Unimplemented Work)

Below is the full list of modules and systems that still require real implementation.

---

## 📝 app/main.py
Missing:
- FastAPI lifespan
- DB startup
- Telemetry initialization
- Worker queue startup
- Graceful shutdown logic

---

## 🗄 Database Layer (MongoDB)
Missing implementations:

### `db/connection.py`
- Motor client
- Retry policies
- Pooling
- Health checks

### `db/models/*`
No real Pydantic schemas for:
- `asset`
- `schedule`
- `prompt`
- `chat_session`
- `job_log`

### `db/crud/*`
CRUD operations not implemented.  
No unit tests.

---

## 🌐 API Layer
Most endpoints in `api/v1/*.py` are **empty stubs**.

Missing:
- Real handlers
- Validation models
- Auth enforcement
- Rate limits
- Integration with orchestrator

### `api/deps/auth.py`
Missing:
- JWT
- OAuth2
- API-key logic
- RBAC
- MFA hooks

---

## 🤖 Services & Integrations

### `services/llm/*`
- Base class is stub
- No working adapter:
  - OpenAI
  - Anthropic
  - Ollama  
  (No concrete implementation completed)

### `services/vectorstore`
- FAISS/Chroma wrapper missing
- Embeddings provider missing

### `services/worker/queue.py`
- No queue integration (Dramatiq / RabbitMQ / Kafka)

### `services/worker/tasks.py`
Missing:
- render_tts
- render_video
- upload_video
- cleanup
- idempotency logic

---

## 🎥 Media Engine

Missing core implementations:

### `media/tts_engine.py`
- Providers not fully implemented
- No chunking/normalization/caching

### `media/video_builder.py`
- No FFmpeg integration
- No templates or timeline engine

### `media/publisher.py`
- No YouTube/TikTok/X adapters implemented

---

## 🧠 Core Logic

Missing:

### `core/orchestrator.py`
- Plan execution
- Dispatching logic
- Retry/recovery
- Monitoring

### `core/flow/*.py`
- Intent classifier logic
- DSL plan builder

---

## 📝 Prompt Agent

Missing:
- YAML loader implementation
- Registry engine
- Prompt versioning
- JSONSchema validation engine

---

## 💬 Chatbot Layer

Missing:
- `session.py` state machine
- Safety middleware
- LLM-based hybrid tools
- Chat pipelines

---

## ⏱ Scheduler + Telemetry

### `services/scheduler.py`
- APScheduler job loop
- Distributed lock
- Job routing

### `services/telemetry/*`
Missing:
- Prometheus metrics wiring
- OpenTelemetry setup

---

## 🧪 Tests & Mocks
Missing:
- Mock LLM
- Mock TTS
- Mock FFmpeg
- Mock publisher
- Real unit tests + E2E tests

---

## 🛠 Infra / CI / Ops

Missing:
- K8s deployments
- Terraform resources
- GitHub Actions workflows wired
- Dockerfiles not fully runnable

---

## 🔐 Security
Missing:
- secrets manager
- validated Pydantic settings
- policy.yaml enforcement in middleware

---

# 🚀 Immediate Next Steps (MVP Path)

The fastest path to a working MVP:

1. **Implement `app/main.py` + config + DB connection**
2. **Complete one working DB model (e.g., Asset)**
3. **CRUD implementation + API + unit tests**
4. **Implement a mock LLM adapter**
5. **Implement a minimal chatbot endpoint**
6. **Implement a simple pipeline worker:**
   - script → mock TTS → mock video builder → asset storage
7. **Add CI pipeline for tests + linting**

This will give NovaCast its first **end-to-end functional loop**.


