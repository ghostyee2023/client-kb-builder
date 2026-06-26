---
title: 系统级skill候选清单
type: system-skill-candidate-list
status: draft
---

# 系统级skill候选清单

本清单列出当前客户知识库建议安装的系统级 skill。客户可按需安装，安装后仍要通过能力开关挂到具体业务流节点。

系统级 skill 是通用能力，不等同于律师业务专属 skill。

律师业务专属 skill 见：

```text
11_能力与工具/01_能力开关/项目级skill清单.md
```

## 律师客户首批推荐

| skill | 状态 | 用途 | 对应节点 | 是否首版必装 |
| --- | --- | --- | --- | --- |
| `documents:documents` | candidate | 处理委托合同、法律意见、代理方案、文书草稿 | 文书与工作底稿 | 是 |
| `pdf:pdf` | candidate | 读取和检查 PDF 材料、裁判文书、扫描件 | 客户材料、证据目录 | 是 |
| `spreadsheets:Spreadsheets` | candidate | 管理证据目录、案件台账、服务耗时 | 证据整理、数据反馈 | 是 |
| `skill-creator` | candidate | 帮客户创建律师项目级 skill | 项目级 skill 创建 | 条件安装 |
| `browser:control-in-app-browser` | candidate | 网页检索、公开资料核验 | 法律检索摘要 | 条件安装 |
| `lark-doc` | candidate | 飞书文档协作 | 飞书客户文档 | 飞书客户必装 |
| `lark-sheets` | candidate | 飞书表格台账 | 飞书客户台账 | 飞书客户必装 |
| `lark-drive` | candidate | 飞书云盘材料管理 | 飞书客户材料 | 飞书客户必装 |

## 安装原则

- 先安装通用文档、PDF、表格能力。
- 再根据客户工具环境安装飞书、浏览器或其他外部工具能力。
- 系统级 skill 安装后，必须登记到能力开关表。
- 未经验证的系统级 skill 只能是 `manual` 或 `candidate`，不能直接设为 `on`。

## 与项目级 skill 的边界

系统级 skill 解决通用文件、工具、平台操作。

项目级 skill 解决律师业务动作，例如：

- 新咨询结构化。
- 冲突检查。
- 证据目录整理。
- 客户进度同步。
- 单案复盘抽取。
