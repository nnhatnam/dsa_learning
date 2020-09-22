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
            raise ValueError("Data cannot be None")

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

    #Test 2
    chain1 = BlockChain()
    chain1.print()                  #print nothing

    #Test 3
    chain2 = BlockChain()
    try:
        chain2.append(None)
    except Exception as e:
        print(e)                    #print Data cannot be None



