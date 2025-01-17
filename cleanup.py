# Contains all functions that deal with stop word removal.
import re
from document import Document


def remove_symbols(text_string: str) -> str:
    """
    Removes all punctuation marks and similar symbols from a given string.
    Occurrences of "'s" are removed as well.
    :param text_string:
    :return:
    """
    text_string = re.sub(r"[^\w\s']", ' ', text_string)  # Remove all punctuation except apostrophes
    text_string = re.sub(r"\s+", ' ', text_string)  # Replace multiple spaces with a single space
    text_string = text_string.replace("'s", '')  # Remove 's
    return text_string.strip().lower()


def is_stop_word(term: str, stop_word_list: list[str]) -> bool:
    """
    Checks if a given term is a stop word.
    :param stop_word_list: List of all considered stop words.
    :param term: The term to be checked.
    :return: True if the term is a stop word.
    """
    return term.lower() in stop_word_list


def remove_stop_words_from_term_list(term_list: list[str]) -> list[str]:
    """
    Takes a list of terms and removes all terms that are stop words.
    :param term_list: List that contains the terms
    :return: List of terms without stop words
    """
    # Hint:  Implement the functions remove_symbols() and is_stop_word() first and use them here.
    # TODO: Implement this function. (PR02)
    cleaned_terms = [remove_symbols(term) for term in term_list]
    return [term for term in cleaned_terms if not is_stop_word(term, cleaned_terms)]


def filter_collection(collection: list[Document]):
    """
    For each document in the given collection, this method takes the term list and filters out the stop words.
    Warning: The result is NOT saved in the documents term list, but in an extra field called filtered_terms.
    :param collection: Document collection to process
    """
    # Hint:  Implement remove_stop_words_from_term_list first and use it here.
    # # TODO: Implement this function. (PR02)
    # raise NotImplementedError('To be implemented in PR02')
    for doc in collection:
        doc.filtered_terms = remove_stop_words_from_term_list(doc.terms)


def load_stop_word_list(raw_file_path: str) -> list[str]:
    """
    Loads a text file that contains stop words and saves it as a list. The text file is expected to be formatted so that
    each stop word is in a new line, e. g. like englishST.txt
    :param raw_file_path: Path to the text file that contains the stop words
    :return: List of stop words
    """
    # # TODO: Implement this function. (PR02)
    # raise NotImplementedError('To be implemented in PR02')
    global STOP_WORDS
    with open(raw_file_path, 'r', encoding='utf-8') as file:
        STOP_WORDS = [line.strip().lower() for line in file]
    return STOP_WORDS


def create_stop_word_list_by_frequency(collection: list[Document]) -> list[str]:
    """
    Uses the method of J. C. Crouch (1990) to generate a stop word list by finding high and low frequency terms in the
    provided collection.
    :param collection: Collection to process
    :return: List of stop words
    """
    # # TODO: Implement this function. (PR02)
    # raise NotImplementedError('To be implemented in PR02')
    term_frequency = {}
    low_thresh: int = 5
    high_thresh: int = 20

    for doc in collection:
        for term in doc['terms']:
            term = term.lower()
            if term in term_frequency:
                term_frequency[term] += 1
            else:
                term_frequency[term] = 1

    stop_words = [term for term, freq in term_frequency.items() if freq <= low_thresh or freq >= high_thresh]
    return stop_words
