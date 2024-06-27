from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.post(
    "/items",
    tags=["这是一个 items 的测试接口"],
    summary="这是测试 summary",
    description="这是测试 description",
    response_description="这是response_description",
    deprecated=True,
)
def post_test():
    return {"items": "items data"}


if __name__ == "__main__":
    uvicorn.run("05_method_para:app", port=8080, reload=True)
