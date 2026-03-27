# 骗子克星

`骗子克星` 是一个合规优先的开源研究骨架，用来讨论“智能眼镜风险提示”这类项目在数据来源、发布方式、维护者安全和产品边界上的约束。

这个仓库当前**不是**可直接部署的人脸识别系统，也**不会**提供以下能力：

- 实时人脸识别推理链路
- 非官方“骗子数据库”抓取与聚合
- 基于网络曝光帖的人身标签匹配
- 面向公共空间的隐蔽监控部署方案

当前版本只提供三类能力：

- 风险清单清单文件的结构化校验
- 数据来源与发布边界的策略判断
- 维护者开源前去风险化文档

项目级指引文件：

- `docs/PRODUCT_VISION.md`: 项目目标、非目标与成功标准
- `docs/ROADMAP.md`: 分阶段技术路线图
- `docs/TODO.md`: 当前待办
- `docs/DEVELOPMENT_BLUEPRINT.md`: 开发蓝图与模块边界
- `AGENTS.md`: 项目级执行约束

## 为什么这样初始化

你描述的方向同时踩中了三个高风险区：

- 生物特征识别
- 公开指认具体个人
- 可能引发现实世界对抗和报复

所以首个开源版本更适合做成“研究框架 + 合规门禁 + 数据清单校验器”，而不是直接交付可执行识别系统。

## 目录结构

- `docs/PERSONAL_OPSEC.md`: 维护者个人信息去风险化策略
- `docs/COMPLIANCE_BOUNDARY.md`: 数据与功能边界
- `docs/ARCHITECTURE.md`: 合规优先的系统骨架
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

## 后续建议

如果你真要继续推进这个方向，下一步应优先做这些事，而不是先写识别代码：

1. 把项目迁移到 GitHub 组织账号，而不是个人账号。
2. 移除个人站上的直连邮箱和微信二维码。
3. 先完成法律评估、DPIA 和误报责任设计。
4. 把数据源限制为官方公开通报，并保留来源 URL、发布日期、法域和撤销机制。
