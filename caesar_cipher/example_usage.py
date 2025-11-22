#!/usr/bin/env python3
"""
Example usage of the Caesar Cipher implementation.

This file demonstrates how to use the caesar_cipher module functions
for encrypting and decrypting text.
"""

from caesar_cipher import encrypt, decrypt, caesar_cipher

def main():
    print("Caesar Cipher Example Usage")
    print("=" * 40)

    # Basic encryption/decryption
    plaintext = "HELLO WORLD"
    shift = 3

    print(f"Plaintext: {plaintext}")
    print(f"Shift: {shift}")

    encrypted = encrypt(plaintext, shift)
    print(f"Encrypted: {encrypted}")

    decrypted = decrypt(encrypted, shift)
    print(f"Decrypted: {decrypted}")
    print()

    # Using caesar_cipher function directly
    print("Using caesar_cipher function directly:")
    forward_shift = caesar_cipher("HELLO", 3)
    print(f"caesar_cipher('HELLO', 3): {forward_shift}")

    backward_shift = caesar_cipher("KHOOR", -3)
    print(f"caesar_cipher('KHOOR', -3): {backward_shift}")
    print()

    # Handling mixed case and special characters
    print("Handling mixed case and special characters:")
    text = "Python 3.9 is Great!"
    encrypted = encrypt(text, 5)
    decrypted = decrypt(encrypted, 5)

    print(f"Original: {text}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print()

    # Brute force decryption (trying all shifts)
    print("Brute force decryption attempt:")
    encrypted_message = "Udwkud lq vwdfwz ldrss"
    print(f"Encrypted message: {encrypted_message}")
    print("Trying all shifts:")

    for shift in range(1, 26):
        possible_plaintext = decrypt(encrypted_message, shift)
        print(f"Shift {shift:2d}: {possible_plaintext}")
    print()

    # Known answer: the message was encrypted with shift 3
    correct_decrypt = decrypt(encrypted_message, 3)
    print(f"Correct decryption (shift 3): {correct_decrypt}")

if __name__ == "__main__":
    main()
