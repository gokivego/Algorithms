# Steps to solve the problem:

* Step 1: Multiply the 2 largest n-digit numbers: The number of digits in the resulting number would be 2n

* Step 2: Take the first n-digits and create a function to form a palindrome (first_half)

* Step 3: Our main goal is to factorize this palindrome into two n-digit numbers,it is possible that this number can't be expressed as product of two n-digit numbers

* Step 4: We first start with assuming a factor of this number, start with the largest n-digit number. If this number doesn't divide the palindrome then decrement this number by 1 and continue.

* Step 5: We have a stopping criterion. If we reach the condition (This number)^2 < palindrome, then we know can break the loop. This is because a palindrome can be a product of two numbers, one greater than the sqrt(palindrome) and the other less than the sqrt(palindrome). The condition ensures that we havent found a number greater than the sqrt(palindrome).

* Step 6: At this point we decrement first_half by 1 and then create a new palindrome. Go back to step Step 4 and repeat until we find a factor that is greater than the sqrt(palindrome) and that divides into the palindrome. 


