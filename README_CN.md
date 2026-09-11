# Scientific Paper Figures — 科学论文图表技能

[English](README.md) | 中文

一个以证据为先的 Codex 技能，用于规划、设计、渲染、修改和审核学术论文中的图与表。

它帮助你把科学主张和证据组织成清晰的视觉论证，同时关注来源追踪、可编辑性、最终尺寸下的可读性以及期刊特定要求。

## 功能

- 为论文、学位论文、预印本和期刊投稿规划整套图表。
- 设计单张图、多面板布局、架构图、数据图、图注和视觉系统。
- 在需要渲染时生成或修改可编辑源文件与导出文件。
- 审核科学准确性、视觉清晰度、可访问性、可追溯性和交付要求。
- 分析参考图的设计方法，但不把参考图中的科学内容当作新论文的权威依据。

## 工作流

技能只会根据请求调用必要的层级：

1. **论文图表规划器** — 建立主张与证据的对应关系，判断哪些结果需要图或表，并组织正文与附录中的叙事顺序。
2. **单图设计器** — 规定单张图的结构、面板、箭头、公式、标签、图注和视觉系统。
3. **图表渲染器** — 生成、修改、导出或审核实际文件，并记录相关数据来源与处理过程。

各层之间通过结构化产物传递信息，避免后续阶段悄然改变前一阶段的决定。

## 证据与质量规则

技能将指导内容分为三类；为保证技能内部及结构化数据的一致性，类名固定使用英文：

- `[Literature/Official Standard]` — 有论文、出版社、期刊或权威机构来源支持的要求或指导。
- `[Skill-Derived Heuristic]` — 本技能归纳出的操作性经验规则。
- `[Domain Template]` — 需要结合稿件和证据调整的领域起始模板。

技能不会编造数据、方法、结果、引文、许可证、样本量、不确定性或期刊要求。如果证据不足，它会提供暂定方案和缺失输入清单，而不是制作看似可投稿但证据虚构的图表。

## 安装

将仓库克隆到 Codex 技能目录：

```powershell
git clone https://github.com/ebxk/scientific-paper-figures-skill.git "$env:USERPROFILE\.codex\skills\scientific-paper-figures"
```

## 使用方法

在 Codex 中显式调用该技能：

```text
使用 $scientific-paper-figures，根据这份稿件和数据集规划整篇论文的图表。
```

其他示例：

```text
使用 $scientific-paper-figures，在保留原始数据与科学主张的前提下重新设计 Figure 2。
```

```text
使用 $scientific-paper-figures，按照最终投稿尺寸审核这些已导出的图片。
```

## 结构化产物校验

[`assets/`](assets/) 中提供了规划、图表规范和质量审核的 JSON 示例。可用以下命令校验结构化 JSON 产物：

```powershell
python scripts/validate_figure_artifact.py <artifact.json>
```

## 仓库结构

```text
scientific-paper-figures/
├── SKILL.md                  # 技能入口与路由规则
├── agents/openai.yaml        # Codex 界面元数据
├── assets/                   # 结构化产物示例
├── references/               # 规划、设计、渲染与标准说明
├── scripts/                  # 产物校验工具
└── tests/                    # 校验器测试
```

## 许可证

本项目采用 [MIT License](https://github.com/ebxk/scientific-paper-figures-skill/blob/main/LICENSE)。
