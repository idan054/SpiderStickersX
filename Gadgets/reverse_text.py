# def get_farsi_text(text):
#     if reshaper.has_arabic_letters(text):
#         words = text.split()
#         reshaped_words = []
#         for word in words:
#             if reshaper.has_arabic_letters(word):
#                 # for reshaping and concating words
#                 reshaped_text = reshaper.reshape(word)
#                 # for right to left
#                 bidi_text = get_display(reshaped_text)
#                 reshaped_words.append(bidi_text)
#             else:
#                 reshaped_words.append(word)
#         reshaped_words.reverse()
#     return ' '.join(reshaped_words)
#     return text

def reverse_text(text):
    string_list = []
    for l in reversed(text):
        # print(l)
        string_list.append(l)
    listToStr = ' '.join([str(elem) for elem in string_list])
    # print(listToStr)
    return listToStr

reverse_text("אחי")
