# 🚀 AI Harness — Setup & Run

Follow the steps below to get the **AI Harness** running locally.

---

## ⚡ Quick Start

### 📁 Step 1 — Enter the Project

Open your terminal and navigate to the project:

```bash
cd aiharness
```

---

### 🧹 Step 2 — Reset the Virtual Environment

Remove the existing virtual environment to ensure a clean setup:

```bash
rm -rf .venv
```

---

### ⚙️ Step 3 — Set Up the Project

Run the setup command:

```bash
make setup
```

This will create and configure the required Python environment and dependencies.

---

### 🧪 Step 4 — Run Tests

Verify that everything is working correctly:

```bash
make test
```

If the tests pass, you're ready to run the harness. ✅

---

### 🔑 Step 5 — Add Your API Key

Set your AI API key as an environment variable.

Replace `YOUR_REAL_API_KEY` with your actual key:

```bash
export AI_API_KEY="YOUR_REAL_API_KEY"
```

> ⚠️ **Security:** Never commit your API key to GitHub or include it directly in your source code.

---

### ▶️ Step 6 — Run the AI Harness

Start the application:

```bash
make run
```

🎉 **That's it! Your AI Harness is now running.**

---

## 🛠️ Complete Setup

If you want to run everything from scratch, execute:

```bash
cd aiharness
rm -rf .venv
make setup
make test
export AI_API_KEY="YOUR_REAL_API_KEY"
make run
```

---

## 💡 Troubleshooting

If you encounter issues:

1. Make sure Python is installed.
2. Make sure your API key is valid.
3. Run `make setup` again after removing `.venv`.
4. Run `make test` to identify setup problems.

---

### ⭐ Ready to Build?

**Set your API key → Run the tests → Launch the harness → Start building!**
