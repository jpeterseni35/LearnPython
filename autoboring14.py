for i in range(4):
    print(i)

for i in [0, 1, 2, 3]:
    print(i)

# the above for loops do the same thing

oven = range(4)
list(oven)

list(range(0, 100, 5))
spam = list(range(0, 100, 5))
print(spam)

# common Python trick below

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']

for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])


supplies = ['pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens',
            'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens']

for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
