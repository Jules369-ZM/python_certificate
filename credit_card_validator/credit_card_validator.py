def verify_card_number(card_number):
    """
    Verifies a credit card number using the Luhn algorithm.

    Args:
        card_number (str): The credit card number as a string, may contain dashes or spaces.

    Returns:
        str: "VALID!" if the number is valid, "INVALID!" otherwise.
    """
    # Remove non-digit characters
    cleaned = ''.join(c for c in card_number if c.isdigit())

    # Check if there are any digits
    if not cleaned:
        return "INVALID!"

    # Convert to list of integers
    digits = [int(d) for d in cleaned]

    # Double every other digit starting from the second last (right to left, excluding check digit)
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    # Sum all digits
    total = sum(digits)

    # Check if sum is multiple of 10
    if total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"


# Test cases
if __name__ == "__main__":
    print("453914889:", verify_card_number("453914889"))
    print("4111-1111-1111-1111:", verify_card_number("4111-1111-1111-1111"))
    print("1234 5678 9012 3456:", verify_card_number("1234 5678 9012 3456"))
