class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪"*self.size

    
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value >= 0:
            self._capacity = value
        else:
            raise ValueError("Capacity can't be negative")

        
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, n):
        if n > self.capacity:
            raise ValueError("Can't exceed the jar capacity")
        elif n < 0:
            raise ValueError(f"Can't withdraw more than {self.size} size")
        else:
            self._size = n

    def deposit(self, n):
            self.size += n

    def withdraw(self, n):
            self.size -= n


def main():
    cookies = Jar(50)
    print(cookies)
    cookies.deposit(10)
    print(cookies)
    cookies.deposit(10)
    print(cookies)
    cookies.deposit(10)
    print(cookies)



if __name__ == "__main__":
    main()