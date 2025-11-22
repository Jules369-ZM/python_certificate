#!/usr/bin/env python3
"""
Caesar Cipher implementation in Python.

This module provides functions to encrypt and decrypt text using the Caesar cipher
algorithm, which shifts letters by a specified number of positions in the alphabet.

Usage as script:
    python caesar_cipher.py encrypt "HELLO" 3
    python caesar_cipher.py decrypt "KHOOR" 3

Usage as module:
    from caesar_cipher import encrypt, decrypt
    >>> encrypt("HELLO", 3)
    'KHOOR'
    >>> decrypt("KHOOR", 3)
    'HELLO'
"""

def caesar_cipher(text: str, shift: int) -> str:
    """
    Apply Caesar cipher shift to the given text.

    Args:
        text: The text to shift
        shift: Number of positions to shift (positive for forward, negative for backward)

    Returns:
        The shifted text
    """
    result = []
    for char in text:
        if char.isupper():
            base = ord('A')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        elif char.islower():
            base = ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return ''.join(result)

def encrypt(text: str, shift: int) -> str:
    """
    Encrypt text using Caesar cipher.

    Args:
        text: The plain text to encrypt
        shift: The shift key (1-25)

    Returns:
        The encrypted text
    """
    return caesar_cipher(text, shift)

def decrypt(text: str, shift: int) -> str:
    """
    Decrypt text using Caesar cipher.

    Args:
        text: The encrypted text to decrypt
        shift: The shift key used for encryption (1-25)

    Returns:
        The decrypted text
    """
    return caesar_cipher(text, -shift)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Caesar Cipher encryption/decryption tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python caesar_cipher.py encrypt "HELLO WORLD" 3
  python caesar_cipher.py decrypt "KHOOR ZRUOG" 3
        """
    )

    parser.add_argument(
        'operation',
        choices=['encrypt', 'decrypt'],
        help='Choose whether to encrypt or decrypt'
    )
    parser.add_argument(
        'text',
        help='The text to encrypt or decrypt'
    )
    parser.add_argument(
        'shift',
        type=int,
        help='The shift value (1-25 for encryption/decryption)'
    )

    args = parser.parse_args()

    if args.operation == 'encrypt':
        result = encrypt(args.text, args.shift)
    else:
        result = decrypt(args.text, args.shift)

    print(result)
