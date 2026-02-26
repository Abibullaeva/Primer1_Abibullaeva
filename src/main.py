def get_vowels(String):
    return [each for each in String if each in "aeiou"]

if __name__ == "__main__":
    print(get_vowels("animal")) # ['a', 'i', 'a']
    print(get_vowels("sky")) # []
    print(get_vowels("football")) # ['o', 'o', 'a']
