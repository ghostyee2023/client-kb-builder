 # Skill 安装与启用说明
 
 > 这份说明告诉你：先装什么、后装什么、装完怎么验证、出问题怎么回退。
 
 ## 安装前检查
 
 | 检查项 | 状态 | 说明 |
 | --- | --- | --- |
 | 你使用哪个 AI 工具 | `{{AI_TOOL}}` | Codex / Claude / 其他 |
 | 系统级 skill 候选清单已确认 | `pending` | 见 `System_Skill_Candidates.md` |
 | 项目级 skill 清单已确认 | `pending` | 见 `Project_Skill_Registry.md` |
 | 是否允许 AI 读取你的业务文件 | `pending` | 必须先定义权限边界 |
 | 是否允许 AI 写入你的业务文件 | `pending` | 必须先定义写入范围 |
 | Python 是否可用（如需运行脚本） | `pending` | 运行 `python --version` 检查 |
 
 ## 启用顺序
 
 按以下顺序操作，不要跳步：
 
 1. **启用根目录执行规则**：确认 `AGENTS.md` 或 `CLAUDE.md` 存在且内容正确。
 2. **启用业务流开关**：打开 `Workflow_Switchboard.md`，确认要跑的流程是 `on`。
 3. **启用能力开关**：打开 `Capability_Switchboard.md`，确认每个节点的能力状态。
 4. **安装系统级 skill**：按 `System_Skill_Candidates.md` 的推荐顺序安装。
 5. **登记项目级 skill**：按 `Project_Skill_Registry.md` 确认待开发清单。
 6. **单个节点试跑**：选一个最简单的节点，用真实输入跑一次。
 7. **写验证记录**：在 `Validation_Records/` 里记一笔结果。
 
 ## 首版最小安装
 
 不要一次全装。首版只装这些：
 
 - `documents:documents`（处理文档）
 - `spreadsheets:Spreadsheets`（处理表格）
 - {{MINIMAL_SKILLS}}
 
 其他 skill 等跑通首条业务流后再按需补装。
 
 ## 验证方法
 
 每装一个 skill，做一次验证：
 
 1. 用一个真实业务文件测试（不要用示例文件）。
 2. 确认 skill 能正确读取和写入指定目录。
 3. 确认 skill 不会越权访问其他目录。
 4. 记录验证结果到 `Validation_Records/`。
 
 ## 回退方法
 
 如果某个 skill 装完有问题：
 
 1. 在能力开关表中把它设为 `blocked`。
 2. 在业务流开关表中确认没有节点依赖它。
 3. 按 skill 自身的卸载方式移除。
 4. 在 `Validation_Records/` 记录回退原因。
 
 ## 禁止事项
 
 - 不允许自动安装未登记的 skill。
 - 不允许 skill 读取超出声明范围的目录。
 - 不允许 skill 绕过人工确认直接对外发送材料。
 - 不允许把敏感业务内容写入公共方法库。
