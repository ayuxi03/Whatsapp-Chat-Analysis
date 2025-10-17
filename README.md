# WhatsApp Chat Analyzer 🟢

[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30-orange)](https://streamlit.io/)
[![MIT License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Click%20Here-brightgreen)](https://whatsapp-chat-analyzer-hgat.onrender.com/)

A **web application** that allows users to analyze their WhatsApp chat history. Upload your exported `.txt` chats to gain insights, visualize activity patterns, and track messaging trends over time. Built with **Python** and **Streamlit** for simplicity and interactivity.

---

## 🚀 Features

- **Chat Analysis:** Analyze exported WhatsApp `.txt` chat files.  
- **Message Insights:** Count total messages, words, and emojis.  
- **User Activity:** Identify the most active users.  
- **Word & Emoji Frequency:** Discover most common words and emojis.  
- **Visual Analytics:** Interactive plots and charts to visualize trends over time.  
- **User-Friendly Interface:** Simple drag-and-drop upload and instant results.  

---

## 🛠 Tech Stack

- **Frontend / App Interface:** Streamlit  
- **Data Analysis & Visualization:** Python, Pandas, Matplotlib, Seaborn  
- **Development Environment:** Jupyter Notebook, VS Code  
- **Deployment:** Render  

---

## ⚡ Installation

1. **Clone the repository:**  
   ```bash
   git clone <your-repo-link>
   cd whatsapp-chat-analyzer

2. **Create and activate a virtual environment**
    ```bash
    python -m venv venv
    # Linux/Mac
    source venv/bin/activate
    # Windows
    venv\Scripts\activate

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt

4. **Run the application**
    ```bash
    streamlit run app.py

5. **Open your browser:**  
    Visit: [http://localhost:8501](http://localhost:8501)

---

## 📝 Usage

1. Export your WhatsApp chat as a `.txt` file.
2. Upload the file in the app interface.
3. Explore analytics such as:
    - Most active users
    - Most common words and emojis
    - Chat activity trends over time
4. Visualizations update interactively based on the uploaded chat.

---

## 💡 Contributing

Contributions to the project are welcome! If you have suggestions or find any issues, please open an issue or submit a pull request.