# Student-GPT

A Python-based AI assistant project aimed at helping students interact with GPT models for academic tasks.

## 🚀 Overview

**Student-GPT** is an AI-powered tool designed to assist students with learning and productivity. It leverages language models to deliver answers, explanations, and supportive features for educational use. The project includes a backend Python script, web templates, and basic test scripts - providing a foundation for building a student-focused chatbot or assistant.

> ℹ️ *There is currently no description provided in the repository itself - you can customize this overview with a live demo link, screenshots, or specific use cases.*

## 🧠 Features

✔️ AI assistant powered by GPT-style models
✔️ Simple web interface using streamlit
✔️ Python backend
✔️ Easily extendable for additional tools (note-taking, reminders, quizzes, summaries, etc.)

## 📁 Project Structure

```
Student-GPT/
├── app.py                  # Main application server
├── htmlTemplates.py        # HTML template routes / render logic
├── requirements.txt        # Python dependencies
├── test.py                 # Test script
├── try.py                  # Additional trial scripts / experiments
└── LICENSE                # MIT License
```

## 🛠️ Tech Stack

* **Python** - Backend logic
* **Langchain GPT Models** - AI response generation
* HTML templates for UI

## 📦 Installation

To install and run the project locally:

1. **Clone the repository**

   ```bash
   git clone https://github.com/Shamanth-V/Student-GPT.git
   cd Student-GPT
   ```

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS / Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment variables**
   Add any required API keys (e.g., OpenAI key) to your environment:

   ```bash
   export OPENAI_API_KEY="your_api_key"
   ```

5. **Run the application**

   ```bash
   python app.py
   ```

   Visit `http://localhost:5000` in your browser (or as configured).

## 📈 Usage

Once running:

* Interact with the AI assistant through the UI
* Send prompts, questions, or study-related queries
* Extend the backend logic to add new endpoints or features

## 🧪 Testing

To run tests:

```bash
python test.py
```

*(Update test file invocation according to actual test framework used.)*

## 📝 Contributing

Contributions are welcome!
Please feel free to submit issues, feature requests, or pull requests.

1. Fork the repo
2. Create a branch (`git checkout -b feature/XYZ`)
3. Commit your changes
4. Push and open a PR

## 📄 License

This project is licensed under the **MIT License** - see the `LICENSE` file for details.
