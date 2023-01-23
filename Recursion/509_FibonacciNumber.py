# method 1:
class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        cache[1] = 1
        cache[0] = 0
        if n in cache:
            return cache[n]
        else:
            result = self.fib(n - 1) + self.fib(n - 2)
            cache[n] = result
        return result

# method2:
class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        def recur_fib(N):
            if N in cache:
                return cache[N]

            if N < 2:
                result = N
            else:
                result = recur_fib(N-1) + recur_fib(N-2)

            # put result in cache for later reference.
            cache[N] = result
            return result
        return recur_fib(n)
 # why method2 time complexity much smaller than method1?