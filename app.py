import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/Her-Pierre-Alex-Jeanty/dp/0997426586/ref=sr_1_2?keywords=her&qid=1575040989&sr=8-2'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content , 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(attrs={"class":"price3P"}).get_text()
    pricee = float(price[2:5])
    print(pricee)
    print(title)
    if(pricee < 599):
        send_mail()
    else:
        print('no mail')




def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('harahismast@gmail.com', 'harshzxcvbnmlpoiuytrewqaz')
    subject = 'price fell down'
    body = 'https://www.amazon.in/Her-Pierre-Alex-Jeanty/dp/0997426586/ref=sr_1_2?keywords=her&qid=1575040989&sr=8-2'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'harahismast@gmail.com',
        'ht50159@gmail.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT')
    server.quit()
check_price()