## Command Line User Interface (CLI)

A Command Line Interface (CLI) is an easy setting to test the underlying logic of an app.
Here that app is a flashcard and multiple choice quiz app. 

I use the [ConEmu terminal emulator](https://en.wikipedia.org/wiki/ConEmu) for Windows which displays unicode characters better than 
the command line terminals that come with Windows. 

A [three-tier](https://en.wikipedia.org/wiki/Multitier_architecture#Three-tier_architecture) or three-layered architecture of 1. data/database, 2. business logic, and 3. presentation/user-interface, allows for separation of concerns and easier change to layers.  

Using a simple CLI user interface for the presentation layer, business logic is easily worked out without the usual complications of user interface code.

A variety of more complicated user interfaces can be added after business logic has been finalized: **Web**; **Desktop**: Windows, macOS, **Linux**; Mobile: iOS, Android.  

I find the [Python Inquirer package](https://github.com/jonfernq/Python-Utilities/tree/main/PythonInquirer) provides a nice CLI user interface to work with, displaying menus and checkboxes for multiple choice questions. 

### Presentation Layer

The presentation layer encapsulates and hides complicated user interface details
with very limited functionality:  

- a. Display the front and back of flashcards
- b. Collect and validates user input
- c. Pass data back to business logic layer. 

This limited functionality allows the app can be more easily ported to different user interfaces, e.g. CLI, React.js, PyQT, Flutter, etc...    

### Business Logic Layer 

In the business logic layer, a simple iterator class iterates over a deck of flashcards, calling a simple flashcard state machine for each succesive flashcard. 

Each flashcard state machine class toggles between flashcard front and back calling the presentation class to present each side of the flashcard.

Then the user response (a self-rating of mastery of the flashcard information) is sent back from the presentation layer to business logic layer and stored in the data layer.   

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




