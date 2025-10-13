import streamlit as st
import preprocessor, helper

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

    # Fetch unique users
    user_list = df['user'].unique().tolist()

    # Replace 'whatsapp_notification' with 'Overall'
    user_list.remove('whatsapp_notification') 
    user_list.sort() # Sort the user list alphabetically
    user_list.insert(0, "Overall")

    # User selection menu
    selected_user = st.sidebar.selectbox("Show analysis wrt", user_list)

    # When the button is clicked, perform analysis
    if st.sidebar.button("Show Analysis"):

        # Fetch stats using helper module
        num_messages, num_words = helper.fetch_stats(selected_user, df)
        
        # Create 4 columns to display stats
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)

        with col2:
            st.header("Total Words")
            st.title(num_words)