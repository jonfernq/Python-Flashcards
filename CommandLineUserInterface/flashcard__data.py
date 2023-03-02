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
