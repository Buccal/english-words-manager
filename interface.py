from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

excludes = ["the", "apple", "this", "that"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    context: str

@app.get("/")
async def main():
    return {"message": "Hello , this is FastAPI."}

@app.post("/wordfrequency/")
async def cal_word_frequency(body: Item):
    context = body.context.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        context = context.replace(ch, " ")
    words  = context.split()
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        if word in excludes:
            continue
        counts[word] = counts.get(word,0) + 1
    items = list(counts.items())
    items.sort(key=lambda x:x[1], reverse=True)
    return items

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)