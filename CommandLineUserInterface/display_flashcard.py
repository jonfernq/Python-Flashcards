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
