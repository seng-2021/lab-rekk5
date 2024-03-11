import codecs

def encode(s):
    if not isinstance(s,str):
        raise TypeError
    originlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if len(s) > 1000:
        raise ValueError
    s = s.ljust(1000, 'j')
    for c in s:
        if c.isalpha() and ord(c) <= ord('z'):
            if c.islower():
                c=c.upper()
            # Rot13 the character for maximum security
            crypted+=codecs.encode(c,'rot13')
        elif c in digitmapping:
          crypted+=digitmapping[c]
        else:
            raise ValueError
    return crypted[0:originlen]

def decode(s):
    return encode(s).lower()