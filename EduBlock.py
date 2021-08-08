import hashlib
import time

class EduBlock:

    prevBlock = None
    merkleRoot = None
    merkleTree = None
    timestamp = None
    isHeader = True
    thisBlock = None

    def __init__(self, prev):
        self.prevBlock = prev
        self.timestamp = int(time.time())
        self.merkleRoot = None
        self.merkleTree = None
        self.isHeader = True
        self.thisBlock = None

    def __str__(self):
        return "ts: "+str(self.timestamp)+"\n"+"prevBlock: "+str(self.prevBlock)

    def addMerkleTree(self, merkleTree):
        self.isHeader = False
        self.merkleTree = merkleTree
        self.merkleRoot = self.merkleTree.getMerkleRoot()
        data = {
            "timestamp": self.timestamp,
            "prevBlock": self.prevBlock,
            "merkleRoot": self.merkleRoot
        }
        self.thisBlock = hashlib.sha256(str(data).encode('utf-8')).hexdigest()
        return self.thisBlock

if __name__ == '__main__':
    pass
