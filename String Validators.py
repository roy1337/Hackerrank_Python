Task

You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string .

Constraints


Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.



if __name__ == '__main__':
    stringtocheck = input()
    
    print (any(s.isalnum() for s in stringtocheck))
    print (any(s.isalpha() for s in stringtocheck))
    print (any(s.isdigit() for s in stringtocheck))
    print (any(s.islower() for s in stringtocheck))
    print (any(s.isupper() for s in stringtocheck))
