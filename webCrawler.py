import requests
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    
    
website=input("Enter the website to review : ")

url ="https://www.trustpilot.com/review/"+website
    

def reviewsAnalyser(review_text):
    obj=SentimentIntensityAnalyzer()
    # print(type(review_text))
    # if(type(review_text)=="NoneType"):
    #     return 0
    if review_text is None:
        return 0
    obj_dict=obj.polarity_scores(review_text)
    # print(f"dict : {obj_dict}")
    postive=obj_dict['pos']
    neutral=obj_dict['neu']
    negative=obj_dict['neg']
    rating=star_rating(postive*100,neutral*100,negative*100)
    return rating


def star_rating(positive,neutral,negative):
    rating=(positive*5+neutral*3+negative*1)/100
    return rating


page=1
sum=0
length=0
while(page!=10):
    urlNew=url+"?page="+str(page)
    # print(urlNew)
    response = requests.get(urlNew)
    soup = BeautifulSoup(response.content, "html.parser")
    reviews = soup.find_all('div', class_='styles_reviewCardInner__EwDq2')
    for review in reviews:
        try:
            review_text=review.find('p',{'class':'typography_body-l__KUYFJ typography_appearance-default__AAY17 typography_color-black__5LYEn'}).text.strip()
        except Exception:
            review_text=review.find('p',{'class':'typography_body-l__KUYFJ typography_appearance-default__AAY17 typography_color-black__5LYEn'})
        
        num=reviewsAnalyser(review_text)
        if(num!=0):
            sum+=num
    # reviewsAnalyser(review_text)    
    # print(review_text)
    # print("")
    page+=1
    length+=len(reviews)
if length==0:
    print(f"Could not find reviews for {website}")
    exit(0)
avg=sum/length
print(f"{length} reviews analysed...")
print(f"Final Outcome : {round(avg,1)} stars")
            
            
# print(f"link_elements: {soup}")
        # for link_element in link_elements:
        #     url = link_element['href']
        #     if "https://www.scrapingcourse.com/ecommerce/" in url:
        #         urls.append(url)


        # for review in reviews:
        #     review_text = review.find('span', {'data-hook': 'review-body'}).text.strip()  # Adjust the selector based on structure
        #     print(review_text)
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     'Accept-Language': 'en-US, en;q=0.5',
# }