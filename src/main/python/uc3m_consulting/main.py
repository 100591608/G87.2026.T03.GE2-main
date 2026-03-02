"""Python Script for getting MD5 Hash of an order"""

from uc3m_consulting import enterprise_project

def showMD5():
    company_cif = "A58818501"
    project_acronym = "PROJECT12"
    project_description = "competition development tests"
    department = "LEGAL"
    date = "30/11/2027"
    budget = 1000000.00

    obj= enterprise_project.EnterpriseProject(company_cif,project_acronym,project_description,department, date,budget)
    print(obj.project_id)

    # Change input values for every test case here, paste output into result on spreadsheet



if __name__ == '__main__':
    showMD5()
