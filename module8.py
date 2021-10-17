from datetime import datetime, date
import random
import os
import json


class InputMessage:
    def userdialog(self):
        """
        :return: number of the message type
        """
        how_to_enter = input("How to enter the message: Manually - 1, From file - 2: ")
        if how_to_enter == "1":
            message_type = input("Please choose the type of message: News - 1, Advert - 2, Joke - 3: ")
        elif how_to_enter == "2":
            how_to_enter = input("Text file - 1, JSON file - 2: ")
            if how_to_enter == "1":
                message_type = 4
            elif how_to_enter == "2":
                message_type = 5
        return message_type

    def inputtext(self):
        """
        :return: entered message
        """
        news_text = input("Please write a text: ")
        return news_text


class WriteMessageToFeed:
    def writeintofile(self, message, mes_type):
        """
        :param message: text should be written into the feed
        :return: the info that message was written into feed
        """
        file_w = open("news_feed.txt", "a")
        file_w.write(message)
        file_w.close()
        print(mes_type + " has been written into feed!")


class WriteNews(WriteMessageToFeed):
    def inputlocation(self):
        """
        :return: entered location
        """
        news_location = input("Please input location: ")
        return news_location

    def currentdate(self):
        """
        :return: current date with time
        """
        date_time = datetime.now()
        cdt = date_time.strftime("%d/%m/%Y %H:%M")
        return cdt

    def preparenews(self, input_text, news_location):
        """
        :param input_text: entered text by user
        :param news_location: entered location by user
        :return: prepared message according to template
        """
        output_message = "------->News<-------\n"
        output_message = output_message + input_text + "\n"
        output_message = output_message + news_location + ", " + self.currentdate() + "\n"
        return output_message


class WriteAdvert(WriteMessageToFeed):
    def inputexpdate(self):
        """
        :return: entered expiration date
        """
        exp_date = input("Please define expiration date (dd/mm/YYYY): ")
        return exp_date

    def datediff(self, exp_date):
        """
        :param exp_date: the date of advert expiration
        :return: number of days left
        """
        date_format = "%d/%m/%Y"
        dd = date.today()
        dd = dd.strftime(date_format)
        day_today = datetime.strptime(dd, date_format)
        day_exp = datetime.strptime(exp_date, date_format)
        delta = day_exp - day_today
        delta_days = str(delta.days)
        return delta_days

    def prepareadvert(self, input_text, exp_date):
        """
        :param input_text: entered text by user
        :param exp_date: expiration date of advert entered by user
        :return:
        """
        output_message = "------->Private Ad<-------\n"
        output_message = output_message + input_text + "\n"
        output_message = output_message + "Actual until: " + exp_date + ", " + self.datediff(exp_date) + " days left\n"
        return output_message

class WriteJoke(WriteMessageToFeed):
    def getrank(self):
        """
        :return: rank of joke
        """
        num2words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                     6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
        random_rank = random.randint(1, 10)
        return num2words[random_rank]

    def preparejoke(self, input_text):
        """
        :param input_text: entered text by user
        :return: prepared message for writing to feed
        """
        output_message = "------->Joke of the day<-------\n"
        output_message = output_message + input_text + "\n"
        output_message = output_message + "Funny master - " + self.getrank() + " of ten\n"
        return output_message

class WriteFromFile(WriteMessageToFeed):
    def reading_file(self, path_to_file):
        """
        Reads input file
        :param path_to_file: path to input file
        :return: list
        """
        file = open(path_to_file, 'r')
        lines = file.readlines()
        return lines

    def delete_file(self, path_to_file):
        """
        Removes file
        :param path_to_file: path to file should be removed
        :return: message that file was removed
        """
        if os.path.exists(path_to_file):
            os.remove(path_to_file)
            print("File has been removed")
        else:
            print("The file does not exist")

    def parse_lines(self, line):
        """
        Splits leines by symbol
        :param line: line
        :return: list
        """
        return line.split("#")

    def readingjson(self, path_to_file):
        """
        Reads json file
        :param path_to_file: input json file
        :return: returns JSON object as a dictionary
        """
        with open(path_to_file, "r") as f:
            t_json = json.load(f)
        return t_json