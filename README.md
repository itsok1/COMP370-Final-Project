
---

## 📝 Project Overview

Our goal was to understand **how North American news media portray Zelenskyy**, using a dataset of **700 articles** from U.S. and Canadian outlets. Each article was manually annotated for:

- **Topic (8 categories)**
- **Sentiment toward Zelenskyy (positive, neutral, negative)**

We then computed:

- **Top 10 TF-IDF terms per topic**
- **LLM-generated representative summaries**
- **Visualizations** of topic distributions, sentiment, and temporal patterns

---

## 🔍 Method Summary

### **1. Data Collection**
- Articles collected from 9 major outlets (U.S. + Canada)
- Final dataset after cleaning: **700 articles**
- Excluded:  
  - Articles not substantially about Zelenskyy  
  - Video-only pages  
  - Passingly referenced mentions  
  - Non-English Canadian outlets (due to sentiment-analysis constraints)

### **2. Topic Development**
- Open coding on 200 stratified articles  
- Final **8 topics**:
  - Military Operations  
  - Aid Policies  
  - Russia-Related Rhetoric  
  - Diplomatic Engagements  
  - Domestic Governance  
  - Economic Structure / Reconstruction  
  - Humanitarian Crisis  
  - Media Representation  

### **3. Sentiment Annotation**
- Title + opening sentence used (per project instructions)
- Clear criteria for classifying sentiment:
  - **Positive**: praise, support, heroic portrayal  
  - **Negative**: criticism, controversy, blame  
  - **Neutral**: factual reporting about actions/events  

### **4. Topic Characterization**
- TF-IDF computation using scikit-learn  
- Stop-word filtering:  
  - default English stopwords  
  - custom removal of “Ukraine”, “Zelenskyy”, etc.  
- LLM summaries generated from CSVs grouped by topic  

### **5. Analysis & Visualization**
Generated:
- Topic distribution by outlet  
- Sentiment distribution by topic  
- Monthly article timeline (2022–2025)  
- TF-IDF heatmap  
- Topic-defining summaries

---

## Key Findings

- **Diplomatic Engagements** dominates coverage—Zelenskyy is portrayed primarily as a global diplomatic actor.
- Sentiment is **overwhelmingly neutral** across all topics.
- **Media Representation** shows the highest proportion of positive coverage.
- Economic Structure & Humanitarian Crisis are the least-covered topics.
- Peaks in coverage align with **major international events**, summits, and speeches.

---

## Team Members

- **Amanda Belidor** — Sentiment annotation, sentiment analysis, discussion, figures  
- **Caroline Wang** — Report writing (Intro, Data, Topic Analysis), topic annotation, TF-IDF, figures  
- **Hao Xiang Zhang** — Data collection, filtering, initial open coding, topic codebook  
