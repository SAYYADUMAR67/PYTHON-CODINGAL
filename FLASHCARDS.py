class flashcards:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+' (' + self.meaning + ')'

flash = []
print("WELCOME TO YOUR SIGMA FLASHCARDS")

while True:
    word = input("enter a name of the word: ")
    meaning = input("enter the meaning of the word: ")
    flash.append(flashcards(word, meaning))
    choice = input("do you want to add more words? (yes/no): ")
    if choice.lower() != 'yes':
        break  

print("\nYour Flashcards:")
for card in flash:
    print(card)