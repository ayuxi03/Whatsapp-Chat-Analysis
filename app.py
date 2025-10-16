import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

st.sidebar.title("WhatsApp Chat Analyzer")
st.set_page_config(layout="wide")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    # Converting bytes to string
    data = bytes_data.decode("utf-8")

    # Preprocess data using preprocessor module
    df = preprocessor.preprocess(data)

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

        # Stats Area
        st.title("Top Statistics")

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
        

        # Montly activity timeline
        st.title('Monthly Activity Timeline')
        timeline = helper.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots(figsize=(15,5))
        ax.plot(timeline['time'], timeline['message_count'])
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # Finding the most active user in the group (only for Overall)
        if selected_user == 'Overall':
            st.title("Most Active Users")
            x, new_df = helper.fetch_most_active_users(df)

            fig, ax = plt.subplots() # Create a figure and axis
            
            # Create 2 columns to display bar chart and pie chart side by side
            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values, color=(0.5,0.3,0.5)) # Bar chart using the axis
                plt.xticks(rotation='vertical') # Rotate x-axis labels vertically
                st.pyplot(fig)
            
            with col2:
                st.dataframe(new_df) # Display dataframe of most active users

            
        # WordCloud
        st.title("Wordcloud")
        df_wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc) # Display the word cloud image
        st.pyplot(fig)


        # Displaying dataframe of most common words
        st.title("Most Common Words")
        most_common_df = helper.most_common_words(selected_user, df)
        fig, ax = plt.subplots(figsize=(10,5))
        ax.barh(most_common_df[0], most_common_df[1], color=(0.5,0.8,0.5)) # Bar chart of most common words
        st.pyplot(fig)


        # emoji analysis
        st.title("Emoji Analysis")
        emoji_df = helper.emoji_helper(selected_user, df)

        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(emoji_df) # Display dataframe of emojis and their counts

        with col2:
            fig, ax = plt.subplots()
            plt.rcParams['font.family'] = 'Segoe UI Emoji'
            ax.pie(
                emoji_df['count'].head(),
                labels=emoji_df['emoji'].head(),
                autopct="%0.2f",
                textprops={'fontsize': 15},
                colors=["#ab2a2a", "#fb9145", "#defb6b", "#66c29a", '#5e4fa2']) # Pie chart of top emojis
            st.pyplot(fig)

