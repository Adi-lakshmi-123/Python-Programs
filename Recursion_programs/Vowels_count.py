'''To count the no.of vowels in a string'''
def countVowels(sentence):
    '''This function counts the vowels'''
    l = ['a', 'e', 'i', 'o', 'u']
    count = 0
    sentence = sentence.lower()
    for c in sentence:
        if c in l:
            count += 1
    return count


if __name__ == '__main__':
    str = "Hello, My name is Adilakshmi"
    '''Calling the above Function'''
    count = countVowels(str)
    print(count)
