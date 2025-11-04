# PrivacyLeak Hunter 🔒

PrivacyLeak Hunter is a full-stack application that analyzes uploaded text or files to detect potential privacy leaks such as **emails, passwords, tokens, and API keys**.  
Built with **Flask (Python)** for the backend and **React + Tailwind + Vite** for the frontend.

---

## 🚀 Features

- 🔍 Detects sensitive information patterns (emails, passwords, tokens, etc.)
- 📁 File upload support
- 📊 Displays analysis results in a clean, visual dashboard
- 🌐 CORS-enabled backend for easy frontend integration
- 💡 Modular structure for extending detection algorithms

---

## 🏗️ Project Structure

```
privacyleak-hunter/
├── backend/
│   ├── app.py
│   ├── algorithms/
│   │   ├── __init__.py
│   │   └── pattern_search.py
│   ├── uploads/
│   └── results/
│
├── frontend/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── src/
│       ├── main.jsx
│       ├── App.jsx
│       ├── pages/
│       │   ├── UploadPage.jsx
│       │   ├── AnalyzePage.jsx
│       │   └── ResultsPage.jsx
│       └── components/
│           └── Navbar.jsx
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Backend Setup (Flask)
```bash
cd backend
pip install flask flask-cors
python app.py
```

### 2️⃣ Frontend Setup (React + Vite)
```bash
cd frontend
npm install
npm run dev
```

By default:
- Frontend runs on **http://localhost:5173**
- Backend runs on **http://127.0.0.1:5000**

---

## 🧠 How It Works

1. Upload a text file or enter raw content.
2. Backend processes the data using regex-based pattern matching.
3. Detected leaks are returned to the frontend for visualization.
4. Results are stored in `/results` for later use.

---

## 🧩 Example API Routes

| Route | Method | Description |
|--------|---------|-------------|
| `/upload` | POST | Uploads a file to the backend |
| `/analyze` | POST | Analyzes text for sensitive info |
| `/results` | GET | Returns stored analysis results |

---

## 🛡️ Future Improvements

- AI-based leak detection using NLP
- Multi-file batch scanning
- Exportable reports (PDF/CSV)
- User authentication

---

## 🧑‍💻 Contributors
- **Kunal Badhan** — Developer & Project Creator

---

## 🪪 License
This project is licensed under the MIT License.
