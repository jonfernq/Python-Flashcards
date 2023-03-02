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

![mastery_ratings](https://user-images.githubusercontent.com/68504324/222575293-4880d663-9a1c-4c90-9d05-1b63e2520078.jpg)

- [flashcard_logic.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/flashcard_logic.py): Loads, iterates through, and collects mastery ratings for, a deck of flashcards.   

```python
# flashcard_logic.py

# business logic or middle layer of 
# three layered flashcard design: 
# data, logic presentation 

from inquirer import Text
from flashcard_presentation import FlashcardPresentation  # Presentation layer 
from flashcard_data import FlashcardData                  # Data layer 

presentation = FlashcardPresentation()                    # Create a FlashcardPresentation object
data         = FlashcardData()                            # Create a FlashcardData object

for card in data.flashcards:                              # Loop through flashcards, display front and back, collect mastery ratings 
    willcontinue = presentation.present_front(card)       # Display the front of the flashcard and prompt user for input
    if willcontinue == 'x':                               # Exit     
        break 
    mastery = presentation.present_back(card)             # Display back of flashcard, prompt user to rate mastery
    data.record_flashcard_mastery_rating(mastery, card)   
presentation.exit() 
data.exit()     
```

- [flashcard_data.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/flashcard__data.py):  Layer performing all data I/O. 

```python
# flashcard_data.py - 

import datetime 

class Flashcard:
    def __init__(self, front, back):
        self.front = front
        self.back = back

class FlashcardData: 
    def __init__(self):

        self.flashcards = [
            Flashcard(front='What is the capital of France?', back='Paris'),
            Flashcard(front='What is the largest country in the world?', back='Russia')
        ]     
        
        self.log = open('log.txt', 'a', encoding='utf-8')     # log file of mastery ratings 

    def record_flashcard_mastery_rating(self, mastery, card): 
        self.log.write(str(datetime.datetime.now()) + '\t' + str(mastery) + '\t front=' + str(card.front) + '\t back=' + str(card.back) + '\n') # write mastery rating to log
        
    def exit(self): 
        self.log.close()         
```

- [flashcard_presentation.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/flashcard_presentation.py): Simple user interface isolated in this class, includes prompting user for input, recording and validating input, opening, reading and writing, and closing from databases and files, sending messages to user.    

```python
# flashcard_presentation.py - 

import inquirer

class FlashcardPresentation:
    def present_front(self, flashcard):
        questions = [
            inquirer.Text('input', message=flashcard.front + '\nHit enter to continue, x to  exit')
        ]
        willcontinue = inquirer.prompt(questions)
        return willcontinue
        
    def present_back(self, flashcard):
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
                
    def exit(self):
        print("Exiting flashcard review\nCheck log file for mastery ratings") 
```

- [log.txt](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/log.csv):  Recorded mastery rating, for future processing:  

```
2023-03-03 04:25:16.424978	2	 front=What is the capital of France?	 back=Paris
2023-03-03 04:25:20.462859	1	 front=What is the largest country in the world?	 back=Russia
2023-03-03 05:00:45.894532	3	 front=What is the capital of France?	 back=Paris
2023-03-03 05:00:49.995731	1	 front=What is the largest country in the world?	 back=Russia
2023-03-03 05:18:36.485844	4	 front=What is the capital of France?	 back=Paris
2023-03-03 05:18:39.163318	1	 front=What is the largest country in the world?	 back=Russia
2023-03-03 05:31:29.844688	3	 front=What is the capital of France?	 back=Paris
2023-03-03 05:31:31.697439	2	 front=What is the largest country in the world?	 back=Russia
```




