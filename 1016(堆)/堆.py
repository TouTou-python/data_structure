class Heap:
    def __init__(self):
        self.data_list = []

    def get_parent_index(self, child_index):
        if child_index == 0 or child_index > len(self.data_list) - 1:
            return None
        else:
            return (child_index - 1) >> 1

    def swap(self, index_a, index_b):

        self.data_list[index_a], self.data_list[index_b] = self.data_list[index_b], self.data_list[index_a]

    def insert(self, data):
        self.data_list.append(data)
        index = len(self.data_list) - 1
        parent = self.get_parent_index(index)
        while parent is not None and self.data_list[index] > self.data_list[parent]:
            self.swap(index, parent)
            index = parent
            parent = self.get_parent_index(index)

    def pop(self):
        del_data = self.data_list[0]
        self.data_list[0] = self.data_list[-1]
        del self.data_list[-1]
        self.heapify(0)
        return del_data

    def heapify(self, index):  # 堆化
        total_index = len(self.data_list) - 1
        while True:
            maxvalue_index = index
            if 2 * index + 1 < total_index and self.data_list[2 * index + 1] > self.data_list[maxvalue_index]:
                maxvalue_index = 2 * index + 1
            if 2 * index + 2 < total_index and self.data_list[2 * index + 2] > self.data_list[maxvalue_index]:
                maxvalue_index = 2 * index + 2
            if maxvalue_index == index:
                break
            self.swap(index, maxvalue_index)
            index = maxvalue_index


if __name__ == '__main__':
    heap = Heap()
    heap.insert(1)
    heap.insert(2)
    heap.insert(3)
    heap.insert(4)
    heap.insert(5)
    heap.insert(6)
    heap.insert(7)
    print(heap.data_list)
