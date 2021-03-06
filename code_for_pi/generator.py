from random import choice
import os
import qrcode


charsets = [
    'abcdefghijklmnopqrstuvwxyz',
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    '0123456789',
    '^!\$%&/()=?{[]}+~#-_.:,;<>|\\',
    ]

def mkpassword(length=16):
    pwd = []
    charset = choice(charsets)
    while len(pwd) < length:
        pwd.append(choice(charset))
        charset = choice(list(set(charsets) - set([charset])))
    return "".join(pwd)

def create_qr_code(token):
    img = qrcode.make(token)
    img.save("./password.png")

if __name__ == '__main__':
    token = mkpassword()
    print(token)
    create_qr_code(token)


