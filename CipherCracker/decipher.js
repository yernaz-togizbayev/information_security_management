function decrypt(ciphertext) {
    // 直接使用提供的映射关系
    const charMap = {
        a: 'a',
        b: 'j',
        c: 'v',
        d: 'q',
        e: 'b',
        f: 'w',
        g: 'h',
        h: 'x',
        i: 'f',
        j: 'p',
        k: 'i',
        l: 'm',
        m: 'g',
        n: 'n',
        o: 'r',
        p: 's',
        q: 'e',
        r: 't',
        s: 'y',
        t: 'z',
        u: 'c',
        v: 'k',
        w: 'd',
        x: 'o',
        y: 'l',
        z: 'u'
    };

    // 替换密文中的字母
    let decryptedText = '';
    for (let char of ciphertext) {
        if (char.match(/[a-z]/i)) {
            decryptedText += charMap[char.toLowerCase()] || char;
        } else {
            decryptedText += char;
        }
    }

    return decryptedText;
}

let ciphertext = `
tzs_wudysghjwakcbln27lgb53g=
`;
console.log(decrypt(ciphertext));