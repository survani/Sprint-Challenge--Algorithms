"""
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""


def count_th(word):
    # TBC

    # count is used for tracking purposes.
    count = 0

    # after we will need to make sure that if the word is only containing less than 1 or less return the count
    # because in no way it can have th in it. Not possible with one or less letters.
    if len(word) <= 1:
        # that is why we just return count.
        return count

    else:
        # if the word has t and h in it then just keep adding it to the count.
        if word[0] == 't' and word[1] == 'h':
            count += 1
    # using recursion to make sure it is checking until they match. I must remove the first index.
    # It wouldn't make sense to check that one so we must move to the next.
    return count + count_th(word[1:])


# testing quickly if it works.
print(count_th('istherethatthattt'))
