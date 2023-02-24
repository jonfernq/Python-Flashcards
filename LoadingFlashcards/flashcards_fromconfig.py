# flashcard_program.py - 
"""
to do: 
1. add 'exit' option during flashcard viewing 
2. validate user input with appropriate error messages 
"""

import csv
import json

# Load the list of CSV flashcard files from the configuration file
with open('config.json', 'r', encoding='utf8') as f:
    config = json.load(f)
flashcard_files = config['flashcard_files']

# Define a function to load the flashcards from a CSV file
def load_flashcards(file_path):
    flashcards = []
    with open(file_path, 'r', encoding='utf8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            flashcards.append(row)
    return flashcards

# Define a function to start the flashcard program
def start_flashcard_program():
    # Prompt the user to select a deck of flashcards
    print('Please select a deck of flashcards:')
    for i, flashcard_file in enumerate(flashcard_files):
        print(f'{i + 1}. {flashcard_file}')
    selected_deck = input()
    # Load the selected deck of flashcards
    flashcards = load_flashcards(flashcard_files[int(selected_deck) - 1])
    # Define a function to present the flashcards to the user
    def present_flashcards(flashcards):
        if len(flashcards) == 0:
            print('You have completed all the flashcards!')
            return
        flashcard = flashcards[0]
        print(f'Front: {flashcard["front"]}')
        print(f'Back: {flashcard["back"]}')
        print('Enter a number 1-5 to rate your mastery of this flashcard (1 = least mastery, 5 = most mastery):')
        mastery = input()
        # Use the Leitner system to determine whether to present the flashcard again
        if int(mastery) > int(flashcard['mastery']):
            present_flashcards(flashcards[1:])
        else:
            present_flashcards([{**flashcard, 'mastery': str(int(flashcard['mastery']) + 1)}, *flashcards[1:]])
    # Start presenting the flashcards to the user
    present_flashcards(flashcards)

# Start the flashcard program
start_flashcard_program()



