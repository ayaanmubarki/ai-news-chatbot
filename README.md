# ai-news-chatbot
An AI-powered News Chatbot built with Python, Tkinter, and NewsAPI. It fetches the latest news on user-specified topics like technology, sports, health, and more, and summarizes articles using NLTK.
# 📰 AI News Chatbot 🤖

This is a Python-based AI News Chatbot that allows users to interact through a graphical interface to receive the latest news headlines and summaries on topics like technology, sports, business, entertainment, science, and health.

## 🔍 Features

- 🧠 Understands topic-based queries (e.g., "Tell me sports news")
- 🌐 Fetches real-time news using the [NewsAPI](https://newsapi.org/)
- ✂️ Summarizes news articles using NLTK's sentence tokenizer
- 🖥️ Easy-to-use GUI built with Python's Tkinter
- 📌 Customizable to include more topics or improve summarization

## 💡 How It Works

1. The user types a query related to a topic (e.g., "What's new in tech?")
2. The chatbot extracts the topic using keyword mapping
3. It fetches top news headlines using NewsAPI
4. Summarizes the content using NLTK
5. Displays the summary in the GUI

## 🛠️ Tech Stack

- **Python 3**
- **Tkinter** (for GUI)
- **NLTK** (for text summarization)
- **NewsAPI** (for real-time news data)
- **Requests** (for API communication)

## 🚀 Getting Started

### Prerequisites

Install Python dependencies:

```bash
pip install requests nltk
