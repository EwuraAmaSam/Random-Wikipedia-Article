# RANDOM WIKIPEDIA ARTICLE

# Requests is used for creating http requests
# beautifulsoup is for web scraping(data scraping)
#  i.e collecting data from the internet.
import requests
from bs4 import BeautifulSoup
import webbrowser
while True:
    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(url.content, "html.parser")
    title = soup.find(class_="firstHeading").text
    print(f"{title} \nDid you know that reading sharpens your thought process and makes you grasp concepts better? We have educational articles for you. Would you like to view and read this article? (Yes/No)")
    ans = input("").lower()
    if ans == "yes":
        url = "https://en.wikipedia.org/wiki/%s" % title
        webbrowser.open(url)
        break
    elif ans == "no":
        print("I have another interesting one for you. Check it out!")
        continue
    else:
        print("Wrong choice! Please try again.")
        break


# Ewura Ama Etruwaa Sam : 87922025
# Salia Abdul-Mumin : 80072025
# Julius Wambua : 89592025
# Darryn Walker : 82522025

# REFERENCES
# https://docs.python-requests.org/en/latest/
# https://www.w3schools.com/python/python_dictionaries.asp
# https://www.tutorialspoint.com/beautiful_soup/beautiful_soup_tutorial.pdf
# https://www.w3schools.com/python/gloss_python_else.asp
# https://realpython.com/beautiful-soup-web-scraper-python/
# https://www.pythonforbeginners.com/code-snippets-source-code/python-webbrowser
# rushylib.wordpress.com/2016/10/18/reading-increases-your-knowledge/