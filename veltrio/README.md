# 🌍 VELTRIO – Real-Time Language Translation & Sentiment Analysis

A web-based AI system that performs real-time language translation and sentiment analysis using only free and open-source tools. Users can enter text, receive an English translation, and detect sentiment (positive, negative, neutral) — all in real time.

---

## 🚀 Features

- 🔤 Translate multilingual text to English (MarianMT)
- 😊 Detect emotional tone using BERT
- ⚡ FastAPI backend + HuggingFace NLP models
- 🌐 Simple frontend with HTML, CSS, JavaScript
- ☁️ Free deployment using GitHub Pages & Render

---

## 🛠 Tech Stack

| Layer       | Technology                |
|-------------|---------------------------|
| Frontend    | HTML, CSS, JavaScript     |
| Backend     | Python, FastAPI           |
| Translation | MarianMT (HuggingFace)    |
| Sentiment   | DistilBERT / BERT         |
| Deployment  | GitHub Pages, Render.com  |

---

## 📁 Folder Structure

veltrio-ai-web/
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── backend/
│   ├── app.py
│   ├── translation.py
│   └── sentiment.py
├── requirements.txt
├── README.md
├── .gitignore

---

## 🖥️ How to Run Locally

1. Install requirements:
   pip install -r requirements.txt

2. Run FastAPI backend:
   cd backend
   uvicorn app:app --reload

3. Open frontend:
   Open frontend/index.html in your browser.

---

## 🌐 Deployment

- Frontend: GitHub Pages
- Backend: Render (Free tier)

---

## 👨‍💻 Team VELTRIO

- Arjun S N – Frontend (HTML, JS, GitHub Pages)
- Aravindan K – Backend (FastAPI, Render Deployment)
- Godfrey T R – Model Integration (MarianMT, BERT via HuggingFace)

---

## 📄 License

This project is free to use for academic and educational purposes.

---

## 📬 Contact

For questions or collaboration:
Email: godfrey.prof@gmail.com
