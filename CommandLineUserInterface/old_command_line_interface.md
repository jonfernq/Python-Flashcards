### CLI User Interface

The CLI flashcard display class: 

![cli_flashcards](https://user-images.githubusercontent.com/68504324/220826507-665dbd92-35de-4b59-a053-773fa4160106.jpg)

- [display_flashcard.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/display_flashcard.py): Displays front and back of flashcard, validates user input, and returns response, if required.  

```python
import inquirer

class Flashcard:
    def __init__(self, front, back):
        self.front = front
        self.back = back

class DisplayFlashcard:
    def display_front(self, flashcard):
        questions = [
            inquirer.Text('input', message=flashcard.front + '\nPress enter to continue')
        ]
        inquirer.prompt(questions)
    
    def display_back(self, flashcard):
        while True:
            mastery_question = [
                inquirer.Text('input', message=flashcard.front + '\n' + flashcard.back + 
                              '\nRate mastery from 1 to 5')
            ]
            mastery_rating = int(inquirer.prompt(mastery_question)['input'])
            if mastery_rating >= 1 and mastery_rating <= 5:
                return mastery_rating
            else:
                print("Invalid input. Please enter an integer from 1 to 5.")
```

- [display_flashcard_test.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/display_flashcard_test.py):  Tests display_flashcard.py with example flashcards. 

```python
from inquirer import Text
from display_flashcard import DisplayFlashcard
from display_flashcard import Flashcard

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
```




