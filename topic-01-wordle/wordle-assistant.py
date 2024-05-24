# world_assistant
"""
create a function guess(data) that will create a wordle guess based on data

    word = guess(state)

    where state = [
      "-a:-b:-c:+d:*e",
      "-f:-g:-h:-i:+j"  
    ]

"""

with open("words.txt", "r") as f:
    words = f.readlines()
words = [w.strip() for w in words]
words = [w for w in words if len(w) == 5]

rejected_words = [
    "aaron", "irish"
]

words = [w for w in words if w not in rejected_words]

def guess(state):
    excluded = []
    included = []
    correct = []
    letters = []
    for word in state:
        items = word.split(":")
        for t in [s[1] for s in items if s[0] == "-"]:
            excluded.append(t)
        for t in [s[1] for s in items if s[0] in "+*"]:
            included.append(t)
        k = 0
        for item in items:
            if item[0] == "*":
                correct.append([item[1],k])
            k = k + 1
    guesses = words[:]
    for item in correct:
        print(item)
    for letter in included:
        guesses = [g for g in guesses if letter in g]
    for letter in excluded:
        guesses = [g for g in guesses if letter not in g]
    for letter, k in correct:
        print(letter, k)
        print("len guesses = ", len(guesses))
        guesses = [g for g in guesses if letter == g[k]]
        print("len guesses = ", len(guesses))
        print(guesses)
    return guesses[0]


def test_word_list_exists():
    print("word list exists")
    global words
    assert type(words) is list
    for item in words:
        assert type(item) is str
        assert len(item) == 5


def test_first_guess():
    print("guess function returns a reasonable first guess")
    state = []
    word = guess(state)
    assert type(word) is str
    assert len(word) == 5


def test_guess_with_included_letters():
    print("guess function respects included letters")
    state = ["-a:-b:-c:-d:-e", "-f:-g:-h:-i:+j"]
    word = guess(state)
    print(word)
    assert "j" in word
    state = ["-a:-b:-c:+d:+e", "-f:-g:-h:-i:+j"]
    word = guess(state)
    print(word)
    for letter in "dej":
        assert letter in word


def test_guess_with_excluded_letters():
    print("guess function respects excluded letters")
    state = ["-a:-b:-c:+d:+e", "-f:-g:-h:-i:+j"]
    word = guess(state)
    print(word)
    for letter in "dej":
        assert letter in word
    for letter in "a":
        assert letter not in word
    state = ["-h:+e:-l:-i:-o", "*j:-a:*d:+e:+d"]
    word = guess(state)
    print(word)
    for letter in "dej":
        assert letter in word
    for letter in "ak":
        assert letter not in word


def test_guess_with_positional_letters():
    print("guess function respects excluded letters")
    # word = "paged"
    state = ["-l:+a:*g:+e:-r", "-f:-l:-i:*e:-r"]
    word = guess(state)
    print(word)
    assert word[2] == "g"
    assert word[3] == "e"
    state = ["-l:+a:*g:+e:-r", "-f:-l:-i:*e:-r", "*p:*a:-n:+d:+a"]
    word = guess(state)
    print(word)
    assert word[2] == "g"
    assert word[3] == "e"
    assert word == "paged"

def test_actual_game():
    state = []
    word = guess(state)
    print(word)
    state = ["-a:-b:-a:-c:-k"]
    word = guess(state)
    print(word)
    state = ["-a:-b:-a:-c:-k", "-d:-e:-e:-d:+s"]
    word = guess(state)
    print(word)
    state = ["-a:-b:-a:-c:-k", "-d:-e:-e:-d:+s", "-f:+i:-l:-l:+s"]
    word = guess(state)
    print(word)
    state = ["-a:-b:-a:-c:-k", "-d:-e:-e:-d:+s", "-f:+i:-l:-l:+s", "-g:+i:-p:*s:-y","+h:-o:*i:*s:-t"]
    word = guess(state)
    print(word)

if __name__ == "__main__":
    print("HELLO!")
    test_first_guess()
    test_word_list_exists()
    test_guess_with_included_letters()
    test_guess_with_excluded_letters()
    test_guess_with_positional_letters()
    test_actual_game()
    print("done.")
