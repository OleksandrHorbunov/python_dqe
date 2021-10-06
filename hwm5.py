from datetime import datetime, date
import random


class InputMessage:
    def userdialog(self):
        """
        :return: number of the message type
        """
        message_type = input("Please choose the type of message: News - 1, Advert - 2, Joke - 3: ")
        return message_type

    def inputtext(self):
        """
        :return: entered message
        """
        news_text = input("Please write a text: ")
        return news_text


class WriteMessageToFeed:
    def writeintofile(self, message):
        """
        :param message: text should be written into the feed
        :return: the info that message was written into feed
        """
        file_w = open("news_feed.txt", "a")
        file_w.write(message)
        file_w.close()
        print("Message has been written into feed!")


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


if __name__ == "__main__":
    im = InputMessage()
    message_type = int(im.userdialog())
    input_text = ""
    if message_type in list(range(1, 4)):
        input_text = im.inputtext()
    if message_type == 1:
        ns = WriteNews()
        news_location = ns.inputlocation()
        output_message = ns.preparenews(input_text, news_location)
        ns.writeintofile(output_message)
    elif message_type == 2:
        ns = WriteAdvert()
        exp_date = ns.inputexpdate()
        output_message = ns.prepareadvert(input_text, exp_date)
        ns.writeintofile(output_message)
    elif message_type == 3:
        ns = WriteJoke()
        output_message = ns.preparejoke(input_text)
        ns.writeintofile(output_message)
    else:
        print("No chance")