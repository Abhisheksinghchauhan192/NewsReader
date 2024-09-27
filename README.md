# Newsreader

 
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Terminal](https://img.shields.io/badge/Terminal-App-green.svg)
![API](https://img.shields.io/badge/NewsAPI-Enabled-orange.svg)

**Newsreader** is a simple, terminal-based Python application that fetches the latest news headlines from various categories—**technical**, **general**, **health**, and **science**—using the powerful [NewsAPI](https://newsapi.org/). This tool brings the news directly to your command line, offering quick, convenient access to important news updates.

## 🎯 Key Features

- Fetch **real-time news** headlines from trusted sources.
- **Terminal-based interface**: Lightweight and efficient.
- Search by **category**: Choose from technical, general, health, and science.
- **Fast** and **reliable** with minimal setup.
- Cross-platform: Works on Linux, macOS, and Windows.

## 🛠️ Project Structure

```
newsreader/
│
├── src/                  # Application source code
│   ├── main.py           # Main entry point for the terminal application

│
├── README.md             # Project documentation (this file)

```

## ⚙️ Installation Guide

1. **Clone this repository**:

   ```bash
   git clone https://github.com/Abhisheksinghchauhan192/newsreader.git
   ```

2. **Navigate to the project folder**:

   ```bash
   cd newsreader
   ```




3. **Configure the API Key**:

   Sign up at [NewsAPI](https://newsapi.org/) to obtain your API key. Then, create a `.env` file in the project root directory with the following content:

   ```bash
   API_KEY=your_api_key_here
   ```

   This file ensures that your API key remains secure and private.

## 🚀 How to Use

Run the application directly from your terminal 

### Steps:

1. **Run the application**:

   ```bash
   python src/main.py
   ```

2. **Select a news category** when prompted:
   - `technical`
   - `general`
   - `health`
   - `science`


The latest news articles will be displayed directly in your terminal!

## 🛠 Technologies Used

- **Python**: For building the core functionality.
- **NewsAPI**: To fetch the latest news.
- **Terminal/CLI**: Lightweight and fast execution in terminal environments.

## 📦 Dependencies

- `requests`: To handle HTTP requests to the NewsAPI.


## 🙌 Contributions

Contributions are welcome! Feel free to fork the project, create an issue, or submit a pull request.

## 📧 Contact

If you have any questions or feedback, feel free to reach out to me via GitHub at [Abhisheksinghchauhan192](https://github.com/Abhisheksinghchauhan192).

---

**Happy coding!** ✨
