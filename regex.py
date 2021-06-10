f = open('C:\\Users\\nmanoj\\Desktop\\google-python-exercises\\babynames\\baby1990.html' , 'r')
file_read = f.read()
#print(file_read)
import re

match = re.findall(r'(.*?\d.*?>)(.*?</)', file_read)
print(match)

str="manoj"
print(dir(str))

