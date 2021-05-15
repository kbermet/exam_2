
count = 0
char = 's'
file = open("task2.txt","r", encoding='utf-8')
for i in file:
    for c in i:
        if c == char:
            count = count + 1
print(f'{char} is found {count} times')

count = 0
char = 't'
file = open("task2.txt","r", encoding='utf-8')
for i in file:
    for c in i:
        if c == char:
            count = count + 1
print(f'{char} is found {count} times')



file = open("task2.txt","r", encoding='utf-8')
for text in file:
    for i in text.upper():
        i.replace('advert')
        #     list_1.replace
        # if i == 't':
        #     count1 = count + 1
#

