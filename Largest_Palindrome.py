"""
Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.

"""

class palindrome:

    def first_half_part(self):
        return int(str(self.upperBound*self.upperBound)[:int(len(str(self.upperBound*self.upperBound))/2)])

    def create_palindrome(self,first_half):
        # We need to reverse the first_half and append it to first_half and return it
        string = str(first_half)
        for i in reversed(string):
            string = string + i
        return int(string)

    def __init__(self, n):
        self.n = n
        self.upperBound = 10**self.n - 1
        self.lowerBound = 10**(self.n-1) + 1
        self.first_half = self.first_half_part()
        #print (self.first_half)

    def largestPalindrome(self):
        """
        :type n: int
        :rtype: int
        """
        if self.n == 1:
            return 9

        found_palindrome = False

        while not found_palindrome:
            self.palindrome = self.create_palindrome(self.first_half)
            #print ('palindrome: ', self.palindrome)
            i = self.upperBound
            while(i > self.lowerBound):
                if (i*i < self.palindrome):
                    break
                elif (self.palindrome % i == 0):
                    found_palindrome = True
                    break
                else:
                    i -= 1
                    #print ('i:' ,i)

            self.first_half -= 1
            #print ('first_half: ', self.first_half)

        #print ('one factor: ',self.palindrome / i)
        #print ('second factor: ', i)
        print (self.palindrome % 1337)




