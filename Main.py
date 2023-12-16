def file_to_lines(file):
    """
    Reads the content of a file and returns a list of lines.

    Parameters:
    - file (str): The path to the file.

    Returns:
    - list: A list of strings representing the lines in the file.
    """
    with open(file, 'r') as f:
        file_content = f.read()
        return file_content.split("\n")

def line_to_words(line):
    """
    Splits a line into a list of words.

    Parameters:
    - line (str): A string representing a line of words.

    Returns:
    - list: A list of words.
    """
    words = line.split(" ")
    return words

def fill_in_madlib(madlib):
    """
    Fills in the blanks in a list of lines containing {blanks}.

    Parameters:
    - madlib (list): A list of strings representing lines with {blanks}.

    Returns:
    - list: A list of strings representing lines with filled-in values.
    """
    filled_madlib = []

    # iterates through each line stored in 'madlib'
    for i in range(len(madlib)):
        words = line_to_words(madlib[i])
        # iterates through each word in current line
        for j in range(len(words)):
            word = words[j]
            # if '{blank}' is in a word, ask user for input and store in 'madlib'
            if "{" in word:
                pre = word[0:word.index("{")]
                post = word[word.index("}")+1:]
                blank_name = blank_toString(word)
                new_word = input(f"{blank_name}: ")
                words[j] = f"{pre}{new_word}{post}"
        filled_madlib.append(" ".join(words))
    
    return filled_madlib

def blank_toString(blank):
    """
    Converts a string inside curly braces to a formatted string.

    Parameters:
    - blank (str): A string inside curly braces.

    Returns:
    - str: The formatted string.
    """
    string = blank[blank.index("{")+1:blank.index("}")].capitalize()
    if "_" in string:
        string = string.replace('_', ' ')
    
    return string

def filename_toString(filename):
    """
    Converts a filename to a formatted string.

    Parameters:
    - filename (str): The filename with '.txt'.

    Returns:
    - str: The formatted filename.
    """
    string = filename[0:filename.index('.')].upper()
    if "_" in string:
        string = string.replace('_', ' ')

    return string

def print_madlib(madlib):
    """
    Prints a filled-in madlib.

    Parameters:
    - madlib (list): A list of strings representing filled-in lines.
    """
    print("\n-------------- COMPLETED MADLIB ---------------\n")
    for line in madlib: print(line)

def print_list_of_madlibs(file_list):
    """
    Prints a list of available madlibs for user selection.

    Parameters:
    - file_list (list): A list of filenames.
    """
    for i in range(len(file_list)):
        file = file_list[i]
        file_name = filename_toString(file)
        print(f"[{i+1}] {file_name}")

def get_valid_input(max_value):
    """
    Gets valid user input within a specified range.

    Parameters:
    - max_value (int): The maximum allowed value.

    Returns:
    - int: The user input as an index.
    """
    while True:
        try:
            user_input = int(input("Enter Mad Lib number: "))
            if 1 <= user_input <= max_value:
                return user_input - 1
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a number.")

    

files = ["christmas.txt", "star_wars.txt", "space_shuttle.txt", "sports.txt"]
game_loop = True

# game loop
while (game_loop):
    print("=================== MAD LIBS ==================\n")

    print("Which MadLib would you like to fill in?")
    print_list_of_madlibs(files)
    files_index = get_valid_input(len(files))
    selected_madlib = file_to_lines(files[files_index]) # stored as list of lines

    print("\n--------------- FILL IN BLANKS ----------------\n")

    complete_madlib = fill_in_madlib(selected_madlib)
    print_madlib(complete_madlib)

    print("\n===============================================\n")

    # ask user to continue game, only stops loop if user inputs 'N'
    if input("Want to complete another MadLib? ('Y' or 'N'): ").upper() == "N":
        game_loop = False

    print("\n\n")