import pandas as pd
import glob
from pathlib import Path
import os
import re


# Load all outlet CSVs
DATA_FOLDER = Path("../data/cleaned")

dfs = []

for csv_path in DATA_FOLDER.glob("*.csv"):
    outlet_name = csv_path.stem          # e.g. "AP" from "AP.csv"
    df = pd.read_csv(csv_path)
    
    df["outlet"] = outlet_name                    # add outlet name

    dfs.append(df)

data = pd.concat(dfs, ignore_index=True)
print("Combined shape:", data.shape)

output_dir = Path("../data/topic")
os.makedirs(output_dir, exist_ok=True)

topics = data["label"].dropna().unique()

for topic in topics:
    subset = data[data["label"] == topic]

    # make file-name-safe version of the topic
    safe_name = re.sub(r"[^A-Za-z0-9]+", "_", str(topic)).strip("_")

    subset.to_csv(f"{output_dir}/topic_{safe_name}.csv", index=False)
    print(f"Saved {len(subset)} rows → topic_{safe_name}.csv")
