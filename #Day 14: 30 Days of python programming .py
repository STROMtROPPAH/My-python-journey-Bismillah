#map fuction
#map fuction is bascily takes a collection of item and change each one of the item depending the map fuction
def perkalian_satu(x):
    return x * 2

perkalian_dua = [1, 2, 3, 4, 5, 6, 7,]

perkalian_satu = list(map(perkalian_satu, perkalian_dua))
print(perkalian_satu)

#filer fuction
# what filter does is it filter every item and still keeps the original if only the item satisfy or followed a specific condition
scores = [50, 60 ,70, 80, 90, 100]
def is_passing(scores):
    return scores >= 60
passing_score = list(filter(is_passing, scores))
print(passing_score)

#reduce fuction
#reduce fuction combines , step by step into a single final value


prices = [12.50, 8.99, 3.49, 15.00]
def add_to_total(current_total, next_price):
    return current_total + next_price
    
total = reduce(add_to_total, prices)
print(total)  
