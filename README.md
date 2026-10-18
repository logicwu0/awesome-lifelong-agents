<div align="center">

# Awesome Lifelong Agents

A curated reading map of lifelong LLM agents: experience, memory, skills, and evaluation.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Checks](https://github.com/logicwu0/awesome-lifelong-agents/actions/workflows/check.yml/badge.svg)](https://github.com/logicwu0/awesome-lifelong-agents/actions/workflows/check.yml)
[![Stars](https://img.shields.io/github/stars/logicwu0/awesome-lifelong-agents?style=flat)](https://github.com/logicwu0/awesome-lifelong-agents/stargazers)

[English](README.md) · [简体中文](README.zh-CN.md) · [Contribute](CONTRIBUTING.md)

</div>

## About

How agents retain, reuse and update capabilities across tasks and time—not a tutorial on building agents.
Initial selection: 11 papers, including surveys, benchmarks and explicitly labeled related methods.
Sources reviewed: 2026-10-18. This is a manually maintained starting point, not an exhaustive survey.
We have not reproduced the reported experiments. The Awesome badge denotes list style, not endorsement or inclusion in the central Awesome directory.

“Parameter updates” describes the method, not provider-side model version changes. No does not mean zero inference cost.
Years are first arXiv submission years, not conference years. Check each paper for the exact persistence and evaluation setting.

## Contents

- [Surveys and roadmaps](#surveys)
- [Experience and reflection](#experience)
- [Long-term memory](#memory)
- [Skills and adaptation](#skills)
- [Benchmarks and evaluation](#evaluation)
- [Related methods and boundaries](#related)
- [Evaluation checklist](#evaluation-checklist)
- [Related resources](#resources)
- [Star History](#star-history)

<a id="surveys"></a>

## Surveys and roadmaps

| Paper | Year | Parameter updates | Retained state / type | Why read it / boundary |
| --- | --- | --- | --- | --- |
| [Lifelong Learning of Large Language Model based Agents: A Roadmap](https://arxiv.org/abs/2501.07278) | 2025 | Survey | Survey | Organizes lifelong agents around perception, memory and action; a starting map, not an executable algorithm. |

<a id="experience"></a>

## Experience and reflection

| Paper | Year | Parameter updates | Retained state / type | Why read it / boundary |
| --- | --- | --- | --- | --- |
| [ExpeL: LLM Agents Are Experiential Learners](https://arxiv.org/abs/2308.10144) | 2023 | No | Insights / experiences | Extracts reusable insights from collected experience for subsequent tasks without fine-tuning the agent LLM. |
| [ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory](https://arxiv.org/abs/2509.25140) | 2025 | No | Reasoning memory | Distills reasoning lessons from successful and failed experiences for later retrieval. |
| [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) | 2023 | No | Reflective text | Uses feedback and episodic reflections across trials; repeated attempts alone do not establish lifelong transfer. |

<a id="memory"></a>

## Long-term memory

| Paper | Year | Parameter updates | Retained state / type | Why read it / boundary |
| --- | --- | --- | --- | --- |
| [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) | 2023 | No | Observations / reflections | Retrieves observations and synthesized reflections to guide simulated behavior; related memory architecture, not a forgetting benchmark. |
| [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory](https://arxiv.org/abs/2504.19413) | 2025 | No | Conversation memories | Extracts and manages conversational memories; memory quality is not by itself proof of continual skill learning. |

<a id="skills"></a>

## Skills and adaptation

| Paper | Year | Parameter updates | Retained state / type | Why read it / boundary |
| --- | --- | --- | --- | --- |
| [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) | 2023 | No | Executable skill library | Combines an automatic curriculum, feedback and a reusable code skill library in Minecraft. |

<a id="evaluation"></a>

## Benchmarks and evaluation

| Paper | Year | Parameter updates | Retained state / type | Why read it / boundary |
| --- | --- | --- | --- | --- |
| [LifelongAgentBench: Evaluating LLM Agents as Lifelong Learners](https://arxiv.org/abs/2505.11942) | 2025 | N/A | Evaluation protocol | A benchmark for assessing LLM agents as lifelong learners; inspect the task sequence and allowed persistent state before comparing methods. |
| [Evaluating Very Long-Term Conversational Memory of LLM Agents](https://arxiv.org/abs/2402.17753) | 2024 | N/A | Evaluation protocol | Introduces LoCoMo for long-term conversational memory evaluation; complementary to, not interchangeable with, lifelong task evaluation. |

<a id="related"></a>

## Related methods and boundaries

| Paper | Year | Parameter updates | Retained state / type | Why read it / boundary |
| --- | --- | --- | --- | --- |
| [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) | 2023 | No | Within-task feedback | Iteratively refines an answer using self-feedback; listed as a related mechanism, not evidence of cross-task lifelong learning. |
| [Learning to Prompt for Continual Learning](https://arxiv.org/abs/2112.08654) | 2021 | Prompts / keys / head | Learned parameters | Vision continual-learning background: trains soft prompts with a frozen backbone, not text-prompt retrieval in an LLM agent. |

<a id="evaluation-checklist"></a>

## Evaluation checklist

- Specify task order, train/test separation and whether test answers can enter memory.
- Compare no-persistence, persistent-memory and shuffled-memory baselines with matched models and budgets.
- Measure new-task gains, old-task degradation, tokens, latency and storage.
- Distinguish repeated attempts, cross-task transfer and long-term distribution shifts; do not compare scores across incompatible protocols.
- Record model versions, prompts, seeds where supported and uncertainty; check propagation of erroneous or malicious memories.

<a id="resources"></a>

## Related resources

- [Lifelong LLM Agent Roadmap](https://github.com/qianlima-lab/awesome-lifelong-llm-agent) — Related survey companion and a useful research map.
- [LifelongAgentBench](https://github.com/caixd-220529/LifelongAgentBench) — Benchmark implementation.
- [AgentFoundry](https://github.com/logicwu0/AgentFoundry) — Our separate algorithm-toolkit scaffold, not a completed reproduction of the listed papers.

## Contributing and maintenance

Suggestions and corrections are welcome via issues and PRs; see [CONTRIBUTING.md](CONTRIBUTING.md).
No fixed update cadence is promised. Next priorities: continual parameter training, adaptation to changing tools and safety evaluation.

## Template and license

Structure adapted from [jthegedus/awesome-list-template](https://github.com/jthegedus/awesome-list-template) (CC0).
Entries and notes are independently curated. Original repository content is released under [CC0 1.0](LICENSE).
Linked papers, software and trademarks retain their own terms; this list is not affiliated with their authors or projects.

<a id="star-history"></a>

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=logicwu0/awesome-lifelong-agents&type=Date)](https://www.star-history.com/#logicwu0/awesome-lifelong-agents&Date)

Chart provided by the third-party Star History service. New repositories may have no data; caching or rate limits can affect display. No GitHub token is committed.
