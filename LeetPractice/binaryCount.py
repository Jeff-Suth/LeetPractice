# Expected output in binary for 2 should be array of [0,1,1]

n = 2

def countBits(n):
    # Convert integer into binary using format function
    temp = format(n,"b")
    print(temp)
    # Break integer down into array
    arr = [int(n) for n in str(temp)]
    print(arr)

    # Reverse tempList so it is in expected order using reverse function
    arr.reverse()
    # We need to make it so that even when it says 0 it knows when it is 1 or 2 and so on...
    arr.append(0)
    print(arr)

    # Check for ones within the binary number then total it

countBits(n)