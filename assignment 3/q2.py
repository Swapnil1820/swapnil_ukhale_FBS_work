# Write a program to input any alphabet and check whether it is vowel or consonant.

chr=input('enter an alphabet -')

if (chr in 'aeiouAEIOU'):
    print('it is a vowel')
else:
    print('it is a constant')