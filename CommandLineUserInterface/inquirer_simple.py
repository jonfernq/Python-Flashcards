import random
import inquirer

def random_number_loop():
    while True:
        msg = ('\n' *12) + (' ' * 30) + str(random.randint(1, 100)) + "\n\n\n" + (' ' * 30) + "type anything to continue" +  "\n" + (' ' * 30) + "type 'x' to exit" + "\n"  
        questions = [
            inquirer.Text('input', message=msg) 
        ]
        answer = inquirer.prompt(questions)['input']
        if answer == 'x': 
            break            
if __name__ == '__main__':
    random_number_loop()
