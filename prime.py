import pickle
class Prime:
    """A class for user first 10,000 Primes in various math problems."""
    def __init__(self):
        
        self.count = 0 # used to reset iterator
        self.index = 0 # used to reset iterator
        primefile = open(
            '/home/beliefs22/python/numberclasses/Data/primetuples','r')
        self.primes = pickle.load(primefile)
        primefile.close()

    def is_prime(self,num):
        """Checks if given number is Prime.

        Args:
            num (int): Number to check Primality

        Returns:
            bool: True if num is Prime, False otherwise
            
        """
        if num == 1:
            return True
        else:
            return num in self.primes

    def gen_Prime(self,length):
        """Return a list of first length primes.

        Args:
            length (int): number of primes to find

        Returns:
            tuple: tuple of the first  "length" primes
            
        """
    
        return self.primes[:length]

    def prime_generator_value(self, maxval=None):
        """Returns generator of primes up to a max value.

            Args:
                maxval (int): max value of prime to generate. Defaults to max
                    prime available if no maxvalue given

            Yields:
                int: next prime in sequence

        """
        
        if maxval == None: #if no value given
            maxval = self.primes[len(self.primes)-1]
        pos = 0
        while self.primes[pos] <= maxval:
            yield self.primes[pos]
            pos += 1
            
    def prime_generator_count(self, maxcount=None):
        """Returns generator of primes up to max count.

        Args:
            maxcount (int): maximum number of primes to generator. Defaults to
                all primes available if no maxcount is given

        Yields:
            int: next prime in sequence

        """
        if maxcount == None:
            maxcount = len(self.primes)
        count = 0
        while  count < maxcount:
            yield self.primes[count]
            count += 1
            
    def getPrime(self,num):
        """Return request prime. I.E. getPrime(number.

        Args:
            num (int): the ith prime to find

        Returns:
            int represeting the ith Prime
        """
        return self.primes[num-1]

    def nextPrime(self):
        """Returns the next Prime based on value of self.count

        Returns:
            int represeting the next prime in sequence
        """
        temp = self.primes[self.count]
        self.count += 1
        return temp
    
    def reset(self,count = False,index = False):
        """Resets self.count and self.index to 0.
            Used for interation and to generated next prime without a generator

        Args:
            count (boolean) :Defaults to fa lse. Set to True if you only
                want to only reset Count
            index (bolean)  :Defaults to false. Set to True if you only want
                to only reset index
                **If you want to reset both, leave both as false**

        """
        if count == False and index == False:
            count,index = True,True
        if self.count > 0 and count:
            self.count = 0
        if self.index and index > 0:
            self.index = 0

    def __iter__(self):
        """Iterates over entire list of primes. Expects user to stop."""
        return self
    def next(self):
        if self.index == len(self.primes)-1:
            raise StopIteration
        temp = self.index
        self.index = self.index +1
        return self.primes[temp]
    

def main():
    t = Prime()
    print t.getPrime(50)
    
    for i in range(100):
        print t.nextPrime()

    first_100 = t.prime_generator_count(100)
    for prime in first_100:
        print prime
    
    for prime in t:
        if prime > 541:
            break
        print prime

    greater_than = t.prime_generator_value(541)
    for prime in greater_than:
        print prime

if __name__ == '__main__':
    main()



