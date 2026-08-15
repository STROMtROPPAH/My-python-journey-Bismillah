import statistics

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age


ages.sort()
print(ages)
print(statistics.mean(ages))
print(statistics.mode(ages)) #most frequent
print(statistics.stdev(ages)) #standard deviation
print(statistics.variance(ages))
print(max(ages))
print(min(ages))