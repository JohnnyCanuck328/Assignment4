def is_valid_file_name():
    '''()->str or None'''
    file_name = None
    try:
        file_name = input("Enter the name of the file: ").strip()
        f = open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name = None
    return file_name


def get_file_name():
    file_name = None
    while file_name == None:
        file_name = is_valid_file_name()
    return file_name


def clean_word(word):
    '''(str)->str
    Returns a new string which is lowercase version of the given word
    with special characters and digits removed

    The returned word should not have any of the following characters:
    ! . ? : , ' " - _ \ ( ) [ ] { } % 0 1 2 3 4 5 6 7 8 9 tab character and new-line character

    >>> clean_word("co-operate.")
    'cooperate'
    >>> clean_word("Anti-viral drug remdesivir has little to no effect on Covid patients' chances of survival, a study from the World Health Organization (WHO) has found.")
    'antiviral drug remdesivir has little to no effect on covid patients chances of survival a study from the world health organization who has found'
    >>> clean_word("1982")
    ''
    >>> clean_word("born_y1982_m08\n")
    'bornym'

    '''
    new_word = word.lower()
    for inc in ['!', '.', '?', ':', ',', '\'', '"', '-', '_', '\\', '(', ')', '[', ']', '{', '}', '%', '0', '1', '2',
                '3', '4', '5', '6', '7', '8', '9', '\t', '\n']:
        if (inc in new_word):
            new_word = new_word.replace(inc, " ")
    return (new_word)


def test_letters(w1, w2):
    '''(str,str)->bool
    Given two strings w1 and w2 representing two words,
    the function returns True if w1 and w2 have exactlly the same letters,
    and False otherwise

    >>> test_letters("listen", "enlist")
    True
    >>> test_letters("eekn", "knee")
    True
    >>> test_letters("teen", "need")
    False
    '''
    if (len(w1) == len(w2)):
        flag = True
        for inc in range(0, len(w1)):
            temp = w1[inc]
            y = w1.count(temp)
            x = w2.count(temp)
            if (y != x):
                flag = False
        return flag
    else:
        flag = False


def create_clean_sorted_nodupicates_list(s):
    '''(str)->list of str
    Given a string s representing a text, the function returns the list of words with the following properties:
    - each word in the list is cleaned-up (no special characters nor numbers)
    - there are no duplicated words in the list, and
    - the list is sorted lexicographicaly (you can use python's .sort() list method or sorted() function.)

    This function must call clean_word function.

    You may find it helpful to first call s.split() to get a list version of s split on white space.

    >>> create_clean_sorted_nodupicates_list('able "acre bale beyond" binary boat brainy care cat cater crate lawn\nlist race react cat sheet silt slit trace boat cat crate.\n')
    ['able', 'acre', 'bale', 'beyond', 'binary', 'boat', 'brainy', 'care', 'cat', 'cater', 'crate', 'lawn', 'list', 'race', 'react', 'sheet', 'silt', 'slit', 'trace']

    >>> create_clean_sorted_nodupicates_list('Across Europe, infection rates are rising, with Russia reporting a record 14,321 daily cases on Wednesday and a further 239 deaths.')
    ['', 'a', 'across', 'and', 'are', 'cases', 'daily', 'deaths', 'europe', 'further', 'infection', 'on', 'rates', 'record', 'reporting', 'rising', 'russia', 'wednesday', 'with']
    '''

    new_string = clean_word(s)
    new_string = list(new_string.split(" "))

    return_list = []
    for inc in new_string:
        if (inc == ''):
            None
        elif (inc not in return_list):
            return_list.append(inc)

    return (return_list)


def word_anagrams(word, wordbook):
    '''(str, list of str) -> list of str
    - a string (representing a word)
    - wordbook is a list of words (with no words duplicated)

    This function should call test_letters function.

    The function returs a (lexicographicaly sorted) list of anagrams of the given word in wordbook
    >>> word_anagrams("listen", wordbook)
    ['enlist', 'silent', 'tinsel']
    >>> word_anagrams("race", wordbook)
    ['acre', 'care']
    >>> word_anagrams("care", wordbook)
    ['acre', 'race']
    >>> word_anagrams("year", wordbook)
    []
    >>> word_anagrams("ear", wordbook)
    ['are', 'era']
    '''
    return_list = []
    for inc in wordbook:
        temp = test_letters(word, inc)
        if (temp == True):
            if (inc != word):
                return_list.append(inc)

    return return_list


def scrabble_anagrams(word, wordbook):
    '''(str, list of str) -> list of str
    - a string (representing a word)
    - wordbook is a list of words (with no words duplicated)

    Finds all anagrams (including itself)
    '''
    return_list = []
    for inc in wordbook:
        temp = test_letters(word, inc)
        if (temp == True):
            return_list.append(inc)

    return return_list


def count_anagrams(l, wordbook):
    '''(list of str, list of str) -> list of int

    - l is a list of words (with no words duplicated)
    - wordbook is another list of words (with no words duplicated)

    The function returns a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    Whenever a word in l is the same as a word in wordbook, that is not counted.

    >>> count_anagrams(["listen","care", "item", "year", "race", "ear"], wordbook)
    [3, 2, 3, 0, 2, 2]

    The above means that "listen" has 3 anagrams in wordbook, that "care" has 2 anagrams in wordbook ...
    Note that wordbook has "care", "race" and "acre" which are all anagrams of each other.
    When we count anagrams of "care" we count "race" and "acre" but not "care" itself.
    '''

    return_list = []
    for inc in l:
        temp = word_anagrams(inc, wordbook)
        temp = len(temp)
        return_list.append(temp)

    return return_list


def k_anagram(l, anagcount, k):
    '''(list of str, list of int, int) -> list of str

    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a  (lexicographicaly sorted) list of all the words
    in l that have exactlly k anagrams (in wordbook as recorded in anagcount)

    k_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2], 2)
    ['care', 'ear', 'race']
    '''

    zipped_lists = zip(l, anagcount)
    sorted_list = sorted(zipped_lists)
    pair = zip(*sorted_list)
    l, anagcount = [list(tuple) for tuple in pair]

    return_list = []
    for inc in range(len(anagcount)):
        if (anagcount[inc] == k):
            return_list.append(l[inc])
    return return_list


def max_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a (lexicographicaly sorted) list of all the words
    in l with maximum number of anagrams (in wordbook as recorded in anagcount)

    >>> max_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2])
    ['item', 'listen']
    '''

    zipped_lists = zip(l, anagcount)
    sorted_list = sorted(zipped_lists)
    pair = zip(*sorted_list)
    l, anagcount = [list(tuple) for tuple in pair]

    return_list = []
    max_value = 0
    for inc in range(len(anagcount)):
        if (anagcount[inc] > max_value):
            return_list = []
            return_list.append(l[inc])
            max_value = anagcount[inc]
        elif (anagcount[inc] == max_value):
            return_list.append(l[inc])
    return return_list


def zero_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a (lexicographicaly sorted) list of all the words
    in l with no anagrams
    (in wordbook as recorded in anagcount)

    >>> zero_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2])
    ['year']
    '''

    zipped_lists = zip(l, anagcount)
    sorted_list = sorted(zipped_lists)
    pair = zip(*sorted_list)
    l, anagcount = [list(tuple) for tuple in pair]

    return_list = []
    for inc in range(len(anagcount)):
        if (anagcount[inc] == 0):
            return_list.append(l[inc])
    return return_list


##############################
# main
##############################
wordbook = open("english_wordbook.txt").read().lower().split()
list(set(wordbook)).sort()

print("Would you like to:")
print("1. Analize anagrams in a text -- given in a file")
print("2. Get small help for Scrabble game")
print("Enter any character other than 1 or 2 to exit: ")
choice = input()

if choice == '1':
    file_name = get_file_name()
    rawtx = open(file_name).read()
    l = create_clean_sorted_nodupicates_list(rawtx)
    anagcount = count_anagrams(l, wordbook)

    print("\nOf all the words in your file, the following words have the most anagrams:")

    anagram_list = max_anagram(l, anagcount)
    print(anagram_list)
    print("Here are their anagrams:")
    for inc in anagram_list:
        print("The anagrams of", inc, "are", word_anagrams(inc, wordbook))

    print("Here are the word in your file that have no anagrams:")
    print(zero_anagram(l, anagcount))

    k_value = int(input(
        "Say you are interested if there is a word in your file that has exactly k anagrams\nEnter an integer for k: "))
    print("Here are the words in your file that have exactly", k_value, "anagrams", k_anagram(l, anagcount, k_value))

elif choice == '2':

    flag = False
    while flag == False:
        scrabble_letters = input("Enter the letters that you have, one after another with no space: ")
        x = " " in scrabble_letters
        if x == False:
            flag = True
        else:
            print("Please enter again with no spaces")

    flag = False
    while flag == False:
        word_len = input(
            "Would you like help forming a word with \n1. all these letters\n2. all but one of these letters?\n")
        if (word_len == "1"):
            num_ana = word_anagrams(scrabble_letters, wordbook)
            if num_ana == []:
                print("There is no word comprised of exactly these letters.")
            else:
                print("Here are the words comprised of exactly these letters:")
                print(num_ana)
            flag = True


        elif (word_len == "2"):
            print("The letters you gave us are:", scrabble_letters)
            for inc in range(0, len(scrabble_letters)):
                temp = list(scrabble_letters)
                temp.pop(inc)
                empty_string = ""
                for l_inc in range(0, len(temp)):
                    empty_string = empty_string + temp[l_inc]

                print("Without the letter in position", inc + 1, "we have the letters", empty_string)
                if ((scrabble_anagrams(empty_string, wordbook)) == []):
                    print("There is no word comprised of letters", empty_string)

                else:
                    print("Here are the words that are comprised of letters", empty_string)
                    print(scrabble_anagrams(empty_string, wordbook))

            flag = True

        else:
            print("That is not a valid option.")



else:
    print("Good bye")


