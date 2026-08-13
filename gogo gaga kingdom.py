def match_words(words):
    ctr = 0
    lst = []

    for word in words:
        if len(word) > 1 and word[0] == word[-1] :
            ctr += 1
            lst.append(word)
    print("The list of words of first and last letter matching is: ", lst)
    return ctr
count = match_words(['abc', 'xyz', 'aba', '1221'])

print("The number of words that match the criteria is:", count)
