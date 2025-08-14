"""Preprocessing utilities for Amharic text.
- simple normalization
- tokenization (naive)
- saving standardized CSV for training
"""
import re, csv, os
from typing import List

def normalize_amharic(text: str) -> str:
    # basic normalizations: remove extra whitespace, fix common punctuation spacing
    t = text.strip()
    t = re.sub(r'\s+', ' ', t)
    # remove weird control chars
    t = re.sub(r'[\x00-\x1f\x7f]', '', t)
    return t

def tokenize(text: str) -> List[str]:
    # naive tokenization splitting on whitespace and punctuation while preserving @user and numbers
    tokens = re.findall(r"[@\w]+|[^\s\w]", text, flags=re.UNICODE)
    return tokens

def csv_to_simple(input_csv: str, output_csv: str):
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    with open(input_csv, 'r', encoding='utf-8') as inf, open(output_csv,'w', encoding='utf-8', newline='') as outf:
        reader = csv.DictReader(inf)
        writer = csv.writer(outf)
        writer.writerow(['message_id','channel','timestamp','message','tokens'])
        for r in reader:
            msg = normalize_amharic(r['message'])
            toks = ' '.join(tokenize(msg))
            writer.writerow([r['message_id'], r.get('channel',''), r.get('timestamp',''), msg, toks])

if __name__ == '__main__':
    # example usage; adjust paths as needed
    csv_to_simple('data/sample_messages.csv','data/preprocessed_messages.csv')
