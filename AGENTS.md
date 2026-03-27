# AGENTS.md

## 项目目标

本项目是一个合规优先的研究骨架，不是可直接部署的实时人脸识别系统。

## 开发约束

- 所有新增能力必须先满足 `docs/COMPLIANCE_BOUNDARY.md`
- 默认拒绝任何民间“骗子数据库”、社媒曝光帖、群众指认数据
- 不实现公共空间实时识别
- 不引入真实生物特征模板或向量库
- 不输出自动定罪式提示文案
- 涉及外部库或 API 的新能力，先查最新官方文档

## 推荐执行顺序

1. 先完善 schema、policy、audit。
2. 再做 mock adapter。
3. 最后才讨论受控环境下的演示层。

## 文档优先级

如有冲突，优先级从高到低如下：

1. `docs/COMPLIANCE_BOUNDARY.md`
2. `docs/PRODUCT_VISION.md`
3. `docs/DEVELOPMENT_BLUEPRINT.md`
4. `docs/ROADMAP.md`
5. `docs/TODO.md`
