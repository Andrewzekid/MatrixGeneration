import random
import math
import numpy as np
import time



class MatrixGenerator:
    size = (2,2)

    def __init__(self,start,end):
        self.start = start
        self.end = end

        #initialize the instance variables
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0

        self.p = 0
        self.q = 0
        self.r = 0
        self.s = 0

    def cycle(self):
        """Main loop, this will be used to go from self.start to self.end and create sequential matricies. """
        for i in range(self.start,self.end):
            for j in range(self.start,self.end):
                #in this case, as br = qc, b = i and j = q
                self.b = i
                self.r = j
                product = self.b * self.r
                
                #get the prime factor decomposition of the product of b and r
                factors = MatrixGenerator.prime_factors(product)

                self.q,self.c = self.parse_factors(factors,product)

                #determine the values for a,d,p,s
                #choose the values of p and s
                for i in range(20,2000):
                    if ((i * (self.b/self.q)).is_integer()):
                        difference_of_p_and_s = i
                        difference_of_p_and_s_multiplied_by_ratio = difference_of_p_and_s * (self.b/self.q)
                        break

                if difference_of_p_and_s_multiplied_by_ratio > 2:
                    self.p = random.randint(2,difference_of_p_and_s_multiplied_by_ratio )
                else:
                    self.p = 2

                self.s = difference_of_p_and_s_multiplied_by_ratio - self.p

                difference_of_a_and_d_multiplied_by_ratio = difference_of_p_and_s_multiplied_by_ratio

                if difference_of_a_and_d_multiplied_by_ratio > 2:
                    self.a = random.randint(2,difference_of_p_and_s_multiplied_by_ratio)
                else:
                    self.a = 2

                self.d = difference_of_a_and_d_multiplied_by_ratio - self.a
                #if p = s
                if self.p == self.s:
                    #this means that p - s will be equal to 0, which is fine....
                    self.a = random.randint(self.start,self.end)
                    self.d = self.a
                    #set the values of d = a equal to each other in order to satisfy the second law
                
                #create our first matrix
                mat_1 = np.array([[self.a,self.b],[self.c,self.d]])
                mat_2 = np.array([[self.p,self.q],[self.r,self.s]])
                
                #check that the two matricies are commutable
                if (MatrixGenerator.check_is_commutable(mat_1,mat_2) and (self.p != self.s)):
                    print("Matricies discovered!")
                    print("Matrix A is equal to: {} , and Matrix B is equal to: {}. The product of the two matricies is equal to: \n {}".format(mat_1,mat_2,np.matmul(mat_1,mat_2)))
                    print("===========================================================================================================================")
                    time.sleep(0.1)
    
    def parse_factors(self,factors,product):
        """Function to find the values of p and q"""
        #a and b are made of more than one of these prime factors 
        #search for a value of q such that q != a and q ! = b
        for i in factors:
            for j in factors:
                if j == i:
                    pass
                elif ((i * j) != self.r) and ((i * j) != self.b):
                    #found one factor
                    q = i * j
                    c = int(product / q)
                    return (q,c)
         #if it hasnt returned anything by this point, we can safely assume that things are probably bugged and head on with our lives:
        q = product
        c = 1
        return (q,c)

    @staticmethod
    def prime_factors(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors 

    @staticmethod
    def check_is_commutable(a,b):
        """Simple function to check if two matricies are commutable"""
        if np.array_equal(np.matmul(a,b),np.matmul(b,a)):
            return True
        else:
            return False


if __name__ == "__main__":
    generator = MatrixGenerator(2,100)
    generator.cycle()
    