# AI-Medical-Chatbot-Assistance

This project is an AI-powered medical chatbot that provides accurate, context-aware answers to user questions using content from The Gale Encyclopedia of Medicine – Second Edition. It combines Flask for the web interface, LangChain for retrieval-augmented generation, Hugging Face sentence-transformer embeddings for semantic understanding, and Pinecone as the vector database for storing and retrieving document chunks. OpenAI's GPT-4o-mini model generates concise answers based on the retrieved context. The chatbot is ideal for learning, research, and exploring trusted medical information.

Features
•	Context-aware answers based on medical documents
•	Retrieval-augmented generation using LangChain
•	Semantic search powered by Hugging Face embeddings
•	Efficient vector storage and retrieval with Pinecone
•	Natural language responses via OpenAI GPT-4o-mini
•	Web-based chat interface using Flask

Tech Stack
•	Python 3.x
•	Flask
•	LangChain
•	Hugging Face Transformers
•	Pinecone
•	OpenAI GPT-4o-mini
•	dotenv (for managing API keys)

How to Run
•	1. Clone the repository:
•	   git clone https://github.com/yourusername/ai-medical-chatbot.git

•	2. Navigate into the project folder:
•	   cd ai-medical-chatbot

•	3. Install dependencies:
•	   pip install -r requirements.txt

•	4. Add your medical PDFs to the Data/ folder

•	5. Create a .env file with your API keys:
•	   OPENAI_API_KEY=your_openai_api_key
•	   PINECONE_API_KEY=your_pinecone_api_key

•	6. Generate the vector store:
•	   python src/create_vector_store.py

•	7. Start the Flask app:
•	   python app.py



