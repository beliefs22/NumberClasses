from prime import Prime
from time import time


def Prime_div(num,Prime,divisors):
    """ Recursively Finds the prime divisors of a given number,

    Args:
        num (int): Number whose Prive divisors will be calculated
        Prime (Prime) : An instance of the Prime class used to generate primes
        divisors (list): A list representing the divisors found so far        
    
    """
    if divisors == []: #if this is the first call add one to list all numbers div by 1
        divisors.append(1)
    
    if Prime.isPrime(num):#base case. when prime number is found we have found all Prime divisors
        temp = divisors        
        divisors.append(num)
        
        
        return divisors
    else:# testing case. If we have not found our base prime, then we keep calling the function
        Prime.reset()
        factor = Prime.nextPrime()
        found = False#Set to false in each call 
        while factor < num/2 and not found:
            if num%factor == 0:
                divisors.append(factor)#Appends a found prime divisor to our list
                found = True
            if not found:
                factor = Prime.nextPrime()#Cycles through prime list until we find a prime the number is divisible by
        return Prime_div(num/factor,Prime,divisors)


def split(mylist,size):
    """Takes a given list and turns it into as many equally-sized list as possible
        i.e: split([1,2,3,4],2): returns [[1,2],[2,3],[3,4]]

        Args:
            mylist (list): list that we want to split
            size (int): size to split list into
    """

    split_list = []

    for index,num in enumerate(mylist):
        if index + size <= len(mylist):#checks so we don't go out of list range
            position = mylist.index(num,index)
            split_list.append(mylist[position:position+size])
    return split_list

def product(mylist):
    """Finds product of all the numbers in a given list

        Args:
            mylist (list): list whose product you want to find
    """
    temp = 1
    for num in mylist:
        temp *= num
    return temp

def helper(num):
    """ Helper function use in Divisor class to map our split function onto our list
        of Prime divisors
    """
            
    return lambda x: num * product(x)
    


class Divisor:
    """A class for finding the divisors of a given number using their prime divisors.
        Finds all the possible unique combinations of a numbers Prime Divisors

    Attributes:
        divisors (list) = list to store the divisors once they are generated
            initiallized to [1] as all numbers are divisible by one
        
"""
    def __init__(self,num,prime):
        """
            Args:
                num (int) = An int whose divisors will be calculated

        """
       # self.start1 = time()
        if num == 0 or type(num) != int:
            raise RuntimeError("Must be an in greater than Zero!!")
       # self.end1 = time()
       # self.start2 = time()
        self.divisors = [1]
       # self.end2 = time()
      #  self.start3 = time()
        self.prime = prime
       # self.end3 = time()
        self.number = num
       # self.start4 = time()
        prime_div = Prime_div(num,self.prime,[])#the given numbers prive divisors
       # self.end4 = time()
       # self.start5 = time()
        for index, div in enumerate(prime_div):
            temp = prime_div[index+1:]
            for i in range(1,len(temp) + 1):
                duplicates = map(helper(div),split(temp,i))#gets rid of duplications(should we just leave them then create a set?)
                for number in duplicates:
                    if number not in self.divisors and number != num:
                        self.divisors.append(number)
       # self.end5 = time()
        #self.start6 = time()
        self.divisors.sort()
       # self.end6 = time()

    def __str__(self):
        """A string representation of the Divisor class
        """
        return str(self.divisors)

    def benchmark(self):

        a = "check for 0 took %f time" %(self.end1-self.start1)
        b = "creating divisor took %f time" %(self.end2-self.start2)
        c = "creating prime took %f " %(self.end3-self.start3)
        d = 'creating prive divisors took %f' %(self.end4 - self.start4)
        e = 'creating actual divisor list took %f' %(self.end5-self.start5)
        f = 'sorting list took %f' %(self.end6-self.start6)

        print a,"\n",b,"\n",c,"\n",d,"\n",e,"\n",f


def main():
    p = Prime()
    start = time()
    for i in range(1,1000):
        test = Divisor(i,p)
    end = time()
    print end-start
    print test

if __name__ == '__main__':
    main()

    
        
        
        
        

        
        
