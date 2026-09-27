# FLAMORIS

**Creative tools for humans and AI with too many ideas.** 🥸

FLAMORIS is an open-source creative ecosystem spanning illustration, animation, video, generative media, AI agents, and the infrastructure that connects them.

We build tools where humans and AI can work in the same creative space, while keeping product state, permissions, and authorship understandable.

## What we build

- 🎨 **Creative applications** — 2D animation, image decomposition and repair, video editing, compositing, and production tools.
- 🤖 **AI & generation** — generative media, AI agents, intelligence gateways, and creative automation.
- 🔌 **Shared infrastructure** — MCP, logging, Studio, runtime coordination, and the small pieces that keep everything talking to everything else.

## 🗺️ Repository map

FLAMORIS is a small ecosystem rather than one giant application. Each repository has a deliberately bounded role.

### 🎨 Creative apps

| Repository | Role |
|---|---|
| [flamoris-2D](https://github.com/flamoris-jp/flamoris-2D) | AI-native 2D animation editor for character motion and MV production. |
| [flamoris-cutwork](https://github.com/flamoris-jp/flamoris-cutwork) | Fast cutout, masking, repair, and part editing for 2D artwork. |
| [flamoris-kachinco](https://github.com/flamoris-jp/flamoris-kachinco) | AI-native video editor with timeline editing, effects, compositing, and MCP-driven workflows. |

### 🎛️ Workspace

| Repository | Role |
|---|---|
| [flamoris-studio](https://github.com/flamoris-jp/flamoris-studio) | Multi-user creative control center connecting AI and production tools. |
| [flamoris-studio-client](https://github.com/flamoris-jp/flamoris-studio-client) | Local bridge between Studio and desktop files, media, and production tools. |

### 🤖 AI

| Repository | Role |
|---|---|
| [flamoris-ai-agent](https://github.com/flamoris-jp/flamoris-ai-agent) | Persistent FLAMORIS-aware Agent with conversations, memory, knowledge, prompts, and tools. |
| [flamoris-ai-runtime](https://github.com/flamoris-jp/flamoris-ai-runtime) | Model-adjacent execution runtime for inference, workflows, jobs, interrupts, capabilities, and real-time traces. |
| [Oblivionis](https://github.com/flamoris-jp/Oblivionis) | Experimental non-LLM dynamic state and memory model built around oscillation, forgetting, association, recall, and evolving internal state. |
| [flamoris-intelligence-mcp](https://github.com/flamoris-jp/flamoris-intelligence-mcp) | Provider-neutral MCP gateway for language, reasoning, and coding AI. |
| [flamoris-generation-mcp](https://github.com/flamoris-jp/flamoris-generation-mcp) | Provider-neutral generative-media gateway for image, video, music, voice, and related media workflows. |

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

```text
                    🌱 FLAMORIS
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
 🎨 Creative Apps    🎛️ Studio        🤖 AI
 2D / Cutwork       Studio / Client   Agent / AI Runtime
 Kachinco                              Oblivionis
                                      Intelligence MCP
                                      Generation MCP
        │                │                │
        └────────────────┼────────────────┘
                         ▼
                 🔌 Runtime & MCP
                 MCP Hub / GPU Manager
                         │
                         ▼
                 🧱 Shared Foundations
                 MCP Core / Logging
                     Commons
```

This is an orientation map, not a strict dependency graph. The detailed authority boundaries live in the individual repositories.

## 🧠 AI & runtime authority map

The current non-desktop AI/runtime side is split by authority rather than by machine name:

- 🧪 [flamoris-generation-mcp](https://github.com/flamoris-jp/flamoris-generation-mcp) — generative-media workflows, jobs, providers, and assets.
- 🧠 [flamoris-intelligence-mcp](https://github.com/flamoris-jp/flamoris-intelligence-mcp) — provider-neutral language, reasoning, and coding gateway.
- 🌱 [flamoris-ai-agent](https://github.com/flamoris-jp/flamoris-ai-agent) — persistent Agent state and bounded Agent MCP surface.
- ⚙️ [flamoris-ai-runtime](https://github.com/flamoris-jp/flamoris-ai-runtime) — model-adjacent inference/workflow execution, jobs, interrupts, capabilities, and structured runtime events.
- 🌘 [Oblivionis](https://github.com/flamoris-jp/Oblivionis) — experimental non-LLM dynamic state and memory model; intentionally keeps an independent model identity while remaining callable from FLAMORIS AI Runtime.
- 🎛️ [flamoris-studio](https://github.com/flamoris-jp/flamoris-studio) — multi-user web creative control plane.
- 🔀 [flamoris-mcp-hub](https://github.com/flamoris-jp/flamoris-mcp-hub) — namespaced MCP aggregation and routing.
- 🖥️ [flamoris-gpu-node-manager](https://github.com/flamoris-jp/flamoris-gpu-node-manager) — provider-neutral local GPU/runtime lifecycle authority.

Machine names such as **LIME** are deployment identities, not public service identities.

> Creating strange and beautiful things with humans, AI, and too many ideas.

## Development status / 開発ステータス

<!-- development-status:start -->
_Status is synchronized automatically from the `development_status` organization custom property. Public repositories only._

| Status | Repositories |
|---|---|
| `stable` | [flamoris-logging](https://github.com/flamoris-jp/flamoris-logging), [flamoris-mcp-core](https://github.com/flamoris-jp/flamoris-mcp-core) |
| `development` | [flamoris-2D](https://github.com/flamoris-jp/flamoris-2D), [flamoris-ai-agent](https://github.com/flamoris-jp/flamoris-ai-agent), [flamoris-ai-runtime](https://github.com/flamoris-jp/flamoris-ai-runtime), [flamoris-cutwork](https://github.com/flamoris-jp/flamoris-cutwork), [flamoris-generation-mcp](https://github.com/flamoris-jp/flamoris-generation-mcp), [flamoris-gpu-node-manager](https://github.com/flamoris-jp/flamoris-gpu-node-manager), [flamoris-intelligence-mcp](https://github.com/flamoris-jp/flamoris-intelligence-mcp), [flamoris-kachinco](https://github.com/flamoris-jp/flamoris-kachinco), [flamoris-mcp-hub](https://github.com/flamoris-jp/flamoris-mcp-hub), [flamoris-studio](https://github.com/flamoris-jp/flamoris-studio) |
| `planned` | [flamoris-studio-client](https://github.com/flamoris-jp/flamoris-studio-client), [Oblivionis](https://github.com/flamoris-jp/Oblivionis) |
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

## 🗺️ Repository Map

FLAMORISは、ひとつの巨大アプリではなく、役割ごとに分かれた小さなエコシステムです。

### 🎨 制作アプリ

| Repository | 役割 |
|---|---|
| [flamoris-2D](https://github.com/flamoris-jp/flamoris-2D) | キャラクターモーションやMV制作のためのAIネイティブ2Dアニメーションエディタ。 |
| [flamoris-cutwork](https://github.com/flamoris-jp/flamoris-cutwork) | 2D原画の切り抜き・マスク・修復・パーツ編集を高速に行うツール。 |
| [flamoris-kachinco](https://github.com/flamoris-jp/flamoris-kachinco) | タイムライン編集・エフェクト・コンポジット・MCP workflowを扱うAIネイティブ動画編集ツール。 |

### 🎛️ 制作ハブ

| Repository | 役割 |
|---|---|
| [flamoris-studio](https://github.com/flamoris-jp/flamoris-studio) | AIと制作ツールをつなぐマルチユーザーのクリエイティブ・コントロールセンター。 |
| [flamoris-studio-client](https://github.com/flamoris-jp/flamoris-studio-client) | Studioとローカルのファイル・メディア・制作ツールをつなぐブリッジ。 |

### 🤖 AI・知能系

| Repository | 役割 |
|---|---|
| [flamoris-ai-agent](https://github.com/flamoris-jp/flamoris-ai-agent) | Conversation・Memory・Knowledge・Prompt・Toolを持つ永続的なFLAMORIS Agent。 |
| [flamoris-ai-runtime](https://github.com/flamoris-jp/flamoris-ai-runtime) | 推論・Workflow・Job・割り込み・Capability・リアルタイム観測を同じ実行層で扱うmodel-adjacent AI Runtime。 |
| [Oblivionis](https://github.com/flamoris-jp/Oblivionis) | 振動・忘却・連想・想起と時間変化する内部状態を扱う、実験的な非LLM動的状態・記憶モデル。 |
| [flamoris-intelligence-mcp](https://github.com/flamoris-jp/flamoris-intelligence-mcp) | 言語・推論・Coding AIを扱うprovider-neutralなMCP gateway。 |
| [flamoris-generation-mcp](https://github.com/flamoris-jp/flamoris-generation-mcp) | 画像・動画・音楽・音声と関連media workflowを扱うprovider-neutralな生成MCP。 |

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

```text
                    🌱 FLAMORIS
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
   🎨 制作アプリ      🎛️ Studio       🤖 AI
 2D / Cutwork       Studio / Client   Agent / AI Runtime
 Kachinco                              Oblivionis
                                      Intelligence MCP
                                      Generation MCP
        │                │                │
        └────────────────┼────────────────┘
                         ▼
                  🔌 Runtime & MCP
                  MCP Hub / GPU Manager
                         │
                         ▼
                     🧱 共通基盤
                  MCP Core / Logging
                      Commons
```

これは厳密な依存関係図ではなく、**初見で迷子にならないための案内図**です。詳細なauthority境界は各Repositoryを正とします。🗺️

## 🧠 AI・runtimeの責任分界

AI/runtime側は、マシン名ではなく**責任範囲（authority）**で分けています。

- 🧪 [flamoris-generation-mcp](https://github.com/flamoris-jp/flamoris-generation-mcp) — generative-mediaのworkflow・job・provider・asset。
- 🧠 [flamoris-intelligence-mcp](https://github.com/flamoris-jp/flamoris-intelligence-mcp) — provider-neutralな言語・推論・Coding gateway。
- 🌱 [flamoris-ai-agent](https://github.com/flamoris-jp/flamoris-ai-agent) — 永続Agent stateとbounded Agent MCP surface。
- ⚙️ [flamoris-ai-runtime](https://github.com/flamoris-jp/flamoris-ai-runtime) — model-adjacentな推論・Workflow実行、Job、割り込み、Capability、structured runtime event。
- 🌘 [Oblivionis](https://github.com/flamoris-jp/Oblivionis) — 実験的な非LLM動的状態・記憶モデル。FLAMORIS AI Runtimeから呼び出せる一方、意図的に独立したモデルidentityを保つ。
- 🎛️ [flamoris-studio](https://github.com/flamoris-jp/flamoris-studio) — マルチユーザーのWeb creative control plane。
- 🔀 [flamoris-mcp-hub](https://github.com/flamoris-jp/flamoris-mcp-hub) — namespaced MCP aggregation / routing。
- 🖥️ [flamoris-gpu-node-manager](https://github.com/flamoris-jp/flamoris-gpu-node-manager) — provider-neutralなローカルGPU/runtime lifecycle authority。

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
