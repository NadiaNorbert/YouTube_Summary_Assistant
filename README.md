YouTube Summary Assistant
The YouTube Summary Assistant is an intelligent tool that summarizes YouTube videos by leveraging the power of Retrieval-Augmented Generation (RAG) and vector search using Qdrant. It extracts transcripts from YouTube videos, formats them, stores them in a vector database, and allows users to ask questions or get summaries using LLMs.

Features
   Load transcripts directly from YouTube using YouTubeLoader

   Format transcripts into structured chunks using TranscriptFormat

   Use RAG to provide intelligent answers or summaries from the transcript

   Store and query data using Qdrant for fast semantic search

   Tech Stack
  
LangChain for orchestrating RAG pipelines

  Qdrant for vector similarity search
  
  YouTubeLoader to extract video transcripts
  
  TranscriptFormat for organizing transcript data
  
  OpenAI / LLM (or compatible) for summarization and question answering
How It Works
  Load Video Transcript:
    The YouTubeLoader fetches the transcript from a given YouTube URL.
  
  Format Transcript:
    The raw transcript is split and structured using the TranscriptFormat module for optimal chunking.
  
  Vectorize and Store:
    Each chunk is embedded and stored in a Qdrant vector database.
  
  Query and Summarize:
    The user can ask questions or request summaries. The system retrieves relevant chunks using semantic similarity and feeds them into the LLM for generation.
