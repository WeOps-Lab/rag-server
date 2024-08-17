import os

from dotenv import load_dotenv
from langchain.chains.hyde.base import HypotheticalDocumentEmbedder
from langchain_community.chat_models import ChatOpenAI

from embedding.remote_embeddings import RemoteEmbeddings

load_dotenv()


def test_hyde():
    llm = ChatOpenAI(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base=os.getenv("OPENAI_BASE_URL"),
        temperature=0.7,
        model="gpt-4-o",
        max_retries=3,
    )
    remote_embedding = RemoteEmbeddings("http://fast-embed-server.ops-pilot")

    embeddings = HypotheticalDocumentEmbedder.from_llm(
        llm,
        base_embeddings=remote_embedding,
        prompt_key="web_search",
    )
    result = embeddings.embed_query("Python最新版本是多少")
    print(result)
