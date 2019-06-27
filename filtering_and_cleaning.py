from string import punctuation
import re
import os
import pandas as pd
import xlwt                


path = os.path.abspath(os.path.dirname(__file__))
f = open(os.path.join(path,'scrapped_data.txt'),'rt',encoding='utf-8')

text_file = f.read().split(' ')
text_lower = [text.lower() for text in text_file]
print('Converting data to lowercase...')
text_letters = [''.join(c for c in s if c not in punctuation) for s in text_lower]
print('Removing special characters...')
text_final = [re.sub(r'[^A-Za-z]+','',x,) for x in text_letters]

#sort the elements of the list
print('Sorting words alphabetically...')
text_final.sort()

#Count the elements of a list
def count_elem(l):	
	elements = {}
	for elem in l:
		if elem in elements.keys():
			elements[elem] += 1
		else:
			elements[elem] = 1
	return elements	
print('Counting the frequency of elements...')

#converting values into a dictionary
dic ={}
dic = count_elem(text_final)

# creating columns of a dataframe
words = []
frequency = []
words = list(dic.keys())
frequency = list(dic.values())


df = pd.DataFrame()
df['Words'] = words
df['Frequency'] = frequency


# Removing the first row as it conatins the blank spaces 
new_df = [[]]
new_df= df.iloc[1:]
new_df.to_excel('file.xls')
print('Words and their frequency is saved in an .xls file\n') 

