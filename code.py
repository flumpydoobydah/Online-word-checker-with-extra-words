def load_words(file_path):
    """
    Load words from a text file into a list.

    Parameters:
    file_path (str): The path to the text file containing words.

    Returns:
    list: List of words loaded from the file.
    """
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words


def find_words(word_list, letters, search_type='start'):
    """
    Search for words in the word_list that start with or contain the specified letters.

    Parameters:
    word_list (list): List of words to search.
    letters (str): Letters to search for (1 to 10 letters).
    search_type (str): Type of search ('start' or 'contain').

    Returns:
    list: List of words that match the specified search criteria.
    """
    # Check if letters length is between 1 and 10
    if (len(letters) < 1 or len(letters) > 10) and letters.lower() != 'exit':
        raise ValueError("letters must be between 1 and 10 characters long")

    # Filter words based on search type
    if search_type == 'start':
        result = [word for word in word_list if word.startswith(letters)]
    elif search_type == 'contain':
        result = [word for word in word_list if letters in word]
    else:
        raise ValueError("search_type must be either 'start' or 'contain'")

    return result


# Load words from the file
word_file_path = 'words.txt'  # Ensure this file is in the correct format and location
words = load_words(word_file_path)

while True:
    # Taking user input
    letters = input("Enter the letters (1 to 10 characters) or type 'exit' to quit: ")
    if letters.lower() == 'exit':
        print("Exiting the program.")
        break

    search_type = input("Enter the search type ('start' or 'contain'): ")

    try:
        matched_words = find_words(words, letters, search_type)
        print("Words that {} with '{}':".format('start' if search_type == 'start' else 'contain', letters))
        print(matched_words)
    except ValueError as e:
        print(e)
