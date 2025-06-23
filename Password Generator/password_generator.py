import string  # Imports module containing ASCII letters, digits, punctuation
import random  # For random selection and shuffling

# Define a function to generate the password
def gen():
    # Step 1: Define character sets to include in the password
    s1 = string.ascii_uppercase   # Uppercase A-Z
    s2 = string.ascii_lowercase   # Lowercase a-z
    s3 = string.digits            # Digits 0-9
    s4 = string.punctuation       # Special characters like !@#$%

    # Step 2: Ask user for desired password length
    passlen = int(input("Enter the Password Length\n"))

    # Step 3: Create an empty list to hold all possible characters
    s = []
    # Step 4: Add all character sets to the list
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    # Step 5: Shuffle the combined character list for randomness
    random.shuffle(s)

    # Step 6: Join the first `passlen` characters from the shuffled list
    pas = "".join(s[0:passlen])

    # Step 7: Print the generated password
    print(pas)

# Step 8: Call the password generator function
gen()
