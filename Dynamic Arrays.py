class DynamicArray:
    def __init__(self, factor=2):
        self.factor = factor
        self.data = []

    def insert(self, index, value):
        if index < 0 or index > len(self.data):
            raise IndexError("Index out of range")

        self.data.insert(index, value)

    def delete(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")

        del self.data[index]

    def size(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def rotate(self, k):
        if len(self.data) == 0 or k % len(self.data) == 0:
            return

        k = k % len(self.data)
        self.data[:] = self.data[-k:] + self.data[:-k]

    def reverse(self):
        self.data.reverse()

    def append(self, value):
        self.data.append(value)

    def prepend(self, value):
        self.data.insert(0, value)

    def merge(self, other_array):
        self.data.extend(other_array.data)

    def interleave(self, other_array):
        result = []
        size = min(len(self.data), len(other_array.data))
        for i in range(size):
            result.append(self.data[i])
            result.append(other_array.data[i])

        if len(self.data) > size:
            result.extend(self.data[size:])
        elif len(other_array.data) > size:
            result.extend(other_array.data[size:])

        self.data = result

    def middle_element(self):
        if len(self.data) == 0:
            return None
        return self.data[len(self.data) // 2]

    def index_of(self, value):
        try:
            return self.data.index(value)
        except ValueError:
            return -1

    def split(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")

        array1 = DynamicArray(factor=self.factor)
        array2 = DynamicArray(factor=self.factor)
        array1.data = self.data[:index]
        array2.data = self.data[index:]
        return array1, array2

    def resize(self, new_factor):
        if new_factor <= 0:
            raise ValueError("Factor must be greater than 0")
        
        new_data = []
        for value in self.data:
            new_data.append(value)
            if len(new_data) % new_factor == 0:
                new_data.extend([None] * (new_factor - 1))

        self.data = new_data

    def print_array(self):
        print(self.data)

# Example :
arr1 = DynamicArray()
arr1.append(1)
arr1.append(2)
arr1.append(3)

arr2 = DynamicArray()
arr2.append(4)
arr2.append(5)
arr2.append(6)

print("Original arrays:")
arr1.print_array()
arr2.print_array()

arr1.merge(arr2)
print("\nAfter merging:")
arr1.print_array()

print("\nMiddle element:", arr1.middle_element())
print("Index of element 3:", arr1.index_of(3))

arr3, arr4 = arr1.split(2)
print("\nAfter splitting at index 2:")
print("First array:")
arr3.print_array()
print("Second array:")
arr4.print_array()

arr1.rotate(2)
print("\nAfter rotating by 2 positions:")
arr1.print_array()

arr1.reverse()
print("\nAfter reversing:")
arr1.print_array()

arr1.insert(1, 7)
print("\nAfter inserting 7 at index 1:")
arr1.print_array()

arr1.delete(3)
print("\nAfter deleting element at index 3:")
arr1.print_array()

print("\nSize of array:", arr1.size())
print("Is the array empty?", arr1.is_empty())

arr1.prepend(0)
print("\nAfter prepending 0 to the array:")
arr1.print_array()

arr5 = DynamicArray()
arr5.append(8)
arr5.append(9)
arr5.append(10)
arr1.interleave(arr5)
print("\nAfter interleaving with another array [8, 9, 10]:")
arr1.print_array()

arr1.resize(3)
print("\nAfter resizing with factor 3:")
arr1.print_array()
