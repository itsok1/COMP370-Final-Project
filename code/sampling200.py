import pandas as pd
import random
import csv
import os

# ------------------------------------------------------
# Configuration: your existing CSV filenames and sampling counts
# ------------------------------------------------------

MEDIA_SAMPLING_PLAN = {
    "left": {
        "CBC": ("data/zelensky_cbc.csv", 20),
    },
    "center-left": {
        "NBC": ("data/zelensky_nbc.csv", 20),
        "NPR": ("data/zelensky_npr.csv", 20),
        "NYTimes": ("data/zelensky_nytimes.csv", 20),
        "CTV": ("data/zelensky_ctv.csv", 20)
    },
    "center": {
        "AP": ("data/zelensky_ap.csv", 20),
        "WSJ": ("data/zelensky_wsj.csv", 20),
        "GlobalNews": ("data/zelensky_globalnews.csv", 20)
    },
    "center-right": {
        "WSJOpinions": ("data/zelensky_wsjopinions.csv", 3)
    },
    "right": {
        "FoxNews": ("data/zelensky_foxnews.csv", 37)
    }
}


OUTPUT_FILE = "open_coding_200.csv"

# Required columns
REQUIRED_COLS = ["date", "title", "short_opening", "URL"]


# ------------------------------------------------------
# Helper: load CSV and ensure required columns exist
# ------------------------------------------------------

def load_and_normalize_csv(csv_file):
    """
    Load a CSV file, and ensure that required columns exist.
    If some columns (e.g., URL) are missing, they will be added with None.
    """

    if not os.path.exists(csv_file):
        raise FileNotFoundError(f"CSV file not found: {csv_file}")

    df = pd.read_csv(csv_file)

    # Add missing columns with None
    for col in REQUIRED_COLS:
        if col not in df.columns:
            df[col] = None

    # Keep only required columns
    return df[REQUIRED_COLS]


# ------------------------------------------------------
# Helper: sample rows from CSV
# ------------------------------------------------------

def sample_rows_from_csv(csv_file, count):
    """
    Load a CSV file, normalize its columns, and randomly sample rows.
    """
    df = load_and_normalize_csv(csv_file)

    if len(df) < count:
        raise ValueError(f"Not enough rows in {csv_file} (need {count}, found {len(df)})")

    return df.sample(n=count, random_state=42).reset_index(drop=True)


# ------------------------------------------------------
# Main: generate 200-item open coding dataset
# ------------------------------------------------------

def generate_open_coding_dataset():
    """
    Create the final open coding dataset with ID, media, leaning,
    plus the four standardized article columns.
    """
    final_rows = []
    global_id = 1

    for leaning, media_dict in MEDIA_SAMPLING_PLAN.items():
        for media_name, (csv_file, num) in media_dict.items():

            sampled_df = sample_rows_from_csv(csv_file, num)

            for _, row in sampled_df.iterrows():
                record = {
                    "id": f"{leaning[:1].upper()}{global_id:03d}",
                    "media": media_name,
                    "leaning": leaning,
                }

                # Add article fields
                for col in REQUIRED_COLS:
                    record[col] = row[col]

                final_rows.append(record)
                global_id += 1

    # Save as CSV
    pd.DataFrame(final_rows).to_csv(OUTPUT_FILE, index=False, encoding="utf-8")

    print(f"Open coding dataset created successfully! Total records: {len(final_rows)}")
    print(f"Saved as: {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_open_coding_dataset()
