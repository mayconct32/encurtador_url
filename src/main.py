from fastapi import FastAPI


app = FastAPI()


@app.post("/shorten-url/")
def shorten_url():
    pass