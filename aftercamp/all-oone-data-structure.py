class AllOne:

    def __init__(self):
        self.mini = 0
        self.maxi = 0
        self.key_count = defaultdict(int)
        self.count_key = defaultdict(set)

    def inc(self, key):
        count = self.key_count[key]
        newmaxi = count
        newmini = self.mini

        if count:
            curr_keys = self.count_key[count]
            curr_keys.remove(key)
            if not curr_keys:
                del self.count_key[count]
            else:
                self.count_key[count] = curr_keys
            if not curr_keys and self.mini == count:
                newmini += 1

            set_count_plus_1 = self.count_key[count + 1]
            set_count_plus_1.add(key)
            self.count_key[count + 1] = set_count_plus_1

            self.key_count[key] = count + 1
            newmaxi = count + 1
        else:
            self.key_count[key] = 1
            curr_keys = self.count_key[1]
            curr_keys.add(key)
            self.count_key[1] = curr_keys
            newmini = 1
            newmaxi = 1

        self.mini = newmini
        self.maxi = max(self.maxi, newmaxi)

    def dec(self, key):
        count = self.key_count[key]
        if count:
            curr_keys = self.count_key[count]
            curr_keys.remove(key)
            if not curr_keys:
                del self.count_key[count]
            else:
                self.count_key[count] = curr_keys

            if count == 1:
                self.key_count.pop(key, None)
            else:
                set_count_minus_1 = self.count_key[count - 1]
                set_count_minus_1.add(key)
                self.count_key[count - 1] = set_count_minus_1

                self.key_count[key] = count - 1

            if not curr_keys and self.maxi == count:
                self.maxi -= 1
            if not curr_keys and self.mini == count:
                min_count = self.maxi
                for k in self.count_key.keys():
                    min_count = min(min_count, k)
                if self.count_key and len(self.count_key) > 0:
                    self.mini = min_count

    def getMaxKey(self):
        set_max = self.count_key[self.maxi]
        if set_max:
            val = set_max.pop()
            set_max.add(val)
            return val
        return ""

    def getMinKey(self):
        set_min = self.count_key[self.mini]
        if set_min:
            val = set_min.pop()
            set_min.add(val)
            return val
        return ""
# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()