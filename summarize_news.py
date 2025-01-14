import pandas as pd
from openai_chatgpt import complete_chat
# sol 1. 依照每一行去做處理
# news = pd.read_csv("news.csv")
# records = news.to_dict(orient='records')
# for record in records[:5]:
#     print(record['title'])

# sol 2.


def summarize_google_news(csv_file="news.csv", max_topic=5):  # max_topic只取前五個
    news = pd.read_csv(csv_file)
    groups = news.groupby('topic_id')  # 依照 topic_id 分組 = 同 topic_id 為一組
    summarizations = list()
    for gid, group in groups:
        temp = list(group['title'])
        message = "\n".join(temp)  # list -> string
        summarization = complete_chat(message)
        print("Summarization = ", summarization, '\n')
        summarizations.append(summarization)
        if gid >= max_topic-1:
            print('Summarization Done.')
            break
    return summarizations


if __name__ == '__main__':
    summarize_google_news()
