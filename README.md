# client-kb-builder

`client-kb-builder` 是一个用于设计和交付客户版知识库操作系统的项目级 skill。

它的目标不是把 OPC 的目录结构直接复制给客户，而是先理解客户业务，再把客户真实的业务流、协作方式、输入输出、能力开关和 AI 执行边界翻译成一套可运行、可交付、可迭代的知识库系统。

## 适用场景

当你需要为客户设计以下内容时，可以使用这个 skill：

- 客户版知识库系统
- 企业或个人业务知识库操作系统
- AI 转型项目的知识库底座
- 客户业务流、能力开关和目录架构
- 可交付的知识库搭建方案、培训方案和迭代清单
- 面向客户的 AI 执行规则、项目 skill 配置和验收清单

典型提示词：

```text
帮我为一个客户从业务诊断开始，设计一套可运行的客户版知识库系统。
```

```text
这个客户是做企业培训的，帮我先做五维诊断，再给出第一版知识库目录。
```

```text
我要交付一个客户知识库项目，帮我生成完整的业务流包、能力开关和验收清单。
```

## 核心原则

不要直接复制 OPC 的目录名或内部机制。

每一次客户知识库设计，都按这个顺序推进：

```text
五维诊断
-> 生命周期映射
-> 业务流包
-> 能力开关
-> 目录落位
-> 交付培训
-> 复盘迭代
```

如果客户需求还很模糊，先输出诊断清单和最小架构草案，不直接创建长期资产。

## 工作流程

1. 识别客户业务类型  
   判断客户的收入模式、交付对象、输入来源、输出资产、协作角色、运行节奏和风险边界。

2. 进行五维诊断  
   从战略上下文、输入系统、生产系统、交付分发、反馈治理五个维度理解客户业务。

3. 映射业务生命周期  
   把客户真实业务翻译为输入、判断、处理、输出、复盘、沉淀、回流等阶段。

4. 设计业务流包  
   每个业务流必须形成完整闭环，而不是单个任务或单个目录。

5. 配置能力开关  
   把 skill、Agent、CLI、模板、规则、自动化和外部工具都视为服务业务节点的能力。

6. 生成客户知识库目录  
   使用客户自己的业务语言命名目录，并保持顶层目录按运行顺序排列。

7. 配置客户 AI 执行层  
   明确 AI 能读什么、能写什么、能调用什么、何时必须停下来让人确认。

8. 输出交付材料  
   包括搭建计划、客户说明、培训路径、首轮验收清单和下一版升级建议。

## 输出模式

轻量输出适合探索阶段，通常包括：

- 客户诊断摘要
- 推荐的知识库形态
- 第一版目录建议
- 缺失信息清单

完整交付输出适合落地阶段，通常包括：

- 客户五维诊断
- 生命周期映射表
- 业务流包清单
- 能力开关清单
- 客户知识库目录树
- AI 执行规则
- 系统级 skill 候选清单
- 项目级 skill 规划
- 培训交付计划
- 复盘与升级清单

## 文件结构

```text
client-kb-builder/
  SKILL.md
  README.md
  agents/
    openai.yaml
  assets/
    customer-kb-directory-template.md
  references/
    acceptance-checklist.md
    capability-switch-template.md
    five-dimensional-diagnosis.md
    workflow-package-template.md
```

文件说明：

- `SKILL.md`：skill 的主入口，定义触发场景、工作流、输出模式和边界。
- `agents/openai.yaml`：面向 OpenAI/Codex 场景的展示名称和默认提示词。
- `assets/customer-kb-directory-template.md`：客户知识库目录模板，使用时需要按客户业务重命名。
- `references/five-dimensional-diagnosis.md`：客户业务五维诊断参考。
- `references/workflow-package-template.md`：业务流包注册模板。
- `references/capability-switch-template.md`：能力开关配置模板。
- `references/acceptance-checklist.md`：客户知识库交付前验收清单。

## 能力边界

这个 skill 默认不写文件，除非用户明确要求保存、落地、生成文件或创建交付物。

客户知识库交付时需要注意：

- 不暴露交付方内部路径和同步机制。
- 不把内部客户名、私人上下文、未公开策略写进客户侧根目录。
- 不把系统级可复用 skill 和客户项目级 skill 混在一起。
- 自动化必须先归入业务流节点和能力开关，不能直接挂在目录上。
- 如果客户不需要完整系统，应主动建议更小版本。

## 交付验收

调用 `references/acceptance-checklist.md` 检查客户根目录是否完成。

一个合格的客户知识库交付物，至少应说明：

```text
Status:
Root path:
Active workflow:
Enabled mechanisms:
Pending decisions:
Validation performed:
```

## 版本

当前版本：`v1.0-beta.1`

