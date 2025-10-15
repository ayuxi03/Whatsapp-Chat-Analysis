from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter

extractor = URLExtract()

def fetch_stats(selected_user, df):

    # if specific user is selected, dataframe is filtered for that user
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    
    # 1. Fetching number of messages
    num_messages = df.shape[0]

    # 2. Fetching number of words
    words = []
    for message in df['message']:
        # Splitting each message into words and adding to the list
        words.extend(message.split())

    # 3. Fetching number of media messages
    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    # 4. Fetching number of links shared
    links = []
    for message in df['message']:
        links.extend(extractor.find_urls(message))

    return num_messages, len(words), num_media_messages, len(links)


def fetch_most_active_users(df):
    
    # 5. Fetching the most active users in the group (top 5)
    # value_counts() : counts number of times each user occurs (desc order)
    x = df['user'].value_counts().head()

    df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(columns={'count': 'percent'})
    return x, df


def create_wordcloud(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    
    temp = df[df['user'] != 'whatsapp_notification']
    temp = temp[~temp['message'].isin(['<Media omitted>\n', 'You deleted this message\n', 'This message was deleted\n'])]

    f = open('banglish_hinglish_stopwords.txt', 'r')
    stop_words = f.read().splitlines()

    wc = WordCloud(
        width=400,
        height=200,
        min_font_size=10,
        background_color='white',
        max_words=100,
        colormap='Spectral_r',
        stopwords=set(stop_words))
    
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))

    return df_wc

def most_common_words(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    
    temp = df[df['user'] != 'whatsapp_notification']
    temp = temp[~temp['message'].isin(['<Media omitted>\n', 'You deleted this message\n', 'This message was deleted\n'])]

    # remove stop words
    # stopwords filter
    
    f = open('banglish_hinglish_stopwords.txt', 'r')
    stop_words = f.read()

    words = []

    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(20))

    return most_common_df