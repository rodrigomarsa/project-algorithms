# def is_palindrome_iterative(word):
#     if len(word) == 0:
#         return False
#     inverted_word = ""
#     for i in range(len(word)):
#         inverted_word += word[len(word) - i - 1]
#     if word == inverted_word:
#         return True
#     else:
#         return False


def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True
