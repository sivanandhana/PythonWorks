class IsFibannociNumber:

    def solution (self,number):

        is_fibo_num = False

        p=0

        c=1

        n = p+c

        while(n<=number):

            n=p+c

            p=c

            c=n

            if n==number:

                is_fibo_num = True

                break

        return is_fibo_num

fib_instance = IsFibannociNumber()

print(fib_instance.solution(8))

print(fib_instance.solution(15))
























    