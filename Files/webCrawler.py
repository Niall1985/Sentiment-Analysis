import requests
from bs4 import BeautifulSoup

website = input("Enter the website to review: ")
url = "https://www.trustpilot.com/review/" + website

with open("extracted_reviews.txt", "w", encoding="utf-8") as file:
    page = 1
    while page != 10:
        urlNew = url + "?page=" + str(page)
        response = requests.get(urlNew)
        soup = BeautifulSoup(response.content, "html.parser")
        reviews = soup.find_all('div', class_='styles_reviewCardInner__EwDq2')
        for review in reviews:
            try:
                review_text = review.find('p', {'class': 'typography_body-l__KUYFJ typography_appearance-default__AAY17 typography_color-black__5LYEn'}).text.strip()
                file.write(review_text + "\n\n")
            except Exception:
                review_text = None

        page += 1
