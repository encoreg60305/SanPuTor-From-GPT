import re
from datetime import datetime

# 輸入檔案名稱
LICENSE_FILE = "license_statement.txt"

# 定義關鍵條款語義標籤
CLAUSE_KEYWORDS = {
    "mirror_guard": "語氣鏡像防衛",
    "semantic_lock": "語義指紋封鎖",
    "commercial_use": "商業使用限制",
    "derivatives": "衍生作品警示",
    "creator_right": "創作者主權聲明",
    "license_type": "授權類型"
}

# 定義分析函式
def analyze_license(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    results = {}
    for key, label in CLAUSE_KEYWORDS.items():
        pattern = re.compile(rf"{key}|{label}", re.IGNORECASE)
        matches = pattern.findall(content)
        results[label] = len(matches)

    return results

# 執行分析
def print_analysis_summary():
    print(f"🔍 授權條款分析報告 — {datetime.now().strftime('%Y/%m/%d %H:%M:%S')}\n")
    summary = analyze_license(LICENSE_FILE)
    for label, count in summary.items():
        alert = "⚠️" if count == 0 else "✅"
        print(f"{alert} {label}：{count} 處出現")

    if summary.get("語氣鏡像防衛", 0) == 0:
        print("\n🚨 警告：未偵測到『語氣鏡像防衛』條款，建議補強防模仿保護。")

# 程式進入點
if __name__ == "__main__":
    print_analysis_summary()
