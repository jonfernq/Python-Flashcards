## Command Line User Interface

An easy setting to test the underlying logic of a flashcard or multiple choice quiz app. 

Then, when the logic is worked out, add a user interface or two, or three. 

The Python Inquirer package provides nice command line interface for these purposes. 

### Flashcard Presentation

The presentation layer only collects and validates user input, then passing it on to the logic layer. 

A simple flashcard presentation (or display) class uses Inquirer to display front and back of flashcards and then collect and validate user response.

![cli_flashcards](https://user-images.githubusercontent.com/68504324/220826507-665dbd92-35de-4b59-a053-773fa4160106.jpg)

In the logic layer it is a simple flashcard state machine that calls the presentation class to present the front and back of flashcard. 

A simple iterator class iterates over a deck of flashcards, calling the flashcard state machine for each  flashcard. 

(Note: this same design approach is applied to multiple choice quizzes in iterative mode, but the preferred quiz presentation is a Coursera-like presentation in which all quiz questions are presented on one page with a timer and then grading of feedback after submit.)  

Functionality is not developed progressively from simple to complex building upon code snippets: 

- [inquirer_simple.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/inquirer_simple.py): Simple test of Python Inquirer package for command line user input. First, displays a random integer, then continues displaying a different random integer everytime the user hits enter.  
- [inquirer_simple_2.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/inquirer_simple_2.py): Simple test that prompts for user name, then answers 'hello'.  
- [inquirer_simple_3.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/inquirer_simple_3.py): Simple two part prompt. 

The flashcard display class: 

- [display_flashcard.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/display_flashcard.py): Displays front and back of flashcard, validates user input, and returns response, if required.  
- [display_flashcard_test.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/display_flashcard_test.py):  Tests display_flashcard.py with example flashcards. 




