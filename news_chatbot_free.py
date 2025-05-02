import requests
import nltk
import tkinter as tk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

NEWS_API_KEY = "218020ae6d2449188d06695408cc1e5c"

valid_topics = ["technology", "sports", "business", "health", "entertainment", "science"]

def fetch_news(topic="technology"):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": topic,
        "sortBy": "publishedAt",
        "language": "en",
        "apiKey": NEWS_API_KEY,
        "pageSize": 10
    }
    response = requests.get(url, params=params)
    return response.json().get("articles", [])

def summarize(text, max_sentences=2):
    if not text:
        return "No content to summarize."
    sentences = sent_tokenize(text)
    return " ".join(sentences[:max_sentences])

def extract_topic(user_input):
    user_input = user_input.lower()
   
    keyword_map = {
        "technology": ["technology", "tech", "technologies"],
        "sports": ["sports", "sport"],
        "business": ["business", "biz", "finance"],
        "health": ["health", "wellness", "fitness"],
        "entertainment": ["entertainment", "movies", "tv", "music", "celebs"],
        "science": ["science", "sci", "research"]
    }

    for topic, variations in keyword_map.items():
        for word in variations:
            if word in user_input:
                return topic
    return None


def handle_user_input(event=None):  # Add event parameter to allow for key binding
    user_message = user_entry.get().strip()
    if user_message == "":
        return

    # Add space after "You"
    chat_box.insert(tk.END, f"\n👤 You: {user_message}\n", "you")

    topic = extract_topic(user_message)
    if topic:
        # Add space after "Bot"
        chat_box.insert(tk.END, f"🤖 Bot: Let me find some news on '{topic}'...\n\n", "bot")
        articles = fetch_news(topic)
        if not articles:
            chat_box.insert(tk.END, "🤖 Bot: Sorry, I couldn't find any news for that topic.\n\n", "bot")
        else:
            for i, article in enumerate(articles, 1):
                title = article.get("title", "No title")
                content = article.get("description") or article.get("content") or ""
                summary = summarize(content)

                chat_box.insert(tk.END, f"📰 {i}. {title}\n", "title")
                chat_box.insert(tk.END, f"📝 Summary: {summary}\n\n", "summary")
    else:
        # Add space after "Bot"
        chat_box.insert(
            tk.END,
            "🤖 Bot: Please ask about one of these topics: technology, sports, business, health, entertainment, science.\n\n",
            "bot"
        )

    user_entry.delete(0, tk.END)


# Setup dynamic window
root = tk.Tk()
root.title("AI News Chatbot")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = int(screen_width * 0.8)
window_height = int(screen_height * 0.8)
root.geometry(f"{window_width}x{window_height}")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Chat display
chat_box = tk.Text(root, font=("Helvetica", 12), wrap="word")
chat_box.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
chat_box.insert(tk.END, "🤖 Bot: Hi! Ask me about news on topics like technology, sports, business, etc.\n\n", "bot")

# Define tag styles
chat_box.tag_config("title", background="#DCEEFF", font=("Helvetica", 13, "bold"))
chat_box.tag_config("summary", background="#E8F5E9", font=("Helvetica", 12))
chat_box.tag_config("bot", foreground="blue", font=("Helvetica", 12, "italic"))
chat_box.tag_config("you", foreground="green", font=("Helvetica", 12, "bold"))

# Entry box
user_entry = tk.Entry(root, font=("Helvetica", 16), bd=2, relief="groove")
user_entry.grid(row=1, column=0, sticky="ew", padx=10, pady=10, ipady=10)
root.columnconfigure(0, weight=3)

# Send button
send_button = tk.Button(
    root,
    text="Send",
    font=("Helvetica", 14, "bold"),
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    padx=20, pady=10,
    relief="raised", bd=3,
    command=handle_user_input
)
send_button.grid(row=1, column=1, sticky="ew", padx=10, pady=10)
root.columnconfigure(1, weight=1)

# Bind the Enter key to trigger the send button action
root.bind('<Return>', handle_user_input)

root.mainloop()
