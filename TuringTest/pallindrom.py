class Palindrome:
    @staticmethod
    def is_palindrome(word):
        #Please write your code here.
        x = word.lower()
        y = x[::-1]
        r = False
        if x == y:
            r = True
        return(word + ' : %s' % r)
        return None

print('Input the word : ')
word = input()
print(Palindrome.is_palindrome(word))