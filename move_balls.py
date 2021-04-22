class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        boxes is a string of 1s and 0s
        empty box = 0
        box with ball = 1
        GOAL: move all the balls to 1 box in the minimum number of moves
        1 move = move ball to adjacent box
        OUTPUT an array with the minimum number of steps it takes to move all the balls to that index
        """
#         number of moves to get to a spot for a give number is spot_index-number's index
#           if num is 1 then summation += abs(destination_index-current_num_index)
#           then append to output
#          the summation (destination_index-current_num_index) = minimum number of moves
#       then append
# boxes = "001011" Output: [11,8,5,4,3,4]
# (5+4+2 = 11), (1-2+1-4+1-5 = 8), (2-2+2-4+2-5=5),(3-2+3-4+3-5=4),etc
# 110
# use a dictionary/set to keep track of all the indexes that have 1

        ball_set = set()
        for i, box in enumerate(boxes):
            if int(box) > 0:
                ball_set.add(i) 
        output = []
        summation = 0
        current_destination = 0
        for i in range(len(boxes)):
            for index in ball_set:
                summation += abs(i-index)
            output.append(summation) 
            summation = 0  
        return output