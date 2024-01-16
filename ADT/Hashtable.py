"""
Quadratic Probing: This technique involves looking for the next slot at an 
incrementally increasing distance from the original index. 
This helps to reduce clustering of entries.

Double Hashing: This method uses a second hash function to determine the 
step size for probing. This can be more effective than quadratic probing 
in reducing clustering but is slightly more complex to implement.

Now, let's address dynamic resizing:

Dynamic Resizing: The hash table should be able to resize itself when it 
becomes too full. A common strategy is to resize when the load factor 
(number of entries divided by the table size) exceeds a certain threshold, 
such as 0.7. Resizing involves creating a new, larger table and rehashing 
all the current entries into it.
"""

class Hashtable:
    def __init__(self, initial_size=100):
        self.size = initial_size
        self.count = 0
        self.keys = [None] * self.size
        self.buckets = [None] * self.size
        self.current_index = 0

    def hash_function(self, key):
        if isinstance(key, str):
            # Convert the string to an integer by summing the ASCII values of its characters
            key_sum = sum(ord(char) for char in key)
        elif isinstance(key, float):
            # Convert the float to an integer by multiplying by a large number
            key_sum = int(key * 1000000)  # This multiplier can be adjusted based on precision needs
        else:
            key_sum = int(key)  # Convert other types to int (for example, if key is already an int)

        return key_sum % self.size

    def rehash_function(self, key, attempt):
        if isinstance(key, str):
            # Convert the string to an integer by summing the ASCII values of its characters
            key_sum = sum(ord(char) for char in key)
        else:
            key_sum = key

        # Use the modified hash function for rehashing
        return (self.hash_function(key_sum) + attempt ** 2) % self.size

    def __setitem__(self, key, value):
        if self.load_factor() > 0.7:
            self.resize()

        index = self.hash_function(key)
        attempt = 1

        while self.buckets[index] is not None and self.keys[index] != key:
            index = self.rehash_function(key, attempt)
            attempt += 1

        if self.buckets[index] is None:
            self.count += 1
        self.buckets[index] = value
        self.keys[index] = key

    def __getitem__(self, key):
        index = self.hash_function(key)
        attempt = 1

        while self.keys[index] != key:
            if self.buckets[index] is None:
                return None
            index = self.rehash_function(key, attempt)
            attempt += 1

        return self.buckets[index]

    def __delitem__(self, key):
        index = self.hash_function(key)
        attempt = 1

        while self.keys[index] != key:
            if self.buckets[index] is None:
                return  # Key not found
            index = self.rehash_function(key, attempt)
            attempt += 1

        self.buckets[index] = None
        self.keys[index] = None
        self.count -= 1

    def __contains__(self, key):
        index = self.hash_function(key)
        attempt = 1

        while self.keys[index] != key:
            if self.buckets[index] is None:
                return False
            index = self.rehash_function(key, attempt)
            attempt += 1

        return True

    def __len__(self):
        return self.count

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        while self.current_index < self.size:
            if self.keys[self.current_index] is not None:
                key = self.keys[self.current_index]
                self.current_index += 1
                return key
            self.current_index += 1
        raise StopIteration

    def clear(self):
        self.size = 10
        self.count = 0
        self.keys = [None] * self.size
        self.buckets = [None] * self.size

    def load_factor(self):
        return self.count / self.size

    def resize(self):
        self.size *= 2
        old_buckets = self.buckets
        old_keys = self.keys
        self.buckets = [None] * self.size
        self.keys = [None] * self.size
        self.count = 0

        for key in old_keys:
            if key is not None:
                self[key] = old_buckets[self.hash_function(key)]