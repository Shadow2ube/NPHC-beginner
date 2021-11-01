# input is for getting user input (you can put a prompt in the brackets)
password = input('Password: ')

# if is for conditions, think of it as a sentence
if password == '12345':
    print('Correct password 1')

    # what if you have multiple options?
    # use elif
elif password == '54321':
    print('Correct password 2')

    # want a default route?
    # use else
else:
    print('incorrect password!')


# what's the difference between elif and else?
# else is the default track of the program
if password == '12345':
    print('Correct password 1')
else:
    print('incorrect password')

# without else, it will still show 'incorrect password'

if password == '12345':
    print('Correct password 1')

# without else, the statements are separated

print('incorrect password')

# what's the point of elif?

if password == '12345':
    print('Correct password 1')
elif password == '54321':
    print('Correct password 2')
else:
    print('incorrect password')

# what if you want to have multiple options for different inputs, but don't want to accidentally run it multiple times?

if password == '12345':
    print('Correct password 1')

if password == '54321':
    print('Correct password 2')

else:
    print('incorrect password')

# this is much slower, because first it check 12345, and even if correct, it will still check 54321. this get's slower over time.