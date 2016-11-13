def wordsAndLineNumbers(filename):
    punctuation = ".,:;'" + '"'
    lineno = 0
    with open(filename) as f:
        for line in f:
            lineno += 1
            words = line.strip().split()
            for word in words:
                yield (word.strip(punctuation), lineno)

def formatted(numberSet):
    separator = ", "
    return separator.join(map(str, sorted(numberSet)))

#targets = { line.strip() for line in open("targets") }
targets = { "ladle", "gull", "hut" }
linesFoundOn = { t:set() for t in targets }

for (word, lineno) in wordsAndLineNumbers("../data/document.txt"):
    if word in targets:
        linesFoundOn[word].add(lineno)

for t in sorted(targets):
    print (t + "  " + formatted(linesFoundOn[t]))
