import re


def text_split(text_orig):
    """Returns list of centences
       Parameters:
       text_orig (str): Origin text
    """

    text_splitted = text_orig.split("\n")
    text_splited = []
    for t in range(len(text_splitted)):
        if len(text_splitted[t]) > 0:
            text_splited.append(text_splitted[t])
    return text_splited


def text_normalize(text_norm):
    """Returns normalized text
       Parameters:
       text_norm (list): List of sentences
    """

    for text_sentence in range(len(text_norm)):
        if text_norm[text_sentence].startswith("\t") == True:
            text_norm[text_sentence] = text_norm[text_sentence].replace("\t", "")
            text_norm[text_sentence] = text_norm[text_sentence].capitalize()
            if text_norm[text_sentence].count(".") > 1:
                sentence_splited = text_norm[text_sentence].split(".")
                for i in range(len(sentence_splited)):
                    if sentence_splited[i] != " " and sentence_splited[i] != "":
                        sentence_splited[i] = sentence_splited[i].strip().capitalize() + "."
                text_norm[text_sentence] = ' '.join(sentence_splited)
                text_norm[text_sentence] = text_norm[text_sentence].strip()
                text_norm[text_sentence] = "\t" + text_norm[text_sentence]
            else:
                text_norm[text_sentence] = text_norm[text_sentence].strip()
                text_norm[text_sentence] = "\t" + text_norm[text_sentence]
        else:
            text_norm[text_sentence] = text_norm[text_sentence].capitalize()
    return text_norm


def more_setences(text_extended):
    """Returns extended sentences with last words from each sentence
       Parametrs:
       text_extend (list): Normalized text
    """

    for ext_sentense in range(len(text_extended)):
        if text_extended[ext_sentense].count(".") > 1:
            sentence_splited = text_extended[ext_sentense].split(".")
            ext_words = []
            for i in range(len(sentence_splited)):
                if sentence_splited[i] != " " and sentence_splited[i] != "":
                    ext_words.append(sentence_splited[i].split(" ")[-1])
            text_extended[ext_sentense] = '. '.join(sentence_splited)
            ext_sentence = ""
            for i in ext_words:
                ext_sentence = ext_sentence + i + " "
            ext_sentence = ext_sentence.strip()
            ext_sentence = ext_sentence.capitalize()
            text_extended[ext_sentense] = text_extended[ext_sentense] + ext_sentence + "."
        else:
            ext_word = text_extended[ext_sentense].split(" ")[-1]
            text_extended[ext_sentense] = text_extended[ext_sentense] + " " + ext_word.capitalize()
    return text_extended


def text_misspell(text_misspelling):
    """Returns corrected sentences
       Parameters:
       text_misspelling (list): Extended text
    """

    for misspel_sentense in range(len(text_misspelling)):
        text_misspelling[misspel_sentense] = re.sub(r'\siz\s', ' is ', text_misspelling[misspel_sentense])
        text_misspelling[misspel_sentense] = re.sub(r'\Wiz\W', ' "iZ"', text_misspelling[misspel_sentense])
    return text_misspelling


def count_whitespaces(misspell_sentences):
    """Returns number of whitespaces and final text
       Parametrs:
       misspell_sentences (list): corrected sentences
    """

    count = 0
    text_result = ""
    for ms in range(len(misspell_sentences)):
        for i in misspell_sentences[ms]:
            if (i.isspace()):
                count += 1
        text_result = text_result + misspell_sentences[ms] + "\n"
    print("Number of whitespaces is:", count)
    print("\nTransformed text is:\n\n", text_result)
