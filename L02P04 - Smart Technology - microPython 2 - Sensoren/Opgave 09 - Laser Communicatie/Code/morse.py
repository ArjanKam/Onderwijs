tolerance = 0.1
TIME_MULTIPLY = .4
TIME_SEPERATOR = 1 * TIME_MULTIPLY
TIME_DOT = 2* TIME_MULTIPLY
TIME_LINE = 3* TIME_MULTIPLY
TIME_SPACE = 4* TIME_MULTIPLY


morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': "......."
}

def time_to_morse(times):
    morse = ""
    end = None
    for t in times:
        dT = t[1] - t[0]
        if end != None and TIME_SPACE - tolerance < t[0]-end < TIME_SPACE + tolerance:
            morse += " "
        if TIME_DOT -tolerance < dT < TIME_DOT + tolerance:
            morse += "."
        elif TIME_LINE - tolerance < dT < TIME_LINE + tolerance:
            morse += "-"
        end = t[1]
    return morse

def getChar(beep):
    if beep in morse_code_dict:
        return morse_code_dict[beep]
    return beep
    
    
def morse_to_text(morse):
    msg = ""
    for beep in morse.split(" "):
        msg += getChar(beep)
    return msg

def text_to_morse(text):
    return ' '.join(morse_code_dict.get(char.upper(), '') for char in text)

def morse_to_time(morse):
    times = []
    start = 2
    for ch in morse:
        if ch == ".":
            end = start + TIME_DOT
            times.append((start, end))
            end += TIME_SEPERATOR
        elif ch == "-":
            end = start + TIME_LINE
            times.append((start, end))
            end += TIME_SEPERATOR
        else:
            end += TIME_SPACE - TIME_SEPERATOR
        start = end
    return times

def morse_to_text(morse_code):
    morse_code_reverse = {code: char for char, code in morse_code_dict.items()}
    return ''.join(morse_code_reverse.get(code, ' ') for code in morse_code.split())

# Example usage
text_message = "dit is een test."
morse_message = text_to_morse(text_message)
print(f'{text_message}  --> {morse_message}')

impulse = morse_to_time(morse_message)
print(impulse)
morse = time_to_morse(impulse)
print(morse)
txt = morse_to_text(morse)
print(txt)