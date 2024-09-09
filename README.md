# Interactive Sentiment Analysis App

This Streamlit-based web application performs real-time sentiment analysis on user-provided text using OpenAI's language model and LangChain.

## Features

- **Real-time Analysis**: Instant sentiment evaluation of input text
- **User-friendly Interface**: Intuitive design with customizable options
- **Detailed Results**: Comprehensive explanations of sentiment analysis
- **Responsive Design**: Styled components for optimal viewing on various devices

## Technologies Used

- [Streamlit](https://streamlit.io/): For creating the interactive web application
- [LangChain](https://python.langchain.com/docs/get_started/introduction): For natural language processing tasks
- [OpenAI](https://platform.openai.com/docs/introduction): Powering the sentiment analysis model

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/interactive-sentiment-analysis.git
   cd interactive-sentiment-analysis
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## Usage

1. Launch the application:
   ```
   streamlit run app.py
   ```

2. Open your web browser and navigate to the provided local URL (usually `http://localhost:8501`)

3. Enter your text in the input area and click "Analyze Sentiment"

4. Adjust model parameters in the sidebar for customized analysis:
   - Temperature: Controls randomness (0.0 to 1.0)
   - Max Tokens: Sets the maximum length of the generated response

## Code Overview

The main application logic is contained in `app.py`. Key components include:

- **Page Configuration**: Sets up the Streamlit interface
- **LangChain Integration**: Configures the prompt template and OpenAI model
- **User Interaction**: Handles input and triggers sentiment analysis
- **UI Enhancement**: Implements styled components for an improved user experience

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
