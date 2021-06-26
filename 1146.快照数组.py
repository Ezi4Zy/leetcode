#
# @lc app=leetcode.cn id=1146 lang=python
#
# [1146] 快照数组
#

# @lc code=start
import copy
class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.data = [0] * length
        self.snapshot_id = 0
        self.snapshot_record = {self.snapshot_id: {}}
        


    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.snapshot_record[self.snapshot_id][index] = val
        self.data[index] = val


    def snap(self):
        """
        :rtype: int
        """
        snapshot_id = self.snapshot_id
        self.snapshot_id += 1
        self.snapshot_record[self.snapshot_id] = {}
        return snapshot_id


    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        ret = self.snapshot_record[snap_id].get(index)
        while ret is None:
            if snap_id == 0:
                return 0
            snap_id -= 1
            ret = self.snapshot_record[snap_id].get(index)
        return ret



# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# @lc code=end

