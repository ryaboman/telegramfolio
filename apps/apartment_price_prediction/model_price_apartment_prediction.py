import joblib
import pandas as pd



def get_predict(text):
    data = pd.DataFrame.from_dict(text)
    return 50