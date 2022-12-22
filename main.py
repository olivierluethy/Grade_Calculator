def calculate_magic_mark(total_marks, num_marks, desired_average):
    """
    Calculates the mark a user needs to get to achieve a desired average.
    
    Parameters:
        total_marks (float): The sum of all marks entered by the user.
        num_marks (int): The number of marks entered by the user.
        desired_average (float): The average the user wants to achieve.
        
    Returns:
        float: The mark the user needs to get to achieve the desired average.
    """
    # Calculate the magic mark using the formula (num_marks + 1) * desired_average - total_marks
    magic_mark = (num_marks + 1) * desired_average - total_marks
    
    # If the magic mark is greater than 6, it is not allowed and a message is printed
    if magic_mark > 6:
        print("The wished mark isn't possible")
        return None
    else:
        return magic_mark
    

def get_marks():
    """
    Prompts the user to enter marks until they stop the input.
    
    Returns:
        tuple: A tuple containing the sum of all marks and the number of marks entered by the user.
    """
    total_marks = 0
    num_marks = 0
    
    # Loop until the user inputs 's' to stop
    while True:
        mark = input("Please enter mark (s for stop):\t\t")
        if mark == 's':
            break
        
        try:
            mark = float(mark)
            # If the mark is greater than 6, it is not allowed
            if mark > 6:
                print("Mark isn't valid.")
            else:
                # Add the mark to the total sum and increment the number of marks
                total_marks += mark
                num_marks += 1
        # If the input cannot be converted to a float, it is not a valid mark
        except ValueError:
            print("Invalid input. Please enter a valid mark or 's' to stop.")
    
    # Return the total sum of marks and the number of marks
    return total_marks, num_marks


def main():
    print("Welcome To BiteX")
    print("A program to calculate the mark you need to get the average wanted\n")
    
    # Loop the program until the user wants to exit
    while True:
        # Get the total sum of marks and the number of marks from the user
        total_marks, num_marks = get_marks()
        
        # Loop until the user inputs a valid average
        while True:
            desired_average = input("Please enter wished average:\t\t")
            try:
                desired_average = float(desired_average)
                # If the average is greater than 6, it is not allowed
                if desired_average > 6:
                    print("Mark isn't valid.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid average.")
        
        # Calculate the magic mark and print the result if it is possible
        magic_mark = calculate_magic_mark(total_marks, num_marks, desired_average)
        if magic_mark is not None:
