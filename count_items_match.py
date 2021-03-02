def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        # our input is a list of lists containing 3 strings: type, color and name
        # the rule key tells you the which string it wants to evaluate and the rule value tells you what that string should be
        # our goal is to return the number of items that comply with the rule
        # to do this, we could put our items in a hash map such that the key would be the type and the value would be a list of strings from each item that describes that types
        # then we could look up the rulekey and count the values that match ruleValues
    count = 0
    hash_items = {}
    hash_items['type'] = []
    hash_items['color'] = []
    hash_items['name'] = []
    
    for row in items:
        hash_items['type'].append(row[0])
        hash_items['color'].append(row[1])
        hash_items['name'].append(row[2])

    for list_element in hash_items[ruleKey]:
        if list_element == ruleValue:
            count += 1
            
    return count