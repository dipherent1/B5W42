# EthioMart — Amharic NER Project (Deliverable)
This repository contains a complete, runnable project scaffold for EthioMart's Amharic NER challenge. It includes:
- Telegram scraping instructions and a sample scraper (Telethon-based).
- Data preprocessing and tokenization scripts.
- A sample labeled dataset (30-50 messages) in CoNLL format.
- Hugging Face training script (`train_ner.py`) to fine-tune XLM-R or an Amharic model for NER.
- Scripts for model evaluation, SHAP/LIME explainability, and a Vendor Scorecard generator.
- `requirements.txt` listing libraries used.


**Note:** This package contains sample/synthetic data and example code. Some steps (like actual Telegram API credentials and GPU training environment) require you to supply credentials and run on a GPU-enabled machine (Colab, local GPU, or remote VM).

## Quick start
1. Unzip the project and `cd` into the folder.
2. Create a Python virtual env and install dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Prepare Telegram credentials and follow `scripts/telegram_scraper.py` comments to start ingesting messages.
4. See `notebooks/` and `train_ner.py` for training instructions.

## Folder layout
```
ethiomart_amharic_ner_project/
  ├─ data/
  │   ├─ sample_messages.csv
  │   └─ labeled_sample.conll
  ├─ scripts/
  │   ├─ telegram_scraper.py
  │   ├─ preprocess.py
  │   ├─ train_ner.py
  │   ├─ evaluate.py
  │   └─ vendor_score.py
  ├─ reports/
  │   └─ final_report.md
  ├─ requirements.txt
  └─ README.md
```
