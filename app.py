import streamlit as st
import preprocessor

st.sidebar.title("WhatsApp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    # Converting bytes to string
    data = bytes_data.decode("utf-8")

    # Preprocess data using preprocessor module
    df = preprocessor.preprocess(data)
    
    # Display the dataframe on the app
    st.dataframe(df)