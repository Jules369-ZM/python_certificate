# Caesar Cipher

A Python implementation of the Caesar cipher encryption/decryption algorithm.

## What is Caesar Cipher?

The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet. For example, with a shift of 3:
- "HELLO" becomes "KHOOR"
- "WORLD" becomes "ZRUOG"

Named after Julius Caesar, who reportedly used it to protect messages.

## Features

- Encrypt and decrypt text using Caesar cipher
- Command-line interface for easy use
- Importable functions for programmatic use
- Handles both uppercase and lowercase letters
- Preserves non-alphabetic characters (spaces, punctuation, numbers)

## Installation

Clone or download this repository. No external dependencies required - works with standard Python 3.

## Usage

### Interactive Tool

Run the interactive application:

```bash
cd caesar_cipher
python3 main.py
```

This provides a menu to encrypt, decrypt, or run examples interactively.

### Command Line

```bash
cd caesar_cipher

# Encrypt text
python caesar_cipher.py encrypt "HELLO WORLD" 3
# Output: KHOOR ZRUOG

# Decrypt text
python caesar_cipher.py decrypt "KHOOR ZRUOG" 3
# Output: HELLO WORLD

# Encrypt with different shift
python caesar_cipher.py encrypt "PYTHON" 5
# Output: UDWHOI
```

### As Python Module

```python
from caesar_cipher import encrypt, decrypt

# Encrypt
ciphertext = encrypt("HELLO", 3)
print(ciphertext)  # KHOOR

# Decrypt
plaintext = decrypt("KHOOR", 3)
print(plaintext)   # HELLO

# Using caesar_cipher function directly
from caesar_cipher import caesar_cipher

encrypted = caesar_cipher("HELLO", 3)    # Forward shift
decrypted = caesar_cipher("KHOOR", -3)   # Backward shift
```

## Examples

```
Original:  "Meet me at the bridge"
Shift:     7
Encrypted: "Tlmeet at kat tolslg ft"

Original:  "Programming is fun"
Shift:     4
Encrypted: "Tvsecwvkpi my kwv"

Original:  "Python 3.9!"
Shift:     13
Encrypted: "Clguba 3.9!"
```

## Security Note
