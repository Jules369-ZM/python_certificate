#!/usr/bin/env python3
"""
Main entry point for the Caesar Cipher application.

This script provides a simple interface to use the Caesar cipher functionality.
"""

from caesar_cipher import encrypt, decrypt

def main():
    print("Caesar Cipher Tool")
    print("=" * 20)
    print("1. Encrypt text")
    print("2. Decrypt text")
    print("3. Run example")
    print("4. Exit")

    while True:
        try:
            choice = input("\nChoose an option (1-4): ").strip()

            if choice == '1':
                text = input("Enter text to encrypt: ")
                shift = int(input("Enter shift value (1-25): "))
                result = encrypt(text, shift)
                print(f"Encrypted: {result}")

            elif choice == '2':
                text = input("Enter text to decrypt: ")
                shift = int(input("Enter shift value (1-25): "))
                result = decrypt(text, shift)
                print(f"Decrypted: {result}")

            elif choice == '3':
                # Run a simple example
                example_text = "HELLO WORLD"
                shift = 3
                encrypted = encrypt(example_text, shift)
                decrypted = decrypt(encrypted, shift)
                print(f"Example: '{example_text}' -> encrypt({shift}) -> '{encrypted}' -> decrypt({shift}) -> '{decrypted}'")

            elif choice == '4':
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please enter 1-4.")

        except ValueError:
            print("Error: Shift must be a number.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
