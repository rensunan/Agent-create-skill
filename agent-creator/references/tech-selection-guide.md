# 技术选型参考指南

本文档为智能体创建过程中的技术选型提供参考，在阶段三加载使用。

---

## Agent 框架选择

| 框架 | 适用场景 | 特点 |
|------|---------|------|
| 原生 SDK（OpenAI/Anthropic） | 简单智能体，单一 LLM 调用 | 最轻量，零额外依赖，完全可控 |
| LangChain | 工具编排、复杂 Chain、RAG | 生态最丰富，社区大，抽象层级多 |
| LlamaIndex | 数据密集型 RAG 应用 | 数据索引能力最强，文档加载器丰富 |
| CrewAI | 多智能体协作 | 角色化智能体分工，任务委派 |
| AutoGen（微软） | 多智能体对话协作 | 智能体间自动对话，人工介入点 |
| Dify / Coze | 低代码/可视化搭建 | 拖拽式，适合非开发者或快速原型 |
| Semantic Kernel（微软） | .NET/企业级 | 与 Azure/AI SDK 深度集成 |

**决策建议**：能用原生 SDK 就不用框架。需要编排多工具时选 LangChain。
多智能体协作选 CrewAI 或 AutoGen。

---

## LLM 模型选型

| 场景 | 推荐 | 理由 |
|------|------|------|
| 简单对话/FAQ | GPT-4o-mini / Claude Haiku / DeepSeek-V3 | 低成本、低延迟 |
| 复杂推理/代码生成 | GPT-4o / Claude Sonnet / DeepSeek-R1 | 推理能力强 |
| 多模态（图片理解） | GPT-4o / Claude Sonnet / Gemini Flash | 原生多模态 |
| 长上下文处理 | Gemini 2.5 Pro / Claude Opus | 超长上下文窗口 |
| 国内/合规需求 | DeepSeek / Qwen / 百度文心 / 豆包 | 国内可用、合规 |
| 离线/本地部署 | Ollama + Qwen2.5 / Llama3 | 数据不出本地 |
| 高并发低成本 | GPT-4o-mini / DeepSeek-V3 | 高性价比 |

**成本估算参考（每百万 token）**：
| 模型 | 输入价格 | 输出价格 |
|------|---------|---------|
| GPT-4o-mini | $0.15 | $0.60 |
| GPT-4o | $2.50 | $10.00 |
| Claude Haiku | $0.25 | $1.25 |
| Claude Sonnet | $3.00 | $15.00 |
| DeepSeek-V3 | ¥1.00 | ¥4.00 |

---

## Prompt 策略

| 策略 | 说明 | 适用场景 |
|------|------|---------|
| System Prompt | 定义角色、能力边界、行为规范 | 所有智能体 |
| Few-shot 示例 | 在 Prompt 中给出输入→输出示例 | 格式约束、分类任务 |
| Chain-of-Thought | 引导模型"一步步思考" | 推理、数学、逻辑任务 |
| ReAct | 思考→行动→观察 循环 | 工具调用场景 |
| 结构化输出 | JSON Mode / Structured Outputs | 需要解析返回值的场景 |

**System Prompt 设计要点**：
- 明确角色（"你是一个xxx专家"）
- 列出能力（"你可以做xxx、xxx"）
- 明确限制（"你不能做xxx"）
- 给出行为规范（"回答简洁"、"遇到不确定就说不知道"）

---

## RAG 决策树

```
是否需要检索外部知识？
├── 否 → 纯 LLM 对话即可
└── 是 → 知识规模多大？
    ├── <1000条 → FAISS / Chroma（轻量级，本地运行）
    ├── 1000-100K条 → Milvus / Qdrant（生产级）
    └── >100K条 → Pinecone / Weaviate Cloud（托管服务）
```

---

## 向量数据库对比

| 方案 | 适用场景 | 特点 |
|------|---------|------|
| Chroma | 原型/小规模 | 零配置，Python原生，内置Embedding |
| FAISS | 高性能本地 | Meta出品，纯向量检索，极快 |
| Milvus | 生产级 | 分布式，混合检索，云原生 |
| Qdrant | 中型项目 | Rust编写，高性能，丰富过滤 |
| Pinecone | 免运维 | 全托管，自动扩缩容 |

---

## Embedding 模型选择

| 模型 | 维度 | 特点 |
|------|------|------|
| text-embedding-3-small | 512/1536 | OpenAI，性价比高 |
| text-embedding-3-large | 256/1024/3072 | OpenAI，精度最高 |
| bge-large-zh-v1.5 | 1024 | 中文最佳，本地部署 |
| moka-ai/m3e-base | 768 | 中文轻量，本地部署 |

---

## 重排序方案

| 方案 | 特点 | 适用 |
|------|------|------|
| Cross-encoder (bge-reranker) | 精度高，本地运行 | 对精度要求高的场景 |
| Cohere Rerank API | 托管服务，效果好 | 不想自己部署 |
| LLM-based Rerank | 用LLM直接排序 | 结果少（<20条），成本高 |

---

## 对话记忆方案

| 方案 | 适用场景 |
|------|---------|
| 滑动窗口（最近N轮） | 简单对话，短期记忆 |
| 摘要压缩 | 长对话，需保留核心信息 |
| 向量记忆 + 检索 | 需要跨会话记忆 |
| 数据库持久化 | 用户登录、长期档案 |

---

## 多智能体协作

| 模式 | 说明 | 适用 |
|------|------|------|
| 顺序流水线 | A→B→C 依次处理 | 数据处理流水线 |
| 分工协作 | 各智能体负责不同子任务 | 复杂任务拆解 |
| 辩论/评审 | 多个智能体互相评审 | 质量控制、安全检查 |
| 层级管理 | 一个管理者智能体分配任务 | 复杂项目管理 |

**框架推荐**：简单协作用原生 SDK 手写，复杂协作用 CrewAI 或 AutoGen。

---

## MCP（Model Context Protocol）

- MCP 是一种标准化协议，让 LLM 安全地访问外部工具和数据源
- 适合场景：需要对接多个外部服务、希望工具接口标准化
- 主流 MCP Server 已有：文件系统、数据库、API 封装、代码执行等
- 是否需要 MCP → 看外部工具是否已有 MCP Server 或是否需要跨平台复用

---

## 多模态支持

| 能力 | 方案 | 说明 |
|------|------|------|
| 图片理解 | GPT-4o / Claude Sonnet / Gemini Flash | 直接识别图片内容 |
| 图片生成 | DALL-E 3 / Stable Diffusion | 按需生成图片 |
| 语音输入（STT） | Whisper / Azure Speech | 语音转文字 |
| 语音输出（TTS） | OpenAI TTS / ElevenLabs / Edge TTS | 文字转语音 |
| 视频理解 | Gemini 2.5 Pro | 长视频内容分析 |

---

## Web部署方案

| 方案 | 适用场景 |
|------|---------|
| Gradio | 快速原型，内部工具，Python生态 |
| Streamlit | 数据应用，仪表盘 |
| Chainlit | 专为LLM对话设计 |
| Next.js + Vercel | 生产级Web应用，对外发布 |
| FastAPI + 静态HTML | 轻量API + 简单前端 |

---

## 函数调用 / Tool Use

- 需要调用外部API → OpenAI Function Calling / Claude Tool Use
- 需要执行代码 → 沙箱执行（E2B / Codex Sandbox）
- 需要数据库操作 → 直接集成相应SDK
- 不需要外部交互 → 跳过

---

## 评估策略

| 方案 | 说明 | 适用 |
|------|------|------|
| 人工评审 | 人工抽查回答质量 | 所有项目（必须） |
| 规则匹配 | 正则/关键词检查输出格式 | 结构化输出 |
| LLM-as-Judge | 用另一个LLM评分 | 开放式回答质量评估 |
| 评测集 + 指标 | 构建测试集，计算准确率/召回率 | 生产级项目 |
| A/B 测试 | 对比不同 Prompt/模型效果 | 持续优化 |

**最低要求**：至少要有人工抽查 5-10 个典型用例的机制。

---

## 安全实践

- **密钥管理**：所有密钥使用环境变量，提供 `.env.example`，`.env` 加入 `.gitignore`
- **速率限制**：API 调用加速率限制（token bucket / sliding window）
- **内容审核**：用户输入用 OpenAI Moderation API 或敏感词过滤
- **Prompt Injection 防护**：
  - 用户输入和 System Prompt 用分隔符隔离
  - 对用户输入中的"忽略上述指令"类攻击做关键词检测
  - 不将用户输入直接拼接到敏感的 System Prompt 中
- **SQL 注入防护**：使用参数化查询，禁止字符串拼接 SQL
- **文件安全**：文件操作限制在指定目录内，禁止路径遍历攻击