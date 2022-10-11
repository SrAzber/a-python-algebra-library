
class Polynomial:

    def __init__(self, values):

        """
            parameters: coefficients list
            init the coefficients and the deg of the passed list
        """

        self.__coefficients = values
        self.__deg = len(values)-1




    def deg(self):

        """
            parameters: passed deg (size)
            returns the degree (size) of the polynomial
        """
        return self.__deg


    def coefficients(self):

        """
            parameters: passed coefficients
            returns the coefficients of the polynomial
        """
        return self.__coefficients




    def simplify(self, other, deg):

        """
            distribute and add values of same degree inside the polynomial
        """

        other2 = []

        length = len(other)

        for i in range(length):
            var = 0
            for j in range(length):
                if other[j][1] == i:
                    var += other[j][0]
            if var != 0:
                other2.insert(0, var)

        return other2




    def set_on_same_degree(self, other):

        """
            parameters: passed polynomial
            set the two polynomials to the same degree
        """

        if other.deg() < self.deg():

            for i in range(self.deg()-other.deg()):
                other.__coefficients.append(0)

        else:

            for i in range(other.deg()-self.deg()):
                self.__coefficients.append(0)

        self.__deg = len(self.__coefficients)-1
        other.__deg = len(other.__coefficients)-1

        return other



    def __add__(self, other):

        """
            parameters: passed polynomial
            add self to another polynomial :

                1. set the two polynomials to the same degree
                2. add each values to each other on the same degree
        """

        other = self.set_on_same_degree(other)

        for i in range(self.deg() + 1):
            self.__coefficients[i] =  self.__coefficients[i] + other.__coefficients[i]

        return self





    def __sub__(self, other):

        """
            parameters: passed polynomial
            subtract self to another polynomial :

                1. set the two polynomials to the same degree
                2. subtract each values to each other on the same degree
        """

        other = self.set_on_same_degree(other)

        for i in range(self.deg() + 1):
            self.__coefficients[i] =  self.__coefficients[i] - other.__coefficients[i]

        return self





    def __mul__(self, other):

        """
            parameters: passed polynomial
            multiply self to another polynomial :

                1. creates a new polynomial
                2. multiply each values to each other and apply commutativity
        """
        newPolynomial = []

        for i in range(self.deg() + 1):
            for j in range(other.deg() + 1):

                newPolynomial.append([self.__coefficients[i]*other.__coefficients[j],(self.deg()+other.deg())-(i+j)])

        self.__coefficients = self.simplify(newPolynomial, other.deg())
        self.__deg = len(self.__coefficients)-1

        return self




    def __truediv__(self, other):

        """
            parameters: passed polynomial
            multiply self to another polynomial :

                1. creates a new polynomial and quotient
                2. divide using euclidian polynomial division algorithm
        """

        ## i'll explain all of this later

        new_Polynomial = self
        final_Quotient = []

        for i in range(self.deg()):

            print(new_Polynomial.__coefficients, other.__coefficients)

            if self.deg() >= other.deg():

                deg = self.deg() - i
                Quotient = new_Polynomial.__coefficients[0]/other.__coefficients[0]

                Quotient_Polynomial = Polynomial([Quotient])

                for j in range(deg):
                    Quotient_Polynomial.__coefficients.append(0)

                Quotient_B = Quotient_Polynomial * other

                for j in range(deg-1):
                    Quotient_B.__coefficients.append(0)

                new_Polynomial = new_Polynomial - Quotient_B

                final_Polynomial = []

                for h in range(1,len(new_Polynomial.__coefficients)):
                    final_Polynomial.append(new_Polynomial.__coefficients[h])

                new_Polynomial = Polynomial(final_Polynomial)

                final_Quotient.append(Quotient)


        final_Quotient = Polynomial(final_Quotient)
        Rest = new_Polynomial.__coefficients[0] or self.__coefficients

        return final_Quotient.__coefficients, Rest

