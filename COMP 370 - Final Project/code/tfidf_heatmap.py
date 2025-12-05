import os
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

output_file = Path("../results")

# Load your file
df = pd.read_csv("top10_tfidf_per_topic.csv")

# Create a matrix: rows = topics (label), columns = words, values = tf-idf
#    Missing combinations get 0 (or you could use NaN if you prefer)
heatmap_df = df.pivot_table(
    index="label",      # rows = topics
    columns="word",     # columns = words
    values="tfidf",     # cell = tf-idf score
    fill_value=0.0
)

# Sort columns by overall importance
# e.g., sort by maximum tf-idf across topics so more important words come first
word_order = heatmap_df.max(axis=0).sort_values(ascending=False).index
heatmap_df = heatmap_df[word_order]

# Plot the entire heatmap with all the TF-IDF scores
plt.figure(figsize=(max(8, 0.4 * len(heatmap_df.columns)), 0.6 * len(heatmap_df.index)))

im = plt.imshow(heatmap_df.values, aspect="auto")  # default colormap

plt.colorbar(im, label="TF-IDF score")

plt.xticks(
    range(heatmap_df.shape[1]),
    heatmap_df.columns,
    rotation=90
)
plt.yticks(
    range(heatmap_df.shape[0]),
    heatmap_df.index
)

plt.xlabel("Word")
plt.ylabel("Topic")
plt.title("TF-IDF heatmap – top 10 terms per topic")
plt.tight_layout()
plt.show()

# Construct another heatmap by keeping only the words that have overlap with other topics or significant scores
words_to_keep = ["trump", "russia","aid", "russian", "said", "war", "troops", "congress", "house", "meeting", "putin"]
heatmap_df_small = heatmap_df[words_to_keep]

plt.figure(figsize=(8, 4))
im = plt.imshow(heatmap_df_small.values, aspect="auto")
plt.colorbar(im, label="TF-IDF score")

plt.xticks(
    range(heatmap_df_small.shape[1]),
    heatmap_df_small.columns,
    rotation=90
)
plt.yticks(
    range(heatmap_df_small.shape[0]),
    heatmap_df_small.index
)

plt.xlabel("Word")
plt.ylabel("Topic")
plt.title("TF-IDF Heatmap of Overlapping and High-Weight Terms")
plt.tight_layout()

plt.savefig(output_file/f"tfidf_heatmap_overlapping.png", dpi=300, bbox_inches="tight")
plt.show()
