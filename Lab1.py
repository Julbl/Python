firstnumber = int(input('Enter an arbitrary number:'))
secondnumber = int(input('Enter the boundary number: '))

if firstnumber < secondnumber:
    print('An arbitrary number is less than a boundary number!')
if firstnumber > 3*secondnumber:
    print('An arbitrary number is three times more than a boundary number!')
elif firstnumber >= secondnumber:
    print('An arbitrary number is more than a boundary number!')