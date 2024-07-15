import re

def validate_email(email):
    # Define the regular expression pattern for a valid email address
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Use the fullmatch method to check if the entire string matches the pattern
    if re.fullmatch(email_pattern, email):
        return True
    else:
        return False

# Example usage
emails = [
    "support@example.com",
    "user.name+tag+sorting@example.com",
    "user@example.co.uk",
    "user@subdomain.example.com",
    "invalid-email@",
    "another.invalid.email@com",
    "yet@another@invalid.email"
]

for email in emails:
    if validate_email(email):
        print(f"{email} is a valid email address.✅")
    else:
        print(f"{email} is not a valid email address.❌")
