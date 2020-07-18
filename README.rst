# CryptoMagic
# Description

An encrypting / decrypting utility for Linux. This utility will take any ASCII file or folder and encrypt it in such a way
that its contents are not readable – until they are decrypted by the utility.


# Specification
1. The utility is called **cryptoMagic** and is written in Python
    a. The utility has 2 command-line switches – they are –encrypt and –decrypt
    b. If none of these switches is specified, then –encrypt is assumed
    c. The utility also takes the name of an **ASCII input file** to encrypt/decrypt as an argument.
    d. For example:
       cryptoMagic –encrypt myFile.txt  will encrypt the contents of the myFile.txt file
       cryptoMagic myFile.txt  will encrypt the contents of the myFile.txt file
       cryptoMagic –decrypt myFile.crp  will decrypt the contents of the myFile.crp file

2. When the utility is asked to –encrypt an ASCII file, it will take the input filename and produce the encrypted file with the same
    base filename and an .crp file extension
       a. For example:
          cryptoMagic –encrypt myFile.txt  will produce an encrypted file called myFile.crp

3. When the utility is asked to –decrypt an encrypted file, it will take the input filename and produce the decrypted file with the
    same base filename and an .txt file extension
       a. For example:
          cryptoMagic –decrypt myFile.crp  will produce a decrypted file called myFile.txt

4. It should be noted that the input file can have any file extension. When asked to _encrypt_ , it will replace the existing file
    extension (if any) with .CRP. Similarly when asked to _decrypt_ , it will replace the existing file extension (if any) with .TXT
       a. Encrypting always produces a file with a .CRP extension, decrypting always produces a file with a .TXT extension
       b. Also note that when asked to encrypt or decrypt a file that has no extension! In this case, it will only append the .TXT (if decrypting) and .CRP (if encrypting)

5. Each line (up to and including the carriage return (noted as <CR> below)) in the unencrypted ASCII file is guaranteed of being less
    than 120 characters. The utility processes the input ASCII file one line at a time. It continues to process the input file
    until it reaches the end of the file.
```       a. Please note that it is not guaranteed that each line actually ends in a carriage return ... how will you handle that?  ```
# Encryption Scheme
6. The encryption scheme is applied to each character in the line:
    a. If the character is a **<tab>** (ASCII value 9) then simply transform it into the output character sequence **TT**.
    b. The **carriage return** characters are **not** to be **encrypted** – they are left as is in the resultant output file (the **<CR>** in the
       example below is meant for illustration **only** – do not output “<CR>”)
       NOTE: The term “carriage return” in this document does not apply to any specific ASCII code. It applies to the typical
       end-of-line character that exists in TEXT files within the Linux OS. You may want to investigate what constitutes a
       _carriage return_ (i.e. end-of-line character in a TEXT file) in the Linux OS
    c. If is not a tab or a carriage return character, then apply the encryption scheme in steps d through f below
    d. Take the ASCII code for the input character and subtract a value of 16 from it. Let’s call this resultant value “outChar”
    e. If the resulting outChar value is less than 32, then another step must be taken: outChar = (outChar – 32) + 144
    f. You need to write the ASCII value of the new encrypted character (i.e. outChar) to the destination file as a 2 digit
       hexadecimal value. Note that this will effectively double the length of the input line in terms of size ...
       For example – if the input (unencrypted) file is:
          Hello There how are you?<CR>
          My name is Sean Clarke.<tab>I like software!<CR>
       Then the encrypted file is:
          38555C5C5F80445855625580585F678051625580695F652F<CR>
          3D69805E515D55805963804355515E80335C51625B558ETT39805C595B5580635F56646751625581<CR>
7. Each line (up to an including the carriage return (if it exists)) in the encrypted ASCII file is guaranteed of being less than 255
    characters. Remember - while processing the input ASCII file you need to process one line at a time.
    
# Decryption Scheme
8. The decryption scheme is applied to each pair of characters in the input line:
    a. You need to see if the pair of characters you are processing is the sequence **TT** – if so, then simply transform this pair of
       characters into a **<tab>** character (ASCII value 9) in the output file.
    b. If the pair of characters is not the sequence TT, then translate the first character of the pair by multiplying its face value by 16. 
    Remember that hex values of A through F take on the _face values_ of 10 through 15. Then add the _face value_ of the second character in the pair. 
        Let’s call the resulting value “outChar”. For example:
            - Reading the pair of characters “38” from the encrypted file will translate into an outChar value of 56 decimal.
            - Reading the pair of characters “5C” from the encrypted file will translate into an outChar value of 92 decimal.
    c. Now you need to add 16 to outChar.
    d. If the resulting outChar value is greater than 127, then another step must be taken: outChar = (outChar - 144) + 32
    e. The outChar value now contains the decrypted ASCII code for the character that you have just decoded. So take this
        decrypted character value (i.e. outChar) and write it to the destination file as a character.
    f. The **carriage return** characters are **not** to be **decrypted** – they are left as is in the resultant file.
    For example – if the input (encrypted) file is:
    4458596380555E5362696064595F5E80635358555D55805963806062556464698067555962548E<CR>
    39635E87648059642F812F<CR>
    Then the decrypted file is:
    This encryption scheme is pretty weird. <CR>

    Isn't it?!? <CR>

