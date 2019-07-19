spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        break
    print('Spam is ' + str(spam))

    spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('Spam is ' + str(spam))
    