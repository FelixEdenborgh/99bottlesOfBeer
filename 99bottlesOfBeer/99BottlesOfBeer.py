def print_bottles_line( n ):
   if n > 0:
    print("{} bottles of beer on the wall". format(n, n))
    print("{} take one down and pass it around, {} bottles of beer on the wall.".format(n-1))
   elif n == 1:
       print("{} bottle of beer on the wall".format(n, n))
       print("{} take one down and pass it around, {} bottle of beer on the wall.".format(n - 1))
   else:
       print("{} bottles of beer on the wall".format(n, n))
       print("{} take one down and pass it around, {} bottles of beer on the wall.".format(n - 1))

for n in range(99,0-1):
    print_bottles_line( n )
print_bottles_line( 0 )




