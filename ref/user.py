from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    print("------------------------------")
    print(token)
    print("------------------------------")
    return {"token": token}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("user:app", host="127.0.0.1", port=8000, reload=True)