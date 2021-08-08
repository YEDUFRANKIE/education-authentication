from EduRecord import EduRecord
import hashlib, time

class EduMerkleTree():
    '''
        Once called `getMerkleRoot` the merkle tree is fixed.
        The new edu record cannot be inserted any more.
    '''
    eduList = None
    nodeHashList = []
    merkleRootHash = None
    isHeader = True

    def __init__(self, eduList=[]):
        self.eduList = eduList
        self.isHeader = True
        self.nodeHashList = []

    def __str__(self):
        nameList = []
        for i in self.eduList:
            nameList.append(i.Name)
        return str(nameList)

    def addNodeToList(self, eduNode):
        if self.isHeader:
            self.eduList.append(eduNode)

    def addListToList(self, eduList):
        if self.isHeader:
            self.eduList.extend(eduList)

    def calculateNodeHash(self):
        self.nodeHashList.clear()
        for i in self.eduList:
            self.nodeHashList.append(i.getHashCode())

    def calculateRootHash(self, nodeHash):
        if len(nodeHash) == 0:
            return hashlib.sha256(str(time.time()).encode('utf-8')).hexdigest()
        if len(nodeHash) == 1:
            return nodeHash[0]
        index = 0
        resultHash = []
        while(index < len(nodeHash)):
            if index+1 == len(nodeHash):
                resultHash.append(nodeHash[index])
                break
            resultHash.append(hashlib.sha256(
                str(nodeHash[index]+nodeHash[index+1]).encode('utf-8')).hexdigest())
            index += 2
        return self.calculateRootHash(resultHash)

    def getMerkleRoot(self):
        self.isHeader = False
        self.calculateNodeHash()
        self.merkleRootHash = self.calculateRootHash(self.nodeHashList)
        return self.merkleRootHash

if __name__ == '__main__':
    pass
