import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/Intel-BX80684I78700K-Core-i7-8700K-Processor/dp/B07598VZR8/ref=sr_1_1?keywords=intel+i7&qid=1579277931&sr=8-1'

headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

def check_price():
    
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()

    price = soup.find(id="priceblock_ourprice").get_text()

    if(int(price)>30000): 
        send_mail()

def send_mail():
    message = f"Subject: {subject}\n\n{body}"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    
    server.starttls()
    server.ehlo()

    server.login("jha.ritwik.17.9@gmail.com","tguiqhzhshizrwkz")
    subject = "Price - dropped"
    body = "chech the link https://www.amazon.in/Intel-BX80684I78700K-Core-i7-8700K-Processor/dp/B07598VZR8/ref=sr_1_1?keywords=intel+i7&qid=1579277931&sr=8-1"

    server.sendmail(
        'jha.ritwik.17.9@gmail.com',
        'nitish.jha.0509@gmail.com',
        message
    )
    print("hey email has been sent")
    server.quit()

check_price()



    
