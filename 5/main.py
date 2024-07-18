from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import spacy

app = FastAPI()

# Load Spacy model
nlp = spacy.load("en_core_web_sm")

class TextInput(BaseModel):
    text: str

@app.post("/summarize/")
async def summarize_text(input: TextInput):
    text = input.text
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, 15)  

    summary_text = " ".join([str(sentence) for sentence in summary])
    words = summary_text.split()

    if len(words) > 100:
        summary_text = " ".join(words[:100]) + "..."

    return {"summary": summary_text}

@app.post("/token_count/")
async def token_count(input: TextInput):
    text = input.text
    doc = nlp(text)
    tokens = [token.text for token in doc]

    return {"token_count": len(tokens)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


