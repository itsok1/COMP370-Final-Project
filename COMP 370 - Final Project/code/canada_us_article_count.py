import os
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# Folder where all your per-outlet CSVs live
DATA_DIR = Path("../data/cleaned")   # <-- change this
output_file = Path("../results/us_canada")

# Map outlet names to CSV filenames
outlet_files = {
    "Associated Press": "zelensky_ap_filtered.csv",
    "CBC News": "zelensky_cbc_filtered.csv",
    "CTV News": "zelensky_ctv_filtered.csv",
    "Fox News": "zelensky_foxnews_filtered.csv",
    "Global News": "zelensky_globalnews_filtered.csv",
    "NBC News": "zelensky_nbc_filtered.csv",
    "NPR": "zelensky_npr_filtered.csv",
    "NY Times": "zelensky_nytimes_filtered.csv",
    "The Wall Street Journal News": "zelensky_wsj_filtered.csv",
    "The Wall Street Journal Opinions": "zelensky_wsjopinions_filtered.csv",
}

# Name of the column that contains the topic label in each CSV
TOPIC_COL = "label" 

country_by_outlet = {
    "Associated Press": "United States",
    "CBC News": "Canada",
    "CTV News": "Canada",
    "Fox News": "United States",
    "Global News": "Canada",
    "NBC News": "United States",
    "NPR": "United States",
    "NY Times": "United States",
    "The Wall Street Journal News": "United States",
    "The Wall Street Journal Opinions": "United States",
}

all_rows = []

for outlet, filename in outlet_files.items():
    file_path = os.path.join(DATA_DIR, filename)
    df = pd.read_csv(file_path)

    # Keep only the topic column and add outlet + country info
    tmp = df[[TOPIC_COL]].copy()
    tmp["Outlet"] = outlet
    tmp["Country"] = country_by_outlet[outlet]

    all_rows.append(tmp)

data = pd.concat(all_rows, ignore_index=True)

counts = (
    data.groupby(["Country", TOPIC_COL])
        .size()
        .unstack("Country", fill_value=0)
        .sort_index()
)

# Move topics back to a column so it's nicer as a CSV
counts = counts.reset_index().rename(columns={TOPIC_COL: "Topic"})

print(counts)

output_path = output_file/f"canada_us_topic_counts.csv"
counts.to_csv(output_path, index=False)
print(f"Saved table to {output_path}")
