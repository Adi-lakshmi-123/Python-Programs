'''A pangram is a string which consists of all 26 characters in a string.'''

def pangram(string):
    list="abcdefghijklmnopqrstuvwxyz"
    string=string.lower()
    for i in list:
        if i not in string:
            return False
    return True
if __name__ == "__main__":
    print(pangram("The quick brown fox jumps over the lazy dog"))
    print(pangram("hello world"))
    
