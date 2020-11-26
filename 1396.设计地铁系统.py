#
# @lc app=leetcode.cn id=1396 lang=python
#
# [1396] 设计地铁系统
#

# @lc code=start
class UndergroundSystem(object):

    def __init__(self):
        self.check_map = {}
        self.station_average_time_map = {}
        self.sep = '---'


    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.check_map[id] = (stationName, t)


    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        start_station, start_time = self.check_map.pop(id)
        station_key = start_station + self.sep + stationName
        cost_time = t - start_time
        if station_key in self.station_average_time_map:
            self.station_average_time_map[station_key] = (self.station_average_time_map[station_key][0] + cost_time, self.station_average_time_map[station_key][1] + 1)
        else:
            self.station_average_time_map[station_key] = (cost_time, 1)


    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        station_key = startStation + self.sep + endStation
        return float(self.station_average_time_map[station_key][0]) / self.station_average_time_map[station_key][1]



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# @lc code=end

