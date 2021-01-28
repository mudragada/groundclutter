"""
1. Input a string
2. Print "True" or "False" whether the string is palindrome
"""

def main():
    var = input("Enter a string: ")
    print(isPalindrome(var))

def isPalindrome(str):
    if (len(str) <= 1):
        return True
    return isPalRecursive(str, 0, len(str)-1)
def isPalRecursive(str, start, end):
    if(str[start] != str[end]):
        return False
    if(start < end + 1):
        return isPalRecursive(str, start+1, end-1)

if __name__ == "__main__":
    main()
