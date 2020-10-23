import random
from typing import List
def randList(n):
    iList = []
    for i in range(n):
        iList.append(random.randint(1,100))
    return iList
