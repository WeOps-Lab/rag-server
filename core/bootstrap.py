import uvicorn
from langserve import add_routes

from core.server_settings import server_settings
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from runnable.elasticsearch_delete_runnable import ElasticSearchDeleteRunnable
from runnable.elasticsearch_index_runnable import ElasticSearchIndexRunnable
from runnable.elasticsearch_rag_runnable import ElasticSearchRagRunnable
from runnable.online_search_runnable import OnlineSearchRagRunnable


class Bootstrap:
    def __init__(self):
        load_dotenv()
        self.app = FastAPI(title=server_settings.app_name)

    def setup_middlewares(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
            expose_headers=["*"],
        )

    def setup_router(self):
        add_routes(self.app, ElasticSearchIndexRunnable().instance(), path='/elasticsearch_index')
        add_routes(self.app, ElasticSearchDeleteRunnable().instance(), path='/elasticsearch_delete')
        add_routes(self.app, ElasticSearchRagRunnable().instance(), path='/elasticsearch_rag')
        add_routes(self.app, OnlineSearchRagRunnable().instance(), path='/online_search')

    def start(self):
        self.setup_middlewares()
        self.setup_router()
        uvicorn.run(self.app, host=server_settings.app_host, port=server_settings.app_port)
