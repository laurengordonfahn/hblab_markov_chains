from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    full_text = open(file_path).read()

    return full_text


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    text_list = text_string.split()

    chains = {}

    text_len = len(text_list)
    for word_index in range(text_len -1 ):
        bi_gram = (text_list[word_index], text_list[word_index +1])
        if word_index + 2 < text_len:
            chains.setdefault(bi_gram, []).append(text_list[word_index + 2])
        else:
            chains.setdefault(bi_gram, [None])


    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    keys_list = chains.keys()
    random_key = choice(keys_list)

    text_list = []
    while random_key[1] != None:
        text_list.append(random_key[0])

        random_list_value = choice(chains[random_key])

        random_key = (random_key[1], random_list_value)

    text_list.append('am.')
    return " ".join(text_list)



input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)
# print input_text
# # Get a Markov chain
chains = make_chains(input_text)
print chains

# # Produce random text
random_text = make_text(chains)

print random_text

