"""Training script using Hugging Face Transformers for token-classification (NER).
Intended to run on Colab or a GPU machine.
Edit MODEL_NAME, data paths, and training args as needed.
"""
import os
from datasets import load_dataset, DatasetDict, ClassLabel, Sequence
from transformers import AutoTokenizer, AutoModelForTokenClassification, TrainingArguments, Trainer, DataCollatorForTokenClassification
import numpy as np
from seqeval.metrics import classification_report, f1_score

MODEL_NAME = os.getenv('MODEL_NAME', 'xlm-roberta-base')  # or afroxmlr / bert-tiny-amharic if available
MAX_LEN = 128
TRAIN_FILE = os.getenv('TRAIN_FILE', 'data/labeled_sample.conll')  # conll format

def read_conll(path):
    sentences = []
    labels = []
    with open(path, 'r', encoding='utf-8') as f:
        toks = []
        labs = []
        for line in f:
            line = line.strip()
            if not line:
                if toks:
                    sentences.append(toks)
                    labels.append(labs)
                toks = []
                labs = []
            else:
                parts = line.split()
                if len(parts) >= 2:
                    toks.append(parts[0])
                    labs.append(parts[1])
        # final
        if toks:
            sentences.append(toks); labels.append(labs)
    return sentences, labels

def get_label_list(labels):
    unique = set([lab for seq in labels for lab in seq])
    label_list = sorted(unique)
    return label_list

def main():
    sentences, labels = read_conll(TRAIN_FILE)
    label_list = get_label_list(labels)
    # map labels to ids
    label_to_id = {l:i for i,l in enumerate(label_list)}
    id_to_label = {i:l for l,i in label_to_id.items()}

    # build dataset for HF datasets
    examples = []
    for toks, labs in zip(sentences, labels):
        examples.append({'tokens': toks, 'ner_tags': [label_to_id[l] for l in labs]})

    ds = DatasetDict({'train': load_dataset('json', data_files={'train':None})})  # placeholder: users should convert to HF dataset
    # NOTE: For brevity this script shows the expected flow; adapt to your environment or use notebooks for interactive processing.
    print('Labels:', label_list)
    print('Prepared', len(examples), 'examples.')
    print('Now adapt this script to create a Hugging Face Dataset from `examples`, tokenize using AutoTokenizer, align labels, and run Trainer.')

if __name__ == '__main__':
    main()
