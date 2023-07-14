class Leaders:
    """ check from last element of the array
        last element is always the leader element
        """
    def leaders_array(self, array):
        result_array = []
        result_array.append(array[-1])

        for i in range(2, len(array)+1):
            """ if iteration got greater element than the previous element add the present 
                                                           to the array"""
            if array[-i] > result_array[len(result_array)-1] :
                result_array.append(array[-i])

        return result_array

array = list(map(int, input().split()))

object = Leaders()

print(object.leaders_array(array))