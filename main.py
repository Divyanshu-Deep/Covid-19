# import win10toast
from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


# create a function to notifyMe
def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=r"C:\Users\Divyanshu\Desktop\covid19\coronaviruspng.ico",
        timeout=15
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
  

    myHtmlData = getData("https://www.mohfw.gov.in/")

    soup = BeautifulSoup(myHtmlData, 'html.parser')
    # print(soup.prettify())
    myStr = ""
    for tr in soup.find_all('tbody')[1].find_all('tr'):
        myStr += tr.get_text()
         myStr = myStr[0:]

         itemList = myStr.split("\n\n")

         states = ['Bihar', 'Karnataka']
          for item in itemList[0:22]:
            dataList = item.split('\n')
           if dataList[1] in states:
             nTitle = 'cases of covid-19'
             nText = f"STATE {dataList[1]}\nIndian:  {dataList[2]}\nCured: {dataList[4]}\nDeaths: {dataList[5]}"
             notifyMe(nTitle, nText)
             time.sleep(2)
            
