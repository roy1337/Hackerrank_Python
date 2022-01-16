Four integers x,y,z and n , each on a separate line.

Constraints

Print the list in lexicographic increasing order.

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) 
if a + b + c != n ])
