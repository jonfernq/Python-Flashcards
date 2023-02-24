import random

flashcards1 = [
    {"question": "What is the capital of France?", "answer": "Paris", "box": 1, "mastery": 0},
    {"question": "What is the capital of Spain?", "answer": "Madrid", "box": 1, "mastery": 0},
    {"question": "What is the capital of Germany?", "answer": "Berlin", "box": 1, "mastery": 0},
    {"question": "What is the capital of Italy?", "answer": "Rome", "box": 1, "mastery": 0},
    {"question": "What is the capital of the United States?", "answer": "Washington, D.C.", "box": 1, "mastery": 0},
    {"question": "What is the capital of Japan?", "answer": "Tokyo", "box": 1, "mastery": 0},
    {"question": "What is the capital of China?", "answer": "Beijing", "box": 1, "mastery": 0},
    {"question": "What is the capital of Russia?", "answer": "Moscow", "box": 1, "mastery": 0},
]

import random

# Define the flashcards as a list of dictionaries
flashcards = [
    {'question': 'What is the capital of France?', 'answer': 'Paris', 'box': 1},
    {'question': 'What is the largest planet in the solar system?', 'answer': 'Jupiter', 'box': 1},
    {'question': 'What is 2 + 2?', 'answer': '4', 'box': 1},
    {'question': 'What is the boiling point of water?', 'answer': '100 degrees Celsius', 'box': 1},
    {'question': 'What is the chemical symbol for gold?', 'answer': 'Au', 'box': 1},
    {'question': 'What is the highest mountain in the world?', 'answer': 'Mount Everest', 'box': 1},
]

# Define the number of boxes in the Leitner system
num_boxes = 3


def process_flashcard(flashcard):
    # Print the question
    print(flashcard['question'],"     (Enter 'q' to quit)")
    #print(f"Enter 'q' to quit")
    # Get the user's answer
    user_answer = input("Your answer: ")
    # Check if the user wants to quit
    if user_answer.lower() == 'q':
        exit()
    # Check the answer
    if user_answer.lower() == flashcard['answer'].lower():
        # If the answer is correct, move the flashcard to the next box
        move_to_next_box(flashcard)
        print("Correct!")
    else:
        # If the answer is incorrect, move the flashcard to the first box
        move_to_first_box(flashcard)
        print(f"Sorry, the correct answer is '{flashcard['answer']}'")
    # Print the current box of the flashcard
    print(f"Current box: {flashcard['box']}")
    print()            

# Define a function to move a flashcard to the next box in the Leitner system
def move_to_next_box(flashcard):
    flashcard['box'] += 1
    if flashcard['box'] > num_boxes:
        flashcard['box'] = num_boxes

# Define a function to move a flashcard to the first box in the Leitner system
def move_to_first_box(flashcard):
    flashcard['box'] = 1

# Shuffle the flashcards
random.shuffle(flashcards)

# initial pass through flashcards, 
# classifying them, outting them in boxes 
for flashcard in flashcards:
    process_flashcard(flashcard) 

box_list = range(1, num_boxes + 1)
# Loop through the boxes in the Leitner system
while True: 
    for box_num in box_list: 
        # Print the message to the user
        print(f"Box {box_num}") 
        # Loop through the flashcards in the current box
        for flashcard in flashcards:
            if flashcard['box'] == box_num:
                process_flashcard(flashcard)

            
    
