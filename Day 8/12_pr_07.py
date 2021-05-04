def remove_and_split(string,word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "      Ayush is good     "    
n = remove_and_split(this, "Ayush")
print(n)