'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# ? RUN IN TERMINAL: python3 test_count_th.py

def count_th(word):
    print(word)

    # * IF LENGTH IS 0 OR LESS THAN 2 (len('th')) RETURN 0
    if len(word) == 0 or len(word) < 2:
        return 0

    # * IF INCREMENTS OF 2 CHARACTERS ARE == 'th'
    # ! RECURSIVE CALL WITH A SLICE OF ONE CHARACTER
    if word[:2] == 'th':
        return count_th(word[1:]) + 1
    else:
        return count_th(word[1:])

count_th('thetthththth124312')
