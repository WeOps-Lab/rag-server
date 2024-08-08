from langserve import CustomUserType


class ElasticSearchDeleteRequest(CustomUserType):
    index_name: str
