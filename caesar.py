def encode(msg, shift):
    result = ''

    for t in msg:
        x = ord(t) + shift
        result += chr(x)
    
    return result


def decode(msg, shift):
    result = ''

    for t in msg:
        x = ord(t) - shift
        result  += chr(x)
    
    return result


if __name__  == '__main__':
    text = input("Enter your secret: ")
    shift = int(input("Enter secret key (0-256): "))
    print("Original text:", text)

    en_text = encode(text, shift)
    print("Encode text:", en_text)
    
    de_text = decode(en_text, shift)
    print("Decode text:", de_text)