import elasticsearch
from langchain_core.runnables import RunnableLambda
from loguru import logger

from core.server_settings import server_settings
from user_types.elasticsearch_delete_request import ElasticSearchDeleteRequest


class ElasticSearchDeleteRunnable:
    def __init__(self):
        pass

    def elasticsearch_delete_func(self, req: ElasticSearchDeleteRequest) -> bool:
        try:
            es = elasticsearch.Elasticsearch(hosts=[server_settings.elasticsearch_url],
                                             basic_auth=("elastic", server_settings.elasticsearch_password))
            es.indices.delete(index=req.index_name)
            return True
        except Exception as e:
            logger.error(f"delete index failed: {req.index_name}, {e}")
            return False

    def instance(self):
        elasticsearch_index_runnable = RunnableLambda(self.elasticsearch_delete_func).with_types(
            input_type=ElasticSearchDeleteRequest, output_type=bool)
        return elasticsearch_index_runnable
