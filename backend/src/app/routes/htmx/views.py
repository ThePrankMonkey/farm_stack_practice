
from bson import ObjectId
from typing import Annotated
from fastapi import APIRouter, Form
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
import jinja2
from markdown import markdown

from app.db import client
from .models import Post

collection = client.posts.user_posts

router = APIRouter(
    prefix="/h",
    tags=["posts"],
)

sections = [
    { "title": "home", "url": "http://localhost:8000/h/home"},
    { "title": "about", "url": "http://localhost:8000/h/about"},
    { "title": "posts", "url": "http://localhost:8000/h/posts"},
    { "title": "add", "url": "http://localhost:8000/h/posts/add"},
]

templateLoader = jinja2.FileSystemLoader(searchpath="./routes/htmx/templates")
templateEnv = jinja2.Environment(loader=templateLoader)

@router.get("/")
async def htmx_root():
    template = templateEnv.get_template("main.html.j2")
    html_content = template.render(sections=sections)
    return HTMLResponse(content=html_content, status_code=200)

NO_POST = "<article>Post not found</article>"

@router.get("/posts")
async def htmx_posts_post():
    template = templateEnv.get_template("posts.html.j2")
    posts = collection.find({}).sort("timestamp", -1)
    if not posts:
        html_content = "No posts yet"
    else:
        keys = {"posts": []}
        for post in posts:
            keys["posts"].append(str(post["_id"]))
        html_content = template.render(**keys)
    return HTMLResponse(content=html_content, status_code=200)

@router.post("/posts")
async def htmx_posts_post(
    user: Annotated[str, Form(...)], 
    title: Annotated[str, Form(...)], 
    body: Annotated[str, Form(...)],
    ):
    post = Post(user=user, title=title, body=body)
    print(post)
    post = jsonable_encoder(post)
    print(post)
    resp = collection.insert_one(post)
    if resp:
        # make html
        html_content = "Success"
        return HTMLResponse(content=html_content, status_code=201)
    return HTMLResponse(content=NO_POST, status_code=404)

@router.get("/posts/add")
async def htmx_posts_add():
    template = templateEnv.get_template("post_form.html.j2")
    html_content = template.render()
    return HTMLResponse(content=html_content, status_code=200)

@router.get("/posts/{post_id}")
async def htmx_posts_get(post_id:str):
    post = collection.find_one({"_id": ObjectId(post_id)})
    post["body"] = markdown(post["body"])
    if post:
        # make html
        template = templateEnv.get_template("post_item.html.j2")
        html_content = template.render(**post)
        return HTMLResponse(content=html_content, status_code=200)
    return HTMLResponse(content=NO_POST, status_code=404)

@router.get("/about")
async def htmx_about_get():
    template = templateEnv.get_template("about.html.j2")
    html_content = template.render()
    return HTMLResponse(content=html_content, status_code=200)
