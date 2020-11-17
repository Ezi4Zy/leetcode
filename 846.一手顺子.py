#
# @lc app=leetcode.cn id=846 lang=python
#
# [846] 一手顺子
#

# @lc code=start
class Solution(object):

    def has_straight(self, hand, W):
        remove_cards = [hand[0]]
        index = 1
        W -= 1
        while W:
            if index == len(hand):
                return None
            if hand[index] - remove_cards[-1] == 1:
                remove_cards.append(hand[index])
                index += 1
                W -= 1
            else:
                index += 1
        for card in remove_cards:
            hand.remove(card)
        return hand


    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if len(hand) % W != 0:
            return False
        if W == 1:
            return True
        hand = sorted(hand)
        while True:
            hand = self.has_straight(hand, W)
            if hand is None:
                return False
            elif hand == []:
                return True
# @lc code=end

