from langserve import CustomUserType


class ElasticSearchRequest(CustomUserType):
    embed_model_address: str = "http://fast-embed-server.ops-pilot"
