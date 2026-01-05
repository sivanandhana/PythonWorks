class ClosesetNumberToZero:

    def solution(self,arr):

        closeset_number =arr[0] 

        for  num in arr:

            if abs(num) < abs(closeset_number): #-1

                closeset_number = num #1

        if closeset_number < 0 and abs(closeset_number) in arr: #1<1

            return abs(closeset_number) #cl_n =1
        
        else:
            
            return closeset_number #1
    
closeset_instance = ClosesetNumberToZero()

print(closeset_instance.solution([-1,-2,1,3,2]))

