text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
text = text.replace(",", "")
text = text.replace(".", "")
words = text.split(" ")
s = [1, 5, 6, 7, 8, 9, 15, 16, 19]
s = list(map(lambda x: x - 1, s))
dic = {}
for index,word in enumerate(words):
    if (index in s):
        dic.update({index:word[0]})
    else:
        dic.update({index:word[:2]})
print (dic)

