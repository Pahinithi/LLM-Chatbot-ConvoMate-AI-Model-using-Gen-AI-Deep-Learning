# ConvoMate AI Model

ConvoMate is an AI-powered chatbot built using Google Gemini-Pro's generative model. It features a sleek and interactive UI, powered by Streamlit, to facilitate engaging conversations with the AI.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Demo](#demo)

## Introduction

ConvoMate is designed to provide an intuitive and responsive chat experience. By leveraging the Google Gemini-Pro AI model, the chatbot can engage in meaningful conversations and adapt to various user inputs.

## Features

- **AI-Powered Chatbot**: Utilizes Google Gemini-Pro's generative model for sophisticated responses.
- **Interactive UI**: Built with Streamlit, featuring custom CSS for a modern and appealing look.
- **Chat History**: Displays previous interactions in a user-friendly chat window.
- **User-Friendly Design**: Customizable chat bubbles and input fields for an enhanced experience.
- **Developer Credit**: Includes a footer crediting the developer.

## Project Structure

The project is organized as follows:

```
ConvoMate_Chatbot/
│
├── main.py                  # Main Streamlit application file
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (not included in version control)
├── streamlit/
│   ├── config.toml          # Streamlit configuration settings
│   ├── credentials.toml     # Streamlit credentials (if needed)
│
└── README.md                # Project documentation
```

## Installation

To set up ConvoMate locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Pahinithi/LLM-Chatbot-ConvoMate-AI-Model-using-Gen-AI-Deep-Learning.git
   cd LLM-Chatbot-ConvoMate-AI-Model-using-Gen-AI-Deep-Learning
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Obtain a Google API Key**:

   - Visit the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or select an existing one.
   - Enable the Google Gemini-Pro API for your project.
   - Navigate to the "Credentials" section and create an API key.
   - Copy the API key and store it in your `.env` file:

     ```plaintext
     GOOGLE_API_KEY=your_google_api_key_here
     ```

5. **Run the Streamlit app**:

   ```bash
   streamlit run main.py
   ```

## Configuration

- **`config.toml`** and **`credentials.toml`** files are located in the `streamlit` directory. Customize these files if necessary to adjust the Streamlit application settings.

## Usage

1. Open the Streamlit app in your browser (usually accessible at `http://localhost:8501`).
2. Start interacting with ConvoMate by entering your messages into the chat input field.
3. View responses from the AI and the chat history as the conversation progresses.

## Customization

- **UI Customization**: Modify the CSS styles in `main.py` to adjust the look and feel of the application.
- **API Integration**: Replace the placeholder Google API key in the `.env` file with your own key.

## Contributing

Contributions are welcome! Please open issues or submit pull requests to help improve the project. Make sure to follow coding standards and provide clear commit messages.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Google Gemini-Pro**: For providing the generative AI model.
- **Streamlit**: For the powerful and user-friendly framework.

## Demo
- Link :https://drive.google.com/file/d/1i16yTZy8ZSlhnMs-g2U03ss7WdHHQcNP/view?usp=sharing
<img width="1728" alt="DL09" src="https://github.com/user-attachments/assets/ebff73ab-ce55-4501-ae09-96335d281378">
