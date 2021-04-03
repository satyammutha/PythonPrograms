def periOfRect(length,width):
    if(length > 0 or width > 0):
        return 2 * (length+width)
    else:
        return 0

length = int(input())
width = int(input())
print(periOfRect(length,width))