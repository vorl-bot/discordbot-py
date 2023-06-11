import random
items = ['A','B','C','D']

def getGacha():
    index = random.randrange(0,len(items))
    item = items[index]

    return item