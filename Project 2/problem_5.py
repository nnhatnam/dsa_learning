import hashlib
from datetime import datetime
import time


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.prev = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class BlockChain:

    def __init__(self):
        self.tail = None
        self.size = 0

    def append(self, data=None):
        if data is None:
            print("Data cannot be None")
            return

        new_block = Block(datetime.utcnow(), data, None)
        if self.tail is None:
            self.tail = new_block
        else:
            new_block.previous_hash = self.tail.hash
            new_block.prev = self.tail
            self.tail = new_block
        self.size += 1

    def print(self):

        tail_block = self.tail
        
        if tail_block is not None:
            print("""
                                        | Data : {}         
                                        | Timestamp : {}    
                                        | hash : {}         
                                        | previous_hash: {}
                                    """.format(tail_block.data, tail_block.timestamp, tail_block.hash,
                                               tail_block.previous_hash))
            tail_block = tail_block.prev
            while tail_block is not None:
                print("""
                                                | Data : {}         
                                        <------ | Timestamp : {}    
                                                | hash : {}         
                                                | previous_hash: {} 
                                    """.format(tail_block.data, tail_block.timestamp, tail_block.hash, tail_block.previous_hash))
                tail_block = tail_block.prev


if __name__ == "__main__":

    #Test 1
    print("Test 1")
    chain = BlockChain()
    chain.append('Test 1')
    time.sleep(0.01)
    chain.append('Test 2')
    time.sleep(0.01)
    chain.append('Test 3')
    chain.print()

    # | Data : Test 3
    # | Timestamp : {time in utc}
    # | hash : 4a13e678473eddaa38956c52a185d6389dfcdf60338957dbd4a3c27b4862fa0b
    # | previous_hash : 32aaca368a545797f698c9422e68692e8c04fc9101a2d749fe4ec929c60992fe
    #
    #             | Data : Test 2
    # < --------- | Timestamp : {time in utc}
    #             | hash : 32aaca368a545797f698c9422e68692e8c04fc9101a2d749fe4ec929c60992fe
    #             | previous_hash: 26ea0ae294881f1260ecafec008426894e80bc4d7dc1cd6557ab9169e1a803ee
    #
    #             | Data : Test 1
    # < --------- | Timestamp : {time in utc}
    #             | hash : 26ea0ae294881f1260ecafec008426894e80bc4d7dc1cd6557ab9169e1a803ee
    #             | previous_hash: None



    # Test 3
    print("Test 2")
    chain.append(None)  #print Data cannot be None
    chain.append('Test 4')
    chain.append('Test 5')
    chain.append('Test 6')
    chain.print()
    # | Data : Test 6
    # | Timestamp : {time in utc}
    # | hash : 8de58fd4b61521298957f9fb14635d988293a404a39e30dfaafc55aeada0ece5
    # | previous_hash : cfde65e6d8b6b0acc9c27fff89938041c056164a84e01aab5db103c622fdcd23
    #
    #             | Data : Test 5
    # < --------- | Timestamp : {time in utc}
    #             | hash : cfde65e6d8b6b0acc9c27fff89938041c056164a84e01aab5db103c622fdcd23
    #             | previous_hash: 0478866021df3264351e23b0ae33fdb2f8be5dd1708133d0116df7121b676365
    #
    #             | Data : Test 4
    # < --------- | Timestamp : {time in utc}
    #             | hash : 0478866021df3264351e23b0ae33fdb2f8be5dd1708133d0116df7121b676365
    #             | previous_hash: 4a13e678473eddaa38956c52a185d6389dfcdf60338957dbd4a3c27b4862fa0b
    #
    #             | Data : Test 3
    # < --------- | Timestamp : {time in utc}
    #             | hash : 4a13e678473eddaa38956c52a185d6389dfcdf60338957dbd4a3c27b4862fa0b
    #             | previous_hash : 32aaca368a545797f698c9422e68692e8c04fc9101a2d749fe4ec929c60992fe
    #
    #             | Data : Test 2
    # < --------- | Timestamp : {time in utc}
    #             | hash : 32aaca368a545797f698c9422e68692e8c04fc9101a2d749fe4ec929c60992fe
    #             | previous_hash: 26ea0ae294881f1260ecafec008426894e80bc4d7dc1cd6557ab9169e1a803ee
    #
    #             | Data : Test 1
    # < --------- | Timestamp : {time in utc}
    #             | hash : 26ea0ae294881f1260ecafec008426894e80bc4d7dc1cd6557ab9169e1a803ee
    #             | previous_hash: None




    # Test 2
    print("Test 3")
    chain1 = BlockChain()
    chain1.print()                  #print nothing


