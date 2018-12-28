#File to work on Python testing from Hacker Rank.
#If-else work using Integers.
def weirdNum(x):
    if x%2 != 0:
        print ('Weird')
    else:
        if 2 <= x <=5:
            print ('Not Weird')
        if 6 <= x <= 20:
            print ('Weird')
        if x > 20:
            print ('Not Weird')

def leapYear(y):
    leap = False

    if y % 4 == 0:
        leap = True
        if y % 100 == 0:
            leap = False
            if y % 400 == 0:
                leap = True

    return leap

def main():
    weirdNum(1)
    weirdNum(3)
    weirdNum(4)
    weirdNum(12)
    weirdNum(17)
    weirdNum(20)
    weirdNum(30)

    leapResult = leapYear(1900)
    print (leapResult)
    leapResult = leapYear(2000)
    print (leapResult)
    leapResult = leapYear(2400)
    print (leapResult)
    

if __name__ == '__main__':
  main()
