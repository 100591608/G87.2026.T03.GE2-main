"""Module """
import json
import datetime
from uc3m_consulting.enterprise_project import EnterpriseProject
from uc3m_consulting.enterprise_management_exception import EnterpriseManagementException

class EnterpriseManager:
    """Class for providing the methods for managing the orders"""
    # def __init__(self):
    #     pass

    def register_project(self, company_cif: str, project_acronym: str,
                         project_description: str, department: str, date: str, budget: float):
        """Registers a new enterprise project"""

        # Company CIF
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

        # Project Acronym
        if not isinstance(project_acronym, str):
            raise EnterpriseManagementException("Invalid Project Acronym - Wrong Data Type")

        if len(project_acronym) < 5:
            raise EnterpriseManagementException("Invalid Project Acronym - Too Short")

        if len(project_acronym) > 10:
            raise EnterpriseManagementException("Invalid Project Acronym - Too Long")

        if not all(char.isdigit() or ('A' <= char <= 'Z') for char in project_acronym):
            raise EnterpriseManagementException("Invalid Project Acronym - Not Valid String")

        # Project Description
        if not isinstance(project_description, str):
            raise EnterpriseManagementException("Invalid Project Description - Wrong Data Type")

        if len(project_description) < 10:
            raise EnterpriseManagementException("Invalid Project Description - Too Short")

        if len(project_description) > 30:
            raise EnterpriseManagementException("Invalid Project Description - Too Long")

        # Department
        if not isinstance(department, str):
            raise EnterpriseManagementException("Invalid Department - Wrong Data Type")

        if department not in {"HR", "LEGAL", "LOGISTICS", "FINANCE"} :
            raise EnterpriseManagementException("Invalid Department - Invalid Value")

        # Date
        if not isinstance(date, str):
            raise EnterpriseManagementException("Invalid Date - Wrong Data Type")

        if not isinstance(date, str):
            raise EnterpriseManagementException("Invalid Date - Wrong Data Type")

        if len(date) != 10 or date[2] != "/" or date[5] != "/":
            raise EnterpriseManagementException("Invalid Date - Wrong Format")

        day_str = date[0:2]
        month_str = date[3:5]
        year_str = date[6:10]

        if not day_str.isdigit() or not month_str.isdigit() or not year_str.isdigit():
            raise EnterpriseManagementException("Invalid Date - Wrong Format")

        day = int(day_str)
        month = int(month_str)
        year = int(year_str)

        if day < 1:
            raise EnterpriseManagementException("Invalid Date - Invalid Day")

        if day > 31:
            raise EnterpriseManagementException("Invalid Date - Invalid Day")

        if month < 1:
            raise EnterpriseManagementException("Invalid Date - Invalid Month")

        if month > 12:
            raise EnterpriseManagementException("Invalid Date - Invalid Month")

        if year < 2025:
            raise EnterpriseManagementException("Invalid Date - Invalid Year")

        if year > 2027:
            raise EnterpriseManagementException("Invalid Date - Invalid Year")

        # Budget
        if not isinstance(budget, float):
            raise EnterpriseManagementException("Invalid Budget - Wrong Data Type")

        if budget < 50000.00:
            raise EnterpriseManagementException("Invalid Budget - Too Low Value")

        if budget > 1000000.00:
            raise EnterpriseManagementException("Invalid Budget - Too High Value")

        if round(budget, 2) != budget:
            raise EnterpriseManagementException("Invalid Budget - Too Many Decimals")

        budget_str = str(budget)
        if '.' in budget_str:
            decimals = len(budget_str.split('.')[1])
            if decimals < 2 and not budget_str.endswith('.0'):
                raise EnterpriseManagementException("Invalid Budget - Too Little Decimals")

        obj = EnterpriseProject(company_cif, project_acronym, project_description, department, date, budget)
        return obj.project_id

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
