# Exercises: Level 2:

#1 Join A and B

#2 Find A ∩ B (Intersection of A and B)

#3 Determine whether A is a subset of B

#4 Determine whether A and B are disjoint sets

#5 Find A ∪ B and B ∪ A

#6 Find the symmetric difference between A and B

#7 Delete the sets completely

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#1 Join A and B
print(A.union(B))
#or
c = A.union(B)
print(c)

#2 Find A ∩ B (Intersection of A and B)
print(A.intersection(B))

#3 Determine whether A is a subset of B
print(A.issubset(B))
