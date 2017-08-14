class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        list1_dict = {list1[i]:i for i in range(len(list1))}
        list2_dict = {list2[i]:i for i in range(len(list2))}
        shared_elements = list(set(list1) & set(list2))
        min_indexed = (shared_elements[0], list1_dict[shared_elements[0]]+list2_dict[shared_elements[0]])
        for element in shared_elements[1:]:
            if list1_dict[element]+list2_dict[element] < min_indexed[1]:
                min_indexed = (element, list1_dict[element]+list2_dict[element])
                
        result = [min_indexed[0]]
        result += [x for x in shared_elements if x != min_indexed[0] and list1_dict[x]+list2_dict[x] == min_indexed[1]]
        return result
        
        