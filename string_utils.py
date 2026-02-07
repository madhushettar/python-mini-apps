# String manipulation utilities

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

if __name__ == "__main__":
    test_str = "Hello World"
    print("Reversed:", reverse_string(test_str))
    print("Vowel count:", count_vowels(test_str))
