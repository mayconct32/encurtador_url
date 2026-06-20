from fastapi import FastAPI


app = FastAPI()


@app.post("/shorten-url/")
def shorten_url():
    pass

@app.get("/{path}")
def access_short_url(path: str):
    pass