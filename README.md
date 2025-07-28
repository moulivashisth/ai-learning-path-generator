# 🧠 AI-Powered Learning Path Generator

This is a Flask web app that uses **Google Gemini (Generative AI)** to generate a personalized 8-week learning path based on a user’s goal (e.g., "I want to learn Python"). It saves the learning path in **MongoDB Atlas** and provides features like:

- ✅ AI-based curriculum planning
- ✅ Progress tracking with checkboxes
- ✅ Real-time progress bar
- ✅ Goal search/filter
- ✅ Expand/Collapse learning path
- ✅ Delete goal feature

## 🗂 Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── db.py
│   └── templates/
│       ├── index.html
│       ├── result.html
│       └── history.html
├── requirements.txt
├── run.py
└── README.md
```

## 🚀 How to Run Locally

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/moulivashisth/ai-learning-path-generator.git
cd ai-learning-path-generator
```

### 🧪 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔑 3. Set Environment Variables

Create a `.env` file or set environment variables manually:

```bash
export GEMINI_API_KEY=your_google_gemini_api_key
export MONGO_URI=your_mongodb_connection_uri
```

On Windows (CMD):

```cmd
set GEMINI_API_KEY=your_google_gemini_api_key
set MONGO_URI=your_mongodb_connection_uri
```

## 🏃 4. Run the App

```bash
python run.py
```

Then visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 🤖 How to Get a Gemini API Key

1. Visit: https://aistudio.google.com/app/apikey
2. Click **Create API Key**
3. Copy the key and use it as `GEMINI_API_KEY`

> This project uses `gemini-2.0-flash` with the REST API:
> `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent`

## 🍃 How to Setup MongoDB Atlas

1. Go to https://www.mongodb.com/cloud/atlas
2. Sign up and **create a free Shared Cluster**
3. Under **Database Access**, create a user & password
4. Under **Network Access**, allow access from your IP or `0.0.0.0/0`
5. Get the **connection URI** from **Connect → Drivers → Python**
   Example URI:
   ```
   mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority
   ```
6. Use this URI as the value of `MONGO_URI`

## ✨ Features

- 🔮 Gemini-powered 8-week plan
- 💾 MongoDB-based storage
- ✅ Mark steps as completed
- 📊 Dynamic progress bar
- 🔍 Search/filter your goal
- 🔽 Expand/collapse learning paths
- 🗑️ Delete a goal



## 📃 License

MIT License. Free to use and modify.