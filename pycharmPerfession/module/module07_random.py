import random

ran = random.random() # 0-1的小数
print(ran)

ran = random.randrange(1,10,2)  #start, stop, step
#Choose a random item from range(start, stop[, step])
for i in range(10):
    print(random.randrange(1,10,2))

#Return random integer in range [a, b], including both end points.
ranint = random.randint(1,10)

list1 = ['lucy','lili','tom','jack']
ranname = random.choice(list1)
for i in range(3):
    print(random.choice(list1))

#打乱列表顺序
pai = ['红桃A','方片K','梅花8']
random.shuffle(pai)
print(pai)

