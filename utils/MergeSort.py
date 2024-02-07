# -----------------------------------------------------
# ST1507 DSAA
# CA2
#
# A class to perform a custom merge sort on a dictionary where 
# the values can be numeric or 'None'.
# The sorting is based on numeric values in descending order, 
# and for 'None' values, it sorts the keys alphabetically.
#
# -----------------------------------------------------
#
# Author    : Lim Zhen Yang
# StudentID : 2214506
# Class     : DAAA/FT/2B/04
# Date      : 7-Feb-2023
# Filename  : MergeSort.py
#
# -----------------------------------------------------
# To run: python main.py
# -----------------------------------------------------
class MergeSort:
    """
    A class to perform a custom merge sort on a dictionary where the values can be numeric or 'None'.
    The sorting is based on numeric values in descending order, and for 'None' values, it sorts the keys alphabetically.
    """

    def __init__(self, data):
        """
        Initializes the MergeSort object with the data to be sorted.

        Parameters:
        - data (dict): The dictionary to be sorted. The values can be numeric or 'None'.
        """
        # Separate entries with 'None' values and sort them alphabetically
        self.__none_entries = [k for k, v in data.items() if v == 'None']
        # Entries with numeric values for sorting
        self.__data = [(k, v) for k, v in data.items() if v != 'None']

    # Getter
    def get_none_entries(self):
        return self.__none_entries
    
    def get_data(self):
        return self.__data
    
    # Setter
    def set_none_entries(self, none_entries):
        self.__none_entries = none_entries
    
    def set_data(self, data):
        self.__data = data

    def merge_sort(self):
        """
        Performs the merge sort on the numeric part of the data.
        """
        self.__data = self.merge_sort_rec(self.__data)

    def merge_sort_rec(self, arr):
        """
        Recursively divides and merges the array during the merge sort process.

        Parameters:
        - arr (list of tuples): The array (or sub-array) to be sorted.

        Returns:
        - list of tuples: The sorted array (or sub-array).
        """
        # Check if the length of the array is greater than 1
        if len(arr) > 1:
            mid = len(arr) // 2  # Calculate the midpoint of the array
            L = arr[:mid]  # Split the array into left half
            R = arr[mid:]  # Split the array into right half

            # Recursively sort the two halves
            L = self.merge_sort_rec(L)  # Sort the left half
            R = self.merge_sort_rec(R)  # Sort the right half

            # Merge the sorted halves
            return self.merge(L, R)  # Merge and return the result
        return arr  # Return the array if its length is 1 or less (base case)

    def merge(self, L, R):
        """
        Merges two sorted arrays during the merge sort process.

        Parameters:
        - L (list of tuples): The left half of the array.
        - R (list of tuples): The right half of the array.

        Returns:
        - list of tuples: The merged and sorted array.
        """
        # Initialize an empty list to store the merged result
        result = []
        # Initialize indices for iterating over L and R
        i = j = 0

        # Merge the two halves in a sorted manner
        while i < len(L) and j < len(R):
            # Check if both elements are not strings
            if not isinstance(L[i][1], str) and not isinstance(R[j][1], str):
                # Compare the numeric values first, then compare letters
                if L[i][1] > R[j][1] or (L[i][1] == R[j][1] and L[i][0] < R[j][0]):
                    result.append(L[i])  # Append the element from L to the result
                    i += 1  # Move to the next element in L
                else:
                    result.append(R[j])  # Append the element from R to the result
                    j += 1  # Move to the next element in R
            else:  # If either element is a string
                # Compare the keys alphabetically
                if L[i][0] < R[j][0]:
                    result.append(L[i])  # Append the element from L to the result
                    i += 1  # Move to the next element in L
                else:
                    result.append(R[j])  # Append the element from R to the result
                    j += 1  # Move to the next element in R

        # Append any remaining elements from L and R
        result.extend(L[i:])
        result.extend(R[j:])
        # Return the merged and sorted array
        return result

    def get_sorted_dict(self):
        """
        Converts the sorted array back into a dictionary, grouping keys by their values, and adds the sorted 'None' entries.

        This method constructs a dictionary from the sorted array where keys are grouped by their corresponding values.
        It also adds the sorted 'None' entries at the end of the dictionary.

        Returns:
        - dict: The sorted dictionary.
        """
        # Initialize an empty dictionary to store the sorted result
        sorted_dict = {}
        
        # Group keys by their values in the sorted array
        for key, value in self.__data:
            # Check if the value is not already a key in the dictionary
            if value not in sorted_dict:
                # If not, create a new key with an empty list as its value
                sorted_dict[value] = []
            # Append the key to the list corresponding to its value in the dictionary
            sorted_dict[value].append(key)

        # Add 'None' entries at the end, already sorted alphabetically
        sorted_dict['None'] = self.merge_sort_rec(self.__none_entries)
        # Return the constructed sorted dictionary
        return sorted_dict
    
    def __str__(self) -> str:
        return "MergeSort class"
    
    def __repr__(self) -> str:
        return "MergeSort class"