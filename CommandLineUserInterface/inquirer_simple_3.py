import inquirer

# ask if user is ready
ready = inquirer.prompt([inquirer.Confirm('ready', message="Are you ready?")])

if ready['ready']:
    # prompt the user for their name
    questions = [
        inquirer.Text("name", message="What is your name?")
    ]
    answers = inquirer.prompt(questions)

    # greet the user
    print("Hello,", answers["name"])
else:
    # say goodbye
    print("Ok, then try again later. Goodbye.")
