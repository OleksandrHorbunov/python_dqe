#from newsfeedmng import *
import newsfeedmng as mng
from m3stringobject import text_normalize
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-m", "--manual", type=str, choices=['news', 'advert', 'joke'],
                    help="The type of news", action="store")
group.add_argument("-f", "--file", type=str, choices=['csv', 'json', 'xml'],
                    help="News from file", action="store")
args = parser.parse_args()

default_csv_file = "input_file.txt"
default_json_file = "input_file.json"
default_xml_file = "input_file.xml"


def pfn(message):
    nt = []
    nt.append(message)
    return text_normalize(nt)

def manual_news(msg):
    input_text = input("Please write a text: ")
    ns = mng.WriteNews()
    news_location = ns.inputlocation()
    ns.writeintofile(ns.preparenews(input_text, news_location), msg)
    mng.WriteToDB("news", ns.preparefordb(input_text, news_location))

def manual_advert(msg):
    input_text = input("Please write a text: ")
    ns = mng.WriteAdvert()
    exp_date = ns.inputexpdate()
    ns.writeintofile(ns.prepareadvert(input_text, exp_date), msg)
    mng.WriteToDB("advert", ns.preparefordb(input_text, exp_date))

def manual_joke(msg):
    input_text = input("Please write a text: ")
    ns = mng.WriteJoke()
    output_message = ns.preparejoke(input_text)
    ns.writeintofile(output_message, msg)
    mng.WriteToDB("joke", ns.preparefordb(input_text))

def file_csv():
    path_to_file = input("Please enter the path to txt file (default): ")
    fs = mng.WriteFromFile()
    if path_to_file == "":
        path_to_file = default_csv_file
        lines = fs.reading_file(path_to_file)
    else:
        lines = fs.reading_file(path_to_file)
    for line in lines:
        parsed_line = text_normalize(fs.parse_lines(line))
        if parsed_line[0].lower() == "news":
            ns = mng.WriteNews()
            output_message = ns.preparenews(parsed_line[2], parsed_line[1])
            ns.writeintofile(output_message, "News")
            mng.WriteToDB("news", ns.preparefordb(parsed_line[2], parsed_line[1]))
        elif parsed_line[0].lower() == "advert":
            ns = mng.WriteAdvert()
            output_message = ns.prepareadvert(parsed_line[2].strip(), parsed_line[1].strip())
            ns.writeintofile(output_message, "Advert")
            mng.WriteToDB("advert", ns.preparefordb(parsed_line[2].strip(), parsed_line[1].strip()))
        elif parsed_line[0].lower() == "joke":
            ns = mng.WriteJoke()
            output_message = ns.preparejoke(parsed_line[1].strip())
            ns.writeintofile(output_message, "Joke")
            mng.WriteToDB("joke", ns.preparefordb(parsed_line[1].strip()))
        else:
            print(parsed_line[0] + " No chance to parse")

def file_json():
    path_to_file = input("Please enter the path to json file (default): ")
    fs = mng.WriteFromFile()
    if path_to_file == "":
        path_to_file = default_json_file
        t_json = fs.readingjson(path_to_file)
    else:
        t_json = fs.readingjson(path_to_file)
    for t_key in t_json.keys():
        nt = []
        nt.append(t_json[t_key]["message"])
        nm = text_normalize(nt)
        if t_key.lower() == "news":
            ns = mng.WriteNews()
            news_location = t_json[t_key]["city"].strip()
            output_message = ns.preparenews(nm[0], news_location)
            ns.writeintofile(output_message, "News")
            mng.WriteToDB("news", ns.preparefordb(nm[0], news_location))
        elif t_key.lower() == "advert":
            ns = mng.WriteAdvert()
            exp_date = t_json[t_key]["exp_date"]
            output_message = ns.prepareadvert(nm[0], exp_date.strip())
            ns.writeintofile(output_message, "Advert")
            mng.WriteToDB("advert", ns.preparefordb(nm[0], exp_date.strip()))
        elif t_key.lower() == "joke":
            ns = mng.WriteJoke()
            output_message = ns.preparejoke(nm[0])
            ns.writeintofile(output_message, "Joke")
            mng.WriteToDB("joke", ns.preparefordb(nm[0]))
        else:
            print(t_key + " No chance to parse")

def file_xml():
    path_to_file = input("Please enter the path to xml file (default): ")
    fs = mng.WriteFromFile()
    if path_to_file == "":
        path_to_file = default_xml_file
        root = fs.readingxml(path_to_file)
    else:
        root = fs.readingxml(path_to_file)
    for child in range(len(root)):
        if root[child].attrib["name"].lower() == "news":
            ns = mng.WriteNews()
            news_location = root[child][0].text.strip()
            nm = pfn(root[child][1].text)
            output_message = ns.preparenews(nm[0], news_location)
            ns.writeintofile(output_message, "News")
            mng.WriteToDB("news", ns.preparefordb(nm[0], news_location))
        elif root[child].attrib["name"].lower() == "advert":
            ns = mng.WriteAdvert()
            exp_date = root[child][0].text.strip()
            nm = pfn(root[child][1].text)
            output_message = ns.prepareadvert(nm[0], exp_date.strip())
            ns.writeintofile(output_message, "Advert")
            mng.WriteToDB("advert", ns.preparefordb(nm[0], exp_date.strip()))
        elif root[child].attrib["name"].lower() == "joke":
            ns = mng.WriteJoke()
            nm = pfn(root[child][0].text)
            output_message = ns.preparejoke(nm[0])
            ns.writeintofile(output_message, "Joke")
            mng.WriteToDB("joke", ns.preparefordb(nm[0]))
        else:
            print(t_key + " No chance to parse")

if __name__ == "__main__":
    if args.manual == "news":
        print(f"The type of news - {args.manual}")
        manual_news(args.manual)
    elif args.manual == "advert":
        print(f"The type of news - {args.manual}")
        manual_advert(args.manual)
    elif args.manual == "joke":
        print(f"The type of news - {args.manual}")
        manual_joke(args.manual)

    if args.file == "csv":
        print(f"News from - {args.file}")
        file_csv()
    elif args.file == "json":
        print(f"News from - {args.file}")
        file_json()
    elif args.file == "xml":
        print(f"News from - {args.file}")
        file_xml()