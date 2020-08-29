# Crypto 

An encrypting / decrypting utility (Linux/Windows). This utility will take any ASCII file or folder and encrypt it in such a way that its contents are not readable until they are decrypted by the utility.

# Table of content

- [Version](#version)
- [Specification](#specification)
- [License](#License)
- [Acknowledgments](#Acknowledgments)

## Version

![Version](https://img.shields.io/badge/Release-v1.0-blue)

# Specification

The utility is called **crypto** and is written in Python

   - The utility has 2 command-line switches
     - `–e ` or `--encrypt`
     - `–d` or `--decrypt`
   - If none of these switches is specified, `–-encrypt` is assumed
   - The utility also takes the name of an **ASCII input file** to encrypt/decrypt as an argument.
   - For example:
     - `py crypto –e/--encrypt myFile.txt` will encrypt the contents of the myFile.txt file
     - `py crypto myFile.txt` will encrypt the contents of the myFile.txt file
     - `py crypto –d/--decrypt myFile.crp` will decrypt the contents of the myFile.crp file

When the utility is asked to –encrypt an ASCII file, it will take the
input filename and produce the encrypted file with the same base filename
and an .crp file extension

   - `py crypto –-encrypt SampleFile.txt` will produce an encrypted file called SampleFile.crp
      ![Encryption Demo](demo/EncryptGif.gif)

When the utility is asked to –decrypt an encrypted file, it will take
the input filename and produce the decrypted file with the same base filename
and an .txt file extension

   - `py crypto –-decrypt SampleFile.crp` will produce a decrypted file called SampleFile.txt
      ![Decryption Demo](demo/DecryptGif.gif)

It should be noted that the input file can have any file extension. When asked to encrypt,
it will replace the existing file extension (if any) with .CRP.
Similarly when asked to decrypt, it will replace the existing file extension (if any) with .TXT
   - Encrypting always produces a file with a .CRP extension
   - Decrypting always produces a file with a .TXT extension
   - When asked to encrypt or decrypt a file that has no extension crypto
     will append the .TXT (if decrypting) and .CRP (if encrypting)
Each line (up to and including the carriage return (noted as <CR\> below))
in the unencrypted ASCII file is guaranteed of being less than 120 characters.
Crypto will process the input ASCII file one line at a time
and will continue to process the input file until you reach the end of the file.

## Encryption scheme

The encryption scheme is applied to each character in the line:

- If the character is a **\<tab\>** (ASCII value 9) it will simply transform it into the output character sequence **TT**.
- The **carriage return** characters are **not encrypted** – they are left as is in the resultant output file.
- NOTE: The term “carriage return” in this document does not apply to any specific ASCII code.
  It applies to the typical end-of-line character that exists in TEXT files within the Linux OS.
- If is not a tab or a carriage return character, then apply the encryption scheme in steps below
- Take the ASCII code for the input character and subtract a value of 16 from it.
- If the resulting outChar value is less than 32, then another step is taken: `outChar = (outChar – 32) + 144`
- Crypto will write the ASCII value of the new encrypted character
  (i.e. outChar) to the destination file as a 2 digit hexadecimal value.
  - For example
    - ```
      Hello There how are you?<CR\>
      My name is Sean Clarke.<tab\>I like software!\<CR\>
      ```
  - The encrypted file is:
    - ```
      38555C5C5F80445855625580585F678051625580695F652F<CR\>
      3D69805E515D55805963804355515E80335C51625B558ETT39805C595B5580635F56646751625581<CR\>
      ```

##Decryption scheme  
The decryption scheme is applied to each pair of characters in the input line:

- If the pair of characters is the sequence **TT**
  it simply transforms into a **<tab\>** character (ASCII value 9) in the output file.
- If the pair of characters is not the sequence **TT**, it translates it from hex to decimal
  - For example:
    - The pair of characters “38” from the encrypted file will translate into an outChar value of 56 decimal.
    - The pair of characters “5C” from the encrypted file will translate into an outChar value of 92 decimal.
- 16 is addedto outChar.
- If the resulting outChar value is greater than 127,
  then another step is taken: `outChar = (outChar - 144) + 32`
- The outChar value now contains the decrypted ASCII code for the character that you have just decoded.
  This decrypted character value (i.e. outChar) will be written to the destination file as a character.
- The **carriage return** characters are **not decrypted**. They are left as is in the resultant file.
  - For example – if the input (encrypted) file is:
    - ```
      4458596380555E5362696064595F5E80635358555D55805963806062556464698067555962548E<CR\>
      39635E87648059642F812F<CR\>
      ```
  - Then the decrypted file is:
    - ```
      This encryption scheme is pretty weird. <CR\>
      Isn't it?!? <CR\>
      ```

## .JPEG

### `Coming Soon - V2`

# Setup

## Python Virtual Env

With python installed, run:

```
python -m venv env
```

Then:

```
# On Windows
.\env\Scripts\Activate.ps1
# On Unix
./env/Scripts/activate
```

Install python packages with

```
pip install -r requirements.txt
```

## Formatting

This project uses [flake8](https://flake8.pycqa.org/en/latest/index.html) for linting, and [black](https://black.readthedocs.io/en/stable/index.html) for formatting.

With the virtual env activated, run:

```
black
flake8
```

# License

This project is licensed under the MIT License - see the
[LICENSE.md](LICENSE.md) file for details

# Acknowledgments

- Sean Clarke
- Kai Prince
