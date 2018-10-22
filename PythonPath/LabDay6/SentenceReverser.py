class SentenceReverser:
    vowels = ['a', 'e', 'i', 'o', 'u']
    sentence = ''
    reverse = ''
    vowelCount = 0
    vowelCountPerPhrase = []

    def __init__(self, sentence):
        self.sentence = sentence
        self.reverseSentence()

    def reverseSentence(self):
        self.reverse = ''.join(reversed(self.sentence.split()))

    def getVowelCount(self):
        for s in self.sentence:
            if s in self.vowels:
                self.vowelCount += 1
            return self.vowelCount

    def getReverse(self):
        return self.reverse

        items = []


for i in range(3):
    sentence = input('Enter a phrase:')
    reverser = SentenceReverser(sentence.strip())
    print(reverser.getReverse())

sortedItems = sorted(items, key=lambda item: item, .getVowelCount(),)
print(sortedItems[0].getReverse())
print("Sorted on vowel count (Descending)\n")

for i in range(len(sortedItems)):
    print("Reverse:", sortedItems[i].getReverse(),
          "Vowel count: ", sortedItems.getVowelCount())
