import re


def keyword_reformat(line):
    formatted_line = line
    # TODO: complete this
    dic = {"set nu": "set number",
            "set rnu": "set relativenumber"}
    for i, j in dic.iteritems():
        formatted_line = re.sub(i+'$', j, formatted_line)
    return formatted_line
