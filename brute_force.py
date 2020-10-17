def decode(msg, shift):
    result = ''

    for t in msg:
        x = ord(t) - shift
        result  += chr(x)
    
    return result


if __name__ == "__main__":
    # shift: 0-256
    text = [
        'L#oryh#frglqj',
        '¥ÈÅÆÖÅÍÒ',
        'lxmn{'
    ]

    for t in text:
        for s in range(32):
            de_text = decode(t, s)
            print(de_text, end=" || ")
        print()
        print("=============")