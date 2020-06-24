def generate_symbol(text: str):
    if text == 'free':
        return '🆓'
    elif text == 'paid':
        return '💰'
    return text


def get_new_line_point_symbol():
    return '🔹'


def generate_flag_symbol(lang: str):
    offset = 127462 - ord('A')
    code = lang.upper()
    return chr(ord(code[0]) + offset) + chr(ord(code[1]) + offset)
