# world_assistant
'''
create a function guess(data) that will create a wordle guess based on data

    state = guess(state)

    where state = {
        "attempt": <number>.   # the number of guesses remaining
        "included": "abc",     # letters included in the word
        "correct": "ab...",    # letters in the correct location in the word
        "excluded": "zwq",     # letters that are not in the word
        "guesses": [ "...", 
                   "..." ].  # guesses so far
        "word":    "abcde",    # word that we are suggesting
    }

'''

with open("words.txt", "r") as f:
    words = f.readlines()
words = [w.strip() for w in words]
words = [w for w in words if len(w) == 5]


def guess(state):
    included = state["included"]
    guesses = words[:]
    for letter in included:
        guesses = [g for g in guesses if letter in g] 
        if len(guesses) < 10:
            print(guesses)
    state["word"] = guesses[0]
    return state


def test_guess_function_exists():
    print('guess function takes a state and returns a state')
    state = {
        "attempt": 1,  
        "included": "abc",     
        "correct": "ab...",    
        "excluded": "zwq",   
        "guesses": [ "...", 
                   "..." ],
        "word":    "hello",    
    }
    state = guess(state)
    assert type(state) is dict
    assert "attempt" in state
    assert type(state["attempt"]) is int
    assert "included" in state
    assert type(state["included"]) is str
    state_items = [
        ["attempt", int],
        ["included", str],
        ["correct", str],    
        ["excluded", str],
        ["guesses", list], 
        ["word", str]
    ]
    for item_name, item_type in state_items:
        assert item_name in state
        assert type(state[item_name]) is item_type
    for item in state["guesses"]:
        assert type(item) is str

def test_first_guess():
    print('guess function returns a reasonable first guess')
    state = {
        "attempt": 1,  
        "included": "",     
        "correct": "",    
        "excluded": "",   
        "guesses": [ ],
        "word": None,    
    }
    state = guess(state)
    assert type(state["word"]) is str
    assert len(state["word"]) == 5

def test_guess_with_included_letters():
    print('guess function respects included letters')
    state = {
        "attempt": 1,  
        "included": "ab",     
        "correct": "",    
        "excluded": "",   
        "guesses": [ ],
        "word": None,    
    }
    included = state["included"]
    state = guess(state)
    assert state["included"] == included
    word = state["word"]
    for letter in included:
        assert letter in word
    state = {
        "attempt": 1,  
        "included": "decal",     
        "correct": "",    
        "excluded": "",   
        "guesses": [ ],
        "word": None,    
    }
    included = state["included"]
    state = guess(state)
    assert state["included"] == included
    word = state["word"]
    print("included = ", included, ", guess = ", word)
    for letter in included:
        assert letter in word

def test_word_list_exists():
    print("word list exists")
    global words
    assert type(words) is list
    for item in words:
        assert type(item) is str
        assert len(item) == 5

if __name__ == "__main__":
    test_guess_function_exists()
    test_first_guess()
    test_word_list_exists()
    test_guess_with_included_letters()
    print("done.")