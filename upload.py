from qdrant_client import QdrantClient
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.document_loaders.youtube import TranscriptFormat



qdrant_client = QdrantClient(
    url="<your_qdrant_url>",
    api_key= "<your_api_key>",
    prefer_grpc=False,
    timeout=30,
    check_compatibility=False)


qdrant_client.set_model("sentence-transformers/all-MiniLM-L6-v2")
qdrant_client.set_sparse_model("Qdrant/bm25")


collectionName = "summarisor"



def upload_file(COLLECTION_NAME ,video_url):

    # Load transcript data from YouTube with chunking
    loader = YoutubeLoader.from_youtube_url(
        video_url,
        add_video_info=False,
        transcript_format=TranscriptFormat.CHUNKS,
        chunk_size_seconds=20,
    )

    docs = loader.load()
   

    transcript,metadata = [],[]

    for doc in docs:
        transcript.append(doc.page_content)
        
        
    for doc in docs:
        metadata.append(doc.metadata)

    qdrant_client.add(
        collection_name=COLLECTION_NAME,
        documents=transcript,
        metadata=metadata,
        batch_size=70,
    )
    
upload_file(collectionName,"https://www.youtube.com/watch?v=u47GtXwePms&t=45s")
print("Uploaded to Qdrant")


