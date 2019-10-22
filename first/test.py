import sys
 
count_en = count_words = count_ju = 0
 
f = open("data.txt", "r")  # 设置文件对象
data = f.read()  # 直接将文件中按行读到list里
f.close()  # 关闭文件

count_en=len(data) #统计字符数量

for y in data.split('.'):   #统计句子数量
    count_ju+=1
for y in data.split('!'):
    count_ju+=1
for y in data.split('?'):
    count_ju+=1
count_ju=count_ju-3

f = open("data.txt", "r")  # 设置文件对象
data2 = f.readlines()  # 按行读取
f.close()  # 关闭文件

words = []
for line in data2:
    for word in line.replace('\n', '').split(" "):
        words.append(word)

count_words=len(words)

print('字符数量为{}' .format(count_en))
print('单词数量为{}' .format(count_words))
print('句子数量为{}' .format(count_ju))