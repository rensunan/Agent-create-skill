# agent-creator — Codex Skill：AI 智能体全流程创建

> 以对话方式梳理需求、设计架构、技术选型、代码编写与测试交付，从零到一创建可本地运行的 AI 智能体。

## 简介

gent-creator 是一个 Codex Skill，提供创建 AI 智能体的完整工作流引导。通过**选项式对话交互**，逐步明确需求、设计框架、选择技术栈、编写规范化代码，最终交付可本地测试的智能体项目。



## 核心原则

| 原则 | 说明 |
|------|------|
| **选项式交互** | 用户只需输入数字即可选择，每轮末尾提供"0 = 都不满意，详细讨论" |
| **对话驱动** | 每阶段以对话形式推进，确认后再进入下一步 |
| **按需推荐** | 技术选型基于已确认的框架和流程，不堆砌无关选项 |
| **渐进明确** | 从粗到细，从框架到细节，逐步收敛 |
| **安全第一** | 密钥、API Key 一律使用环境变量或 .env 文件，代码中绝不硬编码 |
| **可回退** | 任何阶段不满意或需求变更，可回退到前面任意阶段重新讨论 |

## 工作流程

### 复杂度评估（入口）

| 级别 | 特征 | 流程 |
|------|------|------|
| **简单** | 单一功能、无外部依赖、本地运行、单轮交互 | 精简流程（阶段一 → 五 → 六） |
| **中等** | 多轮对话、有 RAG 或工具调用、需 Web 部署 | 完整流程（六个阶段全部执行） |
| **复杂** | 多智能体协作、多模态、复杂工作流、生产级 | 完整流程（每阶段更深入） |

### 六个阶段

1. **阶段一：需求梳理** — 通过选项式对话搞清核心需求（定位、规模、使用场景）
2. **阶段二：框架设计** — 设计整体架构、功能模块划分，输出流程图
3. **阶段三：技术选型** — 基于需求推荐 Agent 框架、LLM 模型、RAG、向量数据库等
4. **阶段四：整体确认** — 汇总前三阶段的决策，展示最终确认清单
5. **阶段五：代码编写** — 按规范编写完整项目代码（含目录结构、密钥保护、README）
6. **阶段六：测试与交付** — 编写冒烟测试、本地验证、交付测试接口

## 技术选型覆盖范围


eferences/tech-selection-guide.md 包含以下维度的详细对比与推荐：

- **Agent 框架**：原生 SDK / LangChain / LlamaIndex / CrewAI / AutoGen / Dify / Semantic Kernel
- **LLM 模型**：GPT-4o / Claude / DeepSeek / Gemini / 国内模型 / Ollama 本地部署
- **RAG 架构**：Chroma / FAISS / Milvus / Qdrant / Pinecone
- **Embedding**：OpenAI / bge-large-zh / m3e
- **重排序**：Cross-encoder / Cohere Rerank / LLM-based
- **对话记忆**：滑动窗口 / 摘要压缩 / 向量记忆 / 数据库持久化
- **多智能体协作**：顺序流水线 / 分工协作 / 辩论评审 / 层级管理
- **多模态**：图片理解 / 图片生成 / 语音输入输出 / 视频理解
- **Web 部署**：Gradio / Streamlit / Chainlit / Next.js / FastAPI
- **Prompt 策略**：System Prompt / Few-shot / CoT / ReAct / 结构化输出
- **评估策略**：人工评审 / 规则匹配 / LLM-as-Judge / 评测集
- **安全实践**：密钥管理 / 速率限制 / 内容审核 / Prompt Injection / SQL 注入防护

## 校验

运行 _validate.py 可检查 SKILL.md 的结构完整性：

`powershell
python _validate.py
`

校验项包括：frontmatter 完整性、选项式交互规范、六个阶段全覆盖。

## 使用方式

将此目录放置于 Codex 的 skills 目录（$CODEX_HOME/skills/）下，然后在对话中引用：

`
使用 agent-creator 创建一个新的 AI 智能体
`

触发后，Skill 将自动执行复杂度评估并进入对应流程。

## 环境要求

- Codex CLI 或 Codex Desktop（支持 Skill 加载）
- Python 3.10+（用于运行校验脚本）
- PyYAML（pip install pyyaml，用于校验脚本）
