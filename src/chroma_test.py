import chromadb
from dotenv import load_dotenv
import os
load_dotenv()



client = chromadb.CloudClient(
  api_key=os.getenv("CHROMA_API_KEY"),
  tenant=os.getenv("CHROMA_TENANT"),
  database=os.getenv("CHROMA_DB_NAME")
)


collection = client.get_collection(name='customer-support-messages')
result = collection.query(query_texts=["I need help with my order"], n_results=3)
print(result)