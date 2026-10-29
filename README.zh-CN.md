<div align="center">

# Awesome Lifelong Agents

终身学习智能体：经验、记忆、技能与评测。

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Checks](https://github.com/logicwu0/awesome-lifelong-agents/actions/workflows/check.yml/badge.svg)](https://github.com/logicwu0/awesome-lifelong-agents/actions/workflows/check.yml)
[![Stars](https://img.shields.io/github/stars/logicwu0/awesome-lifelong-agents?style=flat)](https://github.com/logicwu0/awesome-lifelong-agents/stargazers)

[English](README.md) · [简体中文](README.zh-CN.md) · [Contribute](CONTRIBUTING.md)

</div>

## 关于本清单

关注 Agent 如何在任务与时间之间保留、复用和更新能力，不是开发 Agent 的入门教程。
当前收录 34 篇论文（含综述、基准和明确标记的相关方法），最近一批来源核查：2026-10-29（此前条目核查于 2026-10-18、2026-10-24、2026-10-25）。
这是人工维护的精选起点，不宣称全面覆盖，也没有复现这些论文的实验结果。
Awesome 徽章表示采用这一清单风格，不代表被官方总目录收录或背书。

“参数更新”指方法是否训练参数，不是运行过程中模型服务商是否更新版本；No 不代表没有模型调用成本。
年份采用 arXiv 首次提交年份，不混用会议发表年份。持久状态的具体范围应以原论文实验设置为准。

## 目录

- [综述与路线图](#surveys)
- [经验与反思](#experience)
- [长期记忆](#memory)
- [技能与适应](#skills)
- [持续训练与参数适应](#training)
- [基准与评测](#evaluation)
- [安全与能力保持](#safety)
- [相关方法与边界](#related)
- [评测检查清单](#evaluation-checklist)
- [相关资源](#resources)
- [Star History](#star-history)

<a id="surveys"></a>

## 综述与路线图

| 论文 | 年份 | 参数更新 | 保留内容 / 类型 | 要点与边界 |
| --- | --- | --- | --- | --- |
| [Lifelong Learning of Large Language Model based Agents: A Roadmap](https://arxiv.org/abs/2501.07278) | 2025 | Survey | Survey | 从感知、记忆和行动梳理终身学习智能体；是研究地图，不是算法实现。 |
| [Continual Learning of Large Language Models: A Comprehensive Survey](https://arxiv.org/abs/2404.16789) | 2024 | Survey | Model-level learning taxonomy | 区分持续预训练、领域适配与持续微调；是模型层背景综述，并非专门的 Agent 综述。 |

<a id="experience"></a>

## 经验与反思

| 论文 | 年份 | 参数更新 | 保留内容 / 类型 | 要点与边界 |
| --- | --- | --- | --- | --- |
| [ExpeL: LLM Agents Are Experiential Learners](https://arxiv.org/abs/2308.10144) | 2023 | No | Insights / experiences | 从执行经验中提取可复用知识，用于后续任务，不微调 Agent 的语言模型。 |
| [ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory](https://arxiv.org/abs/2509.25140) | 2025 | No | Reasoning memory | 从成功和失败经历提炼推理经验，供后续检索使用。 |
| [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) | 2023 | No | Reflective text | 利用反馈和情景记忆在多次尝试间改进；重复尝试本身不等于跨任务终身学习。 |
| [CLIN: A Continually Learning Language Agent for Rapid Task Adaptation and Generalization](https://arxiv.org/abs/2310.10134) | 2023 | No | Causal textual memory | 在尝试后更新因果文本记忆，并测试 ScienceWorld 中跨任务与环境迁移；结论需结合其具体实验设置。 |
| [LifeMem: Enabling Lifelong Experience Reuse for LLM Agents](https://arxiv.org/abs/2609.12655) | 2026 | No — memory updates | Workflow clusters / textual skills | 按工作流聚类轨迹并提取文本技能，用于跨环境经验检索；需关注任务顺序与轨迹采集成本，各任务收益并不一致。 |

<a id="memory"></a>

## 长期记忆

| 论文 | 年份 | 参数更新 | 保留内容 / 类型 | 要点与边界 |
| --- | --- | --- | --- | --- |
| [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) | 2023 | No | Observations / reflections | 通过观察记忆与反思支持模拟行为；属于相关记忆架构，不是遗忘评测基准。 |
| [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413) | 2025 | No | Conversation memories | 提取并管理对话记忆；记忆质量本身不能证明技能的持续学习。 |
| [A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110) | 2025 | No | Linked notes / evolving attributes | 构建并更新相互关联的记忆笔记；动态记忆组织本身不能证明终身技能保持。 |
| [Scaling Teams or Scaling Time? Memory Enabled Lifelong Learning in LLM Multi-Agent Systems](https://arxiv.org/abs/2604.03295) | 2026 | Not specified in abstract | Multi-agent experience memory | LLMA-Mem 研究连续任务中的记忆拓扑、团队规模与成本权衡；仅凭摘要不能确认所有组件均无需训练。 |
| [From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://arxiv.org/abs/2502.14802) | 2025 | No — non-parametric memory | Passages / retrieval graph | HippoRAG 2 结合段落整合、图检索与在线模型调用；知识检索收益不能证明工具技能的持续习得。 |
| [MemoryBank: Enhancing Large Language Models with Long-Term Memory](https://arxiv.org/abs/2305.10250) | 2023 | Memory updates; chatbot also fine-tuned | Conversation memory / user summaries | 结合检索与时间相关的记忆保持；须区分记忆机制与 SiliconFriend 微调，也要区分对话评测和终身任务学习。 |

<a id="skills"></a>

## 技能与适应

| 论文 | 年份 | 参数更新 | 保留内容 / 类型 | 要点与边界 |
| --- | --- | --- | --- | --- |
| [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) | 2023 | No | Executable skill library | 在 Minecraft 中结合自动课程、环境反馈和可复用代码技能库。 |
| [SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills](https://arxiv.org/abs/2504.07079) | 2025 | No | Reusable web APIs | 通过练习网站交互合成可复用 API；应将迁移与鲁棒性评测同已练习网站上的表现区分。 |
| [Learning from Research: Toward Lifelong Agent Harness Evolution](https://arxiv.org/abs/2609.40169) | 2026 | No — backbone fixed | Agent harness code | ScholarEvolve 利用研究文献指导工具调用、记忆与执行代码演化；需评估搜索成本和留出任务泛化，不能只看优化任务分数。 |
| [Agent Workflow Memory](https://arxiv.org/abs/2409.07429) | 2024 | No — workflow memory updates | Reusable textual workflows | 从行动轨迹抽象出可复用流程，指导后续网页任务；须区分离线归纳与在线积累，并考虑成功判定器的错误。 |

<a id="training"></a>

## 持续训练与参数适应

| 论文 | 年份 | 参数更新 | 保留内容 / 类型 | 要点与边界 |
| --- | --- | --- | --- | --- |
| [Learning While Acting: A Skill-Enhanced Test-Time Co-Evolution Framework for Online Lifelong Learning Agents](https://arxiv.org/abs/2606.04815) | 2026 | Yes — RL / online policy updates | Skills / policy parameters | LifeSkill 结合验证器指导的技能学习与在线参数内化；成本应包含验证器和训练，而不只是推理 Token。 |
| [Towards Practical Tool Usage for Continually Learning LLMs](https://arxiv.org/abs/2404.09339) | 2024 | Yes — continual fine-tuning | Tool-use model parameters / replay data | 通过合成任务和组合 NLP 任务研究工具模型持续学习，包含经验回放基线；并非任意真实 API 演化的完整基准。 |
| [Harness-Model Collaboration for Long-Horizon Continual Learning](https://arxiv.org/abs/2610.34724) | 2026 | Yes — LoRA / behavioral cloning | Experience cards / adapter / replay trajectories | HaMo 将可检索策略与经验条件训练、回放结合；成本需包含专家轨迹和参数适应，迁移结论应限定于已评测的网页任务设置。 |

<a id="evaluation"></a>

## 基准与评测

| 论文 | 年份 | 参数更新 | 保留内容 / 类型 | 要点与边界 |
| --- | --- | --- | --- | --- |
| [LifelongAgentBench: Evaluating LLM Agents as Lifelong Learners](https://arxiv.org/abs/2505.11942) | 2025 | N/A | Evaluation protocol | 用于评估 LLM 智能体终身学习；比较方法前需核对任务序列及允许保留的状态。 |
| [Evaluating Very Long-Term Conversational Memory of LLM Agents](https://arxiv.org/abs/2402.17753) | 2024 | N/A | Evaluation protocol | 提出 LoCoMo 长期对话记忆评测；可作补充，但不能替代持续任务学习评测。 |
| [SWE-Bench-CL: Continual Learning for Coding Agents](https://arxiv.org/abs/2507.00014) | 2025 | N/A | Chronological coding benchmark | 按时间顺序组织软件问题，考察经验积累与遗忘；需注意仓库版本及信息泄漏控制。 |
| [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://arxiv.org/abs/2410.10813) | 2024 | N/A | Long-term chat evaluation | 测试信息提取、多会话及时间推理、知识更新与拒答；对话记忆准确率不能衡量工具技能习得。 |
| [Continual Learning Bench: Evaluating Frontier AI Systems in Real-World Stateful Environments](https://arxiv.org/abs/2606.05661) | 2026 | N/A | Stateful evaluation / gain metric | 在六类领域中评估连续经验收益，用增益指标区分学习与初始能力；比较时应匹配预算及状态保留规则。 |
| [SkillLearnBench: Benchmarking Continual Learning Methods for Agent Skill Generation on Real-World Tasks](https://arxiv.org/abs/2604.20087) | 2026 | N/A | Skill-learning evaluation | 从技能质量、执行轨迹与任务结果评估 20 个任务；需区分外部反馈与自反馈，不能假设收益适用于所有任务。 |
| [Continual Learning Exam: Benchmarking Long-Horizon RSI and Experiential Learning in LLM Agents](https://arxiv.org/abs/2610.33956) | 2026 | N/A — evaluated models fixed | Five-level task ladders / persistent harness state | CLE 在连续职业任务中评估外部状态积累；须区分跨任务复用与反馈辅助重试，并考虑通关解锁机制及自动评分的影响。 |

<a id="safety"></a>

## 安全与能力保持

这些条目关注保留状态的风险和旧能力退化，不是可直接套用的安全保证。

| 论文 | 年份 | 参数更新 | 保留内容 / 类型 | 要点与边界 |
| --- | --- | --- | --- | --- |
| [Memory Injection Attacks on LLM Agents via Query-Only Interaction](https://arxiv.org/abs/2503.03704) | 2025 | N/A — security study | Poisoned persistent memory | MINJA 研究仅通过查询交互污染持久记忆的风险，不要求直接修改存储；属于威胁模型研究而非学习算法。旧标题为 A Practical Memory Injection Attack against LLM Agents。 |
| [Memory Poisoning Attack and Defense on Memory Based LLM-Agents](https://arxiv.org/abs/2601.05504) | 2026 | N/A — security study | Memory trust / sanitization | 在不同记忆与检索条件下研究 EHR 智能体记忆投毒及防御；防御需要阈值校准，不构成通用安全保证。 |
| [Do Self-Evolving Agents Forget? Capability Degradation and Preservation in Lifelong LLM Agent Adaptation](https://arxiv.org/abs/2605.09315) | 2026 | Varies by evolution channel | Workflows / skills / weights / memory | 研究工作流、技能、模型与记忆四类演化中的能力退化，提出 Capability-Preserving Evolution；应同时跟踪旧能力保持与新任务收益。 |
| [Auditing Self-Evolution in Financial Agents: Capability Gains, Security Drift, and Execution-Interface Mismatch](https://arxiv.org/abs/2608.17684) | 2026 | N/A — security audit | Evolved skills / workflows / memories | 在模拟银行环境审计任务效用、注入暴露和未授权状态修改；结论依赖威胁模型及执行器兼容性，不能只看总成功率。 |

<a id="related"></a>

## 相关方法与边界

| 论文 | 年份 | 参数更新 | 保留内容 / 类型 | 要点与边界 |
| --- | --- | --- | --- | --- |
| [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) | 2023 | No | Within-task feedback | 通过自反馈迭代修正答案；作为相关机制收录，不视为跨任务终身学习证据。 |
| [Learning to Prompt for Continual Learning](https://arxiv.org/abs/2112.08654) | 2021 | Prompts / keys / head | Learned parameters | 视觉持续学习背景：冻结主干并训练软提示等参数，不是 LLM Agent 的文本提示检索。 |
| [ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs](https://arxiv.org/abs/2307.16789) | 2023 | Yes — supervised fine-tuning | Tool-use model parameters | 包含工具使用数据、训练与评测；离线学习工具并不自动等于持续适应变化的 API。 |

<a id="evaluation-checklist"></a>

## 评测检查清单

- 明确任务顺序、训练/测试划分及测试答案是否可能进入记忆。
- 对比不保留经验、保留经验、打乱经验等基线，匹配模型与预算。
- 同时检查新任务收益、旧任务退化、Token/耗时及存储开销。
- 区分同题多次尝试、跨任务迁移和长期分布变化，不直接比较不同协议的分数。
- 记录模型版本、提示词、随机种子（如支持）及不确定性；检查错误经验与恶意内容传播。

<a id="resources"></a>

## 相关资源

- [Lifelong LLM Agent Roadmap](https://github.com/qianlima-lab/awesome-lifelong-llm-agent) — 相关综述配套清单，致谢其领域导航价值。
- [LifelongAgentBench](https://github.com/caixd-220529/LifelongAgentBench) — 基准代码入口。
- [AgentFoundry](https://github.com/logicwu0/AgentFoundry) — 同维护者的独立算法工具包，目前仅骨架，不是本清单论文的已完成复现。

## 贡献与维护

欢迎通过 Issue 或 PR 提交论文和更正；请遵循 [CONTRIBUTING.md](CONTRIBUTING.md).
暂不承诺固定更新频率；后续重点补充工具变化适应及已核实的官方代码入口，并深化全文方法核查。

## 模板与许可

结构改编自 [jthegedus/awesome-list-template](https://github.com/jthegedus/awesome-list-template) (CC0).
论文条目与解读独立整理。仓库原创内容使用 [CC0 1.0](LICENSE).
链接论文、软件与商标仍遵循各自许可；本清单与论文作者及相关项目无隶属关系。

<a id="star-history"></a>

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=logicwu0/awesome-lifelong-agents&type=Date)](https://www.star-history.com/#logicwu0/awesome-lifelong-agents&Date)

图表由第三方 Star History 提供。新仓库可能暂无数据，加载也可能受缓存或限流影响；不需要提交 GitHub Token。
