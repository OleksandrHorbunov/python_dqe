from newsfeedfromfile import WriteFromFile
import csv
from datetime import datetime
default_path_to_file = "news_feed.txt"


class WriteToCsv:
    def __init__(self):
        self.k = ""
        self.wc_fn = "wc" + datetime.now().strftime("%Y%m%d%H%M%S")
        self.lc_fn = "lc" + datetime.now().strftime("%Y%m%d%H%M%S")
        self.lc_header = ["letter", "count_all", "count_uppercase", "percentage"]

    def wordcount(self, word_dict):
        """
        Creates and writes word-number to csv file with name pattern wcYYYYmmddHms
        :param word_dict: takes a dictionary to be written
        :return: a message that file is ready
        """
        with open(self.wc_fn, 'w', newline='') as f:
            writer = csv.writer(f, delimiter="-", quoting=csv.QUOTE_ALL)
            for self.k in word_dict.keys():
                wc_row = [self.k, word_dict[self.k]]
                writer.writerow(wc_row)
        return print(f"{self.wc_fn} csv file is ready")

    def lettercount(self, letter_dict):
        """
        Creates and writes letter, count_all, count_uppercase, percentage to csv file with name pattern lcYYYYmmddHms
        :param letter_dict: takes a dictionary to be written
        :return: a message that file is ready
        """
        with open(self.lc_fn, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_ALL)
            writer.writerow(self.lc_header)
            for self.k in letter_dict.keys():
                lc_row = [self.k, letter_dict[self.k][0], letter_dict[self.k][1], letter_dict[self.k][2]]
                writer.writerow(lc_row)
        return print(f"{self.lc_fn} csv file is ready")


class WordLetterCount:
    def cleartext(self, e_word):
        """
        Clears text from uncountable characters
        :param e_word: line
        :return: cleared line
        """
        c_word = e_word.replace("------->", "")
        c_word = c_word.replace("<-------", "")
        c_word = c_word.replace(".", "")
        c_word = c_word.replace(",", "")
        c_word = c_word.replace(":", "")
        return c_word.strip()

    def dowordcount(self, lines):
        """
        Counts words in a text
        :param lines: list of lines
        :return: dictionary word-count
        """
        dict = {}
        for i in range(len(lines)):
            if lines[i].count(" ") > 0:
                splitted_lines = lines[i].split(" ")
                for x in range(len(splitted_lines)):
                    splitted_lines[x] = self.cleartext(splitted_lines[x]).lower()
                    if len(splitted_lines[x]) > 2:
                        if splitted_lines[x].isalpha():
                            if splitted_lines[x] in dict:
                                dict[splitted_lines[x]] = dict[splitted_lines[x]] + 1
                            else:
                                dict[splitted_lines[x]] = 1
            else:
                lines[i] = self.cleartext(lines[i]).lower()
                if len(lines[i]) > 2:
                    if lines[i].isalpha():
                        if lines[i] in dict:
                            dict[lines[i]] = dict[lines[i]] + 1
                        else:
                            dict[lines[i]] = 1
        return dict

    def dolettercount(self, t_lines):
        """
        Counts letters in a text
        :param t_lines: list of lines
        :return: dictionary with letter, count_all, count_uppercase, percentage
        """
        str = ""
        for y in range(len(t_lines)):
            t_lines[y] = self.cleartext(t_lines[y])
            if t_lines[y].count(" ") > 0:
                s_lines = t_lines[y].split(" ")
                for z in range(len(s_lines)):
                    if s_lines[z].isalpha():
                        str = str + s_lines[z]
            else:
                if t_lines[y].isalpha():
                    str = str + t_lines[y]
        c_letter = {}
        l_uniq = set(list(str.lower()))
        for key in l_uniq:
            c_letter[key] = [str.count(key), str.count(key.upper()), 0]
        tl_count = 0
        for l_key in c_letter.keys():
            tl_count = tl_count + c_letter[l_key][0] + c_letter[l_key][1]
        for l_key in c_letter.keys():
            c_letter[l_key][2] = round((c_letter[l_key][0] + c_letter[l_key][1]) * 100 / tl_count, 2)
        return c_letter


if __name__ == "__main__":
    fs = WriteFromFile()
    lines = fs.reading_file(default_path_to_file)    # Reading the file
    wlc = WordLetterCount()
    w_dict = wlc.dowordcount(lines)                  # Counting words
    wtc = WriteToCsv()
    wtc.wordcount(w_dict)                            # Writing to csv file

    t_lines = fs.reading_file(default_path_to_file)  # Reading the file
    l_dict = wlc.dolettercount(t_lines)              # Counting letters
    wtc.lettercount(l_dict)                          # Writing to csv file
