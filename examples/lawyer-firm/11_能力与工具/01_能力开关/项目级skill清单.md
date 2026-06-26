---
title: 项目级skill清单
type: project-skill-registry
status: draft
---

# 项目级skill清单

项目级 skill 是客户知识库里的可插拔执行能力。它们必须服务某条业务流的某个节点，不能直接绕过业务流。

## 交付类型

| 类型 | 含义 | 处理方式 |
| --- | --- | --- |
| `delivered` | 已随本知识库交付的项目级能力 | 可在验证后启用 |
| `custom` | 客户业务专属定制 | 后期按客户实际流程创建 |
| `training` | 不直接交付成品，而是教学客户自己创建 | 用作培训和陪跑内容 |

## 清单

| skill | 类型 | 状态 | 服务业务流 | 服务节点 | 读取范围 | 写入范围 | 失败回退 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kb-foundry` | `delivered` | planned | 客户知识库搭建阶段 | 业务诊断、目录搭建、能力配置 | 当前客户根目录 | 当前客户根目录 | 退回人工搭建清单 |
| `lawyer-intake` | `custom` | planned | `lawyer_case_delivery_flow` | 新咨询收件、案由识别、待补信息 | `02_客户咨询收件箱/` | `04_案件判断与方案/` | 输出手动填写清单 |
| `lawyer-conflict-check` | `custom` | planned | `lawyer_case_delivery_flow` | 冲突检查 | `04_案件判断与方案/01_冲突检查/` | `10_治理规则/04_运行证据/` | 律师人工核查 |
| `lawyer-evidence-catalog` | `custom` | planned | `lawyer_case_delivery_flow` | 证据目录整理 | `02_客户咨询收件箱/03_客户材料/` | `05_文书与工作底稿/03_证据目录/` | 手动整理证据表 |
| `lawyer-progress-brief` | `custom` | planned | `lawyer_case_delivery_flow` | 客户进度同步 | `06_案件交付/` | `06_案件交付/04_客户进度同步/` | 输出待确认草稿 |
| `lawyer-case-review` | `custom` | planned | `lawyer_case_delivery_flow` | 单案复盘 | `06_案件交付/`, `07_客户交付与归档/` | `09_律师复盘/01_单案复盘/` | 手动复盘 |
| `lawyer-tool-training` | `training` | planned | 能力接入与培训 | 教客户创建和维护项目级 skill | `11_能力与工具/` | `11_能力与工具/07_验证记录/` | 交付方人工演示 |

## 首版说明

首版只登记 planned 状态，不默认安装和启用。实际客户交付时，按客户工具环境决定是否做成 Codex skill、Claude project skill、脚本、模板或纯人工 SOP。

客户侧只维护本清单。
