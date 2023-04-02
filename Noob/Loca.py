class Solution:
    def fizzBuzz(self, n):

        resultado = []

        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                resultado.append("FizzBuzz")

            elif i % 3 == 0:
                resultado.append("Fizz")

            elif i % 5 == 0:
                resultado.append("Buzz")

            else:
                resultado.append(str(i))
        return resultado


n = int(input("Ingrese un número: "))

s = Solution()

result = s.fizzBuzz(n)

print(result)
