FROM python:3.10
LABEL authors="ryaboman"

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN python -m pip install pandas numpy scikit-learn aiogram joblib torch==2.0.1 transformers environs opencv-python

WORKDIR /bot

ADD apps apps
ADD core core
ADD img img
ADD main.py main.py

CMD ["python", "main.py"]
