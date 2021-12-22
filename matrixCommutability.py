import random
import math
import numpy as np
import time



class MatrixGenerator:
    size = (2,2)

    def __init__(self,start,end):
        self.start = start
        self.end = end

    def cycle(self):
        """Main loop, this will be used to go from self.start to self.end and create sequential matricies. """
        for i in range(self.start,self.end):
            for j in range(self.start,self.end):
                #in this case, as br = qc, b = i and j = q
                b = i
                r = j
                q = b * r

                #set c will always be equal to one to make things simpler
                c = 1

                #determine the values for a,d,p,s
                ratio = q/b #its q/b instead of b/q to make things simpler
                
                #the way my code works is that q will always be larger than b. therefore, the ratio will always be an integer which will be equal to r
                #choose the values of p and s
                p = random.randint(self.start,self.end)
                s = random.randint(self.start,self.end)

                #if p = q
                if p == s:
                    #this means that p - s will be equal to 0, which is fine....
                    a = random.randint(self.start,self.end)
                    d = a
                    #set the values of d = a equal to each other in order to satisfy the second law
                else:
                    #p is not equal to q:
                    difference_of_a_and_d_multiplied_by_ratio = ratio * (p - s)
                    d = random.randint(2,self.end)
                    a = d - difference_of_a_and_d_multiplied_by_ratio

                
                #create our first matrix
                mat_1 = np.array([[a,b],[c,d]])
                mat_2 = np.array([[p,q],[r,s]])
                
                #check that the two matricies are commutable
                if (MatrixGenerator.check_is_commutable(mat_1,mat_2)):
                    print("Matricies discovered!")
                    print("Matrix A is equal to: {} , and Matrix B is equal to: {}".format(mat_1,mat_2))
                    print("===========================================================================================================================")
                    time.sleep(0.1)

    @staticmethod
    def check_is_commutable(a,b):
        """Simple function to check if two matricies are commutable"""
        if np.array_equal(np.matmul(a,b),np.matmul(b,a)):
            return True
        else:
            return False


if __name__ == "__main__":
    generator = MatrixGenerator(2,10)
    generator.cycle()
    