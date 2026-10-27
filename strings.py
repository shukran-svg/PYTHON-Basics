name ="Susan"

sentence ="my home area is called \"xyz\"" #escape character

print(sentence)
#operations ->functions
print(sentence.upper())
print(sentence.lower())
sentence=sentence.upper()
print(sentence)
print(sentence.capitalize())
print(sentence.title())

print(name.count("Susan")) # call a function --using,parameter
print(33,"Tom","81")
print(len(sentence))
replaced_sentence =sentence.lower().replace ( "home" , "city")
print(replaced_sentence)
k="123j"
sentence.isnumeric()

print(sentence.isupper())#boolean true/false