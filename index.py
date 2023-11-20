file = open("index.txt", "r")
plain = "{0}".format(file.read()).lower()
file.close()

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "y", "x", "z"]
lexi = []
start = 0
for x in range(len(plain)): 
    if (x > 1):
        index = 1
        for x in range(len(letters)): 
            if (letters[x] == plain[start]):
                lexi.append(index)
            index += 1
        start += 1
encrypt = open("encrypted.txt", "w")
for x in range(len(lexi)): 
    encrypt.write(str(lexi[x]))
    encrypt.write(" ")
encrypt.close()