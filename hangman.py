def print_status(current, penalty):
    print(current + " / " + str(penalty) + " penalty\n")

def input_check(user_input):
    if not user_input:
        print("please enter a letter or a word\n")
        return(True)        
    for c in user_input:
        if (c.isalpha() == 0 and c != "-"):
            print("please enter a letter or a word\n")
            return(True)
    return (False)

def check_letter(letter, word, current):
    i = 0
    count = 0
    new = ""
    while i < len(word):
        if word[i] == letter:
            new += letter
            count += 1
        else:
            new += current[i]
        i += 1
    if count > 0:
        print("found " + str(count) + " '" + letter +"'")
    else:
        print("No '" + letter + "' found")
    return (new)

def check_game_over(current, word, penalty):
    if penalty > 12:
        print("penalty limit attained, game over")
        return (True)
    if current == word:
        print(current + ": correct guess - " + str(penalty) + " penalties")
        return (True)
    return (False)

def main():
    word = "superman"
    word = word.lower()
    current = ""
    penalty = 0

    for c in word:
        current += "_"
    while True:
        print_status(current, penalty)
        user_input = input("$>").lower()
        stop = input_check(user_input)
        if stop:
            continue
        if len(user_input) == 1:
            new = check_letter(user_input, word, current)
            if new != current:
                current = new
            else:
                penalty += 1
        else:
            if user_input == word:
                current = user_input
            else:
                print(user_input + ": incorrect guess")
                penalty += 5
        if check_game_over(current, word, penalty):
            return ()

# Using the special variable 
# __name__
if __name__=="__main__":
    main()