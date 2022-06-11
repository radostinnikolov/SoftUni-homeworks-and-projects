def validator(password):
    is_valid = True
    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    digit_counter = 0
    for i in password:
        if i.isnumeric():
            digit_counter += 1
    if digit_counter < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        return True
    else:
        return False

password_input = input()
if validator(password_input):
    print("Password is valid")
