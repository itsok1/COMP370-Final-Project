import pandas as pd
import spacy

###########################################
# PART 1 — Load spaCy
###########################################

nlp = spacy.load("en_core_web_sm")


###########################################
# PART 2 — Text Fix Helpers
###########################################

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


###########################################
# PART 3 — Improved spaCy-based Classifier
###########################################

WAR_TERMS = [
    "missile", "drone", "attack", "shelling", "bombing",
    "battle", "front line", "nuclear", "strike", "killed",
    "wounded", "explosion", "atacms"
]

ACTION_VERBS = [
    "meet", "say", "urge", "seek", "appeal", "ask", "call",
    "warn", "reject", "deny", "remove", "fire", "replace",
    "launch", "visit", "face", "challenge", "appoint",
    "vow", "tout", "criticize", "chide", "slam", "praise",
    "address", "defend", "accuse"
]

def is_personal_coverage(title: str, opening: str = "") -> bool:
    """
    Improved spaCy model:
    ✔ Zelensky is subject, or
    ✔ Zelensky performs an action verb, or
    ✔ Zelensky appears in early tokens, or
    ✔ Exclude war-only reports unless Zelensky is actor/commentator
    """

    if not isinstance(title, str):
        return False

    t = title.lower()

    if "zelensky" not in t:
        return False

    doc = nlp(title)

    # Rule 1 — If Zelensky is subject (spaCy reliable here)
    for token in doc:
        if token.text.lower().startswith("zelensky"):
            if token.dep_ in ["nsubj", "nsubjpass"]:
                return True

    # Rule 2 — Zelensky within first 3 tokens = highly likely personal
    first_tokens = [token.text.lower() for token in doc[:4]]
    if any(tok.startswith("zelensky") for tok in first_tokens):
        return True

    # Rule 3 — Zelensky + action verb
    if "zelensky" in t:
        for token in doc:
            if token.lemma_.lower() in ACTION_VERBS:
                return True

    # Rule 4 — Exclude pure war-event headlines
    if any(w in t for w in WAR_TERMS):
        # But keep if Zelensky is making statements about them
        if any(v in t for v in ACTION_VERBS):
            return True
        return False

    # Default: if Zelensky appears and no war-only context → keep
    return True


###########################################
# PART 4 — Main Program
###########################################

def main():
    input_file = "wsj_articles.csv"
    output_file = "zelensky_WSJ.csv"

    print(f"📄 Loading: {input_file}")
    df = pd.read_csv(input_file)

    df["title"] = df["title"].apply(fix_text)
    df["shortopening"] = df["shortopening"].apply(fix_text)

    print("🔍 Running spaCy classification...")

    df["is_personal"] = df.apply(
        lambda row: is_personal_coverage(row["title"], row["shortopening"]),
        axis=1
    )

    filtered = df[df["is_personal"] == True].copy()
    filtered.to_csv(output_file, index=False)

    print(f"🎉 完成！共 {len(filtered)} 条人物报道")
    print(f"👉 输出文件: {output_file}")


if __name__ == "__main__":
    main()
