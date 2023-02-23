from inquirer import Text
from display_flashcard import DisplayFlashcard
from display_flashcard import Flashcard

# Define a list of flashcards
#flashcards = [
#    {'front': 'What is the capital of France?', 'back': 'Paris'},
#    {'front': 'What is the largest country in the world?', 'back': 'Russia'}
#]

flashcards = [
    Flashcard(front='What is the capital of France?', back='Paris'),
    Flashcard(front='What is the largest country in the world?', back='Russia')
]

# Create a DisplayFlashcard object
display = DisplayFlashcard()

# Loop through the flashcards and display the front and back
for card in flashcards:
    # Display the front of the flashcard and prompt user for input
    display.display_front(card)

    # Display the back of the flashcard and prompt user to rate mastery
    mastery = display.display_back(card)
    print('Mastery rating:', mastery)
