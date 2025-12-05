import pandas as pd
import os

def build_training_set(input_csv, output_csv="training_set.csv"):
    """
    Build a machine-learning-ready training set from a manually-labeled CSV.

    Requirements for input CSV:
    - Must contain columns: id, title, short_opening, label
    - Additional columns are ignored

    Output:
    - training_set.csv with columns:
        id, title, short_opening, label, text
    """

    # 1. Check file exists
    if not os.path.exists(input_csv):
        raise FileNotFoundError(f"Input file does not exist: {input_csv}")

    # 2. Load data
    df = pd.read_csv(input_csv)

    # 3. Required columns
    required_cols = ["id", "title", "short_opening", "label"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # 4. Clean text fields
    df["title"] = df["title"].fillna("").astype(str)
    df["short_opening"] = df["short_opening"].fillna("").astype(str)
    df["label"] = df["label"].astype(str)

    # 5. Combine text field
    df["text"] = (df["title"] + " " + df["short_opening"]).str.strip()

    # 6. Sort by ID for consistency
    df = df.sort_values("id")

    # 7. Save output
    df.to_csv(output_csv, index=False)
    print(f"Training set generated successfully: {output_csv}")


# Example usage:
#build_training_set("open_coding_200_manual_labeled.csv")
