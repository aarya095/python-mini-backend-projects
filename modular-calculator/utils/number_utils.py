class NumberUtils():

    @staticmethod
    def num_is_even(num):
        """Checks if the number is even"""
        if (num % 2) == 0:
            return True
    @staticmethod
    def num_is_prime(num):
        """Checks if the number is prime"""
        if num == 2:
            return True
        elif num == 1:
            return True
        for i in range(2,num):
            if (i % num) == 0:
                pass
        
        
if __name__ == '__main__':
    instance = NumberUtils()
    result = instance.num_is_even(2)
    print(result)