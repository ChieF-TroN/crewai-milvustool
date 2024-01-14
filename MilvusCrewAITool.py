from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Milvus
from langchain_community.embeddings import OllamaEmbeddings
from langchain.agents import Tool

class MilvusTool(Tool):
    def __init__(self, connection_args=None, collection_name="default"):
        """Initialize vector database"""
        super().__init__(name="MilvusTool", func=self.__init__, description="Initialize the vector database")
    def store_documents(self, documents):
        """Store documents into the vector database"""
        embeddings = OllamaEmbeddings(model="llama-pro:8b-instruct-fp16")
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        docs = text_splitter.split_documents([documents])
        vector_db = Milvusfrom_documents(
            docs,
            embeddings,
            connection_args={"host": "127.0.0.1", "port": "19530"},
            collection_name="default"
        )

    def retrieve_documents(self, query):
        """Retrieve documents from the vector database"""
        embeddings = OllamaEmbeddings(model="llama-pro:8b-instruct-fp16")
        vector_db = Milvus(
            embeddings,
            connection_args={"host": "127.0.0.1", "port": "19530"},
            collection_name="default"
        )

        fl = vector_db.similarity_search(query)
        return [doc["data"] for doc in fl]
