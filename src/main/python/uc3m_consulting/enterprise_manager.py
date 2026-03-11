"""Module """
from .enterprise_project import EnterpriseProject

class EnterpriseManager:
    """Class for providing the methods for managing the orders"""
    # def __init__(self):
    #     pass

    def register_project(self, company_cif: str, project_acronym: str,
                         project_description: str, department: str, date: str, budget: float):
        """Registers a new enterprise project"""
        pass
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
    def validate_cif(cif: str):
        """RETURNs TRUE IF THE IBAN RECEIVED IS VALID SPANISH IBAN,
        OR FALSE IN OTHER CASE"""
        return True
