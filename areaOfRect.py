def areaOfRect(length,width):
    if(length > 0 or width > 0):
        return (length * width)
    else:
        return 0

length = int(input())
width = int(input())
print(areaOfRect(length,width))