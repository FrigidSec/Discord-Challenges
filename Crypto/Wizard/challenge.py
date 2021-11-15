if __name__ == "__main__":
    flag = "<REDACTED>"
    a = 0x31
    b = 0x33
    c = 0x37
    m = 0x1337
    enc = "".join([chr((a*ord(i) + c) % m) for i in flag])
    with open("out.enc", "wb") as wf:
        wf.write(enc.encode())