class TestHash:

    __hash_list = []

    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2

        TestHash.__hash_list.append(hash(self))

    @staticmethod
    def print_hash_objects_list():
        for hash_item in TestHash.__hash_list:
            print(hash_item)

    def __del__(self):
        TestHash.__hash_list.remove(hash(self))
        print('object has removed!')


t = TestHash(1, 10)
t1 = TestHash(2, 10)

TestHash.print_hash_objects_list()

del t

TestHash.print_hash_objects_list()
