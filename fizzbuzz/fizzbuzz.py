class FizzBuzz(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def fizz_buzz(self, number):
        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuz"
        elif number % 3 == 0 and number % 5 != 0:
            return "Fizz" 
        elif number % 3 != 0 and number % 5 == 0:
            return "Buzz"
        else:
            return number
