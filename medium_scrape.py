import os
import requests
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20191126074327/https://medium.com/@subashgandyer/papa-what-is-a-neural-network-c5e5cc427c7"

response = requests.get(url)
if response.status_code == 200:
    html_content = response.text
else:
    print("Failed to retrieve the webpage")
    exit()

soup = BeautifulSoup(html_content, "html.parser")
article_text = soup.get_text(separator="\n")

folder_name = "scraped_articles"
os.makedirs(folder_name, exist_ok=True)

file_path = os.path.join(folder_name, "medium_article.txt")
with open(file_path, "w", encoding="utf-8") as file:
    file.write(article_text)

print("Article scraped and saved successfully!")
