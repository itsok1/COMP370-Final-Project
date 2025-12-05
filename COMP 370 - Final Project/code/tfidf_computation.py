import pandas as pd
from pathlib import Path
import glob
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS


DATA_FOLDER = Path("../data/cleaned")   # folder where the CSVs are
output_csv = Path("../results")

dfs = []

for csv_path in DATA_FOLDER.glob("*.csv"):
    outlet_name = csv_path.stem
    df = pd.read_csv(csv_path)
    
    df["outlet"] = outlet_name                    # add outlet name

    dfs.append(df)

data = pd.concat(dfs, ignore_index=True)

# Rename the outlets from filename to media outlet name
rename_map = {
    "zelensky_ap_filtered": "Associated Press",
    "zelensky_cbc_filtered": "CBC News",
    "zelensky_ctv_filtered": "CTV News",
    "zelensky_foxnews_filtered": "Fox News",
    "zelensky_globalnews_filtered": "Global News",
    "zelensky_nbc_filtered": "NBC News",
    "zelensky_npr_filtered": "NPR",
    "zelensky_nytimes_filtered": "NY Times",
    "zelensky_wsj_filtered": "The Wall Street Journal News",
    "zelensky_wsjopinions_filtered": "The Wall Street Journal Opinions"
}

data["outlet"] = data["outlet"].replace(rename_map)

data = data.dropna(subset=["label", "short_opening"])

topic_docs = data.groupby("label")["short_opening"].apply(lambda x: " ".join(x)).reset_index()
# Normalize U.S. to US
topic_docs["short_opening"] = (
    topic_docs["short_opening"]
        .str.replace(r"\bU\.S\.\b", "US", regex=True)
        .str.replace(r"\bU\.S\b", "US", regex=True)
        .str.replace(r"\bU\. S\.\b", "US", regex=True)
)

# Count out the common stop words and all terms of Volodymyr Zelenskyy and Ukraine
custom_stopwords = {
    "zelensky", "zelenskyy", "volodymyr",
    "ukraine", "ukrainian", "president"
}

stop_words = ENGLISH_STOP_WORDS.union(custom_stopwords)
stop_words = list(stop_words)   # convert frozenset → list

vectorizer = TfidfVectorizer(
    stop_words=stop_words,
    lowercase=True,
    token_pattern=r"[a-zA-Z']+",
    max_features=5000,
)

tfidf_matrix = vectorizer.fit_transform(topic_docs["short_opening"])
feature_names = vectorizer.get_feature_names_out()

rows = []

for i, topic in enumerate(topic_docs["label"]):
    row = tfidf_matrix[i].toarray().ravel()
    sorted_idx = np.argsort(row)[::-1]  # indices from highest to lowest tf-idf

    count = 0
    for idx in sorted_idx:
        word = feature_names[idx]
        score = row[idx]

        rows.append({
            "label": topic,
            "rank": count + 1,
            "word": word,
            "tfidf": score
        })
        count += 1
        if count == 10:   # top 10 per topic
            break

# Make a DataFrame and save
df_top = pd.DataFrame(rows)
df_top.to_csv(output_csv / f"top10_tfidf_per_topic.csv", index=False)

df_top.head()
