import streamlit as st
from llama_index.llms.mistralai import MistralAI
from llama_index.core.llms import ChatMessage

# Function to summarize text using Mistral LLM
def summarize_case(text):
    try:
        # Initialize Mistral client with API key
        llm = MistralAI(api_key=st.secrets["MISTRAL_API_KEY"])
        
        # Create chat messages
        messages = [
            ChatMessage(role="system", content="You are a legal expert. Summarize the following legal case concisely and professionally."),
            ChatMessage(role="user", content=text)
        ]
        
        # Get response from Mistral
        response = llm.chat(messages)
        
        # Extract and return the summary
        return str(response)

    except Exception as e:
        return f"Error: {e}"

# Streamlit app UI
st.title("CaseSummarizer: Legal Case Summarization")
st.write("Upload a legal case text file, and we'll provide a concise summary.")

# File uploader
uploaded_file = st.file_uploader("Upload a .txt file", type="txt")

if uploaded_file is not None:
    try:
        # Read the uploaded file
        case_text = uploaded_file.read().decode("utf-8")
        st.subheader("Uploaded Case Text:")
        st.text_area("Case Content", case_text, height=300)

        # Generate summary
        if st.button("Summarize"):
            st.info("Generating summary, please wait...")
            with st.spinner("Processing..."):
                summary = summarize_case(case_text)
            st.subheader("Case Summary:")
            st.text_area("Summary", summary, height=200)

            # Download summary as a .txt file
            st.download_button(
                label="Download Summary as .txt",
                data=summary,
                file_name="case_summary.txt",
                mime="text/plain"
            )
    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")
