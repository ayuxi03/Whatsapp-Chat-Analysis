def fetch_stats(selected_user, df):

    # if specific user is selected, dataframe is filtered for that user
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    
    # 1. Fetching number of messages
    num_messages = df.shape[0]

    # 2. number of words
    words = []
    for message in df['message']:
        # Splitting each message into words and adding to the list
        words.extend(message.split())

    return num_messages, len(words)