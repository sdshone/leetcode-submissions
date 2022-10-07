from sortedcontainers import SortedDict
class MyCalendarThree(object):


    def __init__(self):

        self.timing = SortedDict()

    def book(self, start, end):
        
        self.timing[start] = self.timing.get(start,0)+1
        self.timing[end] = self.timing.get(end,0)-1
        cur = res = 0
        # print(self.timing.values())
        for v in self.timing.values():
            cur+=v
            res=max(cur,res)
            # print(start,end,v,res)
        return res
# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)



# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)