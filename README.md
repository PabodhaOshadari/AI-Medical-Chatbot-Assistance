# AI-Medical-Chatbot-Assistance

This project develops an AI-powered medical chatbot designed to provide intelligent responses based on a curated knowledge base. It leverages advanced natural language processing (NLP) and retrieval-augmented generation (RAG) techniques to deliver accurate and contextually relevant medical information.

✨ Features

    Contextual Document Retrieval: Utilizes Pinecone for efficient vector-based storage and retrieval of medical documents.

    Semantic Search: Employs Hugging Face sentence transformers to perform semantic searches, ensuring relevant document chunks are retrieved based on the meaning of the query.

    Intelligent Responses: Generates comprehensive and coherent answers using OpenAI's GPT-4o-mini language model.

    Medical Knowledge Ingestion: Processes and extracts information from PDF documents, allowing for easy expansion of the knowledge base.

    Web-based Chat Interface: Provides a user-friendly chat interface built with Flask for seamless interaction.

    Secure API Key Handling: Manages sensitive API keys securely using .env files.

📚 Data Source

The chatbot's knowledge base is built upon data extracted from:

    The Gale Encyclopedia of Medicine – Second Edition

Documents from this resource are processed, split into manageable chunks, and embedded into vector representations for efficient retrieval.

🛠️ Tech Stack

    Python 3.x

    Flask: Web framework for the chat interface.

    LangChain: Framework for building LLM applications, facilitating integration of various components.

    Hugging Face Transformers: Used for embedding models (sentence transformers) for semantic search.

    Pinecone: Vector database for storing and retrieving document embeddings.

    OpenAI GPT (gpt-4o-mini): Large language model for generating intelligent responses.

    dotenv: For managing environment variables and API keys.

⚙️ Setup Instructions

Follow these steps to set up and run the AI Medical Chatbot:

1. Clone the Repository

Bash

git clone https://github.com/yourusername/ai-medical-chatbot.git
cd ai-medical-chatbot

2. Install Dependencies

Bash

pip install -r requirements.txt

3. Configure Environment Variables

Create a .env file in the root directory of the project and add your API keys:

OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key

Replace your_openai_api_key and your_pinecone_api_key with your actual API keys.

4. Add PDF Files

Place your medical PDF files (e.g., "The Gale Encyclopedia of Medicine – Second Edition") inside the Data/ folder.

5. Create or Update Vector Store

This step processes your PDF documents, splits them into chunks, embeds them, and uploads them to your Pinecone index.
Bash

python src/create_vector_store.py

6. Start the Flask Web App

Bash

python app.py
