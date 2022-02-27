from kanji_list import kanji_list
from bs4 import BeautifulSoup
import requests
import os
from rich import print as rprint

r = requests.get("https://hochanh.github.io/rtk/rtk1-v6/index.html")
soup = BeautifulSoup(r.content,"html.parser")


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def main(r,soup):
    clearConsole()
    kanji_num = input("What's the Kanji number : ")

    if int(kanji_num) > 2200:
        print("Invaild number")
        return  

    kanji = kanji_list[kanji_num]

    r = requests.get("https://hochanh.github.io/rtk/{}/index.html".format(kanji))
    soup = BeautifulSoup(r.content,"html.parser")

    kanji_stories = soup.find_all("p")
    kanji_stories_text = [story.text for story in kanji_stories]


    for story in kanji_stories_text:
        rprint(story)
        rprint("============================================================================================================")
    


is_on = True

while is_on:

    main(r,soup)

    re_run = input("Do you want to re run (y/n): ")

    if re_run.lower() != "y":
        is_on = False
