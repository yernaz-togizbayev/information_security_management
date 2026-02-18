def decrypt(ciphertext):
    char_map = {
        'a': 'd',   # ✅ 
        'b': 's',   # ✅ 
        'c': 'q',   # ✅
        'd': 'w',   # ✅ 
        'e': 'x',   # ✅  
        'f': 'p',   # ✅
        'g': 'y',   # ✅ 
        'h': 'z',   # ✅ 
        'i': 'n',   # ✅ 
        'j': 'i',   # ✅ 
        'k': 'm',   # ✅ 
        'l': 'r',   # ✅
        'm': 'u',   # ✅ 
        'n': 'b',   # ✅ 
        'o': 'k',   # ✅
        'p': 'h',   # ✅ 
        'q': 'p',   # ✅ 
        'r': 'c',   # ✅  
        's': 'g',   # ✅
        't': 'f',   # ✅ 
        'u': 'o',   # ✅ 
        'v': 't',   # ✅
        'w': 'a',   # ✅ 
        'x': 'e',   # ✅ 
        'y': 'v',   # ✅ 
        'z': 'l'    # ✅  
    }

    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():
            dec = char_map.get(char.lower(), char)
            decrypted_text += dec.upper() if char.isupper() else dec
        else:
            decrypted_text += char
    return decrypted_text

# Read the ciphertext from "stage_0.txt"
with open("stage_0.txt", "r") as file:
    ciphertext = file.read()

print(decrypt(ciphertext))
