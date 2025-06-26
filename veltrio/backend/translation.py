from transformers import pipeline
translator = pipeline('translation', model='Helsinki-NLP/opus-mt-fr-en')
def translate_text(text):
    return translator(text)[0]['translation_text']