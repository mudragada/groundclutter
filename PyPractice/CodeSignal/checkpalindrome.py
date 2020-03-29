"""
Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
checkPalindrome(inputString) = true;
For inputString = "abac", the output should be
checkPalindrome(inputString) = false;
For inputString = "a", the output should be
checkPalindrome(inputString) = true.
Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A non-empty string consisting of lowercase characters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 105.

[output] boolean

true if inputString is a palindrome, false otherwise.

"""


def main():
    listOfStrings = ["abba", "baba", "text", "02022020", "Sarab BaraS"]
    for inputString in listOfStrings:
        printstr = "Is {0}  Panlindrome? {1}".format(inputString, checkPalindrome(inputString))
        print(printstr)

def checkPalindrome(inputString):
    inputString = inputString.casefold()
    revString = reversed(inputString)
    if (list(inputString) == list(revString)):
        return True
    else:
        return False

if __name__ == '__main__':
    main()
