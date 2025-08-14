"""Small evaluation helper that loads predictions and prints classification report using seqeval."""
from seqeval.metrics import classification_report, f1_score
import json, sys
# expects a JSON with { 'predictions': [[labels...]], 'references': [[labels...]] }
if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv)>1 else 'eval_preds.json'
    data = json.load(open(path,'r',encoding='utf-8'))
    print(classification_report(data['references'], data['predictions']))
    print('F1:', f1_score(data['references'], data['predictions']))
