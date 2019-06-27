from bs4 import BeautifulSoup
import requests 
import os

print('------------------------------------------------------------\n')
print('                   WEB SCRAPING PROJECT \n')
print('------------------------------------------------------------\n')
print('       COUNTING THE MOST FREQUENT WORDS IN A WEBPAGE\n')
print('------------------------------------------------------------\n')
print('------------------------------------------------------------\n')
 

url = input('Enter the url of the Webpage : ')
print('Scraping data from the Webpage...')
data = requests.get(url)
soup = BeautifulSoup(data.content,'lxml')

path = os.path.abspath(os.path.dirname(__file__))
filename = os.path.join(path,'scrapped_data.txt')
links = soup.find_all('div')

print('Scrapped data saved in a .txt file.\n')
with open(filename,'w',encoding = 'utf-8') as f:
	for link in links:
		text = link.text
		headlines_length = len(text.split())
		if headlines_length > 4:
			f.write(text)
			f.write('\n')

f.close()			
