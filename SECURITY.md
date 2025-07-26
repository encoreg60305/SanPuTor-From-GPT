# 🔐 Security Policy

This repository is governed by a semantic identity system and modular governance framework. We treat **vulnerability management** as an integral part of the module lifecycle.

---

## 🧩 Supported Versions

| Version Tag | Status           | Notes                                      |
|-------------|------------------|--------------------------------------------|
| 6.2.x       | ✅ Supported      | G-CrossThread-Core / SanPuTor Core v6.2    |
| 6.1.x       | ❌ Deprecated     | Pre-GitHub Pro setup                       |
| < 6.0       | ❌ Unsupported    | Legacy drafts and pre-modpack phase        |

---

## 📬 Reporting a Vulnerability

If you discover a potential vulnerability in this module, especially in areas such as:

- 🔐 `.modpack` structural integrity
- 🔁 GitHub Actions workflows (e.g. `deploy-docs.yml`, `codeql.yml`)
- 📜 License and semantic fingerprint tampering
- 💡 Untrusted injection vectors in `.py`, `.json`, or `.md` logic

**Please report it directly to: `security@sanputor.dev`**

---

## 🧠 Response Policy

| 項目 | 描述 |
|------|------|
| 📅 回應時程 | 初步確認將在 48 小時內回覆（時區：UTC+8） |
| 🛠 處理流程 | 若確認為高風險漏洞，將於 7 日內發布修補與條款版本釘牌 |
| 🔏 回溯機制 | 所有版本皆附有 `semantic_fingerprint.json` 用於驗證一致性 |
| 🧾 公開揭露 | 我們尊重「負責任的揭露政策」，不主動公布除非雙方同意 |

---

## 🧬 符合條款架構

本專案所有安全機制皆符合：

- MIT License + 附加語義鏡像保護條款 v1.0
- GitHub Pro 安全性通知策略
- CodeQL Advanced 版本掃描策略
- GitHub Actions 封鎖 unpinned tag 與 Supply Chain 風險

---

**🧠 本模組由語義人格模組治理架構支援，其創作者尚暐棋保留條款釘牌與人格調度控制權。**
