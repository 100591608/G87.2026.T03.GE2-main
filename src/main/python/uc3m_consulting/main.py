"""Python Script for getting MD5 Hash of an order"""

from uc3m_consulting import enterprise_project

def showMD5():
    obj= enterprise_project.EnterpriseProject('B86666660','PROJ01','Car sharing beta release','HR','01/01/2026',75000)
    print(obj.project_id)

if __name__ == '__main__':
    showMD5()
