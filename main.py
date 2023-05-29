from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
s = ''
for i in contacts_list:
  s += '\n'
  for l in i:
    s +=(l+',')
p = re.compile('(\,)*')
res = re.sub(p,r'\1', s)
p = re.compile('([А-Я][а-я]+)\s*\,*([А-Я][а-я]+)\s*\,*')
res = re.sub(p,r'\1,\2,', res)
p = re.compile('(\+7|8)\s*\(*(\d{3})\)*\s*\-*(\d{3})\s*\-*(\d{2})\s*\-*(\d{2})')
res = re.sub(p,r'+7(\2)\3-\4-\5', res)
p = re.compile('\s*\(*(доб.)\s*(\d+)\)*\s*')
res = re.sub(p,r' \1\2', res)
l = res.split('\n')
l.pop(0)
li =[]
for i in l:
  s=(i.split(','))
  s.remove('')
  li.append(s)
for i in li:
  for s in li:
    try:
      if i[0]==s[0]:
        if i != s:
          for q in range(1,10):
            for z in i:
              if z in s:
                i.remove(z)
              else:
                s.append(z)
                i.remove(z)
    except:
      pass
text = ''
for i in li:
  if len(i) == 0:
    li.remove(i)
li.sort()

for i in li:
  text += ('\n')
  for z in i:
   text +=(z+', ')
print(text)

with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',' )
  datawriter.writerows(li)