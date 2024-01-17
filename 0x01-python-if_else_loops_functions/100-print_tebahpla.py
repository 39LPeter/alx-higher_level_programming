#!/usr/bin/python3
for character in reversed(range(97, 123)):
    print("{:c}".format(character if (character % 2 == 0) else (character - 32)), end='')
