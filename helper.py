from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji
import re
from matplotlib import cm

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

    # 6. Creating a word cloud of the most commonly used words

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    
    # removing group notifications and media omitted messages
    temp = df[df['user'] != 'whatsapp_notification']
    temp = temp[~temp['message'].isin(['<Media omitted>\n', 'You deleted this message\n', 'This message was deleted\n'])]

    # using custom stop words list from banglish_hinglish_stopwords.txt
    with open('banglish_hinglish_stopwords.txt', 'r') as f:
        stop_words = f.read().splitlines()

    # Combine all messages from temp['message'] into a string separated by " "
    text = temp['message'].str.cat(sep=" ") # same as " ".join(temp['message'])

    # Keep only alphabetic words (removes emojis, numbers, punctuation)
    text = " ".join(re.findall(r'\b[a-zA-Z]+\b', text))


    # Generate the word cloud
    wc = WordCloud(
        width=900,
        height=450,
        min_font_size=10,
        background_color='white',
        max_words=100,
        colormap=cm.inferno,
        stopwords=set(stop_words),
        font_path='C:\\Windows\\Fonts\\seguiemj.ttf')
    
    df_wc = wc.generate(text)

    return df_wc


def most_common_words(selected_user, df):

    # 7. Finding the top 20 most common words

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    
    # removing group notifications and media omitted messages
    temp = df[df['user'] != 'whatsapp_notification']
    temp = temp[~temp['message'].isin(['<Media omitted>\n', 'You deleted this message\n', 'This message was deleted\n'])]

    # using custom stop words list from banglish_hinglish_stopwords.txt
    f = open('banglish_hinglish_stopwords.txt', 'r')
    stop_words = f.read()

    # Collecting all words in a list after removing stop words
    words = []

    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words and not emoji.is_emoji(word):
                words.append(word)

    # Using Counter to get the most common words
    most_common_df = pd.DataFrame(Counter(words).most_common(20))

    return most_common_df


def emoji_helper(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    
    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if emoji.is_emoji(c)])

    # Count each emoji occurrences
    emoji_df = pd.DataFrame(Counter(emojis).most_common(20)).rename(columns={0: 'emoji', 1: 'count'})

    return emoji_df


def monthly_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # Add message count column by month
    monthly_timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()
    monthly_timeline.rename(columns = {'message': 'message_count'}, inplace=True)

    # create month-year column
    time=[]
    for i in range(monthly_timeline.shape[0]):
        time.append(monthly_timeline['month'][i] + "-" + str(monthly_timeline['year'][i]))

    monthly_timeline['time'] = time

    return monthly_timeline


def daily_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # Add message count column by date
    daily_timeline = df.groupby('only_date').count()['message'].reset_index()
    daily_timeline.rename(columns = {'message': 'message_count'}, inplace=True)

    return daily_timeline


def week_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    
    return df['day_name'].value_counts()


def month_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    
    return df['month'].value_counts()


def generate_activity_heatmap(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    
    activity_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)

    return activity_heatmap