## Command Line User Interface (CLI)

A CLI is an easy setting to test the underlying logic of an app.

Here that app is a flashcard and multiple choice quiz app. 

With a CLI, business logic is easily worked out without complications of user interface code.

Then a user interface is added (**Web**; **Desktop**: Windows, macOS, **Linux**; Mobile: iOS, Android).  

### Python Inquirer 

The Python Inquirer package provides a nice CLI for these purposes. 

- [inquirer_simple.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/inquirer_simple.py): Simple test of Python Inquirer package for command line user input. First, displays a random integer, then continues displaying a different random integer everytime the user hits enter.  
- [inquirer_simple_2.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/inquirer_simple_2.py): Simple test that prompts for user name, then answers 'hello'.  
- [inquirer_simple_3.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/inquirer_simple_3.py): Simple two part prompt. 

### Flashcard Presentation

In the presentation layer class complicated user interface details are encapsulated and hidden. 

The presentation layer has very limited functionality. It only:  

- a. Displays the front and back of flashcards
- b. Collects and validats user input
- c. Passes data on to the logic layer. 

This limited functionality is so that the app can be more easily ported to different user interfaces, e.g. CLI, React.js, PyQT, Flutter, etc...    

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
- [display_flashcard_test.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/display_flashcard_test.py):  Tests display_flashcard.py with example flashcards. 




