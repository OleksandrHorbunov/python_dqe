from newsfeedfromfile import *
from m3stringobject import text_normalize

default_path_to_file = "input_file.txt"

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
        ns.writeintofile(output_message, "News")
    elif message_type == 2:
        ns = WriteAdvert()
        exp_date = ns.inputexpdate()
        output_message = ns.prepareadvert(input_text, exp_date)
        ns.writeintofile(output_message, "Advert")
    elif message_type == 3:
        ns = WriteJoke()
        output_message = ns.preparejoke(input_text)
        ns.writeintofile(output_message, "Joke")
    elif message_type == 4:
        path_to_file = input("Please enter the path to file (default): ")
        fs = WriteFromFile()
        if path_to_file == "":
            path_to_file = default_path_to_file
            lines = fs.reading_file(path_to_file)
        else:
            lines = fs.reading_file(path_to_file)
        for line in lines:
            parsed_line = fs.parse_lines(line)
            parsed_line = text_normalize(parsed_line)
            if parsed_line[0].lower() == "news":
                ns = WriteNews()
                news_location = parsed_line[1]
                output_message = ns.preparenews(parsed_line[2], news_location)
                ns.writeintofile(output_message, "News")
            elif parsed_line[0].lower() == "advert":
                ns = WriteAdvert()
                exp_date = parsed_line[1].strip()
                output_message = ns.prepareadvert(parsed_line[2].strip(), exp_date)
                ns.writeintofile(output_message, "Advert")
            elif parsed_line[0].lower() == "joke":
                ns = WriteJoke()
                output_message = ns.preparejoke(parsed_line[1].strip())
                ns.writeintofile(output_message, "Joke")
            else:
                print(parsed_line[0] + " No chance to parse")
        #fs.delete_file(path_to_file)
    else:
        print("No chance to publish")
