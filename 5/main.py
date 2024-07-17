from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from nltk.tokenize import word_tokenize
from gensim import summarize

app = FastAPI()

class TextRequest(BaseModel):
    text: str

class SummaryResponse(BaseModel):
    summary: str

class TokenCountResponse(BaseModel):
    token_count: int

@app.post("/summarize", response_model=SummaryResponse)
def summarize_text(request: TextRequest):
    try:
        summary = summarize(request.text, word_count=100)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/token-count", response_model=TokenCountResponse)
def count_tokens(request: TextRequest):
    tokens = word_tokenize(request.text)
    return {"token_count": len(tokens)}
