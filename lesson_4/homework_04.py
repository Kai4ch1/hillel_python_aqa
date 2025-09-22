import re

adventures_of_tom_sawer = """ \
Tom gave up the brush with reluctance in his  face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""


def tasks_1_2_3():
    print("Tasks 1, 2, and 3:")

    replace_break_string_with_space = adventures_of_tom_sawer.replace("\n", " ")
    four_dots_replace = replace_break_string_with_space.replace("...."," ")
    double_space_replace = re.sub(r'\s+', " ", four_dots_replace)

    print(f"Edited text after tasks 1, 2, and 3: {double_space_replace}")

def task_4():
    print("\n Task 4:")

    both_lower_and_upper_h = re.findall(r"h", adventures_of_tom_sawer, re.IGNORECASE)

    print(f"The count of 'h' and 'H' both is: {len(both_lower_and_upper_h)}")

def task_5():

    print("\n Task 5:")

    word_splitter = adventures_of_tom_sawer.split()
    word_counter = []

    for word in word_splitter:
        if word.istitle():
            word_counter.append(word)

    print(f"Words found: {word_counter}")
    print(f"The count of found words is: {len(word_counter)}")

def task_6():
    print("\n Task 6:")

    tom_finder = adventures_of_tom_sawer.find("Tom")
    tom_finder_second = adventures_of_tom_sawer.find("Tom", tom_finder + 1)
    print(f"The position of the second 'Tom' is: {tom_finder_second}")

def task_7():
    print("\n Task 7:")

    no_string_break = adventures_of_tom_sawer.replace("\n", " ")
    adventures_of_tom_sawer_sentences = no_string_break.split(".")
    print(f"The splitted sentences text is: {adventures_of_tom_sawer_sentences}")

def task_8():
    print("\n Task 8:")

    string_break = adventures_of_tom_sawer.replace("\n", " ")

    clean_text = string_break.replace("....", " ")
    sentence_splitter = clean_text.split(".")
    cleaned_sentences = []

    for sentence in sentence_splitter:
        if sentence.strip():
            cleaned_sentences.append(sentence.strip())

    forth_sentence = cleaned_sentences[3]

    print(f"The lowercased 4th sentence is: {forth_sentence.lower()}")

def task_9():
    print("\n Task 9:")

    success = True
    if "By the time" in adventures_of_tom_sawer:
        print(f"The phrase 'By the time' was found correctly: {success}")

def task_10():
    print("\n Task 10:")

    string_break = adventures_of_tom_sawer.replace("\n", " ")

    clean_text = string_break.replace("....", " ")
    sentence_splitter = clean_text.split(".")
    cleaned_sentences = []

    for sentence in sentence_splitter:
        if sentence.strip():
            cleaned_sentences.append(sentence.strip())

    last_sentence_id = cleaned_sentences[-1]
    last_sentence = last_sentence_id.strip()
    print(f"The lowercased last sentence is: {last_sentence}")



if __name__ == "__main__":
    tasks_1_2_3()
    task_4()
    task_5()
    task_6()
    task_7()
    task_8()
    task_9()
    task_10()
