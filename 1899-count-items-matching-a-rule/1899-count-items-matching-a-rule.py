class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        count = 0
        list = []
        for item in items:
            dict = {
                "type" : item[0],
                "color" : item[1],
                "name" : item[2]
            }
            list.append(dict)
        for i in range(len(list)):
            if list[i][ruleKey] == ruleValue:
                count += 1
        return count
