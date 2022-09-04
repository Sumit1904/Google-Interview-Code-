ph = "3662277"
word=['foo','bar','baz','foobar','emo','cap', 'car', 'cat']


def wordinNum(word, num):
    count=0
    index = 0
    for i in range(len(word)):
        temp = inNum(word[i],num,index)
        if  temp != -1:
            count+=1
            index = i+1
    if count == len(word):
        return 1
    else:
        return 0

def inNum(char, num, index):
    for i in range(index, len(num)):
        if(inLst(char, int(num[i]))):
            return i
    return -1
    
def inLst(char, i):
    lst=[[],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],
    ['p','q','r','s'],['t','u','v'],['w','x','y','z']]
    if lst[i-1].count(char) > 0:
        return 1
    else:
        return 0



words=[]
for i in range(len(word)):
    if wordinNum(word[i], ph):
        words.append(word[i])
        
words.sort()
print(words)
