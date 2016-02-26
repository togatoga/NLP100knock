text = "I am an NLPer"
def bi_gram_word(text):
    result = []
    text = text.split(" ")
    pre = text[0]
    for i in range(1, len(text)):
        result.append(pre + "-" +text[i])
        pre = text[i]
        
    return result
def bi_gram_char(text):
    result = []
    text = text.split(" ")
    for word in text:
        pre = word[0]
        for i in range(1, len(word)):
            result.append(pre + word[i])
            pre = word[i]
    return result
        

print (bi_gram_word(text))
print (bi_gram_char(text))
