//print number
def printNumber(n):
  if n > 0:
    printNumber(n-1)
    print(n, end = ' ')
    
n =int(input())
printNumber(n)

//print array element
def PrintArray(arr,i,n):
    if(i>=n):
        return
    print(arr[i],end=" ")
    PrintArray(arr,i+1,n)
arr=[]
n = int(input("size of the array: "))
print("Elements of the array:")
for i in range(0,n):
    num = int(input())
    arr.append(num)

print("Array Element:")
PrintArray(arr,0,n)
// print n-1
def rev(n):
    if n<=0:
        return
    else:
        print(n, end=" ")
        rev(n-1)
n=int(input())
rev(n)

// maximum of thre given array 
def find_maximum(arr):
    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2
    left_max = find_maximum(arr[:mid])
    right_max = find_maximum(arr[mid:])

    return max(left_max, right_max)

# Example usage:
array = [4, 7, 2, 9, 1, 5]
maximum = find_maximum(array)
print("The maximum number in the array is:", maximum)
