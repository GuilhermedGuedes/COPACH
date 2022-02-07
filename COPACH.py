import numbers

with open("palavras.txt") as file:
    data = file.read().replace(" ", "").split(",")

for x in data:
    if x.isalpha():
        print("{} - Varchar".format(x))
    elif x.isalnum():
        print("{} - int".format(x))
    elif isinstance(x, numbers.Integral):
        print("{} - float".format(x))
    else:
        print("{} - float".format(x))
