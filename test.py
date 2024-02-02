# import collections

# defdict = collections.defaultdict(list)
# defdict[0].append(10)
# defdict[0].append(6)
# defdict[1].append(1)
# print(defdict)

# def default_factory(key):
#     return {key: 0}

# def_dict = collections.defaultdict(default_factory)


# print(def_dict)


# import re
# def spin_words(sentence):
#     names = sentence.split( ) 
#     print(names)
#     for i in names:
#         if len(i) >= 5:
#             names[names.index(i)] = names[names.index(i)][::-1]
#     new_s = " ".join(names)
#     return new_s

# print (spin_words("Ser Moloko Loma Lomaka Chapalo 8548845"))


# from collections import UserDict


# class MyDict(UserDict):
#     def __add__(self, other):
#         self.data.update(other)
#         return self

#     def __sub__(self, other):
#         for key in other:
#             if key in self.data:
#                 self.data.pop(key)
#         return self


# d1 = MyDict({1: 'a', 2: 'b'})
# d2 = MyDict({3: 'c', 4: 'd'})

# d3 = d1 - d2
# print(d3)  # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# d4 = d3 - d2
# print(d4)  # {1: 'a', 2: 'b'}


import csv


with open('eggs.csv', 'w', newline='') as fh:
    spam_writer = csv.writer(fh)
    spam_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
    spam_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


with open('eggs.csv', newline='') as fh:
    spam_reader = csv.reader(fh)
    for row in spam_reader:
        print(', '.join(row))