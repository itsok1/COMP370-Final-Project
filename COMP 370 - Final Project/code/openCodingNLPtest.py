from transformers import pipeline
import pandas as pd

# ---------------------------------------------------------
# Zero-shot classifier (most intelligent option)
# ---------------------------------------------------------

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

LABELS = [
    "Diplomacy",
    "Military Support",
    "Peace Strategy",
    "Domestic Affairs",
    "Leadership Image",
    "War Consequences"
]

# ---------------------------------------------------------
# Function: Assign labels using zero-shot NLP
# ---------------------------------------------------------

def classify_text(text):
    """
    Use zero-shot classification to assign ONLY ONE label (single annotation).
    """
    result = classifier(
        text,
        candidate_labels=LABELS,
        multi_label=True
    )

    # Always pick the highest-scoring label
    top_label = result["labels"][0]

    return top_label



# ---------------------------------------------------------
# Tag entire dataset
# ---------------------------------------------------------

def tag_dataset(input_csv, output_csv="tagged_output_nlp.csv"):
    df = pd.read_csv(input_csv)

    # Ensure required fields
    if "title" not in df.columns or "short_opening" not in df.columns:
        raise ValueError("CSV must contain 'title' and 'short_opening' columns")

    # Combine content
    df["combined"] = (
        df["title"].fillna("") + ". " +
        df["short_opening"].fillna("")
    )

    # Apply classification
    df["tags"] = df["combined"].apply(classify_text)

    # Save output
    df.to_csv(output_csv, index=False, encoding="utf-8")
    print(f"Smart NLP tagging complete! Saved to: {output_csv}")


# ---------------------------------------------------------
# Run
# ---------------------------------------------------------

if __name__ == "__main__":
    tag_dataset("open_coding_200.csv")
