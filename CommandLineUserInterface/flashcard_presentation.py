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
    
