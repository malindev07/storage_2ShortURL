import contextlib
from typing import TypedDict, AsyncIterator

import uvicorn
from fastapi import FastAPI, Depends

from func_handlers.action_data import router
from storage.repository import dependency_repository, Repository


class State(TypedDict):
    repository: Repository


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[State]:
    yield {
        "repository": Repository()
    }


app = FastAPI(lifespan=lifespan)


app.include_router(router, prefix="/api")


if __name__ == '__main__':
    uvicorn.run(app)
