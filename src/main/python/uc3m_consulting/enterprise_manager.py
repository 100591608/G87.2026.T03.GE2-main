"""Module """
from .enterprise_project import EnterpriseProject
from .enterprise_management_exception import EnterpriseManagementException

class EnterpriseManager:
    """Class for providing the methods for managing the orders"""
    # def __init__(self):
    #     pass

    def register_project(self, company_cif: str, project_acronym: str,
                         project_description: str, department: str, date: str, budget: float):
        """Registers a new enterprise project"""
        obj = EnterpriseProject(company_cif, project_acronym, project_description,
                                department, date, budget)

        if not isinstance(company_cif, str):
            raise EnterpriseManagementException("Invalid Company CIF - Wrong Data Type")

        if len(company_cif) > 9:
            raise EnterpriseManagementException("Invalid Company CIF - Too Long")

        if len(company_cif) < 9:
            raise EnterpriseManagementException("Invalid Company CIF - Too Short")

        if not company_cif[0].isalpha() or not company_cif[1:8].isdigit() or not company_cif[8].isalnum():
            raise EnterpriseManagementException("Invalid Company CIF - Wrong Format")

        if not EnterpriseManager.validate_cif(company_cif):
            raise EnterpriseManagementException("Invalid Company CIF")

        if not isinstance(project_acronym, str):
            raise EnterpriseManagementException("Invalid Project Acronym - Wrong Data Type")

        if len(project_acronym) < 5:
            raise EnterpriseManagementException("Invalid Project Acronym - Too Short")

        if len(project_acronym) > 10:
            raise EnterpriseManagementException("Invalid Project Acronym - Too Long")

        if not project_acronym.isalnum() or not project_acronym.isupper():
            raise EnterpriseManagementException("Invalid Project Acronym - Not Valid String")

        if not isinstance(project_description, str):
            raise EnterpriseManagementException("Invalid Project Description - Wrong Data Type")


        return obj.project_id

        # Class example
        # try:
            # obj=EnterpriseProject(company_cif, project_acronym,
                                  # project_description, department, date, budget)
        #     data_list=obj.to_json()
        #     #save data into a file
        #     with open("my_file.json", "w", encoding="utf-8") as file:
        #         json.dump(data_list, file, indent=2)
        # exception (e):
        #     raise managementException("Wrong CIF Value")
        # return obj.project_id

    @staticmethod
    def validate_cif(cif):
        """Validate a CIF identifier. Return True if valid, False otherwise."""

        cif = str(cif).strip().upper()
        if len(cif) != 9:
            return False

        letter = cif[0]
        number_block = cif[1:8]
        control_char = cif[8]

        if not letter.isalpha() or not number_block.isdigit() or not control_char.isalnum():
            return False

        even_sum = sum(int(number_block[i]) for i in (1, 3, 5))

        odd_sum = 0
        for i in (0, 2, 4, 6):
            v = int(number_block[i]) * 2
            odd_sum += (v // 10) + (v % 10)

        total = even_sum + odd_sum
        base_digit = (10 - (total % 10)) % 10

        control_digit = str(base_digit)
        control_letter = "JABCDEFGHI"[base_digit]

        if letter in "ABEH":
            return control_char == control_digit
        if letter in "KPQS":
            return control_char == control_letter
        return control_char in (control_digit, control_letter)
