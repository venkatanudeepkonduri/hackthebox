def getKey(encrypted_file, decrypted_file):
    key = ''
    
    with decrypted_file as df:
        decrypted = df.read()
    
    with encrypted_file as ef:
        encrypted = ef.read()
    
    for ch in range(len(decrypted)):
        for i in range(255):
            temp = chr((ord(encrypted[ch])-i) % 255)
            if(temp == decrypted[ch]):
                key += chr(i)
                break
    return key



decrypted_file = open('check.txt', 'r')
encrypted_file = open('out.txt', 'r')
print(getKey(encrypted_file, decrypted_file))


pwremind_file = open('passwordreminder.txt', 'r')
with pwremind_file as pwf:
        pwremind = pwf.read()
print(decrypt(pwremind, "alexandrovich"))

def encrypt(text, key):
    keylen = len(key)
    keyPos = 0
    encrypted = ""
    for x in text:
        keyChr = key[keyPos]
        newChr = ord(x)
        newChr = chr((newChr + ord(keyChr)) % 255)
        encrypted += newChr
        keyPos += 1
        keyPos = keyPos % keylen
    return encrypted


def decrypt(text, key):
    keylen = len(key)
    keyPos = 0
    decrypted = ""
    for x in text:
        keyChr = key[keyPos]
        newChr = ord(x)
        newChr = chr((newChr - ord(keyChr)) % 255)
        decrypted += newChr
        keyPos += 1
        keyPos = keyPos % keylen
    return decrypted