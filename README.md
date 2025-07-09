# AI-Medical-Chatbot-Assistance

✨ Features
🔍 Contextual document retrieval using Pinecone
🧬 Semantic search via Hugging Face sentence transformers
🤖 Intelligent responses using OpenAI's GPT-4o-mini
📄 Medical knowledge ingestion from PDF documents
🌐 Web-based chat interface built with Flask
🔐 Secure API key handling with `.env`


📚 Data Source
The chatbot uses data extracted from the following resource:
📘 The Gale Encyclopedia of Medicine – Second Edition
Documents are processed, split into chunks, and embedded for efficient vector-based retrieval.


🛠️ Tech Stack
Python 3.x
Flask
LangChain
Hugging Face Transformers
Pinecone
OpenAI GPT (gpt-4o-mini)
dotenv


📁 Project Structure
.
├── app.py                     # Flask server and chatbot logic
├── src/
│   ├── helper.py              # PDF loader, text splitter, embedding setup
│   └── prompt.py              # System prompt for chatbot
├── Data/                      # Directory for medical PDFs
├── templates/
│   └── chat.html              # Web interface
├── .env                       # Environment file with API keys
└── README.md                  # Project documentation


⚙️ Setup Instructions
1. Clone the Repository
   git clone https://github.com/yourusername/ai-medical-chatbot.git
   cd ai-medical-chatbot

2. Install Dependencies
   pip install -r requirements.txt

3. Configure Environment Variables
   Create a .env file with your keys:
   OPENAI_API_KEY=your_openai_api_key
   PINECONE_API_KEY=your_pinecone_api_key

4. Add PDF Files
   Put your medical PDF files (like the Gale Encyclopedia) inside the Data/ folder.

5. Create or Update Vector Store
   python src/create_vector_store.py

6. Start the Flask Web App
   python app.py
   
