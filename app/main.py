from fastapi import FastAPI

app = FastAPI(title="Geek Text API")

@app.get("/health")
def health():
    return {"status": "ok"}