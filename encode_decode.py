"""
Message Encoder & Decoder

A simple Python CLI application that encodes and decodes text messages
using a custom encryption algorithm.

Author: Your Name
Language: Python 3.x
"""

import random
import string

# Allowed key lengths
VALID_KEYS = [3, 4, 6]


def generate_random_string(length: int) -> str:
    """
    Generate a random lowercase string.

    Args:
        length (int): Length of random string.

    Returns:
        str: Random lowercase string.
    """
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def encode_message(message: str, key: int) -> str:
    """
    Encode a message.

    Rules:
    - Words with less than 3 characters are reversed.
    - Longer words move first character to the end.
    - Random prefix and suffix are added.

    Args:
        message (str): Original message.
        key (int): Encryption key.

    Returns:
        str: Encoded message.
    """
    encoded_words = []

    for word in message.split():

        if len(word) < 3:
            encoded_words.append(word[::-1])
            continue

        transformed = word[1:] + word[0]

        prefix = generate_random_string(key)
        suffix = generate_random_string(key)

        encoded_words.append(prefix + transformed + suffix)

    return " ".join(encoded_words)


def decode_message(message: str, key: int) -> str:
    """
    Decode an encoded message.

    Args:
        message (str): Encoded message.
        key (int): Decryption key.

    Returns:
        str: Decoded message.
    """
    decoded_words = []

    for word in message.split():

        if len(word) < 3:
            decoded_words.append(word[::-1])
            continue

        if len(word) <= key * 2:
            raise ValueError(
                f"Invalid encrypted word or incorrect key: '{word}'"
            )

        stripped = word[key:-key]

        original = stripped[-1] + stripped[:-1]

        decoded_words.append(original)

    return " ".join(decoded_words)


def get_key() -> int:
    """
    Ask the user for a valid encryption/decryption key.

    Returns:
        int: Valid key.
    """
    while True:
        try:
            key = int(input("Enter key (3, 4, or 6): "))

            if key not in VALID_KEYS:
                print("❌ Key must be 3, 4, or 6.\n")
                continue

            return key

        except ValueError:
            print("❌ Please enter a valid number.\n")


def display_menu() -> None:
    """Display menu options."""
    print("\n" + "=" * 45)
    print("      MESSAGE ENCODER & DECODER")
    print("=" * 45)
    print("1. Encode Message")
    print("2. Decode Message")
    print("3. Exit")
    print("=" * 45)


def main():
    """Main program."""

    print("\nWelcome to Message Encoder & Decoder!")

    while True:

        display_menu()

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":

            message = input("\nEnter message to encode: ")

            key = get_key()

            encoded = encode_message(message, key)

            print("\n✅ Encoded Message:")
            print(encoded)

        elif choice == "2":

            message = input("\nEnter message to decode: ")

            key = get_key()

            try:
                decoded = decode_message(message, key)

                print("\n✅ Decoded Message:")
                print(decoded)

            except ValueError as error:
                print(f"\n❌ {error}")

        elif choice == "3":

            print("\nThank you for using Message Encoder & Decoder.")
            print("Goodbye!")

            break

        else:

            print("\n❌ Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()