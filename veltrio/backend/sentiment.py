from transformers import pipeline
analyzer = pipeline('sentiment-analysis')
def analyze_sentiment(text):
    return analyzer(text)[0]['label']