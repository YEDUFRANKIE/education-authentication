

from EduRecord import EduRecord
import os, time
import pymysql
from EduRecord import EduRecord
from EduMerkleTree import EduMerkleTree
from EduBlock import EduBlock

host = 'localhost'
port = 3306
db = 'EducationVerification'
user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PWD')

MerkleTreeHeader = EduMerkleTree()


def get_connection():
    conn = pymysql.connect(host=host, port=port, db=db,
                           user=user, password=password)
    return conn


def clean_table(name='Edu_Record'):
    conn = get_connection()
    cursor = conn.cursor()
    sql = 'Delete from '+name
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def createEduRecord(name, id, gender, university, birthday, admissionDate,
                    isGraduated=False, isVerify=False, graduationDate=None,
                    classification=None, style=None, major=None):
    a = EduRecord(name, id, gender, university, birthday, admissionDate,
                  isGraduated, isVerify, graduationDate,
                  classification, style, major)

    conn = get_connection()
    cursor = conn.cursor()
    sql = "Insert into `Edu_Record` value (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    data = [id, name, gender, university, birthday, admissionDate, isGraduated, graduationDate, classification, style, major, isVerify]
    cursor.execute(sql, data)
    conn.commit()
    cursor.close()
    conn.close()

    return a


def authentication(record, merkleTree=MerkleTreeHeader):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "update `Edu_Record` SET isVerify=1 Where id=%s"
    data = [record.Student_ID]
    cursor.execute(sql, data)
    conn.commit()
    cursor.close()
    conn.close()

    merkleTree.addNodeToList(record)

def pushToChain(merkleTree=MerkleTreeHeader):
    # get the last block of the block chain
    conn = get_connection()
    cursor = conn.cursor()
    sql = "select * from Block order by id desc limit 1"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    if not result:
        newBlock = EduBlock(None)
    else:
        newBlock = EduBlock(result[0][1])


    newBlock.addMerkleTree(merkleTree)

    conn = get_connection()
    cursor = conn.cursor()
    sql = "Insert into Block (BlockHash, prevHash, merkleRoot, timeCreated) Value (%s,%s,%s,%s) "
    ts = time.strftime("%Y-%m-%d", time.localtime(newBlock.timestamp))
    data = [newBlock.thisBlock, newBlock.prevBlock, newBlock.merkleRoot, ts]
    cursor.execute(sql, data)
    block_id = cursor.lastrowid
    conn.commit()
    cursor.close()
    conn.close()

    conn = get_connection()
    cursor = conn.cursor()
    sql = "Insert into Search_Set (student_id, block_id) Value (%s, %s)"
    data = []
    for i in merkleTree.eduList:
        data.append((i.Student_ID, block_id))
    cursor.executemany(sql, data)
    conn.commit()
    cursor.close()
    conn.close()

    merkleTree = EduMerkleTree()


def verifyEdu(blockHash, student_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "Select block_id from Search_Set where student_id="+student_id
    cursor.execute(sql)
    Search_Set_result = cursor.fetchall()
    cursor.close()
    conn.close()

    if Search_Set_result:
        conn = get_connection()
        cursor = conn.cursor()
        sql = "Select id from Block where BlockHash='{0}'".format(blockHash)
        cursor.execute(sql)
        Block_result = cursor.fetchall()
        cursor.close()
        conn.close()

        if Block_result:
            for i in Search_Set_result:
                if i[0] == Block_result[0][0]:
                    return True
    return False

if __name__ == "__main__":

    # # Student submit the education information
    # s1 = createEduRecord("zhangsan", '201103', 'male', 'UoL', '2011-01-02', '2021-01-02', 1, 0,'2022-02-02', '', '')
    # s2 = createEduRecord("lizi", '201104', 'female', 'UCLA', '2012-01-02', '2020-01-02', 1, 0,'2022-02-02', '', '')
    # s3 = createEduRecord("alice", '201105', 'male', 'CMU', '2012-01-02', '2020-01-02', 1, 0,'2022-02-02', '', '')
    # s4 = createEduRecord("bob", '201106', 'male', 'NYU', '2012-01-02', '2020-01-02', 1, 0,'2022-02-02', '', '')
    # s5 = createEduRecord("charli", '201107', 'female', 'UCLA', '2012-01-02', '2020-01-02', 1, 0,'2022-02-02', '', '')

    # # Authority confirm the education information and add to the merkle tree
    # authentication(s1)
    # authentication(s2)
    # authentication(s4)
    # authentication(s5)

    # # Push all the nodes in merkel tree in to the block chain
    # pushToChain(MerkleTreeHeader)

    print(verifyEdu(
        "35dd7b3fb3ea4eff399d2bb8c3dd3bae41cf56a5897915206a6dade8ef2577b8", "201105"))
    print(verifyEdu(
        "35dd7b3fb3ea4eff399d2bb8c3dd3bae41cf56a5897915206a6dade8ef2577b8", "201106"))
