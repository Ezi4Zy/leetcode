#
# @lc app=leetcode.cn id=1472 lang=python
#
# [1472] 设计浏览器历史记录
#

# @lc code=start

class VisitHistory(object):
    
    def __init__(self, url, pre=None, next=None):
        self.url = url
        self.pre = pre
        self.next = next

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.homepage = homepage
        self.current_visit = VisitHistory(self.homepage)


    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        visit = VisitHistory(url, pre=self.current_visit)
        self.current_visit.next = visit
        self.current_visit = visit
        


    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps > 0 and self.current_visit.pre != None:
            self.current_visit = self.current_visit.pre
            steps -= 1
        return self.current_visit.url


    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps > 0 and self.current_visit.next != None:
            self.current_visit = self.current_visit.next
            steps -= 1
        return self.current_visit.url



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# @lc code=end

