from bs4 import BeautifulSoup as bs


import requests

# This program was created to experiment with BeautifulSoup.

word = 'goodbye'
url = "http://www.wordreference.com/es/translation.asp?tranword="
url += word
result = requests.get(url)
page = result.text
doc = bs(page, 'html.parser')

search = doc.find_all(class_="ToWrd")
test = str(search)
newTest = test.split('<td class="ToWrd">')

cut_location = []
for word in newTest:
    cut_location.append(word.find('<'))

current = 0
while current < len(newTest):
    word = newTest[current]
    cut = cut_location[current]
    newTest[current] = word[:cut].strip()
    current += 1

current2 = 0
while current2 < len(newTest):
    for item in newTest:
        if item == "Spanish":
            del newTest[current2]
    current2 += 1


print(newTest)











'''
def get_definition(word):
    import requests
    url = "http://www.wordreference.com/es/translation.asp?tranword="
    url += word
    result = requests.get(url)
    page = result.text
    doc = bs(page, 'html.parser')


#get_definition('goodbye')
'''