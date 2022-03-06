import math
import random
import statistics


def task6 (lst: list) -> list:
    new = []
    for item in lst:
        if item > 0:
            new.append(math.log(item))
        else:
            new.append(None)
    return new
print(task6([1, 3, 2.5, -1, 9, 0, 2.71]))


def task17 (lst1: list):
    ind_min = int(lst1.index(min(lst1)))
    ind_max = int(lst1.index(max(lst1)))
    if ind_min < ind_max:
        return (statistics.mean(lst1[ind_min+1:ind_max-1]))
    else:
        lst1[ind_min] = lst1[ind_max] = (lst1[ind_min] + lst1[ind_max])/2
        return(lst1)
print(task17(list(random.randint(1, 100) for _ in range(10))))


def task19(lst3: list):
    new2 = [0 if item == None else item for item in lst3]
    sr_zn = sum(new2) / (len(new2)-lst3.count(None))
    new3 = [sr_zn if item == None else item for item in lst3]
    return (new3)
print(task19([1, 5, 6.3, 6, None, 2.0, -4, None]))


def task11(text):
    new = []
    lst2 = [i.split() for i in text.split("\n")]
    for item in lst2:
        for i in range(len(item)):
            if len(item[i]) > 3:
                new.append(item[i])
    return new
my_text = '''Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''
print(task11(my_text))

