import random, string

def gen_string(size=random.randint(3, 9), chars=string.ascii_uppercase + string.digits):
      return ''.join(random.choice(chars) for _ in range(size))

def poly(not_encoded_payload):
    POLY_CODE_DICT = {
        "A": gen_string(),
        "B": gen_string(),
        "C": gen_string(),
        "D": gen_string(),
        "E": gen_string(),
        "F": gen_string(),
        "G": gen_string(),
        "H": gen_string(),
        "I": gen_string(),
        "J": gen_string(),
        "K": gen_string(),
        "L": gen_string(),
        "M": gen_string(),
        "N": gen_string(),
        "O": gen_string(),
        "P": gen_string(),
        "Q": gen_string(),
        "R": gen_string(),
        "S": gen_string(),
        "T": gen_string(),
        "U": gen_string(),
        "V": gen_string(),
        "W": gen_string(),
        "X": gen_string(),
        "Y": gen_string(),
        "Z": gen_string(),
        # Lower case
        "a": gen_string(),
        "b": gen_string(),
        "c": gen_string(),
        "d": gen_string(),
        "e": gen_string(),
        "f": gen_string(),
        "g": gen_string(),
        "h": gen_string(),
        "i": gen_string(),
        "j": gen_string(),
        "k": gen_string(),
        "l": gen_string(),
        "m": gen_string(),
        "n": gen_string(),
        "o": gen_string(),
        "p": gen_string(),
        "q": gen_string(),
        "r": gen_string(),
        "s": gen_string(),
        "t": gen_string(),
        "u": gen_string(),
        "v": gen_string(),
        "w": gen_string(),
        "x": gen_string(),
        "y": gen_string(),
        "z": gen_string(),
        # Numbers and Symbols
        "1": gen_string(),
        "2": gen_string(),
        "3": gen_string(),
        "4": gen_string(),
        "5": gen_string(),
        "6": gen_string(),
        "7": gen_string(),
        "8": gen_string(),
        "9": gen_string(),
        "0": gen_string(),
        "&": gen_string(),
        "@": gen_string(),
        ":": gen_string(),
        ",": gen_string(),
        ".": gen_string(),
        "'": gen_string(),
        '"': gen_string(),
        "?": gen_string(),
        "/": gen_string(),
        "=": gen_string(),
        "+": gen_string(),
        "-": gen_string(),
        "(": gen_string(),
        ")": gen_string(),
        "!": gen_string(),
        "{": gen_string(),
        "}": gen_string(),
        "$": gen_string(),
        "*": gen_string(),
        "\\": gen_string(),
        "%": gen_string(),
        ";": gen_string(),
        "[": gen_string(),
        "]": gen_string(),
        " ": gen_string(),
        "\n": gen_string(),
        "_": gen_string(),
        "#": gen_string(),
    }


    def encode(message: str) -> str:
        cipher = ""
        for letter in message:
            if letter != " ":
                cipher += POLY_CODE_DICT[letter] + " "
            else:
                cipher += "/ "

        # Remove trailing space added on line 64
        return cipher[:-1]


    def decode(message: str) -> str:
        decipher = ""
        letters = message.split(" ")
        for letter in letters:
            if letter != "/":
                decipher += list(POLY_CODE_DICT.keys())[
                    list(POLY_CODE_DICT.values()).index(letter)
                ]
            else:
                decipher += " "

        return decipher

    #payload = open('./payload.py', 'r').readlines()
    payload = not_encoded_payload
    code = []
    imports = ''

    for line in payload:
        if not line.startswith('import '):
            #line = line.strip()
            #line = line.replace('{', 'OOOO').replace('}', 'PPPP').replace('$', 'LLLL').replace('*', '0000').replace('\\', '1111').replace('%', 'AAAA').replace(';', 'BBBB').replace('[', 'CCCC').replace(']', 'DDDD').replace(' ', '5555').replace('\n', '6666').replace('_', '7777').replace('#', '8888').strip()
            if not line.startswith('from '):
                result = encode(line)
                code.append(result)
            elif line.startswith('from '):
                imports += line
        elif line.startswith('import '):
            imports += line

    new_payload = '''%s

POLY_CODE_DICT = {
    "A": "%s",
    "B": "%s",
    "C": "%s",
    "D": "%s",
    "E": "%s",
    "F": "%s",
    "G": "%s",
    "H": "%s",
    "I": "%s",
    "J": "%s",
    "K": "%s",
    "L": "%s",
    "M": "%s",
    "N": "%s",
    "O": "%s",
    "P": "%s",
    "Q": "%s",
    "R": "%s",
    "S": "%s",
    "T": "%s",
    "U": "%s",
    "V": "%s",
    "W": "%s",
    "X": "%s",
    "Y": "%s",
    "Z": "%s",
    "a": "%s",
    "b": "%s",
    "c": "%s",
    "d": "%s",
    "e": "%s",
    "f": "%s",
    "g": "%s",
    "h": "%s",
    "i": "%s",
    "j": "%s",
    "k": "%s",
    "l": "%s",
    "m": "%s",
    "n": "%s",
    "o": "%s",
    "p": "%s",
    "q": "%s",
    "r": "%s",
    "s": "%s",
    "t": "%s",
    "u": "%s",
    "v": "%s",
    "w": "%s",
    "x": "%s",
    "y": "%s",
    "z": "%s",
    "1": "%s",
    "2": "%s",
    "3": "%s",
    "4": "%s",
    "5": "%s",
    "6": "%s",
    "7": "%s",
    "8": "%s",
    "9": "%s",
    "0": "%s",
    "&": "%s",
    "@": "%s",
    ":": "%s",
    ",": "%s",
    ".": "%s",
    "'": "%s",
    '"': "%s",
    "?": "%s",
    "/": "%s",
    "=": "%s",
    "+": "%s",
    "-": "%s",
    "(": "%s",
    ")": "%s",
    "!": "%s",
    "{": "%s",
    "}": "%s",
    "$": "%s",
    "*": "%s",
    "\\\\": "%s",
    "%%": "%s",
    ";": "%s",
    "[": "%s",
    "]": "%s",
    " ": "%s",
    "\\n": "%s",
    "_": "%s",
    "#": "%s",
}

def decode(message: str) -> str:
    decipher = ""
    letters = message.split(" ")
    for letter in letters:
        if letter != "/":
            decipher += list(POLY_CODE_DICT.keys())[
                list(POLY_CODE_DICT.values()).index(letter)
            ]
        else:
            decipher += " "
    return decipher

ex = %s
roses = ''
for i in ex:
    if not i == '':
        result = decode(i)
        roses +=result
    else:
        roses +=' '
exec(roses)''' % (imports,
    POLY_CODE_DICT["A"], 
    POLY_CODE_DICT["B"], 
    POLY_CODE_DICT["C"], 
    POLY_CODE_DICT["D"], 
    POLY_CODE_DICT["E"], 
    POLY_CODE_DICT["F"], 
    POLY_CODE_DICT["G"], 
    POLY_CODE_DICT["H"], 
    POLY_CODE_DICT["I"], 
    POLY_CODE_DICT["J"], 
    POLY_CODE_DICT["K"], 
    POLY_CODE_DICT["L"], 
    POLY_CODE_DICT["M"], 
    POLY_CODE_DICT["N"], 
    POLY_CODE_DICT["O"], 
    POLY_CODE_DICT["P"], 
    POLY_CODE_DICT["Q"], 
    POLY_CODE_DICT["R"], 
    POLY_CODE_DICT["S"], 
    POLY_CODE_DICT["T"], 
    POLY_CODE_DICT["U"], 
    POLY_CODE_DICT["V"], 
    POLY_CODE_DICT["W"], 
    POLY_CODE_DICT["X"], 
    POLY_CODE_DICT["Y"], 
    POLY_CODE_DICT["Z"], 
    POLY_CODE_DICT["a"], 
    POLY_CODE_DICT["b"], 
    POLY_CODE_DICT["c"], 
    POLY_CODE_DICT["d"], 
    POLY_CODE_DICT["e"], 
    POLY_CODE_DICT["f"], 
    POLY_CODE_DICT["g"], 
    POLY_CODE_DICT["h"], 
    POLY_CODE_DICT["i"], 
    POLY_CODE_DICT["j"], 
    POLY_CODE_DICT["k"], 
    POLY_CODE_DICT["l"], 
    POLY_CODE_DICT["m"], 
    POLY_CODE_DICT["n"], 
    POLY_CODE_DICT["o"], 
    POLY_CODE_DICT["p"], 
    POLY_CODE_DICT["q"], 
    POLY_CODE_DICT["r"], 
    POLY_CODE_DICT["s"], 
    POLY_CODE_DICT["t"], 
    POLY_CODE_DICT["u"], 
    POLY_CODE_DICT["v"], 
    POLY_CODE_DICT["w"], 
    POLY_CODE_DICT["x"], 
    POLY_CODE_DICT["y"], 
    POLY_CODE_DICT["z"], 
    POLY_CODE_DICT["1"], 
    POLY_CODE_DICT["2"], 
    POLY_CODE_DICT["3"], 
    POLY_CODE_DICT["4"], 
    POLY_CODE_DICT["5"], 
    POLY_CODE_DICT["6"], 
    POLY_CODE_DICT["7"], 
    POLY_CODE_DICT["8"], 
    POLY_CODE_DICT["9"], 
    POLY_CODE_DICT["0"], 
    POLY_CODE_DICT["&"], 
    POLY_CODE_DICT["@"], 
    POLY_CODE_DICT[":"], 
    POLY_CODE_DICT[","], 
    POLY_CODE_DICT["."], 
    POLY_CODE_DICT["'"], 
    POLY_CODE_DICT['"'], 
    POLY_CODE_DICT["?"], 
    POLY_CODE_DICT["/"], 
    POLY_CODE_DICT["="], 
    POLY_CODE_DICT["+"], 
    POLY_CODE_DICT["-"], 
    POLY_CODE_DICT["("], 
    POLY_CODE_DICT[")"], 
    POLY_CODE_DICT["!"],
    POLY_CODE_DICT["{"], 
    POLY_CODE_DICT["}"], 
    POLY_CODE_DICT["$"], 
    POLY_CODE_DICT["*"], 
    POLY_CODE_DICT["\\"], 
    POLY_CODE_DICT["%"], 
    POLY_CODE_DICT[";"], 
    POLY_CODE_DICT["["], 
    POLY_CODE_DICT["]"], 
    POLY_CODE_DICT[" "], 
    POLY_CODE_DICT["\n"], 
    POLY_CODE_DICT["_"], 
    POLY_CODE_DICT["#"],  
    code)

    with open('./poly_payload.py', 'w') as f:
        f.write(new_payload)
        f.close()
