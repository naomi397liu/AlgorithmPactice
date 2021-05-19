class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        '''
        
        '''
        different_sizes = set(groupSizes)
        groups = {}
        number_of_people = {}
        final_groups = []
# create dictionary with group size as key and the number of people to be in a group that size is the value
        for size in groupSizes:
            if size in number_of_people:
                number_of_people[size] += 1
            else:
                number_of_people[size] = 1
# find out how many groups for each group size
        for key, val in number_of_people.items():
            number_of_people[key] = int(val/key)
        for different_size in different_sizes:
            groups[different_size] = []
            for i in range(number_of_people[different_size]):
                groups[different_size].append([])
#         if there's more than 1 group for a size, use number_of_people to count down
        for i, group_size in enumerate(groupSizes): 
            num_group = number_of_people[group_size] - 1 #convert to indexes
            if len(groups[group_size][num_group]) == group_size: #if a group is full
                number_of_people[group_size] -= 1 #update which group we're on
                num_group = number_of_people[group_size] - 1
                groups[group_size][num_group].append(i)
            else:
                groups[group_size][num_group].append(i)
        
        for val in groups.values():
            final_groups.extend(val)
        
        return final_groups


