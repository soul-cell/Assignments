"""def mixed(str):
    for k in range(len(str)):
        c = ord(str[k])
        mixed_ascii.append(c)
    return mixed_ascii

def uppercase(upper_case):
    for j in range(len(upper_case)):
        b = ord(upper_case[j])
        ascii_uppercase.append(b)
    return ascii_uppercase

def lowercase(lower_case):
    for i in range(len(lower_case)):
        a = ord(lower_case[i])
        ascii_lowercase.append(a)
    return ascii_lowercase

str=input()
character=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ascii_char=65
l2=[]
for i in character:
    ascii_char=ascii_char+1
    l2.append(ascii_char)
ascii_value=list(zip(character,l2))
print(ascii_value)
lower_case=str.lower()
upper_case=str.upper()
ascii_lowercase=[]
ascii_uppercase=[]
mixed_ascii=[]
print(mixed(str))
print(uppercase(upper_case))
print(lowercase(lower_case))"""
"""def ascii():
    char = 64
    ascii_char = char + 32
    for i in character:
        ascii_char = ascii_char + 1
        ascii_lower.append(ascii_char)
    ascii_value = dict(zip(character,ascii_lower))
    for j in word:
        for k, v in ascii_value.items():
            if j == k:
                list_1.append(v)
            else:
                upper()
    return list_1


def upper():
    ascii_char=32
    for i in upper_case:
        ascii_char = ascii_char + 1
        ascii_upper.append(ascii_char)
    ascii_value = dict(zip(upper_case, ascii_upper))
    for j in word:
        for k, v in ascii_value.items():
            if j == k:
                list_2.append(v)
    return list_2

character=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upper_case=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","W","X","Y","Z"]
ascii_lower=[]
ascii_upper=[]
list_1=[]
list_2=[]
word=input()
print(ascii())
print(upper())"""