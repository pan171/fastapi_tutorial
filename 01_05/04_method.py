from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/get")
def get_test():
    return {"method": "get method"}


@app.post("/post")
def post_test():
    return {"method": "post method"}


@app.put("/put")
def put_test():
    return {"method": "put method"}


@app.delete("/delete")
def put_delete():
    return {"method": "delete method"}


if __name__ == "__main__":
    uvicorn.run("04_method:app", port=8080, reload=True)
