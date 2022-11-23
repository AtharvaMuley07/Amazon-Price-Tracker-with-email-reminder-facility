import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL = input("Enter the product's Amazon link (URL to be specific): ")
desired_price = float(input("Enter Desired Price of the product: "))
desired_time_interval = float(input("Enter the time interval in seconds: "))



# Test URL for Apple iPhone 13 (256GB)-Midnight = 'https://www.amazon.in/dp/B09G9BQS98/ref=twister_B09GG3LLD6?_encoding=UTF8&th=1'
# Test URL for OnePlus 9RT = 'https://www.amazon.in/OnePlus-Hacker-Black-128GB-Storage/dp/B09MQ9WRGZ/ref=sr_1_4?pf_rd_i=1389401031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=fb23d6d8-781b-428f-878d-c40799ff1a34&pf_rd_r=R66QVKBAND1X67N8K78D&pf_rd_s=merchandised-search-1&pf_rd_t=30901&qid=1643785375&refinements=p_89%3AOnePlus&rnid=3837712031&s=electronics&sr=1-4&th=1'
# TEST URL for a Fridge = 'https://www.amazon.in/LG-Refrigerator-GC-B247KQDV-ADSQEBN-Graphite-Compressor/dp/B07612F52G/ref=sr_1_36?crid=17UGKT0GDXAZU&keywords=fridge&qid=1644775617&sprefix=fridge%2Caps%2C233&sr=8-36'
# TEST URL for Amazon's own Alexa Echo Dot = 'https://www.amazon.in/Echo-Dot-4th-Gen-Blue/dp/B084KSRFXJ/ref=sr_1_3?keywords=echo+dot&qid=1644775805&s=amazon-devices&sprefix=echo%2Camazon-devices%2C342&sr=1-3'


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}



# <span id="productTitle" class="a-size-large product-title-word-break">        Apple iPhone 12 Pro, 128GB, Pacific Blue - Unlocked (Renewed Premium)       </span>
# <span class="a-offscreen">₹1,59,900.00</span>



def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    # print(soup.prettify())


    title = soup.find("span", {"id": "productTitle"},{"class": "a-size-large product-title-word-break"}).get_text()
    print(title.strip())


    price = soup.find("span", {"class": "a-offscreen"}).get_text()
    price = price.replace(",", "")
    print(price)


    # converting string to float
    converted_price = float(price[1:])


    flag = 0
    while flag == 0:
        if converted_price <= desired_price:
            send_mail()
            flag = 1
        elif converted_price > desired_price:
            print("Price is still too high")
            time.sleep(desired_time_interval)
            check_price()



def send_mail():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()

    server.starttls()
    server.ehlo()


    server.login('1032191015@mitwpu.edu.in', 'hzemuwmckxgpsjlr')


    subject = 'The product is now available at your desired price'
    body = 'The product from Amazon that you had registered for price tracking is now available at a price that you desired. Check this AMAZON link for the same: '
    url = URL
    price = desired_price


    # Link = print(title.strip())
    # msg = "Subject: {}\n\n My age is {}".format(SUBJECT, AGE)

    msg = f"Subject:{subject,price}\n\n{body,url}"
    server.sendmail(
        '1032191015@mitwpu.edu.in',
        '1032191243@mitwpu.edu.in',
        msg
    )
    print('EMAIL WAS SENT SUCCESSFULLY')
    server.quit()

check_price()
