## Command Line User Interface (CLI)

A CLI is an easy setting to test the underlying logic of a flashcard or multiple choice quiz app. 

Then, when the logic is worked out, a user interfaces are added (Web; Desktop: Windows, macOS, Linux; Mobile: iOS, Android).  

The Python Inquirer package provides a nice CLI for these purposes. 

### Flashcard Presentation

The presentation layer class has limited functionality, only displaying the front and back of flashcards, collecting and validating user input, then passing it on to the logic layer. 

In the logic layer, a simple flashcard state machine class toggles between flashcard front and back, calling the presentation class to present each side of the flashcard, then collecting the user response, which isa self-rating of mastery of the flashcard information.  

Above the flashcard state machine in the logic layer is a a simple iterator class that iterates over a deck of flashcards, calling the flashcard state machine for each  flashcard. 

(Note: this same design approach is applied to multiple choice quizzes in iterative mode, but the preferred quiz presentation is a Coursera-like presentation in which all quiz questions are presented on one page with a timer and then grading of feedback after submit.)  

Functionality is developed progressively from simple to complex building upon code snippets: 

- [inquirer_simple.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/inquirer_simple.py): Simple test of Python Inquirer package for command line user input. First, displays a random integer, then continues displaying a different random integer everytime the user hits enter.  
- [inquirer_simple_2.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/inquirer_simple_2.py): Simple test that prompts for user name, then answers 'hello'.  
- [inquirer_simple_3.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/inquirer_simple_3.py): Simple two part prompt. 

The flashcard display class: 

![cli_flashcards](https://user-images.githubusercontent.com/68504324/220826507-665dbd92-35de-4b59-a053-773fa4160106.jpg)

- [display_flashcard.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/display_flashcard.py): Displays front and back of flashcard, validates user input, and returns response, if required.  
- [display_flashcard_test.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/display_flashcard_test.py):  Tests display_flashcard.py with example flashcards. 




