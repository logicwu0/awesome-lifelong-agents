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
初版收录 11 篇论文（含综述、基准和明确标记的相关方法），资料核查日期：2026-10-18。
这是人工维护的精选起点，不宣称全面覆盖，也没有复现这些论文的实验结果。
Awesome 徽章表示采用这一清单风格，不代表被官方总目录收录或背书。

“参数更新”指方法是否训练参数，不是运行过程中模型服务商是否更新版本；No 不代表没有模型调用成本。
年份采用 arXiv 首次提交年份，不混用会议发表年份。持久状态的具体范围应以原论文实验设置为准。

## 目录

- [综述与路线图](#surveys)
- [经验与反思](#experience)
- [长期记忆](#memory)
- [技能与适应](#skills)
- [基准与评测](#evaluation)
- [相关方法与边界](#related)
- [评测检查清单](#evaluation-checklist)
- [相关资源](#resources)
- [Star History](#star-history)

<a id="surveys"></a>

## 综述与路线图

| 论文 | 年份 | 参数更新 | 保留内容 / 类型 | 要点与边界 |
| --- | --- | --- | --- | --- |
| [Lifelong Learning of Large Language Model based Agents: A Roadmap](https://arxiv.org/abs/2501.07278) | 2025 | Survey | Survey | 从感知、记忆和行动梳理终身学习智能体；是研究地图，不是算法实现。 |

<a id="experience"></a>

## 经验与反思

| 论文 | 年份 | 参数更新 | 保留内容 / 类型 | 要点与边界 |
| --- | --- | --- | --- | --- |
| [ExpeL: LLM Agents Are Experiential Learners](https://arxiv.org/abs/2308.10144) | 2023 | No | Insights / experiences | 从执行经验中提取可复用知识，用于后续任务，不微调 Agent 的语言模型。 |
| [ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory](https://arxiv.org/abs/2509.25140) | 2025 | No | Reasoning memory | 从成功和失败经历提炼推理经验，供后续检索使用。 |
| [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) | 2023 | No | Reflective text | 利用反馈和情景记忆在多次尝试间改进；重复尝试本身不等于跨任务终身学习。 |

<a id="memory"></a>

## 长期记忆

| 论文 | 年份 | 参数更新 | 保留内容 / 类型 | 要点与边界 |
| --- | --- | --- | --- | --- |
| [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) | 2023 | No | Observations / reflections | 通过观察记忆与反思支持模拟行为；属于相关记忆架构，不是遗忘评测基准。 |
| [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413) | 2025 | No | Conversation memories | 提取并管理对话记忆；记忆质量本身不能证明技能的持续学习。 |

<a id="skills"></a>

## 技能与适应

| 论文 | 年份 | 参数更新 | 保留内容 / 类型 | 要点与边界 |
| --- | --- | --- | --- | --- |
| [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) | 2023 | No | Executable skill library | 在 Minecraft 中结合自动课程、环境反馈和可复用代码技能库。 |

<a id="evaluation"></a>

## 基准与评测

| 论文 | 年份 | 参数更新 | 保留内容 / 类型 | 要点与边界 |
| --- | --- | --- | --- | --- |
| [LifelongAgentBench: Evaluating LLM Agents as Lifelong Learners](https://arxiv.org/abs/2505.11942) | 2025 | N/A | Evaluation protocol | 用于评估 LLM 智能体终身学习；比较方法前需核对任务序列及允许保留的状态。 |
| [Evaluating Very Long-Term Conversational Memory of LLM Agents](https://arxiv.org/abs/2402.17753) | 2024 | N/A | Evaluation protocol | 提出 LoCoMo 长期对话记忆评测；可作补充，但不能替代持续任务学习评测。 |

<a id="related"></a>

## 相关方法与边界

| 论文 | 年份 | 参数更新 | 保留内容 / 类型 | 要点与边界 |
| --- | --- | --- | --- | --- |
| [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) | 2023 | No | Within-task feedback | 通过自反馈迭代修正答案；作为相关机制收录，不视为跨任务终身学习证据。 |
| [Learning to Prompt for Continual Learning](https://arxiv.org/abs/2112.08654) | 2021 | Prompts / keys / head | Learned parameters | 视觉持续学习背景：冻结主干并训练软提示等参数，不是 LLM Agent 的文本提示检索。 |

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
暂不承诺固定更新频率；后续重点补充持续参数训练、工具变化适应和安全评测。

## 模板与许可

结构改编自 [jthegedus/awesome-list-template](https://github.com/jthegedus/awesome-list-template) (CC0).
论文条目与解读独立整理。仓库原创内容使用 [CC0 1.0](LICENSE).
链接论文、软件与商标仍遵循各自许可；本清单与论文作者及相关项目无隶属关系。

<a id="star-history"></a>

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=logicwu0/awesome-lifelong-agents&type=Date)](https://www.star-history.com/#logicwu0/awesome-lifelong-agents&Date)

图表由第三方 Star History 提供。新仓库可能暂无数据，加载也可能受缓存或限流影响；不需要提交 GitHub Token。
