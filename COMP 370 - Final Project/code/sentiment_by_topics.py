import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
cleaned_path = project_root / "data" / "cleaned"

csv_files = list(cleaned_path.glob("zelensky_*_filtered.csv"))

if not csv_files:
    raise FileNotFoundError(f"No CSV files found in {cleaned_path}")

# Map filenames to full outlet names
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
    "zelensky_wsjopinions_filtered": "The Wall Street Journal Opinions",
}

all_dfs = []

for file in csv_files:
    df = pd.read_csv(file)
    outlet_key = file.stem
    outlet = rename_map.get(outlet_key, outlet_key)
    df["outlet"] = outlet

    df["sentiment"] = (
        df["sentiment"]
        .astype(str)
        .str.strip()
        .str.lower()
    )
    df = df[df["sentiment"] != "nan"]

    all_dfs.append(df)

full_df = pd.concat(all_dfs, ignore_index=True)

results_dir = project_root / "results"
results_dir.mkdir(exist_ok=True)

sentiment_order = ["negative", "neutral", "positive"]
full_df["sentiment"] = pd.Categorical(
    full_df["sentiment"],
    categories=sentiment_order,
    ordered=True
)

# Sentiment by outlet 

grouped_outlet = full_df.groupby(["sentiment", "outlet"]).size().unstack(fill_value=0)

grouped_outlet.plot(kind="bar", stacked=True, figsize=(10, 6))

plt.xlabel("Sentiment")
plt.ylabel("Number of Articles")
plt.title("Article Sentiment Toward Zelensky by Outlet")
plt.legend(title="Outlet", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

output_path_outlet = results_dir / "sentiment_by_outlet.png"
plt.savefig(output_path_outlet, dpi=300)
plt.close()


# Sentiment by topic  

TOPIC_COL = "label"

if TOPIC_COL not in full_df.columns:
    raise KeyError(f"Column '{TOPIC_COL}' not found in dataframe. "
                   f"Change TOPIC_COL to your actual topic column name.")

topic_df = full_df.dropna(subset=[TOPIC_COL])

# Group by topic + sentiment
grouped_topic = (
    topic_df
    .groupby([TOPIC_COL, "sentiment"])
    .size()
    .unstack(fill_value=0)
)

grouped_topic = grouped_topic.loc[grouped_topic.sum(axis=1).sort_values(ascending=False).index]
# Plot
ax = grouped_topic.plot(
    kind="bar",
    stacked=True,
    figsize=(12, 6)
)

plt.xlabel("Topic")
plt.ylabel("Number of Articles")
plt.title("Article Sentiment Toward Zelensky by Topic")
plt.xticks(rotation=45, ha="right")
plt.legend(title="Sentiment", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

output_path_topic = results_dir / "sentiment_by_topic.png"
plt.savefig(output_path_topic, dpi=300)
plt.close()

# Topic Trends Over Time

DATE_COL = "date"
TOPIC_COL = "label"

# Convert date
full_df[DATE_COL] = pd.to_datetime(full_df[DATE_COL], errors="coerce")

time_df = full_df.dropna(subset=[DATE_COL, TOPIC_COL]).copy()
time_df = time_df[
    (time_df[DATE_COL].dt.year >= 2022) &
    (time_df[DATE_COL].dt.year <= 2025)
]

time_df["year"] = time_df[DATE_COL].dt.year
time_df["month"] = time_df[DATE_COL].dt.month
topic_trends = (
    time_df
    .groupby(["year", "month", TOPIC_COL])
    .size()
    .unstack(fill_value=0)
)

# Build from 2022-01 to 2025-12
years = range(2022, 2026)
months = range(1, 13)
full_index = pd.MultiIndex.from_product(
    [years, months],
    names=["year", "month"]
)
topic_trends = topic_trends.reindex(full_index, fill_value=0)
topic_trends.index = [f"{y}-{m:02d}" for (y, m) in topic_trends.index]

# Plot topic trends
ax = topic_trends.plot(
    kind="line",
    figsize=(12, 6),
    marker="o"
)

plt.xlabel("Month (2022–2025)")
plt.ylabel("Number of Articles")
plt.title("Topic Coverage Trends Over Time")

#Every three months
xticks = range(0, len(topic_trends.index), 3)
plt.xticks(xticks, [topic_trends.index[i] for i in xticks], rotation=45, ha="right")

plt.legend(title="Topic", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

output_path_time = results_dir / "topic_trends_over_time.png"
plt.savefig(output_path_time, dpi=300)
plt.close()


