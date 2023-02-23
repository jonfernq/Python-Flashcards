import inquirer

# print message to the console
print("Welcome to the program!")

# define the question
questions = [
    inquirer.Text("name", message="What is your name?")
]

# prompt the user for input
answers = inquirer.prompt(questions)

# print the user's name
print("Hello,", answers["name"])
