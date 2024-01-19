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
        self.none_entries = [k for k, v in data.items() if v == 'None']
        # Entries with numeric values for sorting
        self.data = [(k, v) for k, v in data.items() if v != 'None']

    def merge_sort(self):
        """
        Performs the merge sort on the numeric part of the data.
        """
        self.data = self.merge_sort_rec(self.data)

    def merge_sort_rec(self, arr):
        """
        Recursively divides and merges the array during the merge sort process.

        Parameters:
        - arr (list of tuples): The array (or sub-array) to be sorted.

        Returns:
        - list of tuples: The sorted array (or sub-array).
        """
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            # Recursively sort the two halves
            L = self.merge_sort_rec(L)
            R = self.merge_sort_rec(R)

            # Merge the sorted halves
            return self.merge(L, R)
        return arr

    def merge(self, L, R):
        """
        Merges two sorted arrays during the merge sort process.

        Parameters:
        - L (list of tuples): The left half of the array.
        - R (list of tuples): The right half of the array.

        Returns:
        - list of tuples: The merged and sorted array.
        """
        result = []
        i = j = 0

        # Merge the two halves in a sorted manner
        while i < len(L) and j < len(R):
            if not isinstance(L[i][1], str) and not isinstance(R[i][1], str):
                if L[i][1] > R[j][1] or (L[i][1] == R[j][1] and L[i][0] < R[j][0]):
                    result.append(L[i])
                    i += 1
                else:
                    result.append(R[j])
                    j += 1
            else:
                if L[i][0] < R[j][0]:
                    result.append(L[i])
                    i += 1
                else:
                    result.append(R[j])
                    j += 1

        # Append any remaining elements
        result.extend(L[i:])
        result.extend(R[j:])
        return result

    def get_sorted_dict(self):
        """
        Converts the sorted array back into a dictionary, grouping keys by their values, and adds the sorted 'None' entries.

        Returns:
        - dict: The sorted dictionary.
        """
        sorted_dict = {}
        for key, value in self.data:
            if value not in sorted_dict:
                sorted_dict[value] = []
            sorted_dict[value].append(key)

        # Add 'None' entries at the end, already sorted alphabetically
        sorted_dict['None'] = self.merge_sort_rec(self.none_entries)
        return sorted_dict