"""
A BIT of This OR That
The bitwise OR (|) operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if either of the corresponding bits of either number are 1. For example:

    a:  00101010  42
    b:  00001111  15       
================
a | b:  00101111  47
Note that the bitwise | operator can only create results that are greater than or equal to the larger of the two integer inputs.

So remember, for every given bit in a and b:

0 | 0 = 0
0 | 1 = 1 
1 | 0 = 1
1 | 1 = 1
Meaning

 110 (6) | 1010 (10) = 1110 (14)
Instructions
For practice, print out the result of using | on 0b1110 and 0b101 as a binary string. Try to do it on your own without using the | operator if you can help it.
"""



#print bin(0b1110 or 0b101)
# FIRST METHOD:
#print bin(0b1110 | 0b101)

# SECOND METHOD:
def policz_or (a,b):
    c=["0","b"]
    lena=len(list(str(bin(a))))
    lenb=len(list(str(bin(b))))
    lista=list(str(bin(a)))
    listb=list(str(bin(b)))
    lista=lista[2:]
    listb=listb[2:]
    diff=abs(lena-lenb)
    
    if lena<=lenb:
        lista=["0"]*diff+lista
        lenc=len(lista)
    else:
        listb=["0"]*diff+listb
        lenc=len(listb)
    
    for x in range(lenc):
        if ((lista[x]=="1") or (listb[x]=="1")):
            c.append("1")
        else:
            c.append("0")
    return "".join(c)
print policz_or(0b1110,0b101)
print policz_or(0b1110,0b10110)
