from __future__ import annotations

from pianzi_kexing.models import PolicyDecision, WatchlistEntry

ALLOWED_SOURCE_TYPES = {
    "official_wanted_notice",
    "court_public_notice",
    "police_bulletin",
}

BLOCKED_SOURCE_TYPES = {
    "crowdsourced_expose_post",
    "community_blacklist",
    "social_media_thread",
    "scammer_database",
}


def evaluate_entry(entry: WatchlistEntry) -> PolicyDecision:
    issues: list[str] = []

    if entry.source_type in BLOCKED_SOURCE_TYPES:
        issues.append("source_type 属于仓库明令拒绝的数据来源")

    if entry.source_type not in ALLOWED_SOURCE_TYPES:
        issues.append("source_type 不在允许列表中")

    if not entry.source_url.startswith("https://"):
        issues.append("source_url 必须使用 https")

    if not entry.official_source_confirmed:
        issues.append("缺少官方来源确认")

    if not entry.legal_basis.strip():
        issues.append("缺少 legal_basis")

    if not entry.supports_retraction:
        issues.append("缺少撤销或更新机制")

    if entry.contains_biometric_template:
        issues.append("当前仓库不接受包含生物特征模板的清单")

    if entry.uses_crowdsourced_accusation:
        issues.append("当前仓库不接受群众曝光式指认数据")

    if entry.status not in {"active", "revoked", "archived"}:
        issues.append("status 不合法")

    return PolicyDecision(allowed=not issues, issues=issues)


def opsec_checklist() -> list[str]:
    return [
        "移除个人站直连邮箱，改用表单或邮件别名",
        "移除微信二维码和任何即时通信公开入口",
        "项目首发使用 GitHub Organization，而不是个人账号",
        "GitHub 个人资料不展示到城市级位置",
        "准备 SECURITY.md、CODE_OF_CONDUCT.md 和 SUPPORT.md",
        "为公开邮箱配置过滤规则、别名和封禁策略",
    ]
