from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

print("=" * 20)
print(soup.p)
print(soup.p.string)
print("=" * 20)
print(soup.a)
print(soup.a.string)
print("=" * 20)

# soup.find
p_with_class_story = soup.find("p", class_="story")
p_with_class_story = soup.find("p", attrs={"class": "story"})  # 等同於上
print(p_with_class_story, '\n')
print(p_with_class_story.parent)
print("=" * 20)

# soup.select
a_in_story = soup.select("p a")
print(a_in_story, '\n')
# print(a_in_story.parent)
print("=" * 20)
