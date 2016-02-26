text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
text = text.replace(",", "")
text = text.replace(".", "")
res = []
for x in text.split(" "):
    res.append(len(x))
print (res)
