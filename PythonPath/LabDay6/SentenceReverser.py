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

    def getReverse(self):
        return self.reverse


items = []

for i in range(3):
    sentence = input('Enter a phrase:')
    reverser = SentenceReverser(sentence.strip())
    print(reverser.getReverse())
