import pandas as pd
import matplotlib.pyplot as plt
import xlrd

df = pd.read_excel('file.xls')

a = df.nlargest(10,'Frequency')
print(a)

m = []
n = []
m = a['Words']
n = a['Frequency']

print('Plotting the Most frequent Words :')
plt.bar(m,n,color='#B19CD9')
plt.xlabel('Words',fontsize=15)
plt.ylabel('Frequency',fontsize=15)
plt.title('The Most Frequent Words are :',fontsize=18)
plt.show()
