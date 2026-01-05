#[[1,3],[2,6],[8,10],[15,18]]


class MergedIntervals:

    def solution(self,intervals):

        merged =[]

        merged.append(intervals[0])


        for lst in intervals:

            if merged[-1][1] >lst[0]:
               
              merged[-1][1]=lst[1]


            else:
               
               merged.append(lst)

        return merged
    

merge_instance =MergedIntervals()

print(merge_instance.solution([[1,3],[2,6],[8,10],[15,18]]))
            

            
               
            