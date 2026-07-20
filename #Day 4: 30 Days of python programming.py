#String Concatenation 
a = "thirty"
b = "days"
c = "of"
d ="python"
space = " "
full_sentence = a + space + b + space + c + space + d

print(full_sentence)


company = 'coding for all'
print (company)

#len
company = len('coding for all')
print (company)

#upper
company = 'coding for all'
print (company.upper())
print (company.lower())
print (company.title())
print (company.swapcase())

# Check if contains "Coding"
print("coding" in company)
print(company.find("coding"))

text = 'coding for all'
print(text.replace("coding", "python"))

# Split by space
FAANG = "facebook, Amazon, Apple, Netflix, Google"
print(FAANG.split(", "))

word = "coding for all"
print("position of 'c': ", word.index("c"))
print("position of 'f': ", word.rindex("f"))


sentence = "You cannot end a sentence with because because because is a conjunction"
print("the first 'because,: ", sentence.index("because"))
print("the first 'because,: ", sentence.find("because"))
print("the last 'because,: ", sentence.rindex("because"))

#slice
sentence = "You cannot end a sentence with because because because is a conjunction"
start = sentence.find("because")
end = sentence.rindex("because") + len("because")
print("Sliced phrase:", sentence[start:end])

#join
some_bushi = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(some_bushi))

