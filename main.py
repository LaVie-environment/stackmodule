#!/usr/bin/python3

import stackModule

mystack = stackModule.getStack()

for item in range(1, 5):
    stackModule.push(mystack, item)
    print('Pushing', item, 'on stack')

while not stackModule.isEmpty(mystack):
    item = stackModule.pop(mystack)
    print('Popping', item, 'from stack')