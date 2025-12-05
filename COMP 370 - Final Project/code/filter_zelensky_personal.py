import pandas as pd
import spacy
import re

############################################
#  PART 1 — LOAD NLP Model
############################################

nlp = spacy.load("en_core_web_sm")

############################################
#  PART 2 — ENCODING FIX
############################################

def fix_common_encoding_errors(s: str) -> str:
    if not isinstance(s, str):
        return s
    try:
        return s.encode("latin1").decode("utf8")
    except:
        return s

def fix_text(s: str) -> str:
    if not isinstance(s, str):
        return s

    repaired = fix_common_encoding_errors(s)
    replacements = {
        "Â": "",
        "â€™": "’", "â€œ": "“", "â€": "”",
        "â€“": "–", "â€”": "—",
        "â€¢": "•", "â€¦": "…",
        "â€˜": "‘",
    }
    for bad, good in replacements.items():
        repaired = repaired.replace(bad, good)

    return repaired


############################################
#  PART 3 — IMPROVED CLASSIFIER
############################################

# 扩展版 Zelenskyy 名称/指代识别
Z_NAMES = [
    "zelenskyy",
    "volodymyr zelenskyy",
    "zelensky",
    "ukrainian president",
    "president of ukraine",
    "ukraine's president",
]

WAR_KEYWORDS = [
    "russian attack", "missile", "drone", "explosion", "shelling",
    "kills", "wounds", "death toll", "battle", "front line",
    "nuclear plant", "strike", "bombing"
]

# 言论类动词模式（新闻写法）
SPEECH_VERBS = [
    "says", "warns", "urges", "calls for", "tells", "asks",
    "insists", "vows", "pledges", "argues", "claims", "appeals",
    "demands", "says he", "says ukraine"
]

# 重要外交互动对象
INTERACT = [
    "nato", "eu", "european union", "white house", "pentagon",
    "biden", "scholz", "sunak", "meloni", "macron", "putin",
    "congress", "senate", "house of representatives"
]


def contains_z_name(text: str) -> bool:
    return any(name in text for name in Z_NAMES)


def is_pure_war_news(text: str) -> bool:
    """
    排除那些纯事件型战况新闻：
    例如 "Russian missile kills 5 in Kharkiv"
    """
    if contains_z_name(text):
        return False
    return any(kw in text for kw in WAR_KEYWORDS)


def is_speech_pattern(text: str) -> bool:
    return any(v in text for v in SPEECH_VERBS)


def is_interaction_news(text: str) -> bool:
    return contains_z_name(text) and any(i in text for i in INTERACT)


def is_spacy_subject(doc) -> bool:
    for token in doc:
        if token.text.lower() in ["zelenskyy", "volodymyr"]:
            if token.dep_ in ["nsubj", "nsubjpass"]:
                return True
    return False


def is_personal_coverage(title: str, opening: str = "") -> bool:
    """综合判断 Zelenskyy 个人报道（更宽松版本）"""

    if not isinstance(title, str):
        return False

    text = title.lower()
    doc = nlp(title)

    # 1) 排除纯战况新闻
    if is_pure_war_news(text):
        return False

    # 2) 只要标题包含 Zelenskyy 的角色指代 → 大概率是个人报道
    if contains_z_name(text):
        return True

    # 3) 言论新闻（即便标题没写他的名字）
    # 如 "Ukraine says it needs more air defense"
    if is_speech_pattern(text) and "ukraine" in text:
        return True

    # 4) 外交互动报道
    if is_interaction_news(text):
        return True

    # 5) spaCy 识别 Zelenskyy 为主语（加分项）
    if is_spacy_subject(doc):
        return True

    return False


############################################
#  PART 4 — MAIN PROGRAM
############################################

def main():
    input_file = "zelensky_globalnews_unfiltered.csv"
    output_file = "zelensky_globalnews.csv"

    print(f"读取 CSV 文件：{input_file}")
    df = pd.read_csv(input_file)

    # 修复乱码
    df["title"] = df["title"].apply(fix_text)
    df["short_opening"] = df["short_opening"].apply(fix_text)

    # 分类
    df["is_personal"] = df.apply(
        lambda row: is_personal_coverage(row["title"], row.get("short_opening", "")),
        axis=1
    )

    # 过滤
    filtered = df[df["is_personal"] == True].copy()

    # 存储
    filtered.to_csv(output_file, index=False)

    print(f"筛选完成！共 {len(filtered)} 条个人报道")
    print(f"输出文件：{output_file}")


if __name__ == "__main__":
    main()
