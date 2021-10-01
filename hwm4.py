import m2collections
import m3stringobject
import random

text = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""


def resultoutput(str_message, str_output):
    """Returns formatted message
       Parameters:
       str_message, str_output (str)
    """
    print(f"{str_message}:\n {str_output}")


if __name__ == "__main__":
    print("Module 2: collections\n---------------------")
    # Generate random number of dicts
    number_dicts = random.randint(2, 10)
    g_dict_list = m2collections.get_dicts(number_dicts)
    g_dict_common = m2collections.get_common_dict(g_dict_list)
    print("List of dicts\n", g_dict_list)
    print("Common dict\n", g_dict_common)
    # <----------------------------------------------------------------------------->
    print("\nModule 3: string object\n-----------------------")
    #resultoutput("Normalized text", m3stringobject.text_normalize(m3stringobject.text_split(text)))
    text_normalizing = m3stringobject.text_normalize(m3stringobject.text_split(text))
    extended_sentense = m3stringobject.more_setences(text_normalizing)
    #resultoutput("Extended sentences", m3stringobject.more_setences(text_normalizing))
    #resultoutput("Corrected spelling", m3stringobject.text_misspell(extended_sentense))
    misspell_sentences = m3stringobject.text_misspell(extended_sentense)
    m3stringobject.count_whitespaces(misspell_sentences)
