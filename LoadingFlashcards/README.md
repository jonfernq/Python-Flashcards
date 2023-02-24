## Loading Flashcards 

Flashcard can be stored and loaded into an app in various ways. 

Before some code exploring these different ways is presented, 
some general ideas about flashcard data and its repurposing for different 
learning approaches will be outlined. 

### Flashcard Data-Gathering & Restructuring

CSV spreadsheet files are the most convenient way to collect data for the initial creation of flashcards.
  
Once one starts organizing, structuring and adding information to this raw data, however, CSV files become limiting.  

For instance, flashcards for words can be structured into word frequency of usage, subject area of word as a thesaurus does.

Flashcards can also be transformed into multiple choice questions for quizzes.

Data is added to flashcards when tracking performance and mastery of the facts of flashcards.
Self-rating of mastery or a quiz score, can be added to a flashcard. 
  
A relational database allows for more facile structuring of data.  
  
We start with the flashcard data and basic descriptive information.   

### Flashcards, Decks, and Descriptors

In its most elemental form, flashcards are basically lists of points on a given topic to learn.
A list item basically looks like this:

HEAD - DESCRIPTION

In a word list of vocabulary a list item looks like this:  

bird - นก 

A cross-language meaning map. This is transformed into a flashcard
by putting the left side on the front of a flashcard and the right side on the back. 
A single flashcard is one card in a deck of flashcards, for example animal flashcards.
  
### Different Approaches to Loading Flashcards

I have always preferred having all the CSV flashcard files in a sub-directory 
loaded when the flashcard app starts.

Then as a learner views the cards and self-rates their mastery or takes a quiz 
and gets a score that indicates mastery, these ratings and scores can be written 
to a transaction log with a time-stamp. Later, this raw data can be repurposed
to achieve different objectives. The raw transaction log allows for flexibility 
and renconfiguration and is non-commital towards eventual app functionalities. 

However, other approaches are possible. For instance, flashcard deck CSV files 
can be listed in a config file for loading at the beginning of a session.

The flashcard CSV files in a special CSV file folder can also be automatically loaded
into a SQLite database by the app. In the first session the database and tables are created and any existing 
flashcard deck CSV files are processed and loaded into the database. In subsequent sessions
any new flashcard deck CSV files are added to the database. 

Each flashcard has four fields added to the database: 'deck name' which is the name of the CSV file,
card front, card back, and a timestamp.
