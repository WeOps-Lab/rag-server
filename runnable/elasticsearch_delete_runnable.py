import elasticsearch
from langchain_core.runnables import RunnableLambda
from loguru import logger

from core.server_settings import server_settings
from user_types.elasticsearch_delete_request import ElasticSearchDeleteRequest


class ElasticSearchDeleteRunnable:
    def __init__(self):
        pass

    def execute(self, req: ElasticSearchDeleteRequest) -> bool:
        try:
            es = elasticsearch.Elasticsearch(hosts=[server_settings.elasticsearch_url],
                                             basic_auth=("elastic", server_settings.elasticsearch_password))
            if req.mode == "delete_index":
                es.indices.delete(index=req.index_name)
            elif req.mode == "delete_document_by_knowledge_id":
                query = {
                    "query": {
                        "terms": {
                            "metadata.knowledge_id": req.delete_knowledge_ids
                        }
                    }
                }
                es.delete_by_query(index=req.index_name, body=query)
            return True
        except Exception as e:
            logger.error(f"delete index failed: {req.index_name}, {e}")
            return False

    def instance(self):
        elasticsearch_index_runnable = RunnableLambda(self.execute).with_types(
            input_type=ElasticSearchDeleteRequest, output_type=bool)
        return elasticsearch_index_runnable
