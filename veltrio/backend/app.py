from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from translation import translate_text
from sentiment import analyze_sentiment

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*'])

@app.post('/process/')
async def process_text(request: Request):
    data = await request.json()
    text = data['text']
    translated = translate_text(text)
    sentiment = analyze_sentiment(translated)
    return {"translated": translated, "sentiment": sentiment}