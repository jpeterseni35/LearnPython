def hello():
    print('Howdy!')
    print('Howdy!!')
    print('Hello there.')


hello()
hello()
hello()


def hello(name):
    print('Hello ' + name)


hello('Alice')
hello('Bob')


print('Hello has ' + str(len('hello')) + ' letters in it')


def plusOne(number):
    return number + 1


newNumber = plusOne(5)
print(newNumber)

print('Hello ', end='')
print('World')

print('cat', 'dog', 'mouse', sep='ABC')
