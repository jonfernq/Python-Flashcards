## Loading Flashcards 

Flashcards can be stored and loaded into an app in various ways.

In most flashcard apps (e.g. Anki) one opens a file dialogue and loads a deck of flashcards directly from a file.

However, manual loading of each flashcard deck from a file each time 
is not suitable for a more wholistic approach to learning.

For learning all the words of the Academic Word List (AWL)
over multiple decks and multiple sessions, pre-loading many related decks makes more sense. 

Pre-loading decks once and for all allows for reorganization of decks based on mastery.

Flashcards can be presented as a prioritized list for learning.
Flashcards with a low-level of mastery are given a high priority and high-level of mastery
are given a low priority. 

Here are some ways to pre-load decks: 

- Automatically loaded from CSV files from sub-directories each time the app starts.
- Manually loaded either by app creator or user from CSV files into a SQLite database. 
- Automatically loaded from a list in a config file. 
- And so on... 

Before some code exploring these different ways is presented, 
some general ideas about flashcard data and its repurposing for different 
learning approaches will be outlined. 

### Flashcard Data-Gathering & Restructuring

CSV spreadsheet files are the most convenient way to collect data for the initial creation of flashcards.

And, it is sometimes best to keep it simple, putting a single deck of around 20 flashcards to be studied at a single time in a CSV file for instance. The name of the deck is simply the name of the CSV file, and the fields of the CSV file could be as simple as two fields: 'front' and 'back', or 'question' and 'answer'. 
  
Once one starts organizing, structuring and adding supplorting information, however, CSV files become limiting. A relational database allows this extra flashcard metadata to be added in additional database tables without modifying the flashcard table itself. 

There are many ways that flashcards can be structured, flashcards for words, for instance, can be structured into word frequency of usage, subject area of word as a thesaurus does.

Flashcards can also be transformed into multiple choice questions for quizzes.

Data is also added to flashcards when tracking performance and mastery of the facts of flashcards.
For instance, self-rating of mastery or a quiz score, can be added to a flashcard. 
  
A relational database allows for more facile structuring of data.  Here, we start with the flashcard data and basic descriptive information.   

### Flashcards, Decks, and Descriptors

In its most elemental form, flashcards are basically lists of points on a given topic to learn.
A list item basically looks like this:

FRONT    - BACK
QUESTION - ANSWER 
HEAD     - DESCRIPTION

In a word list of vocabulary a list item looks like this:  

bird - ?????? 

A cross-language meaning map. This is transformed into a flashcard
by putting the left side on the front of a flashcard and the right side on the back. 
A single flashcard is one card in a deck of flashcards, for example animal flashcards.
  
### Different Approaches to Loading Flashcards

One approach is to have all the CSV flashcard files in a sub-directory 
loaded when the flashcard app starts.

Then as a learner views the cards and self-rates their mastery or takes a quiz 
and gets a score that indicates mastery, these ratings and scores can be written 
to a transaction log with a time-stamp. Later, this raw data can be repurposed
to achieve different objectives. The raw transaction log allows for flexibility 
and renconfiguration and is non-commital towards eventual app functionalities. 

However, other approaches are possible. For instance, flashcard deck CSV files 
can be listed in a config file for loading at the beginning of a session:

- [flashcards_fromconfig.py](https://github.com/jonfernq/Python-Flashcards/blob/main/LoadingFlashcards/flashcards_fromconfig.py)
- [config.json](https://github.com/jonfernq/Python-Flashcards/blob/main/LoadingFlashcards/config.json) 
- Flashcard CSV files: [Academic Word List (AWL)](https://github.com/jonfernq/Python-Flashcards/blob/main/LoadingFlashcards/awl_flashcard_1.csv), 
[Burmese location words](https://github.com/jonfernq/Python-Flashcards/blob/main/LoadingFlashcards/burmese_location_words.csv), 
[City Populations](https://github.com/jonfernq/Python-Flashcards/blob/main/LoadingFlashcards/city_populations.csv), 
[Country Populations](https://github.com/jonfernq/Python-Flashcards/blob/main/LoadingFlashcards/country_populations.csv), 
[Pali Sentences](https://github.com/jonfernq/Python-Flashcards/blob/main/LoadingFlashcards/pali_sentences.csv), 
[Short Russian Words and Letters](https://github.com/jonfernq/Python-Flashcards/blob/main/LoadingFlashcards/short_russian_words.csv), 
[Simple Thai Verbs](https://github.com/jonfernq/Python-Flashcards/blob/main/LoadingFlashcards/simple_thai_verbs.csv), 
[Thai Location Words](https://github.com/jonfernq/Python-Flashcards/blob/main/LoadingFlashcards/thai_location_words.csv). 

The flashcard CSV files in a special CSV file folder can also be automatically loaded
into a SQLite database by the app. In the first session the database and tables are created and any existing 
flashcard deck CSV files are processed and loaded into the database. In subsequent sessions
any new flashcard deck CSV files are added to the database. 

Each flashcard has four fields added to the database: 'deck name' which is the name of the CSV file,
card front, card back, and a timestamp:

- [csv2db.py](https://github.com/jonfernq/Python-Flashcards/blob/main/LoadingFlashcards/csv2db.py): Creates database and table for CSV file, checking to see if it already exists first, then reading CSV data into it. As simple example and test uses [pali_sentences.csv](https://github.com/jonfernq/Python-Flashcards/blob/main/LoadingFlashcards/pali_sentences.csv) 

In this example, the read_csv_file() function reads the CSV file into a list of lists using the csv module. The create_flashcard_table() function then creates a SQLite database file called flashcard_data.db in a sub-directory called flashcard_data, creates a table with the same name as the CSV file (minus the file extension) and with columns named after the CSV headings, and inserts the CSV data into the table.

Note that in this example, the function assumes that the first row of the CSV file contains the column headings. Also, the function assumes that the CSV data has already been validated and cleaned, and does not perform any additional data validation or cleaning.
