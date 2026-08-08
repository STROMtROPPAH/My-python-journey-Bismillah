def count_lines_words(filename):
    with open(filename, 'r') as f:
        text = f.read()

    lines = text.split('\n')
    words = text.split()

    return len(lines), len(words)

lines, words = count_lines_words('Prophet Muhammad (ﷺ) last sermon (Khutbah) .txt')
print(f"lines: {lines}")
print(f"words: {words}")