# FLAMORIS

![FLAMORIS: I JUST WANT TO MAKE AN MV](flamoris-jp.png)

**Creative tools for humans and AI with too many ideas.** 🥸

FLAMORIS is an open-source creative ecosystem spanning illustration, animation, video, generative media, AI agents, and the infrastructure that connects them.

We build tools where humans and AI can work in the same creative space, while keeping product state, permissions, and authorship understandable.

## What we build

- 🎨 **Creative applications** — 2D animation, image decomposition and repair, video editing, compositing, and production tools.
- 🤖 **AI & generation** — generative media, AI agents, intelligence gateways, and creative automation.
- 🔌 **Shared infrastructure** — MCP, logging, Studio, runtime coordination, and the small pieces that keep everything talking to everything else.

## 🚀 Start here

**I just want to make an MV!** 🎬 FLAMORIS grew from that creative goal into a set of tools for making and connecting media. You do not have to understand every repository to get started.

| I want to… | Explore | Where to start |
|---|---|---|
| 🎬 **CREATE** a music video | 2D animation, cutout artwork, video editing | [2D](https://github.com/flamoris-jp/flamoris-2D) · [Cutwork](https://github.com/flamoris-jp/flamoris-cutwork) · [Kachinco](https://github.com/flamoris-jp/flamoris-kachinco) |
| ✨ **GENERATE** creative materials | Studio workspace, image/audio generation, language intelligence | [Studio](https://github.com/flamoris-jp/flamoris-studio) · [Generation Controller](https://github.com/flamoris-jp/flamoris-generation-controller) · [Intelligence](https://github.com/flamoris-jp/flamoris-intelligence-mcp) |
| 🔌 **CONNECT** humans and AI | Agent conversations, external MCP access, tool routing | [AI Agent](https://github.com/flamoris-jp/flamoris-ai-agent) · [Generation MCP](https://github.com/flamoris-jp/flamoris-generation-mcp) · [MCP Hub](https://github.com/flamoris-jp/flamoris-mcp-hub) |
| ⚙️ **OPERATE** the environment | Runtime lifecycle, managed updates, observability | [GPU Node Manager](https://github.com/flamoris-jp/flamoris-gpu-node-manager) · [Updater](https://github.com/flamoris-jp/flamoris-updater) · [Observer](https://github.com/flamoris-jp/flamoris-observer) |

**New to FLAMORIS?** Start with the creative applications or Studio. Building an integration? Follow the AI/MCP repositories. Looking for technical boundaries? Read the [AI architecture](https://github.com/flamoris-jp/flamoris-ai/blob/main/docs/ARCHITECTURE.md) and the repository map below.

> The map describes roles, not installation readiness. Features, release maturity and live acceptance vary by project; each repository's own README is authoritative.

## 🗺️ Repository map

FLAMORIS is a small ecosystem rather than one giant application. Each repository has a deliberately bounded role.

### 🎨 Creative apps

| Repository | Role |
|---|---|
| [flamoris-2D](https://github.com/flamoris-jp/flamoris-2D) | AI-native 2D animation editor for character motion and MV production. |
| [flamoris-cutwork](https://github.com/flamoris-jp/flamoris-cutwork) | Fast cutout, masking, repair, and part editing for 2D artwork. |
| [flamoris-kachinco](https://github.com/flamoris-jp/flamoris-kachinco) | AI-native video editor with timeline editing, effects, compositing, and MCP editing tools. |

### 🎛️ Workspace

| Repository | Role |
|---|---|
| [flamoris-studio](https://github.com/flamoris-jp/flamoris-studio) | Multi-user creative control center connecting AI and production tools. |
| [flamoris-studio-client](https://github.com/flamoris-jp/flamoris-studio-client) | Local bridge between Studio and desktop files, media, and production tools. |

### 🤖 AI

| Repository | Role |
|---|---|
| [flamoris-ai-agent](https://github.com/flamoris-jp/flamoris-ai-agent) | Persistent FLAMORIS-aware Agent with conversations, memory, knowledge, prompts, and tools. |
| [flamoris-ai-runtime](https://github.com/flamoris-jp/flamoris-ai-runtime) | Model-adjacent inference runtime owning ExecuteFlow, compiled ExecutionPlan, jobs, interrupts, resources, and execution traces. |
| [Maidionis](https://github.com/flamoris-jp/Maidionis) | Specialization-neutral foundation for training, evaluating, and packaging small bounded task-specific AI models. |
| [Arbitrium](https://github.com/flamoris-jp/Arbitrium) | First Maidionis Decision specialization for bounded advisory judgments over supplied evidence. |
| [Oblivionis](https://github.com/flamoris-jp/Oblivionis) | Experimental non-LLM model exploring experience-dependent AI behavior through oscillatory firing and runtime modulation, with forgetting and associative recall. |
| [flamoris-intelligence-mcp](https://github.com/flamoris-jp/flamoris-intelligence-mcp) | Shared non-MCP provider adapters for language, reasoning, and coding, with an optional external MCP facade. |
| [flamoris-generation-mcp](https://github.com/flamoris-jp/flamoris-generation-mcp) | External MCP facade for the shared Generation Controller, with protocol validation, provenance ingress and content mapping. |
| [flamoris-generation-controller](https://github.com/flamoris-jp/flamoris-generation-controller) | Implemented MCP-free generation core: provider recipes, jobs, inputs and assets, with authenticated internal HTTP. |

### 🔌 Runtime & MCP

| Repository | Role |
|---|---|
| [flamoris-mcp-hub](https://github.com/flamoris-jp/flamoris-mcp-hub) | Single-entry MCP aggregation and namespaced routing across multiple MCP servers. |
| [flamoris-gpu-node-manager](https://github.com/flamoris-jp/flamoris-gpu-node-manager) | Provider-neutral local GPU/runtime lifecycle and resource coordination. |

### 🧱 Shared foundations

| Repository | Role |
|---|---|
| [flamoris-mcp-core](https://github.com/flamoris-jp/flamoris-mcp-core) | Shared MCP infrastructure for FLAMORIS applications and tools. |
| [flamoris-logging](https://github.com/flamoris-jp/flamoris-logging) | Shared structured logging and diagnostics foundation. |
| [flamoris-commons](https://github.com/flamoris-jp/flamoris-commons) | Shared architecture, policies, and ecosystem foundations. |

### 🧭 Coordination & meta

| Repository | Role |
|---|---|
| [flamoris-ai](https://github.com/flamoris-jp/flamoris-ai) | Architecture boundaries and roadmap coordination for FLAMORIS AI. |
| [.github](https://github.com/flamoris-jp/.github) | Organization profile and shared GitHub configuration. |

This map describes repository responsibilities and explicitly marked future scope. Detailed contracts and acceptance evidence live in the individual repositories; [FLAMORIS AI progress](https://github.com/flamoris-jp/flamoris-ai/blob/main/PROGRESS.md) separates source completion, pending live acceptance, and held work.

## 🧠 AI & runtime authority map

The current non-desktop AI/runtime side is split by authority rather than by machine name:

- 🧪 [flamoris-generation-mcp](https://github.com/flamoris-jp/flamoris-generation-mcp) — bounded generation requests/recipes, provider execution, jobs, inputs, and assets; domain code and the external MCP adapter currently share this package.
- 🧭 [flamoris-generation-controller](https://github.com/flamoris-jp/flamoris-generation-controller) — a future common non-MCP generation contract; documentation only, with design and implementation held.
- 🧠 [flamoris-intelligence-mcp](https://github.com/flamoris-jp/flamoris-intelligence-mcp) — shared provider adapters in `flamoris_intelligence`, plus the optional external MCP facade.
- 🌱 [flamoris-ai-agent](https://github.com/flamoris-jp/flamoris-ai-agent) — optional personality, conversations, memory, and principal/session policy; internal JSON HTTP and a separate external Agent MCP surface.
- ⚙️ [flamoris-ai-runtime](https://github.com/flamoris-jp/flamoris-ai-runtime) — inference and ExecuteFlow, compiled ExecutionPlan, jobs, interrupts, resources, and structured runtime events.
- 🧩 [Maidionis](https://github.com/flamoris-jp/Maidionis) — specialization-neutral training, evaluation, artifact, and bounded inference contracts for small specialized AI models.
- ⚖️ [Arbitrium](https://github.com/flamoris-jp/Arbitrium) — the first Maidionis specialization, owning Decision-specific tasks, curricula, research evidence, and bounded advisory judgments.
- 🌘 [Oblivionis](https://github.com/flamoris-jp/Oblivionis): experimental non-LLM state/memory model whose history-shaped firing is intended to supply runtime fluctuation; it retains its independent model identity and Runtime owns execution.
- 🎛️ [flamoris-studio](https://github.com/flamoris-jp/flamoris-studio) — multi-user web creative control plane.
- 🔀 [flamoris-mcp-hub](https://github.com/flamoris-jp/flamoris-mcp-hub) — namespaced MCP aggregation and routing.
- 🖥️ [flamoris-gpu-node-manager](https://github.com/flamoris-jp/flamoris-gpu-node-manager) — provider-neutral local GPU/runtime lifecycle authority.

MCP Hub aggregates external entry points such as ChatGPT. Studio raw Intelligence and Agent execution use the shared provider adapters directly; Studio Agent Support uses Agent JSON HTTP. Studio generation uses authenticated Controller HTTP; Generation MCP and Studio share one Controller authority. Accepted source and pending live rollout are tracked in [AI progress](https://github.com/flamoris-jp/flamoris-ai/blob/main/PROGRESS.md). `ComfyWorkFlow` means a ComfyUI graph/API-format JSON executed by ComfyUI; Runtime owns `ExecuteFlow` and its compiled `ExecutionPlan`. See the [current AI architecture](https://github.com/flamoris-jp/flamoris-ai/blob/main/docs/ARCHITECTURE.md).

Maidionis separates reusable specialization machinery from specialization semantics: Maidionis owns specialization-neutral model/training/evaluation/artifact contracts, while Arbitrium owns Decision-specific semantics and research evidence. AI Runtime remains the execution/orchestration authority around those models.

Oblivionis explores **experience → changing state → firing → runtime modulation → changed behavior**. Using a response to modulate execution is distinct from using it to start new work. These are planned integration boundaries: AI Runtime retains execution authority, and Profundumis handles latent association/recall rather than ordinary firing. See the [AI ecosystem map](https://github.com/flamoris-jp/flamoris-ai/blob/main/docs/ai-ecosystem.md) and the [Oblivionis model concept](https://github.com/flamoris-jp/Oblivionis/blob/main/docs/MODEL.md).

Machine names such as **LIME** are deployment identities, not public service identities.

> Creating strange and beautiful things with humans, AI, and too many ideas.

## Development status / 開発ステータス

<!-- development-status:start -->
_Status is synchronized automatically from the `development_status` organization custom property. Public repositories only._

| Status | Repositories |
|---|---|
| `stable` | [flamoris-gpu-node-manager](https://github.com/flamoris-jp/flamoris-gpu-node-manager), [flamoris-logging](https://github.com/flamoris-jp/flamoris-logging), [flamoris-mcp-core](https://github.com/flamoris-jp/flamoris-mcp-core) |
| `development` | [Arbitrium](https://github.com/flamoris-jp/Arbitrium), [flamoris-2D](https://github.com/flamoris-jp/flamoris-2D), [flamoris-ai-agent](https://github.com/flamoris-jp/flamoris-ai-agent), [flamoris-ai-runtime](https://github.com/flamoris-jp/flamoris-ai-runtime), [flamoris-cutwork](https://github.com/flamoris-jp/flamoris-cutwork), [flamoris-generation-mcp](https://github.com/flamoris-jp/flamoris-generation-mcp), [flamoris-intelligence-mcp](https://github.com/flamoris-jp/flamoris-intelligence-mcp), [flamoris-kachinco](https://github.com/flamoris-jp/flamoris-kachinco), [flamoris-mcp-hub](https://github.com/flamoris-jp/flamoris-mcp-hub), [flamoris-studio](https://github.com/flamoris-jp/flamoris-studio), [Maidionis](https://github.com/flamoris-jp/Maidionis), [Oblivionis](https://github.com/flamoris-jp/Oblivionis) |
| `planned` | [flamoris-studio-client](https://github.com/flamoris-jp/flamoris-studio-client) |
| `meta` | [.github](https://github.com/flamoris-jp/.github), [flamoris-ai](https://github.com/flamoris-jp/flamoris-ai), [flamoris-commons](https://github.com/flamoris-jp/flamoris-commons) |
<!-- development-status:end -->

## Use it however you like 🥸
<sub>Within the terms of the Apache License 2.0.</sub>

Modify it, build it into something else, or use it to make something interesting or strange 🤣🤣

Commercial use is welcome too 👍  
You do not need our permission.  
If you feel like telling us what you made with FLAMORIS, we'd be happy to hear about it.  
Completely optional.

FLAMORIS software is provided as-is.  
There is no guaranteed individual support or warranty.

If you run into trouble, let your AI assistant read the README, documentation, Issues, and source code and help you work it out 👹

If FLAMORIS helps you, or you simply find it interesting, support for development is always appreciated.  
It helps FLAMORIS keep growing. 🌱  
[💖 Sponsor FLAMORIS](https://github.com/sponsors/flamoris-jp)  
<sub>Mostly GPU bills and things like that.</sub>

> Characters, illustrations, music, video, and other creative works by **artist FLAMORIS** are not necessarily covered by the Apache License 2.0.

---

# FLAMORIS

**人とAIと、ちょっと多すぎるアイデアのための制作環境。** 🥸

FLAMORISでは、イラスト、アニメーション、映像、生成AI、AIエージェント、そしてそれらをつなぐ基盤まで、オープンソースのクリエイティブツールを作っています。

人とAIが同じ制作空間で一緒に作りながらも、作品の状態や権限、誰が何を作ったのかが分からなくならない仕組みを目指しています。

## つくっているもの

- 🎨 **制作アプリ** — 2Dアニメーション、画像の切り抜き・修復、動画編集、コンポジット、制作ツール。
- 🤖 **AI・生成系** — 画像・動画・音楽・音声などの生成、AIエージェント、知能系ゲートウェイ、制作自動化。
- 🔌 **共通基盤** — MCP、Logging、Studio、runtime連携、そして全部をつなぐ小さな仕組みたち。

## 🚀 はじめての方へ

**「MVを作りたい！」** 🎬 その思いから、FLAMORISは制作アプリとAI、そして両者をつなぐ仕組みへ広がりました。最初から全リポジトリを理解する必要はありません。

| やりたいこと | できること | 入口 |
|---|---|---|
| 🎬 **CREATE** 作品を作る | 2Dアニメ、画像のパーツ編集、動画編集 | [2D](https://github.com/flamoris-jp/flamoris-2D) · [Cutwork](https://github.com/flamoris-jp/flamoris-cutwork) · [Kachinco](https://github.com/flamoris-jp/flamoris-kachinco) |
| ✨ **GENERATE** 素材を生み出す | Studio、画像・音声などの生成、知能機能 | [Studio](https://github.com/flamoris-jp/flamoris-studio) · [Generation Controller](https://github.com/flamoris-jp/flamoris-generation-controller) · [Intelligence](https://github.com/flamoris-jp/flamoris-intelligence-mcp) |
| 🔌 **CONNECT** AIとつなぐ | エージェントとの対話、MCP公開、ツール連携 | [AI Agent](https://github.com/flamoris-jp/flamoris-ai-agent) · [Generation MCP](https://github.com/flamoris-jp/flamoris-generation-mcp) · [MCP Hub](https://github.com/flamoris-jp/flamoris-mcp-hub) |
| ⚙️ **OPERATE** 環境を支える | GPUランタイム管理、更新、観測 | [GPU Node Manager](https://github.com/flamoris-jp/flamoris-gpu-node-manager) · [Updater](https://github.com/flamoris-jp/flamoris-updater) · [Observer](https://github.com/flamoris-jp/flamoris-observer) |

**制作したい人**は制作アプリやStudioから。**AI連携を作りたい人**はAgentやMCPへ。全体の仕組みを知りたい人は[AIアーキテクチャ](https://github.com/flamoris-jp/flamoris-ai/blob/main/docs/ARCHITECTURE.md)と下のリポジトリ地図をどうぞ。

> この案内は各リポジトリの役割を示すもので、インストール可能・実機検証済みを保証するものではありません。成熟度や対応機能は各リポジトリのREADMEを確認してください。

## 🗺️ Repository Map

FLAMORISは、ひとつの巨大アプリではなく、役割ごとに分かれた小さなエコシステムです。

### 🎨 制作アプリ

| Repository | 役割 |
|---|---|
| [flamoris-2D](https://github.com/flamoris-jp/flamoris-2D) | キャラクターモーションやMV制作のためのAIネイティブ2Dアニメーションエディタ。 |
| [flamoris-cutwork](https://github.com/flamoris-jp/flamoris-cutwork) | 2D原画の切り抜き・マスク・修復・パーツ編集を高速に行うツール。 |
| [flamoris-kachinco](https://github.com/flamoris-jp/flamoris-kachinco) | タイムライン編集・エフェクト・コンポジット・MCP編集ツールを扱うAIネイティブ動画編集ツール。 |

### 🎛️ 制作ハブ

| Repository | 役割 |
|---|---|
| [flamoris-studio](https://github.com/flamoris-jp/flamoris-studio) | AIと制作ツールをつなぐマルチユーザーのクリエイティブ・コントロールセンター。 |
| [flamoris-studio-client](https://github.com/flamoris-jp/flamoris-studio-client) | Studioとローカルのファイル・メディア・制作ツールをつなぐブリッジ。 |

### 🤖 AI・知能系

| Repository | 役割 |
|---|---|
| [flamoris-ai-agent](https://github.com/flamoris-jp/flamoris-ai-agent) | Conversation・Memory・Knowledge・Prompt・Toolを持つ永続的なFLAMORIS Agent。 |
| [flamoris-ai-runtime](https://github.com/flamoris-jp/flamoris-ai-runtime) | 推論・ExecuteFlow・コンパイル済みExecutionPlan・Job・割り込み・リソース・実行観測を所有するmodel-adjacent AI Runtime。 |
| [Maidionis](https://github.com/flamoris-jp/Maidionis) | 小さな専門AIを教育・評価・packageするためのspecialization-neutralな共通基盤。 |
| [Arbitrium](https://github.com/flamoris-jp/Arbitrium) | Maidionis最初のDecision specialization。与えられたevidenceに対するboundedな助言判断を担当。 |
| [Oblivionis](https://github.com/flamoris-jp/Oblivionis) | 経験で変わる振動状態の発火からRuntimeへ揺らぎを与え、AIの振る舞いを変えることを目指す、忘却・連想・想起を持つ実験的な非LLMモデル。 |
| [flamoris-intelligence-mcp](https://github.com/flamoris-jp/flamoris-intelligence-mcp) | 言語・推論・Codingの非MCP provider adapterと、任意の外部MCP facadeを持つ共通package。 |
| [flamoris-generation-mcp](https://github.com/flamoris-jp/flamoris-generation-mcp) | 共通Generation Controllerの外部MCP facade。protocol検証・provenance ingress・content mappingを担当。 |
| [flamoris-generation-controller](https://github.com/flamoris-jp/flamoris-generation-controller) | 実装済みの非MCP生成core。provider recipe・job・input・assetと認証付き内部HTTPを担当。 |

### 🔌 Runtime・MCP基盤

| Repository | 役割 |
|---|---|
| [flamoris-mcp-hub](https://github.com/flamoris-jp/flamoris-mcp-hub) | 複数MCPを名前空間付きで集約・ルーティングする単一の入口。 |
| [flamoris-gpu-node-manager](https://github.com/flamoris-jp/flamoris-gpu-node-manager) | ローカルGPU・AI runtimeの起動停止とリソース調整を担当するauthority。 |

### 🧱 共通基盤

| Repository | 役割 |
|---|---|
| [flamoris-mcp-core](https://github.com/flamoris-jp/flamoris-mcp-core) | FLAMORISアプリ・ツール共通のMCP基盤。 |
| [flamoris-logging](https://github.com/flamoris-jp/flamoris-logging) | 共通の構造化Logging・診断基盤。 |
| [flamoris-commons](https://github.com/flamoris-jp/flamoris-commons) | 共通architecture・policy・エコシステム基盤。 |

### 🧭 設計・運用

| Repository | 役割 |
|---|---|
| [flamoris-ai](https://github.com/flamoris-jp/flamoris-ai) | FLAMORIS AI全体のarchitecture境界とroadmapを整理する管制塔。 |
| [.github](https://github.com/flamoris-jp/.github) | Organization profileと共通GitHub設定。 |

この地図は各Repositoryの責務と、将来構想として明記した範囲を案内します。詳細な契約・検証は各Repositoryを正とし、[FLAMORIS AIの進捗](https://github.com/flamoris-jp/flamoris-ai/blob/main/PROGRESS.md) でソース完了・実機未受け入れ・保留中の作業を区別します。🗺️

## 🧠 AI・runtimeの責任分界

AI/runtime側は、マシン名ではなく**責任範囲（authority）**で分けています。

- 🧪 [flamoris-generation-mcp](https://github.com/flamoris-jp/flamoris-generation-mcp) — 保持されたgeneration request/recipe、provider実行、job・input・asset。現状はdomain実装と外部MCP adapterが同じpackageに共存。
- 🧭 [flamoris-generation-controller](https://github.com/flamoris-jp/flamoris-generation-controller) — 将来の共通非MCP generation契約。文書のみで、具体設計・実装は保留。
- 🧠 [flamoris-intelligence-mcp](https://github.com/flamoris-jp/flamoris-intelligence-mcp) — `flamoris_intelligence` の共通provider adapterと、任意の外部MCP facade。
- 🌱 [flamoris-ai-agent](https://github.com/flamoris-jp/flamoris-ai-agent) — 任意の人格・Conversation・Memory・principal/session方針。内部JSON HTTPと、別の外部Agent MCP入口。
- ⚙️ [flamoris-ai-runtime](https://github.com/flamoris-jp/flamoris-ai-runtime) — 推論・ExecuteFlow・コンパイル済みExecutionPlan・Job・割り込み・リソース・structured runtime event。
- 🧩 [Maidionis](https://github.com/flamoris-jp/Maidionis) — 小さな専門AIを作るためのspecialization-neutralな学習・評価・artifact・bounded inference contract。
- ⚖️ [Arbitrium](https://github.com/flamoris-jp/Arbitrium) — Maidionis最初のDecision specialization。Decision固有のTaskSpec・curriculum・研究結果・bounded advisory judgmentを所有する。
- 🌘 [Oblivionis](https://github.com/flamoris-jp/Oblivionis): 経験で変わる発火をRuntimeの揺らぎへつなぐことを目指す、実験的な非LLM状態・記憶モデル。独立したモデルidentityを保ち、実行はRuntimeが所有する。
- 🎛️ [flamoris-studio](https://github.com/flamoris-jp/flamoris-studio) — マルチユーザーのWeb creative control plane。
- 🔀 [flamoris-mcp-hub](https://github.com/flamoris-jp/flamoris-mcp-hub) — namespaced MCP aggregation / routing。
- 🖥️ [flamoris-gpu-node-manager](https://github.com/flamoris-jp/flamoris-gpu-node-manager) — provider-neutralなローカルGPU/runtime lifecycle authority。

MCP HubはChatGPTなどの外部入口を集約します。Studioのraw IntelligenceとAgent内部の実行は共通provider adapterへ直接接続し、StudioのAgent SupportはAgent JSON HTTPを使います。StudioのGenerationは認証付きController HTTPを使い、Generation MCPと同じController authorityへ接続します。ソース受け入れと未完了の実機反映は [AI進捗](https://github.com/flamoris-jp/flamoris-ai/blob/main/PROGRESS.md) に記録します。`ComfyWorkFlow` はComfyUIが実行するグラフ・API-format JSON、`ExecuteFlow` とコンパイル済み `ExecutionPlan` はRuntimeの責務です。詳細は [現行AI architecture](https://github.com/flamoris-jp/flamoris-ai/blob/main/docs/ARCHITECTURE.md) を参照してください。

Maidionisはspecialization共通のmodel/training/evaluation/artifact contractを持ち、ArbitriumはDecision固有のsemanticsと研究証跡を持ちます。これらを実行・合成するauthorityはAI Runtime側に残します。

Oblivionisの狙いは、**経験 → 状態変化 → 発火 → Runtimeへの揺らぎ → 振る舞いの変化**。発火を実行中の振る舞いへ作用させることと、新しい処理を始めるトリガにすることは分けます。連携は構想段階で、実行のauthorityはAI Runtime側、深淵からの連想・想起はProfundumis側です。詳細は [AI全体地図](https://github.com/flamoris-jp/flamoris-ai/blob/main/docs/ai-ecosystem.md) と [Oblivionisのモデル概念](https://github.com/flamoris-jp/Oblivionis/blob/main/docs/MODEL.md) を参照してください。

**LIME**のようなマシン名はdeployment identityであり、公開サービスのidentityではありません。

> 人とAIと、ちょっと多すぎるアイデアで、変で美しいものをつくる。

## 勝手に使ってください🥸
<sub>※ Apache License 2.0 の範囲で</sub>

改造しても、組み込んでも、面白いものや変なものを作ってもOKです🤣🤣

商用作品や製品で使う場合も、許可は不要です👍  
もしよければ「こんなのに使ったよ」と教えてもらえるとうれしいです。  
もちろん強制ではありません。

FLAMORISのソフトウェアは現状のまま提供されます。  
個別サポートや動作保証はありません。

困ったときは、README、ドキュメント、Issue、ソースコードをあなたのAIに読ませて、自己サポートしてもらってください👹

もし、あなたのお役に立てたり、面白いと思っていただけたなら、  
開発費用をご支援いただけるとうれしいです。  
FLAMORISは元気になって育ちます。🌱  
[💖 FLAMORISを支援する](https://github.com/sponsors/flamoris-jp)  
<sub>主にGPU代とか。</sub>

> ソフトウェアコード以外の、キャラクター、イラスト、音楽、映像などの  
> **アーティスト FLAMORISの制作物**は、Apache License 2.0の対象とは限りません。
