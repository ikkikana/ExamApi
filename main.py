from os import sync
from fastapi import FastAPI, requests
from pip._internal import req
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List

app = FastAPI()



@app.get("/ping", status_code= 200)
async def ping():
    return {
        "pong"
    }



@app.get("/home")
async def home():
        return ("""
    <html>
        <body>
            <h1>"Welcome home!"</h1>
        </body>
    </html>
    """)


@app.post("/posts", status_code=)
class posts(BaseModel):
    author: str
    title: str
    content: str
    creation_datetime: timestamp

@app.get("/posts", status_code= 200)
async def posts():
    return posts


@app.put('/posts', (req, res) => {
const existingPostIndex = posts.findIndex(post => post.title === title);

if (existingPostIndex !== -1) {
const existingPost = posts[existingPostIndex];
if (existingPost.content !== content || existingPost.author !== author) {
posts[existingPostIndex] = { title, content, author };
return res.status(200);
} else {
    posts.push({ title, content, author });
return res.status(201);
}
});

@app.get("/ping/auth", response_class=PlainTextResponse)
async def ping_auth(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Authentication required", headers={"Content-Type": "text/plain"})

    if not authorization.startswith("Basic"):
        raise HTTPException(status_code=401, detail="Invalid authentication scheme", headers={"Content-Type": "text/plain"})

        if (username == "admin" and password == "123456"){
        return "pong"
        }
        else{
            raise HTTPException(status_code=401, detail="Invalid credentials", headers={"Content-Type": "text/plain"})
        }



