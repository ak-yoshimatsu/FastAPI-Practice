from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index() -> dict[str, str]:
    return {"result": "index"}


@app.post("/")
def store() -> dict[str, str]:
    return {"result": "store"}


@app.get("/{id}")
def show(id: str) -> dict[str, str]:
    return {"result": f"show id is {id}"}


@app.put("/{id}")
def update(id: str) -> dict[str, str]:
    return {"result": f"update id is {id}"}


@app.delete("/{id}")
def destroy(id: str) -> dict[str, str]:
    return {"result": f"destroy id is {id}"}
