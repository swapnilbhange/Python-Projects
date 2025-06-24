import smtplib  # Import the SMTP library to send emails using the Simple Mail Transfer Protocol

# Prompt user to enter the recipient's email address
to = input("Enter the Email of Recipient:\n")

# Prompt user to enter the email content
content = input("Enter the Content of mail:\n")

# Define a function to send email
def sendemail(to, content):
    # Step 1: Connect to Gmail's SMTP server on port 587 (TLS)
    server = smtplib.SMTP('smtp.gmail.com', 587)

    # Step 2: Identify this client to the server
    server.ehlo()

    # Step 3: Start TLS encryption for secure communication
    server.starttls()

    # Step 4: Login to the sender's email account
    # ⚠️ NOTE: Replace 'senderemail@gmail.com' and '1234' with actual email and app password
    server.login('senderemail@gmail.com', '1234')

    # Step 5: Send the email from sender to recipient with the specified content
    server.sendmail('senderemail@gmail.com', to, content)

    # Step 6: Close the connection to the SMTP server
    server.close()

# Call the sendemail function with user-provided inputs
sendemail(to, content)
