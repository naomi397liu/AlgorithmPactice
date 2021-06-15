
def getMutualFriends(userA, userB):
    '''
    getFriends for userA
    getFriends for userB
    and find overlap
    userA friends in userB

    '''
    userA_friends = set(getFriends(userA))
    userB_friends = getFriends(userB)
    mutual_friends = []
    for friend in userB_friends:
        if friend in userA_friends:
            mutual_friends.append(friend)
    return mutual_friends

def peopleYouMayKnow(userId):
    '''
    all friends of friends that I'm not already friends with
    sort by who has the most mutual friends with me

    '''

    myfriends = set(getFriends(userId))
    suggested_friends = []
    sorted_suggested = {}
    for friend in myfriends:
        friend_of_friend = getFriends(friend)
        for friend_2 in friend_of_friend:
            if friend_2 is not in myfriends:
                suggested_friends.append(friend_2)
    
    for friend in suggested_friends:
        sorted_suggested[friend] = len(getMutualFriends(friend,userId))
    return sorted(sorted_suggested, key = sorted_suggested.get)



[
 x  x  |  
[5,10,15],
 x  | 
[3,21,25],
 |
[18,19,20]

]

#always look at M number of items
# iterate thru each list in the list and pop from the front - smallest items from each
# append the min of those items to a list until the len list is k-1



