import torch
from apps.digit_recognition import preprocessing as pprc


model = torch.jit.load('apps/digit_recognition/digit_rec_jit.pkl')

def get_predict(img_path):
    img = pprc.preprocessing_img(img_path)
    img_torch = torch.from_numpy(img).float()
    return model(img_torch).detach().numpy().argmax()

# img_path = '../../img/7.jpg'
# print(get_predict(img_path))