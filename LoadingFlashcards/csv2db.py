import csv
import os
import sqlite3


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite version {sqlite3.version}")
    except sqlite3.Error as e:
        print(e)

    return conn


def read_csv_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        data = [row for row in csv_reader]
    return data

def create_flashcard_data_table(conn, cursor, csv_file_path):
    table_name = 'flashcard_data'
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
    table_exists = cursor.fetchone()
    csv_data = read_csv_file(csv_file_path)
    headings = csv_data[0]
    if table_exists:
        print(f"The table '{table_name}' already exists.")
    else:
        cursor.execute(f"CREATE TABLE {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT)") 
        cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN deck TEXT")
        for heading in headings:
            if heading.lower() == 'id':
                continue
            cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {heading} TEXT")
        
    cursor.execute(f"BEGIN TRANSACTION")
    for row in csv_data[1:]:
        cursor.execute(f"INSERT INTO {table_name} ({', '.join(headings)}, deck) VALUES ({', '.join(['?']*len(headings))}, ?)",
                       (*row, os.path.basename(csv_file_path)))
    cursor.execute(f"COMMIT")
    print(f"The table '{table_name}' has been created and populated with data from {csv_file_path}.")

def create_flashcard_data_database(csv_directory):
    database_file = os.path.join(csv_directory, 'flashcard_data', 'flashcard_data.db')
    os.makedirs(os.path.dirname(database_file), exist_ok=True)
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()
    create_flashcard_data_table(cursor, cursor, os.path.join(csv_directory, 'flashcard_data.csv'))
    conn.commit()
    conn.close()
    print(f"The database '{database_file}' has been created.")

# Example usage:

def main():
    csv_file_path = 'pali_sentences.csv'
    csv_data = read_csv_file(csv_file_path)
    
    db_filename = 'flashcard_data/flashcard_data.db'
    os.makedirs(os.path.dirname(db_filename), exist_ok=True)
    conn = create_connection(db_filename) 
    cursor = conn.cursor()
    create_flashcard_data_table(conn, cursor, csv_file_path)
    #insert_flashcard_data(cursor, csv_data, csv_file_path)
    conn.commit()
    conn.close()
    
if __name__ == '__main__':
    main()    
