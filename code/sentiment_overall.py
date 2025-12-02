import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Find paths
project_root = Path(__file__).resolve().parents[1]
cleaned_path = project_root / "data" / "cleaned"

# Get all zelensky_*_filtered.csv files
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
    "zelensky_wsjopinions_filtered": "The Wall Street Journal Opinions"
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
grouped = full_df.groupby(["sentiment", "outlet"]).size().unstack(fill_value=0)

results_dir = project_root / "results"

# Plot stacked bar chart
grouped.plot(kind="bar", stacked=True, figsize=(10, 6))

plt.xlabel("Sentiment")
plt.ylabel("Number of Articles")
plt.title("Article Sentiment Toward Zelensky by Outlet")
plt.legend(title="Outlet", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

output_path = results_dir / "sentiment_by_outlet.png"
plt.savefig(output_path, dpi=300)
print(f"\nSaved figure to: {output_path}")
