import streamlit as st
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
import os
from dotenv import load_dotenv

load_dotenv()

# Set up Streamlit page
st.set_page_config(page_title="Sentiment Analysis App",
                   page_icon="😊", layout="wide")
st.title("Interactive Sentiment Analysis")

# Create sidebar for additional options
st.sidebar.header("Options")
temperature = st.sidebar.slider("Model Temperature", 0.0, 1.0, 0.7, 0.1)
max_tokens = st.sidebar.number_input("Max Tokens", 50, 500, 200, 50)

# Create prompt template
prompt = PromptTemplate(
    input_variables=["text"],
    template="Analyze the sentiment of the following text: {text}. Provide a detailed explanation of the sentiment, including any key phrases or words that contribute to this sentiment."
)

# Create OpenAI model instance
llm = OpenAI(temperature=temperature, max_tokens=max_tokens)

# Create RunnableSequence
chain = RunnableSequence(prompt | llm)

# Create two columns for input and output
col1, col2 = st.columns(2)

with col1:
    st.subheader("Input")
    user_input = st.text_area(
        "Enter your text for sentiment analysis:", height=200)
    analyze_button = st.button("Analyze Sentiment", key="analyze")

with col2:
    st.subheader("Analysis Result")
    result_placeholder = st.empty()

if analyze_button:
    if user_input:
        with st.spinner("Analyzing sentiment..."):
            # Get sentiment analysis
            result = chain.invoke({"text": user_input})

            # Display result with formatting
            result_placeholder.markdown(f"**Sentiment Analysis:**\n\n{result}")
    else:
        result_placeholder.warning("Please enter some text to analyze.")

# Add an expander for more information
with st.expander("About Sentiment Analysis"):
    st.write("""
    Sentiment analysis is the process of determining the emotional tone behind a series of words. 
    This app uses advanced natural language processing to analyze the sentiment of your input text.
    The analysis considers various factors such as word choice, context, and language patterns to provide a detailed explanation of the detected sentiment.
    """)

# Styling
st.markdown("""
<style>
.stTextInput > div > div > input {
    background-color: #f0f2f6;
}
.stButton > button {
    background-color: #4CAF50;
    color: white;
    font-weight: bold;
    border-radius: 5px;
    padding: 0.5rem 1rem;
    transition: all 0.3s ease;
}
.stButton > button:hover {
    background-color: #45a049;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #f0f2f6;
    color: #333;
    text-align: center;
    padding: 15px 0;
    font-size: 16px;
    box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
}
.footer a {
    color: #4CAF50;
    text-decoration: none;
    font-weight: bold;
    transition: color 0.3s ease;
}
.footer a:hover {
    color: #45a049;
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <div class="footer">
        © 2024 Akilesh Jayakumar | Built with 
        <a href="https://streamlit.io/" target="_blank">Streamlit</a>, 
        <a href="https://python.langchain.com/docs/get_started/introduction" target="_blank">LangChain</a>, and 
        <a href="https://platform.openai.com/docs/introduction" target="_blank">OpenAI</a>
    </div>
    """,
    unsafe_allow_html=True
)
