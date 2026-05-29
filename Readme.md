# Streamlit LLM Chatbot

A simple Generative AI chatbot built using **Streamlit**, **LangChain**, and **Groq's Llama 3.1 models**. The application provides a clean chat interface with conversation memory using Streamlit Session State.

## Features

* Interactive chat interface using Streamlit
* Powered by Groq's Llama 3.1 models
* Conversation history persistence using Session State
* Fast response generation
* Simple and beginner-friendly codebase
* Environment variable management using `.env`

## Tech Stack

* Python
* Streamlit
* LangChain
* Groq API
* python-dotenv

## Project Structure

```text
.
├── chatbot.py
├── requirements.txt
├── .gitignore
├── env_template.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/aditya212005/Streamlit-LLM-Chatbot.git
cd Streamlit-LLM-Chatbot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key_here
```

## Running the Application

```bash
streamlit run chatbot.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## Example

User:

```text
What is Machine Learning?
```

Assistant:

```text
Machine Learning is a branch of Artificial Intelligence that enables systems to learn patterns from data and improve performance without being explicitly programmed.
```

## Learning Outcomes

This project helped me understand:

* Streamlit fundamentals
* Session State management
* Chat interfaces in Python
* LangChain integration
* Working with LLM APIs
* Environment variable handling
* Git and GitHub workflows

## Future Improvements

* Streaming responses
* Multiple model selection
* Conversation export
* Persistent chat storage
* Retrieval-Augmented Generation (RAG)
* Authentication and user management

## Author

Aditya Ramakrishna 