import pandas as pd
import numpy as np
import torch
import transformers


tokenizer = transformers.BertTokenizer(vocab_file='apps/text_classification/rubert-tiny2/vocab.txt')
config = transformers.BertConfig.from_json_file('apps/text_classification/rubert-tiny2/config.json')
model_bert = transformers.BertModel.from_pretrained(
    'apps/text_classification/rubert-tiny2/pytorch_model.bin', config=config)

max_len = 318#133

def preprocessing(data):
    vector = data['text'].apply(
        lambda x: tokenizer.encode(x, add_special_tokens=True)
    )

    padded = np.array([i + [0]*(max_len - len(i)) for i in vector.values])
    attention_mask = np.where(padded != 0, 1, 0)

    padded = torch.LongTensor(padded)
    attention_mask = torch.LongTensor(attention_mask)

    with torch.no_grad():
        embeddings = model_bert(padded, attention_mask=attention_mask)

    return embeddings[0][:, 0, :].numpy()

