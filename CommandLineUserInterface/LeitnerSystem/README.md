## Leitner System 

The [Leitner system](https://en.wikipedia.org/wiki/Leitner_system) is a method for using flashcards to study. 

"It is a simple implementation of the principle of spaced repetition, where cards are reviewed at increasing intervals... 
flashcards are sorted into groups according to how well the learner knows each one in Leitner's learning box. 
The learners try to recall the solution written on a flashcard. If they succeed, they send the card to the next group. 
If they fail, they send it back to the first group. Each succeeding group has a longer period before the learner 
is required to revisit the cards." (Source: [Wikipedia](https://en.wikipedia.org/wiki/Leitner_system))

### Cycling Through Flashcards

There is no standard way to cycle through the boxes in the Leitner system. However, here are some common approaches:

Fixed order: The simplest approach is to cycle through the boxes in a fixed order, such as starting with box 1 and then moving on to box 2, 3, and 4 in sequence. This ensures that all the flashcards in each box are reviewed before moving on to the next box.

Random order: Another approach is to cycle through the boxes in a random order, which can help prevent users from anticipating which box a flashcard will be in and potentially relying on that knowledge instead of actually learning the material.

Mastery-based order: As you mentioned, the Leitner system places flashcards in boxes with increasing numbers indicating mastery. One approach is to cycle through the boxes in order of increasing mastery, starting with the box containing the flashcards with the least mastery and moving on to the box containing the flashcards with the most mastery. This approach ensures that flashcards that have been mastered more recently are reviewed less frequently, while those that are still being learned are reviewed more frequently.

Adaptive order: Some implementations of the Leitner system use an adaptive approach, where the order of the boxes is determined based on the user's performance. For example, if the user consistently struggles with flashcards in a particular box, that box could be reviewed more frequently. Conversely, if the user consistently performs well on flashcards in a particular box, that box could be reviewed less frequently. This approach can help personalize the learning experience for each user and optimize the review process.

### Simple Implementation

In this simple implementation, the first pass places flashcards in the boxes.
After that, the program cycles through the boxes from 1 to 3 until the user quits:

```python
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
```


