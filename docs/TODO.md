# 待办事项

## P0

- 定义 manifest JSON schema
- 增加 `revoked_at`、`reviewed_by`、`review_status` 字段
- 增加 schema 校验测试
- 为 CLI 增加 `explain-policy` 子命令
- 新增 `SECURITY.md`、`CODE_OF_CONDUCT.md`、`SUPPORT.md`
- 新增 `CHANGELOG.md` 和首个公开版本发布说明
- 为 `watchlist_manifest` 设计字段级校验错误码
- 增加“来源不合法 / 生物特征模板 / 群众曝光源”三类拒绝样例
- 为策略校验输出增加 `--json` 机器可读模式

## P1

- 增加策略规则配置文件
- 支持输出机器可读的审计报告 JSON
- 增加变更历史和版本快照机制
- 提供 mock matcher adapter 和 mock alert adapter
- 增加审计日志目录结构与落盘规范
- 设计 `matcher` / `alerting` / `audit` 三个模块的接口草案
- 增加本地演示模式的 feature flag，默认关闭

## P2

- 做一个本地只读 Web 控制台
- 增加清单 diff 视图
- 增加人工复核工作流草案
- 准备 GitHub Organization 发布草案
- 准备远端仓库初始化与开源发布检查清单
- 设计“只发布独立仓库，不直接公开 Project-files 全仓”的发布流程

## 本轮已确认决策

- 当前按保守方案推进，不对历史做彻底重写
- 未来优先发布独立子仓库，不直接整体公开 `Project-files`
- “骗子克星”后续优先在 GitHub Organization 下发布
- 项目保持“合规优先研究骨架”定位，不实现公共空间实时识别

## 永久约束

- 不引入真实人脸模板
- 不引入民间曝光源
- 不实现公共空间实时识别
