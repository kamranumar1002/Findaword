from lib2to3.pgen2 import grammar
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.

def index(request):
    return render(request, 'index.html')

def search(request):
    word1 = request.GET['word']
    word = word1.upper()


    page = requests.get("https://www.dictionary.com/browse/" + word)
    soup = BeautifulSoup(page.text, 'lxml')
    # whole = soup.find('div', class_ = 'default-content')

    try:
        pos1 = soup.find_all('span', class_ = 'luna-pos')
        pos = pos1[1].text

        meaning = soup.find('div', value='1').text.upper()
    except:
        pos = 'WORD NOT FOUND'
        meaning = ''

    page2 = requests.get("https://www.thesaurus.com/browse/" + word)
    soup2 = BeautifulSoup(page2.text, 'lxml')

    try:
        whole2 = soup2.find('div', class_ = 'css-1fsijta')

        synonym = [x.get_text().upper() for x in whole2.find_all('a', class_ = 'eh475bn0')]
        
        whole3 = soup2.find('div', class_ = 'e1q3oo7j0')
        antonym = [x.get_text().upper() for x in whole3.find_all('a', class_ = 'eh475bn0')]

    
    except:
        synonym = ''

        antonym = ''
       


    context = {'word':word,'pos':pos,'meaning':meaning, 'synonym':synonym, 'antonym':antonym}



    return render(request, 'search.html',context)