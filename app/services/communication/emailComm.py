import smtplib
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Generate a random OTP
def generate_otp(length=6):
    characters = string.digits
    otp = ''.join(random.choice(characters) for i in range(length))
    print(otp)  # Optional: Print OTP for testing
    return otp

# Send an OTP email
def send_otp_email(email, otp):
    sender_email = 'amyadav@mitaoe.ac.in'   
    sender_app_password = 'YourAppPassword'  # Use an app-specific password

    subject = 'OTP Verification'
    message = f'Your OTP for email verification is: {otp}'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Connect to the SMTP server (for Gmail, use smtp.gmail.com)
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Gmail SMTP server and port
        server.starttls()

        # Enable SMTP debugging
        server.set_debuglevel(1)

        # Log in to your email account using an app password
        server.login(sender_email, sender_app_password)

        # Send the email
        server.sendmail(sender_email, email, msg.as_string())

        # Close the SMTP server connection
        server.quit()
        print('OTP email sent successfully.')
    except Exception as e:
        print('Error sending OTP email:', str(e))

# Function to verify OTP
def verify_otp(user_input, otp):
    # Compare the user's input with the OTP
    return user_input == otp

# Example usage
if __name__ == '__main__':
    # Generate an OTP
    generated_otp = generate_otp()

    # Simulate user input
    user_input = input("Enter the OTP sent to your email: ")

    # Verify the OTP
    if verify_otp(user_input, generated_otp):
        print("OTP is valid. User is verified.")
    else:
        print("Invalid OTP. User verification failed.")

    # Send the OTP via email (you can call this in your registration or verification process)
    email = 'krajito77@gmail.com'  # Replace with the recipient's email address
    send_otp_email(email, generated_otp)
