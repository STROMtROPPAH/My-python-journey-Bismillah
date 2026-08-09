with open('Prophet Muhammad (ﷺ) last sermon (Khutbah) .txt', 'r') as f:
    text = f.read().lower()

words = text.split()

count = {}
for word in words:
    clean = ''
    for c in word:
        if c.isalpha():
            clean += c
    if clean:
        count[clean] = count.get(clean, 0) + 1

top = sorted(count.items(), key=lambda x: x[1], reverse=True)[:10]

for word, num in top:
    print(f"{word}: {num}")
    