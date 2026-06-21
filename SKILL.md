---
name: client-kb-builder
description: Build customer-facing knowledge-base operating systems from business diagnosis to directory architecture, workflow packages, capability switches, delivery materials, and iteration plans. This is not a generic wiki builder; use it when a user asks to create, design, configure, productize, or deliver a client/customer knowledge-base operating system, client workflow architecture, capability configuration, AI execution layer, or knowledge-base delivery package.
---

# Client KB Builder

Version: v1.0-beta.1

## Core Rule

Do not copy OPC directory names directly into a customer project. Always translate from the customer's business model.

This skill is not a generic knowledge-base generator. It is for customer-facing knowledge-base operating systems where business workflows, capability switches, AI execution rules, handoff materials, and iteration evidence matter.

Use this order every time:

```text
Five-dimensional diagnosis
-> lifecycle mapping
-> workflow packages
-> capability switches
-> directory placement
-> delivery and training
-> review and iteration
```

If the user provides only a vague customer need, first produce a diagnosis checklist and a minimal architecture draft. Do not create long-term customer assets until the target customer, business type, and delivery scope are clear.

Before designing a full system, choose the delivery scale:

- Lite: one or two core workflows, a small directory, no heavy capability registry unless needed.
- Standard: workflow switchboard, capability switchboard, templates, and AI execution rules.
- Full delivery: complete directory architecture, workflow packages, capability switches, project skill plan, training materials, and validation records.

## Workflow

1. Classify the customer business.
   Identify revenue model, delivery object, input sources, output assets, collaboration roles, operating rhythm, and risk boundaries.

2. Choose the delivery scale.
   Decide whether the customer needs Lite, Standard, or Full delivery. Small customers should not receive an over-engineered system by default.

3. Run the five-dimensional diagnosis.
   Use `references/five-dimensional-diagnosis.md` when the customer business is unclear, cross-functional, or needs a formal diagnosis artifact.

4. Map the lifecycle.
   Convert the customer's real business lifecycle into stages such as input, qualification, production, delivery, feedback, review, and asset reuse.

5. Design workflow packages.
   Each workflow package must include input, judgment, processing, output, review, sedimentation, and feedback loop. Use `references/workflow-package-template.md` for formal registration.

6. Configure capability switches.
   Treat skills, agents, CLIs, templates, automations, rules, and external tools as capabilities serving workflow nodes. Use `references/capability-switch-template.md`.

7. Generate the customer directory.
   Use business-readable names. Keep top-level directories ordered by operating sequence. Use `assets/customer-kb-directory-template.md` as the starting scaffold, then rename for the customer's business. Include root AI execution files such as `AGENTS.md` and `CLAUDE.md` when the customer will use AI agents.

8. Produce delivery materials.
   For paid or client-facing work, output a setup plan, customer explanation, training path, and next iteration list.

9. Configure customer AI execution.
   Add root rules, workflow switches, capability switches, system skill candidate list, project skill registry, skill installation plan, AI boundaries, and validation records. Customer AI must know what it can read, write, call, install, and when to stop for human confirmation.

   Distinguish system-level skills from project-level skills:
   - System-level skills are reusable capabilities already available on the delivery machine. Give customers a curated install list so their AI can install or request installation.
   - Project-level skills are business-specific to the customer. They can be extracted from OPC and rewritten internally, created as later custom skills, or taught to the customer. Do not expose the internal sync mechanism in the customer root.

10. Record review signals.
   End every implementation with usage blockers, missing inputs, capabilities to add, and productization opportunities.

11. Validate before handoff.
   Use `references/acceptance-checklist.md` before calling a customer root complete. Customer roots must not expose OPC sync mechanics or internal paths.

## Output Modes

Use a lightweight output when the user is exploring:

- customer diagnosis summary
- recommended knowledge-base shape
- first-version directory proposal
- missing information list
- recommended delivery scale

Use a full delivery output when the user asks to build, land, save, scaffold, or prepare a customer package:

- customer diagnosis
- lifecycle map
- workflow package list
- capability switch list
- directory tree
- AI execution rules
- system skill candidate list
- key templates
- project skill and installation plan
- training and handoff plan
- review and upgrade checklist

## Validation Status

This is a beta skill. Be explicit about validation state in customer-facing or contest-facing outputs:

- Validated: methodology design, reference templates, internal structure, and simulated customer scenarios.
- Pending: real customer end-to-end delivery evidence across multiple industries.
- Known risk: full delivery may feel heavy for small customers; use Lite or Standard scale first.
- Known risk: platform or public API availability may vary after installation; provide fallback instructions and manual usage paths.

## Boundaries

- Preserve customer confidentiality. Do not expose OPC internal paths, internal customer names, private business details, or unpublished strategy unless the user explicitly wants an internal artifact.
- Do not write files by default. Write only when the user asks to save, scaffold, land, generate files, or create a deliverable.
- For OPC productization assets, write under `12_客户版知识库产品/` or related delivery paths. For reusable capability records, write under `11_能力与Agent/`.
- If the customer needs an automation, first register the workflow node and capability switch. Do not bolt automation directly onto a folder.
- If the customer needs AI agents, add root execution rules and project skill configuration before enabling any skill or automation.
- If the customer needs skills, first separate system-level skills from project-level skills. Do not mix installable tool skills with customer business skills.
- For customer-side project skills, use customer-facing labels such as `delivered`, `custom`, and `training` in one project skill registry. Keep internal sync details in OPC-side governance, not the customer root.
- If a customer business does not need the full system, recommend a smaller version.
- If installation, public API access, or runtime availability is uncertain, state the uncertainty and provide a manual fallback instead of claiming full automation.

## References

- `references/five-dimensional-diagnosis.md`: use for customer diagnosis and business model translation.
- `references/workflow-package-template.md`: use when designing formal customer workflow packages.
- `references/capability-switch-template.md`: use when configuring skills, tools, agents, templates, and automations.
- `references/acceptance-checklist.md`: use before handoff or after scaffolding a customer root.
- `assets/customer-kb-directory-template.md`: use as a scaffold for a customer knowledge-base directory.
