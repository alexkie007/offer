def process(text, width):
    code, msg = check_params(text, width)
    if code == 400:
        return msg
    size = len(text)
    line = 1
    result = []
    string = ""
    line_count = 0
    for index, value in enumerate(text):
        if index > 0 and index % width == 0:
            if (text[index].isalpha() and text[index - 1].isalpha()) or text[index - 1] == text[index] == " ":
                line_count += 1
            line += 1
        if 0 < index < size:
            # 如果当前索引对应的字符与前一个字符不是相同类型，则说明前面的字符串已经是一节，因此考虑增加到输出
            if (text[index].isalpha() and text[index - 1] == " ") or (text[index] == " " and text[index - 1].isalpha()):
                # 需要考虑当前索引是否进行了换行，如果换行了需要将行号减1
                if index % width == 0:
                    lines = [str(x) for x in range(line - 1 - line_count, line)]
                else:
                    lines = [str(x) for x in range(line - line_count, line + 1)]
                result.append(string + "(" + ",".join(lines) + ")")
                line_count = 0
                string = ""
        string += value
        if index == size - 1:
            lines = [str(x) for x in range(line - line_count, line + 1)]
            result.append(string + "(" + ",".join(lines) + ")")
    return ";".join(result) + ";"


def check_params(text, width):
    code = 200
    msg = ""
    if width < 10 or width > 80:
        code = 400
        msg = "ERROR: Width out of range!"
    for s in text:
        if s.isalpha() or s == " ":
            continue
        code = 400
        msg = "ERROR: Invalid character detected!"
    return code, msg

