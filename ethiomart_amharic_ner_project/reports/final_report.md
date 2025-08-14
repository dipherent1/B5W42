    # Final Report — EthioMart Amharic NER Project


    ## Executive Summary

This project implements a repeatable workflow to ingest Telegram e-commerce messages, preprocess and label Amharic text, fine-tune NER models, and produce vendor analytics for micro-lending decisions. Included are sample datasets and runnable scripts; training requires a GPU environment and valid Telegram API credentials.

## What I built
- **Data ingestion**: Telethon-based scraper scaffold.
- **Preprocessing**: Normalization and tokenization scripts for Amharic.
- **Labeling**: Example CoNLL file with 30 labelled messages (in `data/labeled_sample.conll`).
- **Model training**: Hugging Face training script template (`scripts/train_ner.py`) to fine-tune XLM-R.
- **Evaluation**: `scripts/evaluate.py` using seqeval.
- **Explainability**: guidance and code snippets (see sections below) to run SHAP and LIME.
- **Vendor scorecard**: `scripts/vendor_score.py` computes simple lending metrics.

## How to reproduce (high-level)
1. Run the Telethon scraper with your `TG_API_ID` and `TG_API_HASH` to collect channel messages.
2. Preprocess messages using `scripts/preprocess.py`.
3. Label 30–50 messages in CoNLL format (we provide a labeled sample). Use tools like [Doccano] or [Prodigy] for faster annotation.
4. Convert the labeled CoNLL into Hugging Face Dataset and run `scripts/train_ner.py` on Colab with GPU.
5. After training, run evaluation and use SHAP/LIME to inspect model outputs.
6. Enrich posts with metadata (views) and run `scripts/vendor_score.py` to create the Vendor Scorecard.

## Recommendations
- Use `xlm-roberta-base` or an Amharic-specific model (if available) as the base checkpoint.
- Label more data (>=1k messages) for production-grade performance.
- Consider image OCR pipeline (Tesseract or Google Vision) for text inside images.

## Limitations
- Provided dataset is synthetic and small; real performance depends on high-quality labeled data.

## Appendix
See scripts/ and data/ for examples and runnable code.
