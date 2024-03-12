meme_dict = {
            "CRINGE": "Что-то очень странное или стыдное",
            "LOL": "Что-то очень смешное"
            }
# dictionary - Key: Value

word = input("Введите непонятное слово (большими буквами!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("I'm not found this word in my dict")
