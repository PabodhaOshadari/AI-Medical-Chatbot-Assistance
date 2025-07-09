
from flask import Flask, render_template, jsonify, request
from langchain_openai import ChatOpenAI 
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from src.helper import download_hugging_face_embeddings 
from src.prompt import system_prompt 
import os


app = Flask(__name__)

#Load environment variables 
load_dotenv() 

# Get API keys from environment variables
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')


if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY environment variable not set.")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set.")


print("--- Initializing chatbot components ---")

#Initialize embeddings 
embeddings = download_hugging_face_embeddings()
print("Embeddings model loaded for retrieval.")


index_name = "medichatbot1" 

#Load existing Pinecone index (for retrieval)
print(f"Loading Pinecone index '{index_name}' for retrieval...")

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings,
    
    
)
print("Pinecone vector store loaded.")


#Create a retriever from the loaded Pinecone index
print("Creating retriever...")
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})
print("Retriever created.")

#Initialize the Language Model (LLM)
print("Initializing LLM (ChatOpenAI)...")

llm = ChatOpenAI(
    temperature=0.4,
    openai_api_key=OPENAI_API_KEY, 
    model_name="gpt-4o-mini", 
    max_tokens=500 
)
print(f"LLM initialized: {llm.model_name}")


print("Setting up prompt template...")

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt), 
    ("human", "{input}"),
])
print("Prompt template configured.")

# Create the RAG chains
print("Creating RAG chains...")
Youtube_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, Youtube_chain)
print("RAG chains created successfully.")
print("--- Chatbot initialization complete ---")


@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    user_input = msg 
    print(f"User query: {user_input}")

    try:
        response = rag_chain.invoke({"input": user_input})
        chatbot_answer = response["answer"]
        print(f"Chatbot Response: {chatbot_answer}")
        return str(chatbot_answer)
    except Exception as e:
        print(f"Error processing query: {e}")
        
        if "insufficient_quota" in str(e).lower() or "429" in str(e):
            return "Apologies, I'm currently unable to process your request due to an API quota issue. Please try again later, or contact the administrator."
        return "An error occurred while processing your request. Please try again."


if __name__ == '__main__':
    
    app.run(host="0.0.0.0", port=8080, debug=True)