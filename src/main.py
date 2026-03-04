def get_vowels(string_in):
    """Returns a list of vowels from the input string (case-insensitive)."""
    return [char for char in string_in if char.lower() in "aeiou"]

if __name__ == "__main__":
    # Test cases
    print(get_vowels("animal"))    # Expected: ['a', 'i', 'a']
    print(get_vowels("sky"))       # Expected: []
    print(get_vowels("football"))  # Expected: ['o', 'o', 'a']
    print(get_vowels("ALPHABET"))  # Case-insensitive check: ['A', 'A', 'E']
