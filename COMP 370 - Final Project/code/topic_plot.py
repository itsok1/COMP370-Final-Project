import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# Folder where all the outlet CSVs are stored
data_folder = Path("../data/cleaned")
output_folder = Path("../results")
TOPIC_COL = "label"

dfs = []

for csv_path in data_folder.glob("*.csv"):
    outlet_name = csv_path.stem  # e.g. "AP", "CBC", "FoxNews" from "AP.csv"
    df = pd.read_csv(csv_path)
    
    if TOPIC_COL not in df.columns:
        print(f" Warning: '{TOPIC_COL}' column not found in {csv_path.name}")
    
    df["Outlet"] = outlet_name

    dfs.append(df)

# Combine all outlets into a single DataFrame
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

data["Outlet"] = data["Outlet"].replace(rename_map)

# Count articles per (topic, outlet) to get the table
topic_counts = (
    data
    .groupby(TOPIC_COL)
    .size()
    .reset_index(name="count")
)

# Plot with the count of articles for each topic
topic_outlet_counts = pd.crosstab(
    data["label"],    # rows = topics
    data["Outlet"]    # columns = outlets
)

# Plot with separated bars for each topic
ax1 = topic_outlet_counts.plot(
    kind="bar",
    stacked=True,   
    figsize=(12, 6)
)

ax1.set_title("Number of Articles per Topic, by Media Outlet")
ax1.set_xlabel("Topic")
ax1.set_ylabel("Number of articles")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

fig = ax1.get_figure()
fig.savefig(output_folder / f"label_counts_per_topic_media.png", dpi=300, bbox_inches="tight")
