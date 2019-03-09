## The Caesar Cipher: encrypting a message
We're going to show you four simple programs in order to present some aspects of string processing in Python. They are purposefully simple, but the lab problems will be significantly more complicated.

The first problem we want to show you is called the Caesar cipher - more details here: [Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher).

This cipher was (probably) invented and used by Gaius Julius Caesar and his troops during the Gallic Wars. The idea is rather simple - every letter of the message is replaced by letter in position *k* from the original letter, which *k* is the *chiper key* (ex. letter = ABCZ, key = 2,  A becomes C, B becomes D, C becomes E and Z becomes B).

We've written it using the following assumptions:

- it accepts Latin letters only.
- all letters of the message are in original case.

The code, fed with this message:
```
msg = AVE caesar 123 !
key = 2
```
outputs:
```
CXH echuct 123 !
```