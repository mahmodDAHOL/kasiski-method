This repo has 

1- an implementation of kasiski test, this test aims to try to deduce the keyword used in the cipher text.

2- an implementation of rc4 stream cipher, it encrypts messages one byte at a time via an algorithm.

# To run the kasiski test code

1- open up command line interface.

2- move to folder that has kasiski python file.

3- write:

  python kasiski.py --cipher-text CIPHER_TEXT --max-key-len MAX_KEY_LEN
  
  where:
  
  CIPHER_TEXT is a string variable 
  
  MAX_KEY_LEN is a intiger variable, EX:MAX_KEY_LEN=5 


# To run the rc4 code

1- open up command line interface.

2- move to folder that has rc4 python file.

3- write:

  python rc4.py --plain-text PLAIN_TEXT 
  
  where:
  
  PLAIN_TEXT is a string variable represents text that will be encrypted
  
