# 骗子克星

> 一个面向“智能眼镜风险提示”方向的合规优先研究骨架。  
> A compliance-first research skeleton for risk-alert experiences on smart glasses.

`骗子克星` 不是一个现成的实时人脸识别产品，而是一个公开的研究起点：它试图回答一个更难、也更值得先回答的问题。

如果智能眼镜未来真的要承担“风险提示”能力，什么数据可以进系统，什么数据绝对不能进，什么提示可以发出，什么提示必须先被拦下？

这个仓库当前把重点放在：

- 风险清单结构设计
- 数据来源合法性门禁
- 提示前的策略判断与审计
- 开源维护者与项目本身的去风险化

## 这个项目为什么存在

现实世界里，很多人都直觉性地想做“眼镜看到可疑对象就提醒”的系统，但这类项目往往一上来就掉进两个错误：

1. 先做识别能力，再补合规和治理
2. 把民间曝光帖、非官方名单、未核验爆料混成所谓“数据库”

`骗子克星` 反过来做。

它的第一原则不是“识别得更快”，而是“默认更保守、更可审计、更能被约束”。如果这条线走不通，那就说明这个方向还不应该被做成现实产品。

## 当前定位

这个仓库当前**不是**以下任何东西：

- 不是可直接部署的人脸识别系统
- 不是民间“骗子数据库”聚合器
- 不是面向公共空间的实时监控方案
- 不是对具体自然人进行自动指认的工具

当前版本只提供三类能力：

- 风险清单 manifest 的结构化校验
- 数据来源与发布边界的策略判断
- 围绕开源发布、误报治理和维护者安全的文档框架

## 当前仓库状态

截至本轮收工，仓库已经完成这些基础动作：

- 已拆出 `Project-files`，使用独立 Git 历史
- 已发布到 GitHub Organization
- 已切换为公开仓库
- 已补齐 README、LICENSE、SECURITY、SUPPORT、CONTRIBUTING、协作模板
- 已建立中文优先、英文可协作的文档基线

这意味着项目现在适合进入下一阶段：补 schema、policy 输出和审计层，而不是继续纠结发布基础设施。

## 想邀请谁参与

### 开发者

如果你关心这些问题，欢迎加入：

- 如何把“默认拒绝”做成真正可执行的策略引擎
- 如何为高风险清单设计 schema、状态流转和审计日志
- 如何把“合规门禁”前置到产品能力之前
- 如何在不引入真实生物特征模板的前提下搭出研究级原型

### 智能眼镜 / 硬件厂商

如果你在做智能眼镜、边缘计算设备、AR 提示系统或可穿戴设备，这个仓库尤其值得你看。

我们想推动的不是“再做一个更激进的识别 demo”，而是更早把这些问题拉到台前：

- 设备端什么能力应该默认禁用
- 什么场景必须要求显式授权和受控环境
- 如何设计人工复核、撤销机制和审计链
- 如何避免硬件最终变成“模糊合法、清晰危险”的现实工具

如果你是厂商、方案商或相关工程团队，欢迎把它当成一个“先补治理层”的讨论入口。

## 中文支持

当前仓库采用 **中文优先** 的文档策略。

- README 与核心设计文档默认使用中文
- 关键定位会附带简短英文说明，方便跨语言协作
- 欢迎后续补充英文版文档、双语 issue 模板和英文 README

如果你更习惯英文协作，也欢迎直接提英文 issue 或 PR。

## 项目级指引文件

- `docs/PRODUCT_VISION.md`: 项目目标、非目标与成功标准
- `docs/ROADMAP.md`: 分阶段技术路线图
- `docs/TODO.md`: 当前待办
- `docs/DEVELOPMENT_BLUEPRINT.md`: 开发蓝图与模块边界
- `docs/COMPLIANCE_BOUNDARY.md`: 数据与功能边界
- `docs/PERSONAL_OPSEC.md`: 维护者与项目去风险策略
- `AGENTS.md`: 项目级执行约束

## 目录结构

- `docs/`: 设计、边界、路线图和治理文档
- `src/pianzi_kexing/`: Python 包
- `tests/`: 最小测试
- `examples/watchlist_manifest.json`: 示例清单

## 快速开始

```bash
cd "23骗子克星"
python3 -m venv .venv
source .venv/bin/activate
pip install -e . pytest
pytest
python -m pianzi_kexing.cli validate-manifest examples/watchlist_manifest.json
python -m pianzi_kexing.cli print-opsec-checklist
```

## 当前命令

- `validate-manifest <path>`: 校验风险清单是否满足仓库策略
- `print-opsec-checklist`: 输出维护者开源前检查项

## 当前最重要的约束

- 不引入真实人脸模板
- 不引入民间曝光源
- 不实现公共空间实时识别
- 不输出自动定罪式提示

## 接下来会做什么

当前优先级不是“把识别跑起来”，而是把下面这些基础层补完整：

1. manifest schema 与字段级校验
2. 策略引擎的机器可读输出
3. 审计日志与版本快照结构
4. mock matcher / alerting / audit 接口
5. 面向公开发布的基础仓库门面

具体待办见 `docs/TODO.md`。

## 如何参与

- 想讨论边界与方向：先读 `docs/PRODUCT_VISION.md` 和 `docs/COMPLIANCE_BOUNDARY.md`
- 想讨论架构：看 `docs/DEVELOPMENT_BLUEPRINT.md`
- 想挑开发任务：看 `docs/TODO.md`
- 想提安全或合规问题：看 `SECURITY.md`

## 开源说明

这个项目当前以“研究骨架”方式开源，不承诺任何生产可用性。

如果你打算把它用于真实识别、真实部署或公共空间使用，请先停下来，重新审视：

- 数据来源是否合法
- 是否存在误报申诉与撤销机制
- 是否有明确法域依据
- 是否真的应该做
