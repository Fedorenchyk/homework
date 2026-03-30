def popular_words (text, words):
    text = text.lower()

    popular_dict = {"i": 0,
                    "was": 0,
                    "three": 0,
                    "near": 0}
    for word in words:
        count = text.split().count(word)
        popular_dict[word] = count

    return popular_dict





assert popular_words('When I was One I had just begun When I was Two I was nearly new ', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')



