def fetch_stats(selected_user, df):

    if selected_user == 'Overall':
        # 1. Fetching number of messages
        num_messages = df.shape[0]

        # 2. number of words
        words = []
        for message in df['message']:
            # Splitting each message into words and adding to the list
            words.extend(message.split())
        
        return num_messages, len(words)
    
    else:
        # Fetching number of messages for the selected user
        new_df = df[df['user'] == selected_user]
        num_messages = new_df.shape[0]

        # number of words for the selected user
        words = []
        for message in new_df['message']:
            words.extend(message.split())
            
        return num_messages, len(words)