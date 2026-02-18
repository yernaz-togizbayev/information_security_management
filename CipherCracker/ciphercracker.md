Stage_0: first, I wrote a simple python program which will read a stage_0.txt file and replace letters in it. So I created a dictionary a alphabetically sorted letters
as keys, and then tried to decrypt text in stage_0 by my oww. Since it was encrypted using substitution cipher, I was trying to guess each letter one by one. For example,
at the first ciphertext in stage_0.txt is "j'k". For me it looked immediately similar to "i'm", wich means in decryption "j=i" and "k=m". After that I was trying to search
for words with only 2 or 3 letters which already contained known letters 'j' and 'k'. I found then "ji" and "kg". Since we already know that j is i and k is m, the first
what come to my mind for "ji" is "in", and for "kg" is "my". After this we already know 4 letters, so {'j' : 'i', 'k' : 'm', 'i' : 'n', 'g' : 'y'}. And so I continued with
guess further until I didn't found the replacement for all letter for decryption.

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

It was easy because substitution ciphers keep letter patterns and frequencies. English has common letters (like 'e', 't', 'a') and common words ("i'm", "it's", "the", "and"),
making it simple to guess the real message. Simple substitution ciphers aren't secure. To make messages safer, it's better to use more advanced encryption methods (like AES
or RSA) or ciphers that change letters differently each time.

stage_1: For this stage, I wrote two functions: one that XORs two hexadecimal strings and another that converts hexadecimal strings into readable ASCII. So first, in the stage
hints is written that we should use "long enough key". So I just took two longest decrypted hexadecimals from stage_1.txt and assigned them into cipher1 and cipher2. And for
variable plain1 I took a result of xor_result function as long as possible. But for variable plain2 it was tricky. What I basically did, is that I googled for something like
"most common word in English for sentence beginning" and found this list of words from Promova app (https://promova.com/content/119_English_Introductory_Words_List_6621f2f4c0.png).
So for each of the words I looked up for hex code and one by one started inserting them into plain2 until I won't find any meaningful word. And when I came to word "therefore",
it gave me an output "let'sa.=q". So I see that it starts with "let's". So I guessed that the first word probably "there" and after thatI XORed the longest decrypted hex code
from stage_1.txt with all other hex codes one by one. After that I was trying to guess all other sentences. For example, one of cipher gave me beginning "histo". So the first
word which came to my mind is "history ". I again checked for a hex code for this word and again compared put all hex codes from stage_1.txt into cipher1 and cipher2. Then
I guessed the beginning "i thought" at cipher15, which gave the sentence beginning "i help pe" for cipher1. And I guessed it as "i help people ". And so on I continued to
guess complete sentences until I didn't find my while flag.
The reason why I could crack it because the same encryption key was mistakenly used for multiple messages. This allowed me to XOR ciphertexts against each other and use common
English phrases to guess the plaintext. The critical mistake was reusing the same one-time-pad key for more than one message. A one-time-pad key must be random, secret, and
used exactly once to stay secure.

def hex_xor(hex1, hex2):
    result = []
    for i in range(0, min(len(hex1), len(hex2)), 2):
        byte1 = int(hex1[i:i+2], 16)
        byte2 = int(hex2[i:i+2], 16)
        xor_byte = byte1 ^ byte2
        result.append(format(xor_byte, '02x'))
    return ''.join(result)

def hex_to_ascii(hex_string):
    ascii_chars = []
    for i in range(0, len(hex_string), 2):
        hex_code = hex_string[i:i+2]
        char_code = int(hex_code, 16)
        if 32 <= char_code <= 126:
            ascii_chars.append(chr(char_code))
        else:
            ascii_chars.append('.')
    return ''.join(ascii_chars)

cipher1 = "475857455745474556461652180d5c5e130d5b13010b040a050f540219420b56105d154d5e524654124b10125a5f52554a174009034006144b140559410416145d44535a5c4551571250465d464343165d06445212414c1513501409454643135c0b53591e424152041542160a11185a111710184b574c1a"
cipher2 = "5f5546104142570a42081113150b124d5b1650564a451a09114153595715075c424c5d58421b1452545617151749564559561406135c43525650435113135907510b1c1659111e45445b094613541b045b115a4e46510a470d46400e51461b135111175e4d09"
xor_result = hex_xor(cipher1, cipher2)

plain1 = xor_result[:200]
plain2 = "7468657265666F7265"

final_result = hex_to_ascii(hex_xor(plain1, plain2))
print(final_result)

# cipher1: i hel -> i help -> i help pe -> i help people -> i help people with -> i help people with pro -> i help people with problems -> i help people with problems. ✅
# cipher2: well, -> well, e -> well ,eve -> well, everybod -> well, everybody ne -> well, everybody needs -> well, everybody needs a hobb -> well, everybody needs a hobby. ✅
# cipher3: in my -> in my -> in my bus -> in business -> in my business you -> in my business you pre -> in my business you prepare f -> in my business you prepare for the u -> in my business you prepare for the uexpected -> in my business you prepare for the uexpected.✅
# cipher4: and y -> and you -> and youth -> and youth is n -> and youth is no gu -> and youth is no guaran -> and youth is no guarantee of -> and youth is no guarantee of innov -> and youth is no guarantee of innovation. ✅
# cipher5: if yo -> if you -> if you ca -> if you can't t -> if you can't trust -> if you can't trust a s -> if you can't trust a swiss b -> if you can't trust a swiss banker, w -> if you can't trust a swiss banker, what's th -> if you can't trust a swiss banker, what's the wo
# cipher6: hire -> hire me -> hire me o -> hire me or fir -> hire me or fire me -> hire me of fire me. it -> hire me of fire me. it's ent -> hire me or fire me. it's entirely up to you. ✅
# cipher7: let's -> let's c -> let's cou -> let's count to -> let's just count to thr -> let's count to three. -> let's count to three. you ca -> let's count to three. you can do that, can't -> let's count to three. you can do that, can't you
# cipher8: histo -> history -> history i -> history isn't -> history isn't kind -> history isn't kind to -> history isn't kind to men wh -> history isn't kind to men who play g -> history isn't kind to men who play god. ✅
# cipher9: well -> well ju -> well just -> well just goes -> well just goes to -> well just goes to show -> well just goes to show, no o -> well just goes to show, no one's ind -> well just goes to show, no one's indestructi -> well just goes to show, no one's indestructible. ✅
# cipher10: i'll -> i'll do -> i'll do a -> i'll do anythi -> i'll do anything f -> i'll do anything for a -> i'll do anything for a woman -> i'll do anything for a woman with a -> i'll do anything for a woman with a knife. ✅
# cipher11: there -> there's -> there's a -> there's a sayi -> there's a saying i -> there's a saying in en -> there's a saying in england: -> there's a saying in england: where t -> there's a saying in england: where there's s -> there's a saying in england: where there's s smoke
# cihper12: that -> that la -> that last -> that last hand -> that last hand nea -> that last hand nearly -> that last hand nearly killed -> that last hand nearly killed me. ✅
# cihper13: so yo -> so you -> so you wa -> so yo want me -> so you want me to -> so you want me to be h -> so you want me to be half mo -> so you want me to be half momk, half -> so you want me to be half momk, half hitman. ✅
# cihper14: well, -> well, i -> well, i l -> well, i like t -> well, i like to do -> well, i like to do som -> well, i like to do some thin -> well, i like to do some things the o -> well, i like to do some things the old-fashi -> well, i like to do some things the old-fashioned
# cihper15: i tho -> i thoug -> i thought -> i thought chri -> i thought christma -> i thought christmas on -> i thought christmas only com -> i thought christmas only come once -> i thought christmas only come once a year. ✅
# cihper16: that' -> that's -> that's ju -> that's just as -> that's just as bad -> that's just as bad as -> that's just as bad as listen -> that's just as bad as listening to t -> that's just as bad as listening to the beatl -> that's just as bad as listening to the beatles w
# cihper17: a mar -> a marti -> a martini -> a martini. sha -> a martini. shaken, -> a martini. shaken, not -> a martini. shaken, not stirr -> a martini. shaken, not stirred. ✅
  
# challenge: flg_a -> flg_aowvgyziagvfemavw37co7q=