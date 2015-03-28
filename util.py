import re


def keyword_reformat(line):
    formatted_line = line
    # TODO: complete this
    dic = {"nu": "number",
           "rnu": "relativenumber"}
    dic_with_params = {"ts": "tabstop",
                       "sts": "softtabstop"}

    for i, j in dic.iteritems():
        formatted_line = re.sub("set "+i+'$', "set "+j, formatted_line)

    for i, j in dic_with_params.iteritems():
        formatted_line = re.sub("set "+i+'=', "set "+j+"=", formatted_line)
    return formatted_line
