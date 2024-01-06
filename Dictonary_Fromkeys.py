d = {'a':10 , 'b': 20 , 'c': 30 , 'd': 40 , 'e': 50}
print(d)
x = dict.fromkeys(d) # Not initialized any value so by default considered 'None'
y = dict.fromkeys(d , 10) # 10 initialized so every value considered as 10
print(x) # {'a': None, 'b': None, 'c': None, 'd': None, 'e': None}
print(y) # {'a': 10, 'b': 10, 'c': 10, 'd': 10, 'e': 10}
