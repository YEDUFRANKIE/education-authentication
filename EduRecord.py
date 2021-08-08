
import time, hashlib

class EduRecord:

    Name = ""
    Student_ID = ""
    Gender = ""
    University = None
    Birthday = None
    AdmissionDate = None
    isGraduated = False
    GraduationDate = None
    Classification = None
    Style = None
    Major = None
    isVerify = False

    def __init__(self, name, id, gender, university, birthday, admissionDate,
                 isGraduated=False, isVerify=False, graduationDate=None,
                classification=None, style=None, major=None):
        '''
            birthday, admissionDate, graduationDate is formated as yyyy-mm-dd.
            Will cause ValueError, once the input date is invalid.
        '''
        self.Name = name
        self.Student_ID = id
        self.Gender = gender
        self.University = university

        self.Birthday = time.mktime(time.strptime(birthday, "%Y-%m-%d"))
        self.AdmissionDate = time.mktime(time.strptime(admissionDate, "%Y-%m-%d"))

        self.isGraduated = isGraduated
        self.isVerify = isVerify

        if isGraduated:
            self.GraduationDate = time.mktime(
                time.strptime(graduationDate, "%Y-%m-%d"))
        else:
            self.GraduationDate = graduationDate
        self.Classification = classification
        self.Style = style
        self.Major = major

    def __str__(self):
        data = {
            "Name": self.Name,
            "Student_ID": self.Student_ID,
            "Gender": self.Gender,
            "University": self.University,
            "Birthday": self.Birthday,
            "AdmissionDate": self.AdmissionDate,
            "isGraduated": self.isGraduated,
            "GraduationDate": self.GraduationDate,
            "Classification": self.Classification,
            "Style": self.Style,
            "Major": self.Major,
            "isVerify": self.isVerify,
        }
        return str(data)

    def getHashCode(self):
        data = {
            "Name": self.Name,
            "Student_ID": self.Student_ID,
            "Gender": self.Gender,
            "University": self.University,
            "Birthday": self.Birthday,
            "AdmissionDate": self.AdmissionDate,
            "isGraduated": self.isGraduated,
            "GraduationDate": self.GraduationDate,
            "Classification": self.Classification,
            "Style": self.Style,
            "Major": self.Major,
            "isVerify": self.isVerify,
        }
        return hashlib.sha256(str(data).encode('utf-8')).hexdigest()

if __name__ == "__main__":
    pass
