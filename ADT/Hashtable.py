from ADT.BinarySearchTree import BinarySearchTree

class Hashtable:
    """
    Represents a hashtable data structure, which stores key-value pairs for efficient retrieval.
    References: https://www.programiz.com/dsa/hash-table
    """

    def __init__(self, initial_size=100):
        """
        Initializes a hashtable with an optional initial size.

        Parameters:
            initial_size (int): The initial size of the hashtable. Defaults to 100.
        """
        self.__size = initial_size
        self.__count = 0
        self.__keys = [None] * self.__size
        self.__buckets = [None] * self.__size
        self.__current_index = 0
        self.__bst = BinarySearchTree()

    # Getter methods
    def get_size(self):
        return self.__size

    def get_count(self):
        return self.__count

    def get_keys(self):
        return self.__keys

    def get_buckets(self):
        return self.__buckets

    def get_current_index(self):
        return self.__current_index

    def get_bst(self):
        return self.__bst

    # Setter methods
    def set_size(self, size):
        self.__size = size

    def set_count(self, count):
        self.__count = count

    def set_keys(self, keys):
        self.__keys = keys

    def set_buckets(self, buckets):
        self.__buckets = buckets

    def set_current_index(self, current_index):
        self.__current_index = current_index

    def set_bst(self, bst):
        self.__bst = bst

    def hash_function(self, key):
        """
        Calculates the hash value for a given key.

        Parameters:
            key: The key for which the hash value is to be calculated. It can be of any data type.

        Returns:
            int: The hash value, an integer representing the calculated hash value.

        This method calculates the hash value based on the type of the key:
        - If the key is a string, it computes the sum of the ASCII values of its characters.
        - If the key is a float, it multiplies it by 1,000,000 and converts it to an integer.
        - For other data types, it converts the key to an integer directly.

        The hash value is then computed as the remainder when dividing the calculated sum by the size of the hashtable.

        Note: The modulo operation ensures that the hash value falls within the range of the hashtable size,
        effectively mapping keys to valid indices in the hashtable.
        """
        if isinstance(key, str):
            # Calculate the sum of ASCII values of characters in the string key
            key_sum = sum(ord(char) for char in key)
        elif isinstance(key, float):
            # Convert the float key to an integer by multiplying it by 1000000
            key_sum = int(key * 1000000)
        else:
            # Convert the key to an integer
            key_sum = int(key)

        # Compute the hash value by taking the remainder when dividing the key_sum by the size of the hashtable
        return key_sum % self.__size

    def rehash_function(self, key, attempt):
        """
        Calculates the rehash value for a given key and attempt.

        Parameters:
            key: The key for which the rehash value is to be calculated. It can be of any data type.
            attempt (int): The attempt number for rehashing. It represents the number of times rehashing has been attempted.

        Returns:
            int: The rehash value, an integer representing the calculated rehash value.

        This method calculates the rehash value based on the type of the key and the attempt number:
        - If the key is a string, it computes the sum of the ASCII values of its characters.
        - For other data types, it directly uses the key value.
        - The rehash value is then computed as the sum of the hash value of the key and the square of the attempt number,
          followed by taking the remainder when dividing by the size of the hashtable.

        Note: The modulo operation ensures that the rehash value falls within the range of the hashtable size,
        effectively mapping keys to valid indices in the hashtable.
        """
        if isinstance(key, str):
            # Calculate the sum of ASCII values of characters in the string key
            key_sum = sum(ord(char) for char in key)
        else:
            # For other data types, use the key value directly
            key_sum = key

        # Compute the rehash value by adding the square of the attempt number to the hash value of the key
        # Then take the remainder when dividing by the size of the hashtable
        return (self.hash_function(key_sum) + attempt ** 2) % self.__size

    def __setitem__(self, key, value):
        """
        Sets a key-value pair in the hashtable.

        Parameters:
            key: The key of the entry. It can be of any data type.
            value: The value of the entry. It can be of any data type.
        """
        # Check the load factor and resize the hashtable if necessary
        if self.load_factor() > 0.7:
            self.resize()

        # Calculate the index using the hash function
        index = self.hash_function(key)
        attempt = 1

        # Handle collisions using linear probing
        while self.__buckets[index] is not None and self.__keys[index] != key:
            # Rehash the index if collision occurs
            index = self.rehash_function(key, attempt)
            attempt += 1

        # If the bucket at the calculated index is empty, increment the count
        if self.__buckets[index] is None:
            self.__count += 1
        
        # Set the key-value pair in the hashtable
        self.__buckets[index] = value
        self.__keys[index] = key

        # Add the key to the binary search tree for inorder traversal
        self.__bst.add(key)

    def __getitem__(self, key):
        """
        Retrieves the value associated with the given key.

        Parameters:
            key: The key whose value is to be retrieved.

        Returns:
            object: The value associated with the key, or None if the key is not found.
        """
        # Calculate the index using the hash function
        index = self.hash_function(key)
        attempt = 1

        # Linear probing to handle collisions
        while self.__keys[index] != key:
            # If the key is not found and the bucket is empty, return None
            if self.__buckets[index] is None:
                return None
            # Rehash the index if collision occurs
            index = self.rehash_function(key, attempt)
            attempt += 1

        # Return the value associated with the key
        return self.__buckets[index]
    
    def getitem_inorder(self):
        """
        Retrieves the key-value pairs from the hashtable in inorder traversal order.

        Returns:
            list: A list of key-value pairs in inorder traversal order.
        """
        # Initialize an empty list to store key-value pairs in inorder traversal order
        items_inorder = []

        # Traverse the binary search tree in inorder traversal
        for key in self.__bst.inorder_traversal():
            # Retrieve the value associated with the key using __getitem__ method
            value = self[key]
            # Append the key-value pair to the list
            items_inorder.append((key, value))

        # Return the list of key-value pairs
        return items_inorder

    def __delitem__(self, key):
        """
        Deletes the entry with the given key from the hashtable.

        Parameters:
            key: The key of the entry to be deleted.
        """
        # Calculate the initial index using the hash function
        index = self.hash_function(key)
        attempt = 1

        # Continue probing until the key is found or an empty slot is encountered
        while self.__keys[index] != key:
            if self.__buckets[index] is None:
                return  # Key not found, exit the method
            index = self.rehash_function(key, attempt)
            attempt += 1

        # Once the key is found, delete the entry by setting the bucket and key to None
        self.__buckets[index] = None
        self.__keys[index] = None
        self.__count -= 1  # Decrement the count of entries
        self.__bst.delete(key)  # Delete the key from the binary search tree

    def __contains__(self, key):
        """
        Checks if the hashtable contains a given key.

        Parameters:
            key: The key to be checked.

        Returns:
            bool: True if the key is present, False otherwise.
        """
        # Calculate the initial index using the hash function
        index = self.hash_function(key)
        attempt = 1

        # Continue probing until the key is found or an empty slot is encountered
        while self.__keys[index] != key:
            if self.__buckets[index] is None:
                return False  # Key not found, return False
            index = self.rehash_function(key, attempt)
            attempt += 1

        return True  # Key found, return True

    def __len__(self):
        """
        Returns the number of entries in the hashtable.

        Returns:
            int: The number of entries.
        """
        return self.__count

    def __iter__(self):
        """
        Initializes the iterator for the hashtable.

        Returns:
            Hashtable: The hashtable iterator.
        """
        # Reset the current index to the beginning of the hashtable
        self.__current_index = 0
        return self

    def __next__(self):
        """
        Retrieves the next key in the hashtable.

        Returns:
            object: The next key.
        
        Raises:
            StopIteration: If there are no more __keys to iterate over.
        """
        # Iterate over the hashtable until a key is found or the end is reached
        while self.__current_index < self.__size:
            # If the current index points to a non-empty slot, return the key
            if self.__keys[self.__current_index] is not None:
                key = self.__keys[self.__current_index]
                self.__current_index += 1
                return key
            # Move to the next index
            self.__current_index += 1
        
        # If no more keys are found, raise StopIteration
        raise StopIteration

    def clear(self):
        """
        Clears all entries from the hashtable.
        """
        self.__size = 100
        self.__count = 0
        self.__keys = [None] * self.__size
        self.__buckets = [None] * self.__size
        self.__bst = BinarySearchTree()

    def load_factor(self):
        """
        Calculates the load factor of the hashtable.

        Returns:
            float: The load factor.
        """
        return self.__count / self.__size

    def resize(self):
        """
        Dynamic Resizing resizes the hashtable when the load factor exceeds a threshold.
        """
        # Calculate the new size as double the current size
        new_size = self.__size * 2
        # Store references to the old buckets and keys
        old_buckets = self.__buckets
        old_keys = self.__keys
        # Initialize new buckets and keys lists with the new size
        self.__buckets = [None] * new_size
        self.__keys = [None] * new_size
        # Update the size attribute
        self.__size = new_size
        # Reset the count of entries to 0
        self.__count = 0
        # Reinitialize the binary search tree
        self.__bst = BinarySearchTree()

        # Rehash and reinsert all the old key-value pairs into the resized hashtable
        for key in old_keys:
            if key is not None:
                self[key] = old_buckets[old_keys.index(key)]

    """
    OOP Principles applied

    Encapsulation:
    Private attributes: Attributes such as __size, __count, __keys, __buckets, __current_index, and __bst are declared as private by prefixing them with double underscores (__). This ensures that they cannot be directly accessed or modified from outside the class.
    Getter methods: Methods like get_size(), get_count(), get_keys(), get_buckets(), get_current_index(), and get_bst() are provided to access the private attributes.
    Setter methods: Methods like set_size(), set_count(), set_keys(), set_buckets(), set_current_index(), and set_bst() are provided to modify the private attributes. This allows controlled access to these attributes.

    Polymorphism:
    Special methods like __getitem__(), __setitem__(), __delitem__(), __contains__(), __len__(), __iter__(), and __next__() provide a common interface for interacting with the Hashtable object.
    For example, __getitem__() allows retrieving values associated with keys using the indexing notation (my_hashtable[key]), __iter__() enables iteration over the hashtable keys using a loop or comprehension, and so on. These methods exhibit polymorphic behavior, allowing flexibility in how the Hashtable object is used.

    Abstraction:
    Internal implementation details of the hashtable, such as hash function computation, rehashing, resizing, and handling collisions, are abstracted away from the user.
    Users interact with the Hashtable class through its public interface, which includes methods like __getitem__(), __setitem__(), __delitem__(), __contains__(), __len__(), __iter__(), and clear(). This abstraction hides the complexity of the underlying operations, providing a simplified interface for users to work with.

    Modularity:
    Each method in the Hashtable class serves a specific purpose, promoting modularity and code reusability. 
    This modular design makes the class easier to understand, maintain, and extend.

    """