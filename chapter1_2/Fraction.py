class Fraction:
    #start with our initializer
    def __init__(self, top, bottom):
        #check that both the numerator and denominator are both integers
        if isinstance(top,int) and isinstance(bottom,int):
            #if the denomintor is a negative number
            if bottom < 0:
                top *= -1
                bottom *= -1
            #immediately reduce the fraction
            common_divisor = self.greatest_common_den(top,bottom)


            self.num = top // common_divisor
            self.den = bottom // common_divisor
        else:
            raise RuntimeError("Both numerator and denominator need to be integers!")


    def __check_type(self,thing):

        otherfrac = None

        if isinstance(thing,int): #maybe we don't use isinstance here?
            otherfrac = Fraction(thing,1)
        elif isinstance(thing,float):
            otherfrac = Fraction(int(thing * 100), 100)
        elif isinstance(thing,Fraction):
            otherfrac = thing
        else:
            raise ValueError("What is that? Only ints or floats plz!")

        return otherfrac

    #override the default print method
    def __str__(self):
        return str(self.num) + "/" +  str(self.den)
    #make a new represent
    def __repr__(self):
        return self.__str__()


    #implement a method which reutnrs the numerator
    def getNum(self):
        return self.num
    #method to return the denominator
    def getDen(self):
        return self.den
    #
    #override the default equality method so we can use deep equality on Fractions
    def __eq__(self,otherfrac):

        firstnum = self.num * otherfrac.den
        secondnum = otherfrac.num * self.den

        return firstnum == secondnum
    #override the default not equal to method
    def __ne__(self,otherfrac):

        return not self.__eq__( otherfrac)
    #override the default greater than method
    def __gt__(self,otherfrac):

        lhs_num = self.num * otherfrac.den
        rhs_num = self.den * otherfrac.num

        return lhs_num > rhs_num

    #override the default greater than or equal to method
    def __ge__(self,otherfrac):

        return self.__gt__( otherfrac) or self.__eq__( otherfrac)

    #override the default less than method
    def __lt__(self,otherfrac):

        lhs_num = self.num * otherfrac.den
        rhs_num = self.den * otherfrac.num

        return lhs_num < rhs_num

    #override the default greater than or equal to method
    def __ge__(self,otherfrac):

        return self.__lt__( otherfrac) or self.__eq__( otherfrac)

    #override the default add method
    def __add__(self,thing):
        otherfrac = self.__check_type(thing)

        newnum = self.num * otherfrac.den + self.den * otherfrac.num
        newden = self.den * otherfrac.den

        return Fraction(newnum,newden)

    #override the default right add method
    def __radd__(self,thing):
        otherfrac = self.__check_type(thing)

        newnum = self.num * otherfrac.den + self.den * otherfrac.num
        newden = self.den * otherfrac.den

        return Fraction(newnum,newden)




    #override the default subtraction method
    def __sub__(self,thing):
        otherfrac = self.__check_type(thing)

        new_shared_denom = self.den * otherfrac.den


        lhs_num = self.num * otherfrac.den
        rhs_num = otherfrac.num * self.den

        new_numerator = lhs_num - rhs_num

        return Fraction(new_numerator,new_shared_denom)



    #overide the multiplication
    def __mul__(self,thing):
        otherfrac = self.__check_type(thing)

        new_numerator = self.num * otherfrac.num
        new_denom = self.den * otherfrac.den


        return Fraction(new_numerator,new_denom)


    #override the /  method
    def __truediv__(self,thing):
        print("HEY GIRL")
        otherfrac = self.__check_type(thing)
        print(otherfrac)
        flipped_divisor = Fraction(otherfrac.den,otherfrac.num)


        return self.__mul__( flipped_divisor)

    #define the Euclid's Algorithm to get the greatest common divisor
    def greatest_common_den(self, m,n):
        while m%n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm%oldn
        return n
