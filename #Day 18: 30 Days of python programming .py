from collections import Counter
import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

clean = re.sub(r'[^\w\s]', '', paragraph.lower())

words = clean.split()

word_count = Counter(words)


most_common = word_count.most_common(1)[0]
print(f"Most frequent word: '{most_common[0]}' appears {most_common[1]} times")