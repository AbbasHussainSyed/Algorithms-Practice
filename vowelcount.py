# code to count vowels in a string
def vowel_count(text, vowel_count):

    for vowel in text.lower():
        if vowel in 'aeiou':
            vowel_count += 1;
    print(vowel_count)

vowel_count("ABBAS HUSSAIN", vowel_count=0)