#! /usr/bin/env python
# -*- coding: utf-8 -*-

fizz = None
buzz = None
#fizzbuzz = None

print "!!!Bienvenidos a FizzBuzz!!! "

try:
    num = int(raw_input("Introduzca un numero: "))
    if num > 0:
        for i in range(1, num + 1):
            if i == 3:
                fizz = i % 3
                if fizz == 0:
                    #print "i({}).Fizz({})".format(i, fizz)
                    print "Fizz"
            elif i == 5:
                buzz = i % 5
                if buzz == 0:
                    print "Buzz"
                    #print "i({}).Buzz({})".format(i, fizz)
            elif i > 5:
                fizz = i % 3
                buzz = i % 5
                if fizz == 0 and buzz == 0:
                    print "FizzBuzz"
                elif fizz == 0:
                    print "Fizz"
                    #print "i({}).fizz({})".format(i, fizz)
                elif buzz == 0:
                    print "Buzz"
                    #print "i({}).buzz({})".format(i, buzz)
                else:
                    print i
            else:
                print i
    else:
        print "Por favor, no introduzca numeros negativos!"
except ValueError:
    print "Por favor, introduzca solo números."