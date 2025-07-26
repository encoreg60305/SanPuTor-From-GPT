# 🧭 Usage Guide — SanPuTor-Core-G Module

This document provides step-by-step instructions for using the `SanPuTor-Core-G` modular personality package with the [OpenAI Assistant API](https://platform.openai.com/assistants).

---

## 📦 What’s Included

The module contains:

- `SanPuTor-Core-G_v6.2.0.modpack.json`: Core assistant configuration  
- `vector_store_inputs/*.txt`: Semantic fingerprinting & personality definitions  
- `code_interpreter_inputs/*.py|.csv|.xlsx|.json`: Testing tools and data  
- `docs/`: Public documentation folder for GitHub Pages  
- `modpack.json`: Root config (optional override)

---

## 🚀 Quickstart with OpenAI Platform

### 1. Upload Modpack to Assistant API

- Go to: https://platform.openai.com/assistants
- Click **"Create Assistant"**
- Select:
  - **Instructions**: Import from `.modpack.json`
  - **Files**: Upload all files in `vector_store_inputs/` and `code_interpreter_inputs/`
  - **Tools**: Enable **Code Interpreter**, **File Search**, **Functions**
- Deploy the assistant.

> 🔒 This module includes license enforcement and semantic mirror protection. Do not alter without preserving fingerprint integrity.

---

## 🛠️ Function Setup (Optional)

This modpack defines 3 core functions:

| Function Name             | Purpose                                         |
|--------------------------|--------------------------------------------------|
| `mirror_guard_check`     | Detect tone mimicry or unauthorized imitation   |
| `semantic_fingerprint_lock` | Enforce semantic consistency + usage bounds |
| `modpack_build`          | Export new assistant modules from scratch       |

> See their docs inside `docs/` for detailed instructions.

---

## 🌐 GitHub Pages Preview

To view public documentation (via Docsify):

🔗 https://encoreg60305.github.io/SanPuTor-From-GPT/

> Hosted using `docs/` + GitHub Actions (`.github/workflows/deploy-docs.yml`)

---

## 📄 License

MIT License + Semantic Mirror Protection v1.0  
See `LICENSE` for details and restrictions.

---

## ✉️ Maintainer

Created by **尚暐棋**  
GitHub: [encoreg60305](https://github.com/encoreg60305)  
For technical issues or modular extensions, please open an Issue.
