# Grade Calculator
This code is a program that helps a user calculate the mark they need to get in order to achieve a desired average. 

## How the program works
The program prompts the user to input marks, and once the user is finished entering marks, they can input the desired average. The program will then calculate the mark the user needs to get to achieve that average and print it out. If the user wants to calculate a new average, they can input 'Y' to start the process again, or they can input 'N' to exit the program.

The program has two functions: type_mark() and get_magic_mark(). The type_mark() function is used to get the marks from the user and store them in a total sum. The get_magic_mark() function is used to calculate the mark the user needs to get to achieve the desired average.

The type_mark() function has a while loop that prompts the user to input a mark. If the input is a valid number or decimal, it is added to the total sum and the loop continues. If the input is a letter, the program calls the get_magic_mark() function.

The get_magic_mark() function has a while loop that prompts the user to input a desired average. If the input is a valid number or decimal, the program uses a formula to calculate the mark the user needs to get to achieve that average. The program then checks if the calculated mark is greater than 6, as marks higher than 6 are not allowed. If the calculated mark is valid, the program prints out the result and prompts the user to input 'Y' to calculate a new average or 'N' to exit the program. If the user inputs an invalid letter, the program prompts the user to enter a valid input.