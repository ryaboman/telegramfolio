import joblib
import pandas as pd
from apps.text_classification import text_preprocessing as tp

model = joblib.load('apps/text_classification/model_text_classification.pkl')

def get_predict(text):
    data = pd.DataFrame(data={text}, columns=['text'])
    features = tp.preprocessing(data=data)
    return model.predict(features)[0]
