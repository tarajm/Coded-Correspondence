"""
You and your pen pal, Vishal, have been exchanging letters for some time now. Recently, he has become interested in cryptography and the two of you have 
started sending encoded messages within your letters.

In this project, you will use your Python skills to decipher the messages you receive and to encode your own responses! Put your programming skills to the 
test with these fun cryptography puzzles. Here is his most recent letter:

    Hey there! How have you been? I've been great! I just learned about this really cool type of cipher called a Caesar Cipher. Here's how it works: 
    You take your message, something like "hello" and then you shift all of the letters by a certain offset. 

    For example, if I chose an offset of 3 and a message of "hello", I would encode my message by shifting each letter 3 places to the left with respect to the alphabet. 
    So "h" becomes "e", "e" becomes "b", "l" becomes "i", and "o" becomes "l". Then I have my encoded message, "ebiil"! Now I can send you my message and the offset and 
    you can decode it by shifting each letter 3 places to the right. The best thing is that Julius Caesar himself used this cipher, that's why it's called the Caesar Cipher! 
    Isn't that so cool! Okay, now I'm going to send you a longer encoded message that you have to decode yourself!
    
" xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
    
    This message has an offset of 10. Can you decode it?
    

#### Step 1: Decode Vishal's Message
In the cell below, use your Python skills to decode Vishal's message and print the result. Hint: you can account for shifts that go past the end of the alphabet using the modulus operator, but I'll let you figure out how!
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

translated_message = ""

for character in message:
    if character in alphabet:
        char_val = alphabet.find(character)
        translated_message += alphabet[(char_val + 10) % 26]
    else:
        translated_message += character

print(translated_message)



"""
#### Step 2: Send Vishal a Coded Message
Great job! Now send Vishal back a message using the same offset. Your message can be anything you want! Remember, encoding happens in opposite direction of decoding.
"""

message_for_v = "Hi, Vishal! Cool Cipher!  What happens next?"

translated_message_for_v = ""

for character in message_for_v:
    if character in alphabet:
        char_val = alphabet.find(character)
        translated_message_for_v += alphabet[(char_val - 10 )% 26]
    else:
        translated_message_for_v += character

print(translated_message_for_v)




#### Step 3: Make functions for decoding and coding 

# Vishal sent over another reply, this time with two coded messages!
    
#     You're getting the hang of this! Okay here are two more messages, the first one is coded just like before with an offset of ten, and it contains a hint for decoding the second message!
#     First message:
#         jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.

#     Second message:
#         bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!
    
# Decode both of these messages. 
# If you haven't already, define two functions `caesar_decode(message, offset)` and `caesar_encode(message, offset)` that can be used to quickly decode and encode messages given any offset.


message_one = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
mesasge_two = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

def decode(message, offset):
    decoded_message = ""

    for character in message:
        if character in alphabet:
            char_val = alphabet.find(character)
            decoded_message += alphabet[(char_val + offset) % 26]
        else:
            decoded_message += character
    return decoded_message

print(decode(message_one,10))
print(decode(mesasge_two,14))


message = "Pretty cool to do mutliple ciphers to keep messages secure!"

def encode(message, offset):
    encoded_message = ""

    for character in alphabet:
            if character in message:
                char_val = alphabet.find(character)
                encoded_message += alphabet[(char_val - offset) % 26]
            else:
                encoded_message += character
    return encoded_message

print(encode(message, 20))
