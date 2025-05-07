from qdrant_client import QdrantClient
from docling.chunking import HybridChunker
from docling.datamodel.base_models import InputFormat
from docling.document_converter import DocumentConverter
from response import token
#from test import load_youtube_transcript


qdrant_client = QdrantClient(
    url="<your_qdrant_url>",
    api_key= "<your_api_key>",
    prefer_grpc=False,
    timeout=30,
    check_compatibility=False)

qdrant_client.set_model("sentence-transformers/all-MiniLM-L6-v2")
qdrant_client.set_sparse_model("Qdrant/bm25")

User_input = input("Hello there! shoot me your question: ")
question  = User_input

points = qdrant_client.query(
    collection_name = "summarisor",
    query_text = question,
    limit = 7,
    )

# for i, point in enumerate(points):
#     print(f"=== {i} ===")
#     print(point.document)
#     print(point.score)

final_points = ""

for point in points:
    final_points += point.document


prompt = f"""
 context: {final_points}
 Question: {question}
Answer : Answer the question based on the content.
"""

# print(token(prompt, "openai/gpt-4.1"))
for tok in token(prompt, "openai/gpt-4.1"):
    print(tok, end="", flush=True)
#print(prompt)
