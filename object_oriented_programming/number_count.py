class NumberCount:

    def solution(*args,**kwargs):

        val=kwargs.get("value")

        lst=list(args)

        count=lst.count(val)

        return count


num_count_instance=NumberCount()

print(num_count_instance.solution(10,20,110,10,65,10,value=10))

