import requests
from bs4 import BeautifulSoup

# step 1 : request webpage html
url = "https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRFptTXpJU0JYcG9MVlJYS0FBUAE?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant"
response = requests.get(url)
# print(response)
# print(len(response.text))

# step 2 : Convert text into soup
soup = BeautifulSoup(response.text, 'html.parser')

# step 3 : Find element
topic_elements = soup.find_all("div", class_="W8yrY")
print(len(topic_elements))

# for topic_element in topic_elements:
# left_side_a = topic_element.find('a', class_="gPFEn")
# print(left_side_a, '\n')
# print(left_side_a.text)  # 新聞標題
# print(left_side_a['href'], '\n')  # 　原新聞連結
# print()

for topic_element in topic_elements:
    # 新聞標題
    news_titles = topic_element.find_all('a', class_="gPFEn")
    # 新聞媒體
    medias = topic_element.find_all('div', class_='vr1PYe')
    # 發布時間
    public_times = topic_element.find_all('time', class_='hvbAAd')

    for media, news_title, public_time in zip(medias, news_titles, public_times):
        print(media.text)
        print(news_title.text)  # 新聞標題
        print(public_time['datetime'])
        print()

    # break
