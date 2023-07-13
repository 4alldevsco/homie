from langchain.document_loaders import WebBaseLoader
from langchain.indexes import VectorstoreIndexCreator
# Document loader
loader = WebBaseLoader("")
# Index that wraps above steps
index = VectorstoreIndexCreator().from_loaders([loader])
# Question-answering
question = "Pergunta"
index.query(question)