import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt

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
        num_messages, num_words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)
        
        # Create 4 columns to display stats
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)

        with col2:
            st.header("Total Words")
            st.title(num_words)

        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)
        
        with col4:
            st.header("Links Shared")
            st.title(num_links)

        # Finding the most active user in the group (only for Overall)
        if selected_user == 'Overall':
            st.title("Most Active Users")
            x, new_df = helper.fetch_most_active_users(df)

            fig, ax = plt.subplots() # Create a figure and axis
            
            # Create 2 columns to display bar chart and pie chart side by side
            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values) # Bar chart using the axis
                plt.xticks(rotation='vertical') # Rotate x-axis labels vertically
                st.pyplot(fig)
            
            with col2:
                st.dataframe(new_df) # Display dataframe of most active users

            
        # WordCloud
        st.title("Wordcloud")
        df_wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)


        # most common words
        st.title("Most Common Words")
        most_common_df = helper.most_common_words(selected_user, df)

        st.dataframe(most_common_df)
