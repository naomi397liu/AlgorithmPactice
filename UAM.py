class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        '''
        index = UAM
        element at that index = number of users 
        
        collect the UAM for each user
        at index 0, element should be the count of users whose UAM == 1
        
        create output array
        create a dictionary 
            - where the key is user_id and the value is UAM 
            (maybe the key is the UAM and val is num users)
        iterate through the output array and get the values that match the index+1 and count
        
        '''

   
        ans = [0]*k
     
        UAM = {}
        for log in logs:
            if log[0] in UAM.keys():
                UAM[log[0]].add(log[1])
            else:
                UAM[log[0]] = {log[1]}
        print(UAM)
        for key in UAM:
            ans[len(UAM[key])-1] += 1
        return ans