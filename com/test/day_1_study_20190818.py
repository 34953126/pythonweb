12345password_list = ['*#*#','12345']
def account_login():
    password = input('Password:')
    password_correct = password = password_list[-1]
    password_reset = password = password_list[0]
    if password_correct:
        print("Login Success!")
    elif password_reset:
        new_password = print('Enter a new Password!')
        password_list.append(new_password)
        print('Your password has changed successfully!')
        account_login()
    else:
        print('Wrong password or invalid input!')
        account_login()

account_login()


#循环
for  ever_letter in 'hello world!':
print(ever_letter)