#tuple
#challenge:Create an empty tuple
#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
#Join brples and assign it to siblings
#How many siblings do you have?
#Modify the siblings tuple and add the name of your father and mother and assign it to family_memberothers and sisters tus

family_male = ('bob', 'bobi', 'ludwing')
family_female = ('hannah banana', 'angelina')
sibling = family_female + family_male
family_member = list(sibling)
family_member.append('Mr.Robert')
family_member.append('Ms.Robert')

print(family_member)
print(len(family_female + family_male))
print(family_female + family_male)

#unpack
a, b, c, d, e, father, mother = family_member
print(f"sibling: {a}, {b}, {c}, {d}, {e}")
print(f"father: {father}")
print(f"mother: {mother}")