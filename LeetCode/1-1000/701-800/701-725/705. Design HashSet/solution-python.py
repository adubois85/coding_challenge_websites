class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_table = {}

    def add(self, key: int) -> None:
        hashed = hash(key)
        if not self.contains(key):
            # Had to swich to a try/except block as I was getting key errors
            # even when I was just checking if a key existed.  I initially also
            # tried using tuples, but it became problematic in the remove
            # method if e.g. we needed to remove the second item at a hash as
            # tuples are immutable
            # If there's a hash collision, it will set anything already there
            # as the second item in a list and the new key as the first;
            # otherwise, the second item in the list is just None
            try:
                self.hash_table[hashed] = [key, self.hash_table[hashed]]
            except KeyError:
                self.hash_table[hashed] = [key, None]

    def remove(self, key: int) -> None:
        if self.contains(key):
            hashed = hash(key)
            # if the 2nd item in the list is None, there are no hash collisions
            # and we can just delete the key.  If it isn't None...
            if self.hash_table[hashed][1] is None:
                del self.hash_table[hashed]
                return
            head = self.hash_table[hashed]
            # There could be many keys at a given hash chained together, so we
            # need to figure out how deep in the stack it is
            depth = 0
            while self.hash_table[hashed] is not None:
                if key == self.hash_table[hashed][0]:
                    break
                depth += 1
                self.hash_table[hashed] = self.hash_table[hashed][1]
            self.hash_table[hashed] = head
            if depth == 0:
                # if the key to be removed is the first at a hash, just set the
                # hash's value to the 2nd item, whether that's a single other
                # key or several chained together
                self.hash_table[hashed] = self.hash_table[hashed][1]
            else:
                # if it's not, we need to join the value before the one to be
                # removed with the one after
                for i in range(depth - 1):
                    self.hash_table[hashed] = self.hash_table[hashed][1]
                self.hash_table[hashed][1] = self.hash_table[hashed][1][1]
                self.hash_table[hashed] = head

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashed = hash(key)
        # as with the add method, had to switch to a try/except block because
        # I was getting key errors when attempting to check if a key were in
        # the hash table
        try:
            if self.hash_table[hashed] is not None:
                if key == self.hash_table[hashed][0]:
                    return True
                if self.hash_table[hashed][1] is None:
                    return False
                temp = self.hash_table[hashed]
                while self.hash_table[hashed] is not None:
                    self.hash_table[hashed] = self.hash_table[hashed][1]
                    if key == self.hash_table[hashed][0]:
                        self.hash_table[hashed] = temp
                        return True
                self.hash_table[hashed] = temp
        except KeyError:
            return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
