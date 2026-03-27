# 开发蓝图

## 总体原则

- Governance first
- Human in the loop
- Default deny
- Audit by default

## 模块分层

### `dataset`

职责：

- 读取 manifest
- 做基础字段转换

不负责：

- 业务策略判断

### `policy`

职责：

- 判定条目是否可进入研究清单
- 输出拒绝原因
- 维护维护者去风险检查项

不负责：

- 真实识别推理

### `matcher`

职责：

- 未来只定义接口

限制：

- 当前阶段只允许 mock

### `alerting`

职责：

- 定义提示等级、文案和人工确认门槛

限制：

- 不做自动公开指认

### `audit`

职责：

- 记录策略结果
- 记录条目状态变化
- 支持复核结论沉淀

## 推荐开发顺序

1. 先补 schema 和 policy 测试。
2. 再做审计输出。
3. 再抽象 adapter 接口。
4. 最后才考虑受控环境下的 mock 演示。
