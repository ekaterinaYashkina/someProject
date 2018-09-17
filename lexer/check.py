import re
from lexer.lexems import Lexem

types = [Lexem.Hard_key, Lexem.Soft_key, Lexem.Modifier]
t = 0
end = 0
def check_keyword(word, lexem_type, index):
    for type in lexem_type:
        pattern = r'.{' + str(index) + '}' + type.value
        match = re.match(pattern, word, re.DOTALL)
        if match:
            return match, type
    return None, None

for type in Lexem:
    pattern = r'.{' + str(0) + '}' + type.value
    match = re.match(pattern, "abracadarsvd", re.DOTALL)
    if match:
        if type == Lexem.IDENTIFIER:
            for elem in types:
                key_match, type1 = check_keyword("abracadarsvd", elem, 0)
                if key_match:
                    type = type1
                    end = key_match.end(1)
                    break
        t = type
        break

print(t)