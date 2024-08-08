from typing import List

from langserve import CustomUserType


class ElasticSearchDeleteRequest(CustomUserType):
    index_name: str
    mode: str = "delete_index"
    delete_knowledge_ids: List[int] = []
