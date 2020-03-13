spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello')  # returns 0

spam.index('heyas')  # returns 3


spam = ['cat', 'dog', 'bat']
spam.append('moose')  # adds "moose" to end of list
spam

spam.insert(1, 'chicken')  # inserts "chicken" into the 1 slot
spam

spam = ['cat', 'bat', 'rate', 'elpehant']
spam.remove('bat')


del spam[1]
spam.append('cat')
spam.append('cat')
spam.append('cat')
spam.append('cat')
spam.append('cat')

# the remove method only removes the first appearnce of the value
spam.remove('cat')
spam

spam = ['2', '5', '3.14', '1', '-7']
spam.sort()  # sort can sort the number values from smallet to largest
spam

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()  # can sort strings in alphabetical order as well
spam

# reverse takes a boolean and can reverse the order alphabetically
spam.sort(reverse=True)
spam

# sort method cannot sort a list with different types of variables (ex = ints and strings)

spam = ['Alice', 'Bob', 'ants', 'badgers', 'Carol', 'cats']
spam.sort()  # upper case characters are sorted before lower case
spam

spam = ['Alice', 'Bob', 'ants', 'badgers', 'Carol', 'cats']
# this keyword argument sorts in true alphabetical order
spam.sort(key=str.lower)
spam
