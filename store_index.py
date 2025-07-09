from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv 
import os


load_dotenv() 

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')


if PINECONE_API_KEY is None:
    raise ValueError("PINECONE_API_KEY not found. Make sure it's set in your .env file or system environment variables.")


if OPENAI_API_KEY is None:
    print("Warning: OPENAI_API_KEY not found. Some functionalities (e.g., OpenAI embeddings/LLMs) may not work.")




extracted_data = load_pdf_file(data='Data/')
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings() 

pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "medichatbot1"

# Check if index exists before creating, to prevent errors on re-run
if index_name not in pc.list_indexes():
    pc.create_index(
        name=index_name,
        dimension=384, 
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )
else:
    print(f"Index '{index_name}' already exists. Skipping creation.")

docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings,
)

print(f"Vector store '{index_name}' created/updated successfully with {len(text_chunks)} documents.")