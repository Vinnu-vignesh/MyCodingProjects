import hashlib

PASSWORD_HASH  = input("Enter the hash value: ")

wordlist = "/home/vinnuhacker/rockyou.txt"

with open(wordlist, "r") as wl:
    
    word = wl.readline()
    while word != "":
        hashvalue = hashlib.md5(word[:-1].encode()).hexdigest()
        if hashvalue == PASSWORD_HASH:
            print(f"Cracking Status: {word[:-1]} --> {PASSWORD_HASH}")
            print(f"Password Cracked: [{word[:-1]}]")
            break

        print(f"Cracking Status: {word[:-1]} --> {PASSWORD_HASH}")
        word = wl.readline()
    wl.close()