"""
============================================================================
File: base4Coding.py

Contains code to encode or decode the base-4 table from Homework 1.
============================================================================
"""

# The base-4 encoding mapped to the corresponding letter
base4Table = {'000': 'A', '001': 'B', '002': 'C', '003': 'D',
              '010': 'E', '011': 'F', '012': 'G', '013': 'H',
              '020': 'I', '021': 'J', '022': 'K', '023': 'L',
              '030': 'M', '031': 'N', '032': 'O', '033': 'P',
              '100': 'Q', '101': 'R', '102': 'S', '103': 'T',
              '110': 'U', '111': 'V', '112': 'W', '113': 'X',
              '120': 'Y', '121': 'Z', '122': '0', '123': '1',
              '130': '2', '131': '3', '132': '4', '133': '5',
              '200': '6', '201': '7', '202': '8', '203': '9',
              '210': ' ', '211': '.', '212': '?', '213': ',',
              '220': '+', '221': '-', '222': '*', '223': '/',
              '230': ';', '231': ':', '232': '(', '233': ')',
              '300': '&', '301': '^', '302': '%', '303': '$',
              '310': '#', '311': '@', '312': '!', '313': '~',
              '320': "'", '321': '"', '322': '=', '323': '\\',
              '330': '<', '331': '>', '332': '{', '333': '}'}
              
# The reverse of the base-4 encoding, constructed from it              
reverseTable = {v: k for k, v in base4Table.items()}


def encodeMessage(messageString):
    """ Takes in a message as a string, and produces an encoding into base-4
    digits. Given as a string because it is just as easy to use characters
    as integers. Prints a message if it sees a symbol that it cannot encode,
    and automatically converts alphabetic characters to uppercase.
    """
    codedDigits = ""
    for ch in messageString:
        ch = ch.upper()
        if ch in reverseTable:
            code = reverseTable[ch]
            codedDigits += code
        else:
            print("Invalid symbol to encode: ", ch)
    return codedDigits


def decodeMessage(digitString):
    """Takes a string of base-4 digits, and converts them back to a message 
    using the base-4 encoding. If there aren't exactly a multiple of three
    digits, it doesn't do anything, and it prints a message if somehow a trio
    of digits is invalid. Returns the resulting decoded string.
    """
    if len(digitString) % 3 != 0:   # if string isn't exactly a multiple of three
        print("Cannot decode message that lacks three symbols per character.")
        return ""
    uncodedString = ""
    for i in range(0, len(digitString), 3):
        trio = digitString[i:i+3]
        if trio in base4Table:
            ch = base4Table[trio]
            uncodedString += ch
        else:
            print("Invalid digit sequence to decode: ", trio)
    return uncodedString