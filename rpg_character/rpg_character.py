def create_character(character_name, strength, intelligence, charisma):
    # Validate character name
    if not isinstance(character_name, str):
        return "The character name should be a string"
    if len(character_name) > 10:
        return "The character name is too long"
    if ' ' in character_name:
        return "The character name should not contain spaces"

    # Validate stats are integers
    stats = [strength, intelligence, charisma]
    if not all(isinstance(s, int) for s in stats):
        return "All stats should be integers"

    # Validate stats range
    if not all(1 <= s <= 4 for s in stats):
        if not all(1 <= s for s in stats):
            return "All stats should be no less than 1"
        else:
            return "All stats should be no more than 4"

    # Validate sum
    if sum(stats) != 7:
        return "The character should start with 7 points"

    # Generate dots
    def dots(value):
        return '●' * value + '○' * (10 - value)

    # Return formatted string
    return f"{character_name}\nSTR {dots(strength)}\nINT {dots(intelligence)}\nCHA {dots(charisma)}"
