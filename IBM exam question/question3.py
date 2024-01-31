'''
Write python code with all the test cases pass....

The table below contains some reference values for
converting between integers (i.e., Arabic numerals)
and Roman numerals:
Roman
XL
L
XC
C
CD
D
CM
M
Arabic Roman
1
2
3
5
6



Sample Input 0

STDIN          Function
______           --------------

5    ->   numbers[]  size n = 5
1     -> numbers  = [1,2,3,4,5]
2
3
4
5

Sample Output 0

I
IV
III
IV
V

Explanation 0 
we perform the following n=5 conversions on the array [1,2,3,4,5].
       0. numbers[0]=1  corresponds to Roman numeral I. 
       1. numbers[1]=2  corresponds to Roman numeral II. 
       2. numbers[2]=3  corresponds to Roman numeral III. 
       3. numbers[3]=4  corresponds to Roman numeral IV. 
       4. numbers[4]=5  corresponds to Roman numeral V. 


Return the array ["I","II","III","IV","V"] as the answer.



'''


def convert_to_roman(number):
    values = [1, 4, 5, 9, 10, 40, 50, 90, 100]
    symbols = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C"]

    result = ""
    i = 8  # Start from the largest symbol

    while number > 0:
        div = number // values[i]
        number %= values[i]

        # Append the Roman numeral symbols to the result
        result += symbols[i] * div

        i -= 1  # Move to the next symbol

    return result


def convert_numbers_to_roman(numbers):
    return [convert_to_roman(num) for num in numbers]


# Sample Input
n = 5
numbers = [1, 2, 3, 4, 5]

# Sample Output
output = convert_numbers_to_roman(numbers)
print(output)
