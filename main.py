from random import choice
from bs4 import BeautifulSoup
import requests
from colorama import Fore

abc = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Э', 'Ю', 'Я']

session = requests.Session()


print("========================СЛОВАРИЯ!========================")

return_ = int(input("СКОЛЬКО СЛОВ ПРОГРАММА ДОЛЖНА НАЙТИ? "))

for i in range(return_):
    letter1 = choice(abc)

    page1 = session.get(f'https://ozhegov.slovaronline.com/articles/{letter1}/page-1')
    page1_soup = BeautifulSoup(page1.content, 'lxml')

    words1 = page1_soup.find_all('div', class_="col-lg-4")

    word1 = choice(words1).text
    word1_len = len(word1)
    last3 = word1[word1_len - 3:word1_len]


    page2 = session.get(f'https://ozhegov.slovaronline.com/articles/{"Б"}/page-1')
    page2_soup = BeautifulSoup(page2.content, 'lxml')

    try:
        letter2 = last3[0]
    except:
        pass


    page2 = session.get(f'https://ozhegov.slovaronline.com/articles/{letter2}/page-1')
    page2_soup = BeautifulSoup(page2.content, 'lxml')
    words2 = page2_soup.find_all('div', class_="col-lg-4")

    for wordlist in words2:
        word2 = wordlist.text
        if word2[0:3] == last3 and word2 != last3:
            print(Fore.GREEN + word1.replace(last3, "").lower() + word2 + Fore.RESET)
            break
    page2 = session.get(f'https://ozhegov.slovaronline.com/articles/{letter2}/page-2')
    page2_soup = BeautifulSoup(page2.content, 'lxml')
    words2 = page2_soup.find_all('div', class_="col-lg-4")
    for wordlist in words2:
        word2 = wordlist.text
        if word2[0:3] == last3 and word2 != last3:
            print(Fore.GREEN + word1.replace(last3, "").lower() + word2 + Fore.RESET)
            break