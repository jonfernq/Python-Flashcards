## Command Line User Interface (CLI)

A CLI is an easy setting to test the underlying logic of an app.

Here that app is a flashcard and multiple choice quiz app. 

With a CLI user interface, business logic is easily worked out without the usual complications of user interface code.

Then more complicated user interfaces can be added (**Web**; **Desktop**: Windows, macOS, **Linux**; Mobile: iOS, Android).  

### Python Inquirer 

The Python Inquirer package provides a nice CLI user interface: 

- [inquirer_simple.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/inquirer_simple.py): Simple test of Python Inquirer package for command line user input. First, displays a random integer, then continues displaying a different random integer everytime the user hits enter.  
- [inquirer_simple_2.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/inquirer_simple_2.py): Simple test that prompts for user name, then answers 'hello'.  
- [inquirer_simple_3.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/inquirer_simple_3.py): Simple two part prompt. 

### Presentation Layer

In the presentation layer, complicated user interface details are encapsulated and hidden. 

The presentation layer has very limited functionality. It only:  

- a. Displays the front and back of flashcards
- b. Collects and validates user input
- c. Passes data back to logic layer. 

This limited functionality is so that the app can be more easily ported to different user interfaces, e.g. CLI, React.js, PyQT, Flutter, etc...    

### Logic Layer 

In the logic layer, a simple iterator class iterates over a deck of flashcards calling a simple flashcard state machine for each flashcard. 

The flashcard state machine class toggles between flashcard front and back.

It calls the presentation class to present each side of the flashcard.

Then it collects the user response (a self-rating of mastery of the flashcard information).  

![diagram400](https://user-images.githubusercontent.com/68504324/221042530-fc380752-d65b-4bf5-a5a4-5fe037700d26.jpg)

(Note: this same design approach is applied to multiple choice quizzes in iterative mode, but the preferred quiz presentation format is a Coursera-like full-page presentation in which all quiz questions are presented on one page with a timer and then grading with feedback after submit.)  

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




