meme_dict = {
                "КРИНЖ": "Что-то очень странное или стыдное",
                "ЛОЛ": "Что-то очень смешное",
                'РОФЛ':'Шутка',
                "ЩИЩ": 'одобрение или восторг',
                "КРИПОВЫЙ": "Что-то страшное или мерзкое",
                'АГРИТЬСЯ':'злиться',
                }
word = input("Введите непонятное слово (большими буквами!): ")
if word in meme_dict.keys():
        # Что делать, если слово нашлось?
    print(word ,'-', meme_dict[word])
else:
    print('Нам неизвестно')
