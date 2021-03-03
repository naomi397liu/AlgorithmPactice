class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
# 1 = big, 2 = medium, 3 = small
# index 0 = number of big car spots, index 1 = number of medium car spots, index 2 = number of small car spots

# we should go thru each add car item and if it is a 1, then subtract 1 from index 0 of parking system and append true if the resulting integer is greater than 0, otherwise append false
        
        if carType == 1:
            self.big = self.big - 1
            if self.big >= 0:
                return True
            else:
                return False
        elif carType == 2:
            self.medium = self.medium - 1
            if self.medium >= 0:
                return True
            else:
                return False
        elif carType == 3:
            self.small = self.small -1
            if self.small >= 0:
                return True
            else:
                return False

class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        #can put attributes in a dictionary for quick look ups
        self.spots = {1:big , 2:medium, 3:small}

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        
        self.spots[carType] -= 1
        return (self.spots[carType] >= 0)

