import json
from typing import List


from fastapi import APIRouter, Depends, FastAPI, Request

from model.model import DataURLS
from storage.repository import Repository, dependency_repository


def make_short_url(long_url: str) -> str:
    # TODO: нужно релизовать генерация короткого url
    return "sdfsdf"


router = APIRouter()


@router.get("/url")
def show_all_urls_handler(req: Request) -> DataURLS:
    return req.state.repository.load()


@router.put("/url")
def update_url_handler(short_url: str, long_url: str, req: Request) -> DataURLS:
    return req.state.repository.add(short_url=short_url, long_url=long_url)


@router.delete("/url")
def delete_url_handler(short_url: str, req: Request) -> DataURLS:
    return req.state.repository.delete_url(short_url=short_url)


@router.post("/url")
def add_url_handler(short_url: str, long_url: str, req: Request) -> DataURLS:
    return req.state.repository.add(short_url=short_url, long_url=long_url)




