def in_array(array1, array2):
    # your code
    word_set = []
    array1_ordered = sorted(array1)
    for word1 in array1_ordered:
        for word2 in array2:
            if word1 in word2:
                word_set = word_set + [word1]
    return sorted(list(set(word_set)))