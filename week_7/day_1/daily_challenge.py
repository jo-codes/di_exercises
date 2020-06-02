alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet = list(alphabet)
letter_keys = range(1, 27)
reverse_dict = dict(zip(letter_keys, alphabet))
forward_dict = dict(zip(alphabet, letter_keys))


# I created two dictionaries for convenience sake, as well as for less iteration all over the place. Keeping code dry doesn't mean never hard coding anything...

decode = False
cipher = int(input("Please input cipher "))
text = input("Please enter message ")
choice = input('To encode press enter, to decode type "decode" ')

if len(choice) > 0:
    decode = True


def add_cipher(num, cipher):
    number = num + cipher
    if number > 26:
        return number - 26
    elif number <= 0:
        return number + 26
    else:
        return number


def crypt_or_decrypt(decode, msg, cipher):
    if decode:
        cipher = cipher * -1

    msg_nums = []
    encoded_nums = []
    for letter in msg:
        if letter in forward_dict:
            msg_nums.append(forward_dict[letter])

    for num in msg_nums:
        encoded_nums.append(add_cipher(num, cipher))

    encoded_msg = []

    for num in encoded_nums:
        if num in reverse_dict:
            encoded_msg.append(reverse_dict[num])

    print(''.join(encoded_msg))


crypt_or_decrypt(decode, text, cipher)

# works for words without spaces. I'm pretty proud of reusing the above function by inputing a boolean for decode!
