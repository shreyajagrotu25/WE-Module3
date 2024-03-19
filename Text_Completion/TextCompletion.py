import random

def generate_text(text_corpus, start_word, output_length):
    """
    Generates text of a given length using a Markov chain model based on a sample corpus.

    Args:
        text_corpus: (str) The text corpus to use for generating text.
        start_word: (str) The word to start the generated text.
        output_length: (int) The desired length of the generated text.

    Returns:
        (str) The generated text.
    """

    # Preprocess the text corpus
    words = text_corpus.lower().split()

    # Function to build transitions dictionary recursively
    def build_transitions(remaining_words):
        if not remaining_words:
            return {}
        current_word = remaining_words[0]
        next_word = remaining_words[1] if len(remaining_words) > 1 else None
        transitions = build_transitions(remaining_words[1:])
        transitions[current_word] = transitions.get(current_word, {})
        transitions[current_word][next_word] = transitions[current_word].get(next_word, 0) + 1
        return transitions

    # Build the transitions dictionary
    transitions = build_transitions(words)

    # Function to generate text recursively with basic functionality
    def generate_text_helper_basic(current_word, remaining_length):
        if remaining_length == 0 or current_word not in transitions:
            return []
        next_word_distribution = transitions[current_word]
        next_word = random.choices(list(next_word_distribution.keys()), weights=list(next_word_distribution.values()))[0]
        return [current_word] + generate_text_helper_basic(next_word, remaining_length - 1)

    # Generate the text
    text = generate_text_helper_basic(start_word, output_length)
    return ' '.join(text)

# Test Case 1: Basic Functionality
def test_case_1():
    start_word = "the"
    output_length = 5
    text = generate_text(text_corpus, start_word, output_length)
    print(f"Test Case 1: Output - {text}")

# Test Case 2: Handling Unseen Words
def test_case_2():
    start_word = "hello"  # Not present in the corpus
    output_length = 10
    text = generate_text(text_corpus, start_word, output_length)
    print(f"Test Case 2: Output - {text} (expected: empty string)")

# Test Case 3: Empty Corpus
def test_case_3():
    start_word = "any"
    output_length = 5
    text = generate_text("", start_word, output_length)
    print(f"Test Case 3: Output - {text} (expected: empty string)")

# Sample text corpus
text_corpus = "The quick brown fox jumps over the lazy dog."

# Run the test cases
test_case_1()
test_case_2()
test_case_3()
