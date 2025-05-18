## 🎬 Text2Manim - Ai-Powered 2D-Anim Video Generator System

A FastAPI-powered service that generates **Python scripts for Manim** and renders them into **2D educational animations** using natural language prompts and LLMs (Groq-hosted models).

---

## 🚀 Features

- 🎨 Accepts natural language input and converts it to Manim animations.
- 🧠 Uses LLMs (like `deepseek-r1-distill-llama-70b`) for script generation.
- 📼 Automatically renders animations to `.mp4` using Manim.
- 🔒 Clean error handling and output sanitization.
- 📁 Stores generated `.py` files and videos in a structured directory.

---

## 🛠 Tech Stack

- **FastAPI** – for building the API.
- **Manim** – for 2D animation rendering.
- **LangChain + Groq** – for connecting to large language models.
- **Python 3.10+**
- **Dotenv** – for environment management.

---

## 📦 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/Brigu09/Text2Manim-Ai.git
cd 2d-animation-api


.
├── backend/
│   ├── llm/
│   │   └── engine.py           # LLM prompt + generation logic
│   ├── manim_engine/
│   │   ├── runner.py           # Saves and renders scripts
│   │   └── utils.py            # Scene name extraction
│   └── schemas/
│       └── prompt.py           # Request model
├── outputs/                    # Stores generated scripts and videos
├── .env
├── main.py                     # FastAPI app
└── README.md
