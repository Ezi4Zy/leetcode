#
# @lc app=leetcode.cn id=729 lang=python
#
# [729] 我的日程安排表 I
#


# @lc code=start
class MyCalendar(object):

    def __init__(self):
        self.book_ = []
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if len(self.book_) == 0:
            self.book_.append((start, end))
            return True
        i = 0
        j = len(self.book_)
        while i < j:
            mid = (i+j) / 2
            if mid == i or mid == j:
                break
            if self.book_[mid][0] > start:
                j = mid
            elif self.book_[mid][0] == start:
                return False
            else:
                i = mid
        if self.book_[i][0] > start:
            if end <= self.book_[i][0]:
                self.book_.insert(i, (start, end))
                return True
            else:
                return False
        else:
            if self.book_[i][1] <= start:
                if j < len(self.book_) and end > self.book_[j][0]:
                    return False
                self.book_.insert(j, (start, end))
                return True
            else:
                return False
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end

