# filthy-password-generator-py

[![MIT licensed](https://img.shields.io/badge/license-MIT-green.svg)](https://raw.githubusercontent.com/gabfl/password-generator-py/master/LICENSE)

## Description

One day I was using a password generator it a few of the ones coming out contained some filthy output, not intentionally of course, just a side effect of using a pre made dictionary file. After the creator used a list of obscene words to clean it up, I decided it was so funny that I would use the obscene words exclusively and see what kind of filth comes out, and lo and behold we have the filthy password generator.

## Setup
Just run:
'''
python setup.py install
'''

Then you can run
'''
python getfilthy.py
'''
for a continuous stream of filth.


## Use within Python script

```python
>>> from filthypasswordgenerator import pwgenerator

>>> pwgenerator.generate()
'Ass+Snatch:Pissing;553'
```

## Examples

Here are a few filthy passwords that have been generated:

```
Orgy-Anus;70+Tranny
Vibrator=268%Nambla_Camslut
466=Paki=Kinky-Twink
Ecchi:Jailbait;Bollocks.890
Slanteye%719*Ecchi=Dildo
Faggot;722-Hooker=Bulldyke
```




## Advanced options

```
passwordgenerator [-h] [-n MIN_WORD_LENGTH] [-x MAX_WORD_LENGTH]
                  [-i MAX_INT_VALUE] [-e NUMBER_OF_ELEMENTS] [-s]

optional arguments:
  -h, --help            show this help message and exit
  -n MIN_WORD_LENGTH, --min_word_length MIN_WORD_LENGTH
                        Minimum length for each word
  -x MAX_WORD_LENGTH, --max_word_length MAX_WORD_LENGTH
                        Maximum length for each word
  -i MAX_INT_VALUE, --max_int_value MAX_INT_VALUE
                        Maximum value for the integer
  -e NUMBER_OF_ELEMENTS, --number_of_elements NUMBER_OF_ELEMENTS
                        Number of elements in the password (ie. 4 = 3 words +
                        1 integer)
  -s, --no_special_characters
                        Do not use special characters
```
