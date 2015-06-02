
class Prime:
    """A class for generating the first 10,000 Primes from list

    Attributes:
        primes (dict)= where the keys are the prime number
            stored as string, and the value is the value of that
            prime stored as int
        ordred (list of ints)= A list containing all primes in order by value
            smalled to largest
        index (int) = used for interation initializd to 0
        count (int) = used for generating one prime at a time initlized to 0

"""
    def __init__(self):
        """
            Args: None
        """
        self.count = 0
        __myfile = open("primes.txt",'r')        
        self.primes = {}
        self.ordered = []
        for line in __myfile:           
            temp = line.rstrip("\n")
            self.primes[temp] = int(temp)
            self.ordered.append(int(temp))
        __myfile.close()
        self.index = 0

    def isPrime(self,num):
        """Checks if given number is Prime

        Args:
            num (int): Number to check Primality

        Returns:
            True if num is Prime, False otherwise
        """
        if num == 1:
            return True
        else:
            return str(num) in self.primes

    def genPrime(self,length):
        """Return a list of primes a given number in length

        Args:
            length (int): how long the list should be

        Returns:
            list of the first "length" primes
        """
        prime_list = []
        for i in range(length):
            prime_list.append(self.ordered[i])            
        return prime_list

    def getPrime(self,num):
        """Gets the ith prime where i is given number

        Args:
            num (int): the ith prime to find

        Returns:
            int represeting the ith Prime
        """
        return self.ordered[num-1]

    def nextPrime(self):
        """Returns the next Prime based on value of self.count

        Args: None

        Returns:
            int represeting the next prime in sequence
        """
        temp = self.ordered[self.count]
        self.count += 1
        return temp
    def reset(self,c = False,i = False):
        """Resets self.count and self.index to 0. To begin new count or iteration

        Args:
            c (boolean) :Defaults to false. Set to True if you only want to only reset Count
            i (bolean)  :Defaults to false. Set to True if you only want to only reset index
            **If you want to reset both, leave both as false**

        """
        if c == False and i == False:
            c,i = True,True
        if self.count > 0 and c:
            self.count = 0
        if self.index and i > 0:
            self.index = 0

    def __iter__(self):
        """Iterates over entire list of primes"""
        return self
    def next(self):
        if self.index == len(self.ordered)-1:
            raise StopIteration
        temp = self.index
        self.index = self.index +1
        return self.ordered[temp]
    

def main():
    t = Prime()
    iter(t)
    print t.getPrime(50)
    
    for i in range(100):
        print t.nextPrime()

    for prime in t:
        print prime
        if prime > 541:
            break
    t.reset(c=False,i=True)
    for i in range(100):
        print t.nextPrime()
    for prime in t:
        print prime
        if prime > 541:
            break
    t.reset()
    for prime in t:
        print t.nextPrime()
        print prime
        if prime > 541:
            break


if __name__ == '__main__':
    main()



