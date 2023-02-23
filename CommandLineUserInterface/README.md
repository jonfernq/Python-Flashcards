## Command Line User Interface

A command line user interface provides an easy setting to test the logic for user interaction with flashcards 
and multiple choice quiz questions. 

The Python Inquirer package provides a powerful interface to the command line for these purposes. 

### Flashcard Display Class

A simple class that uses Inquirer to display the front and back of flashcards and collect user responses.

![cli_flashcards](https://user-images.githubusercontent.com/68504324/220826507-665dbd92-35de-4b59-a053-773fa4160106.jpg)

It is called by a flashcard state machine class that implements each flashcard with the state design pattern
and a set (or 'deck') of flashcards with the iterator design pattern. 

A similar class is also called by a multiple choice state machine that implements a Coursera-like quiz using the state design pattern.

- [inquirer_simple.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/inquirer_simple.py): Simple test of Python Inquirer package for command line user input. First, displays a random integer, then continues displaying a different random integer everytime the user hits enter.  
- [inquirer_simple_2.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/inquirer_simple_2.py): Simple test that prompts for user name, then answers 'hello'.  
- [inquirer_simple_3.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/inquirer_simple_3.py): Simple two part prompt. 

The flashcard display class: 

- [display_flashcard.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/display_flashcard.py): Displays front and back of flashcard, validates user input, and returns response, if required.  
- [display_flashcard_test.py](https://github.com/jonfernq/Python-Flashcards/blob/main/CommandLineUserInterface/display_flashcard_test.py):  Tests display_flashcard.py with example flashcards. 




