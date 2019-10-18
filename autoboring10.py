# def spam():
#     print (eggs)
# eggs = 42
# spam()


# def spam():
#     eggs = 'Hello'
#     print(eggs)


# eggs = 42
# spam()
# print(eggs)


# def spam():
#     eggs = 99
#     bacon()
#     print(eggs)

# def bacon():
#     ham = 101
#     eggs = 0

# spam()


def spam():
    global eggs
    eggs = 99
    print(eggs)


eggs = 42
spam()
print(eggs)
