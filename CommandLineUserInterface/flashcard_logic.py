# flashcard_logic.py

# business logic or middle layer of 
# three layered flashcard design: 
# data, logic presentation 

from inquirer import Text
from flashcard_presentation import FlashcardPresentation  # Presentation layer 
from flashcard_data import FlashcardData                  # Data layer 

presentation = FlashcardPresentation()                    # Create a FlashcardPresentation object
data         = FlashcardData()                            # Create a FlashcardData object

for card in data.flashcards:                              # Loop through flashcards, display front and back, collect mastery ratings 
    willcontinue = presentation.present_front(card)       # Display the front of the flashcard and prompt user for input
    if willcontinue == 'x':                               # Exit     
        break 
    mastery = presentation.present_back(card)             # Display back of flashcard, prompt user to rate mastery
    data.record_flashcard_mastery_rating(mastery, card)   
presentation.exit() 
data.exit()     

  
