from newsfeed import *


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
