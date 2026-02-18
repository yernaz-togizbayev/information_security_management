def hex_xor(hex1, hex2):
    result = []
    # Process two hex digits (one byte) at a time.
    for i in range(0, min(len(hex1), len(hex2)), 2):
        byte1 = int(hex1[i:i+2], 16)
        byte2 = int(hex2[i:i+2], 16)
        xor_byte = byte1 ^ byte2
        # Format the result as a two-digit hex string.
        result.append(format(xor_byte, '02x'))
    return ''.join(result)

def hex_to_ascii(hex_string):
    ascii_chars = []
    # Process two hex digits at a time.
    for i in range(0, len(hex_string), 2):
        hex_code = hex_string[i:i+2]
        char_code = int(hex_code, 16)
        # If the character code is within printable ASCII range, use it; otherwise, use a dot.
        if 32 <= char_code <= 126:
            ascii_chars.append(chr(char_code))
        else:
            ascii_chars.append('.')
    return ''.join(ascii_chars)

# Example usage:
cipher1 = "475857455745474556461652180d5c5e130d5b13010b040a050f540219420b56105d154d5e524654124b10125a5f52554a174009034006144b140559410416145d44535a5c4551571250465d464343165d06445212414c1513501409454643135c0b53591e424152041542160a11185a111710184b574c1a"
cipher2 = "5f5546104142570a42081113150b124d5b1650564a451a09114153595715075c424c5d58421b1452545617151749564559561406135c43525650435113135907510b1c1659111e45445b094613541b045b115a4e46510a470d46400e51461b135111175e4d09"
xor_result = hex_xor(cipher1, cipher2)

# Take the first 11 characters of the result.
plain1 = xor_result[:200]
plain2 = "7468657265666F7265"

# XOR plain1 and plain2, then convert to ASCII.
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