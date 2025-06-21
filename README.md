# <p align="center">🤖 AI Chatbot with Azure OpenAI & MongoDB</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python 3.x">
  <img src="https://img.shields.io/badge/Flask-2.3.2-black.svg" alt="Flask">
  <img src="https://img.shields.io/badge/Azure_OpenAI-GPT--3.5-0078D4.svg" alt="Azure OpenAI">
  <img src="https://img.shields.io/badge/Database-MongoDB-47A248.svg" alt="MongoDB">
  <img src="https://img.shields.io/badge/Styling-TailwindCSS-38B2AC.svg" alt="Tailwind CSS">
</p>

<p align="center">
  A modern, conversational AI chatbot powered by Python, Flask, and the Azure OpenAI Service. This project provides a sleek web interface for interacting with an intelligent assistant, complete with chat history stored in a MongoDB database.
</p>

<p align="center">
  <img src="./static/images/snapshot.gif" alt="Chatbot Snapshot" width="80%">
</p>

## ✨ Core Features

-   **🧠 Intelligent Conversations:** Leverages Azure's powerful `gpt-35-turbo` model to provide smart, context-aware responses.
-   **💾 Persistent Chat History:** Securely stores and retrieves conversation logs from a MongoDB database, allowing users to pick up where they left off.
-   **🌐 Clean Web Interface:** A beautifully simple UI built with Flask and styled with Tailwind CSS for a modern user experience.
-   **🔑 Secure Configuration:** Manages all API keys and sensitive credentials safely using a `.env` file.
-   **🔧 Extensible Foundation:** Designed to be a flexible and powerful starting point for building your own custom chatbot applications.

## 🛠️ Tech Stack

| Category      | Technology                                                                                                  |
| ------------- | ----------------------------------------------------------------------------------------------------------- |
| **Backend**   | <img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python 3.x"> <img src="https://img.shields.io/badge/Flask-2.3.2-black.svg" alt="Flask">                               |
| **AI Service**| <img src="https://img.shields.io/badge/Azure_OpenAI-GPT--3.5-0078D4.svg" alt="Azure OpenAI">                  |
| **Database**  | <img src="https://img.shields.io/badge/Database-MongoDB-47A248.svg" alt="MongoDB">                              |
| **Frontend**  | <img src="https://img.shields.io/badge/HTML5-E34F26.svg" alt="HTML5"> <img src="https://img.shields.io/badge/CSS3-1572B6.svg" alt="CSS3"> <img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg" alt="JavaScript"> |
| **Styling**   | <img src="https://img.shields.io/badge/Styling-TailwindCSS-38B2AC.svg" alt="Tailwind CSS">                    |


## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### ✅ Prerequisites

-   Python 3.x installed on your system.
-   An active Microsoft Azure account with access to the OpenAI service.
-   A MongoDB database and its connection string.

### ⚙️ Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/pavansaicharan/chatbot.git
    cd chatbot/ChatGPT
    ```

2.  **Set Up a Virtual Environment** (Recommended)
    ```bash
    # Create the virtual environment
    python -m venv venv
    
    # Activate it
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables**
    Create a file named `.env` in the `ChatGPT` directory and add your Azure credentials:
    ```dotenv
    AZURE_OPENAI_ENDPOINT="<your-azure-openai-endpoint>"
    AZURE_OPENAI_API_KEY="<your-azure-openai-api-key>"
    ```

5.  **Run the Tailwind CSS Build Process**
    Open a terminal and run this command to compile the CSS in watch mode:
    ```bash
    npx tailwindcss -i ./static/input.css -o ./static/css/main.css --watch
    ```

6.  **Launch the Application**
    Open a second terminal and run the Flask app:
    ```bash
    python main.py
    ```

Your chatbot is now live and ready to use in your web browser!

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/pavansaicharan/chatbot/issues).

---

<p align="center">
  This project builds upon an initial version by jaypokharna and has been enhanced to integrate with Azure OpenAI.
</p>
