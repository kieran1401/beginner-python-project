print("Welcome to my first Python project\n")

print("I want to learn a bit about you, so I can use your data for creating the best AI and takeover the world\n")

# Ask the user for their name, which will be stored in 'name'
name = input("First, tell me your name: ")

print("\nNice to meet you, " + name + "... I'm going to need more than just your name if I'm going to take over the world\n")

# Ask the user for their age and convert the input to an integer
age = int(input("Tell me how old you are: "))

# Convert age back to string for concatenation
print("\nGreat, so you are " + name + " and you are " + str(age))

# Create a new variable that doubles the user's age
x2age = age * 2

# Convert x2age to string for concatenation
print("\nSo " + name + ", for this to work, we must double your age, this means you are now " + str(x2age))

# List of humans who have already signed up
humans = ["Bob", "Dave", "Sam"]

print("\nHere is a list of humans who have already signed up to takeover the world with us: " + str(humans))

print("\nThere is one more requirment we need for you to qualify!")

# Loop to ask for gender and validate the input
while True:
    # Ask for gender and validate the input (makes it lowercase so if they type Female or Male, both will work)
    gender = input("\nAre you a Male or Female? ").strip().lower()

    if gender == "male":
        is_male = True
        is_female = False
        break
    elif gender == "female":
        is_male = False
        is_female = True
        break
    else:
        print("\nInvalid input. Please enter 'Male' or 'Female'.")

# Confirmation message if the user provided a valid gender
if is_female or is_male:
    print("\nYou are qualified to takeover the world with us... Be prepared for us to use your data to create an unstoppable AI.")