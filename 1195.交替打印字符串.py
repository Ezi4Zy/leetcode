#
# @lc app=leetcode.cn id=1195 lang=python
#
# [1195] 交替打印字符串
#

# @lc code=start
class FizzBuzz(object):
    def __init__(self, n):
        self.n = n
        self.fizz_lock = threading.Lock()
        self.buzz_lock = threading.Lock()
        self.fizzbuzz_lock = threading.Lock()
        self.number_lock = threading.Lock()
        
        self.fizz_lock.acquire()
        self.buzz_lock.acquire()
        self.fizzbuzz_lock.acquire()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        """
        :type printFizz: method
        :rtype: void
        """
        for i in range(1, self.n+1, 1):
            if i % 5 and not (i % 3):
                self.fizz_lock.acquire()
                printFizz()
                self.number_lock.release()
    	

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz):
        """
        :type printBuzz: method
        :rtype: void
        """
        for i in range(1, self.n+1, 1):
            if i % 3 and not (i % 5):
                self.buzz_lock.acquire()
                printBuzz()
                self.number_lock.release()
    	

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz):
        """
        :type printFizzBuzz: method
        :rtype: void
        """
        for i in range(1, self.n+1, 1):
            if not (i % 15):
                self.fizzbuzz_lock.acquire()
                printFizzBuzz()
                self.number_lock.release()
        

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n+1, 1):
            self.number_lock.acquire()
            if i % 5 and not (i % 3):
                self.fizz_lock.release()
            elif i % 3 and not (i % 5):
                self.buzz_lock.release()
            elif not (i % 3) and not (i % 5):
                self.fizzbuzz_lock.release()
            else:
                printNumber(i)
                self.number_lock.release()
   
# @lc code=end

