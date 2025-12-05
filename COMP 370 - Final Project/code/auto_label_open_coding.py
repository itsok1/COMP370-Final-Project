import pandas as pd
from sentence_transformers import SentenceTransformer, util
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# ===============================
# Load models
# ===============================
print("Loading bi-encoder (SentenceTransformer)...")
bi_model = SentenceTransformer('all-MiniLM-L6-v2')

print("Loading cross-encoder (DeBERTa NLI model)...")
cross_model_name = "cross-encoder/nli-deberta-v3-base"
cross_tokenizer = AutoTokenizer.from_pretrained(cross_model_name)
cross_model = AutoModelForSequenceClassification.from_pretrained(cross_model_name)

# ===============================
# Label definitions (strong, high-contrast descriptions)
# ===============================
LABELS = {
    "Diplomacy": 
        "international relations, foreign policy decisions, diplomatic meetings, or state-to-state interactions",

    "Military Affairs": 
        "battlefield actions, troop movements, airstrikes, combat operations, and military aid including weapons and defense support",

    "Peace Strategy": 
        "peace talks, ceasefire negotiations, mediation efforts, or conflict de-escalation initiatives",

    "Domestic Affairs": 
        "domestic policy, internal politics, government decisions, or national identity issues",

    "Leadership Image": 
        "political leader's public image, speeches, personal reputation, or media portrayal of leadership",

    "War Consequences": 
        "civilian casualties, humanitarian suffering, destruction, or long-term social and economic impacts of war"
}



label_names = list(LABELS.keys())
label_texts = list(LABELS.values())

# Encode label descriptions with bi-encoder
print("Encoding label embeddings...")
label_embeddings = bi_model.encode(label_texts, convert_to_tensor=True)

# ===============================
# Load CSV
# ===============================
CSV_PATH = "open_coding_200.csv"
OUTPUT_CSV = "open_coding_200_labeled.csv"

print("Reading CSV...")
df = pd.read_csv(CSV_PATH)

# Combine columns
df["combined"] = df["title"].fillna("") + " " + df["short_opening"].fillna("")
texts = df["combined"].tolist()

print(f"Total rows: {len(texts)}")

# ===============================
# Bi-Encoder Step: Encode all texts
# ===============================
print("Encoding texts with bi-encoder...")
text_embeddings = bi_model.encode(texts, convert_to_tensor=True)

print("Bi-encoder output shape:", text_embeddings.shape)

# ===============================
# Classification loop (Bi + Cross encoder)
# ===============================
predicted_labels = []

print("\nStarting classification (bi-encoder → cross-encoder)...")

for idx in range(len(df)):
    text = texts[idx]

    # ---------------------------
    # Step 1: Bi-encoder top-3 candidates
    # ---------------------------
    emb = text_embeddings[idx]
    sims = util.cos_sim(emb, label_embeddings)[0]
    topk = torch.topk(sims, k=3)
    candidate_idxs = topk.indices.tolist()

    candidates = [label_names[i] for i in candidate_idxs]
    candidate_descs = [LABELS[name] for name in candidates]

    # ---------------------------
    # Step 2: Cross-encoder deep scoring
    # ---------------------------
    cross_scores = []
    for desc in candidate_descs:
        inputs = cross_tokenizer(
            (text, desc),
            return_tensors='pt',
            truncation=True,
            padding=True  # <-- required fix!
        )
        logits = cross_model(**inputs).logits
        entail_score = logits.softmax(dim=1)[0][2].item()  # entailment score
        cross_scores.append(entail_score)

    best_idx = cross_scores.index(max(cross_scores))
    best_label = candidates[best_idx]
    predicted_labels.append(best_label)

    # Optional progress print
    if idx % 20 == 0:
        print(f"Processed {idx}/{len(df)}")

# ===============================
# Save results
# ===============================
print("\nFinished classification.")
print("Saving results...")

df["predicted_label"] = predicted_labels
df.to_csv(OUTPUT_CSV, index=False)

print("\n====================================")
print(" Classification Completed")
print(f" Labeled file saved to: {OUTPUT_CSV}")
print("====================================")
