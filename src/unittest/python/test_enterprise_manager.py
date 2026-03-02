"""Testing file for EnterpriseManager"""
from unittest import TestCase
from uc3m_consulting import EnterpriseManager
from uc3m_consulting import EnterpriseManagementException


class TestEnterpriseManager(TestCase):
    """Class for testing the EnterpriseManager class"""

    def test_TC1(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.00
        output = enterprise_manager.register_project(company_cif, project_acronym, project_description, department, date, budget)
        self.assertEqual("e59f691d9ac4975dde6e5acfca0f98e8", output)

    def test_TC2(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ12"
        project_description = "competition"
        department = "FINANCE"
        date = "02/02/2026"
        budget = 50000.01
        output = enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                     date, budget)
        self.assertEqual("06bfa76853c4414f4607e8ed6107db6e", output)

    def test_TC3(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJECT12"
        project_description = "competition development tests"
        department = "LEGAL"
        date = "30/11/2027"
        budget = 1000000.00
        output = enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                     date, budget)
        self.assertEqual("6241127df42cb7486858e3c8b46b58c2", output)

    def test_TC4(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJECT123"
        project_description = "competitions development tests"
        department = "LOGISTICS"
        date = "31/12/2025"
        budget = 999999.99 # Have a look if this value is correct -TA
        output = enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                     date, budget)
        self.assertEqual("b21123066aa51951c4887d33c68faf0d", output)

    def test_TC5(self):
        enterprise_manager = EnterpriseManager()
        company_cif = 123
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                date, budget)
        self.assertEqual(cm.exception.message, "Invalid Company CIF")

    def test_TC6(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818502"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                         date, budget)
        self.assertEqual(cm.exception.message, "Invalid Company CIF")

    def test_TC7(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A588185012"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                         date, budget)
        self.assertEqual(cm.exception.message, "Invalid Company CIF")

    def test_TC8(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A5881850"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                         date, budget)
        self.assertEqual(cm.exception.message, "Invalid Company CIF")

    def test_TC9(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "158818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                         date, budget)
        self.assertEqual(cm.exception.message, "Invalid Company CIF")

    def test_TC10(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = 10000
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                date, budget)
        self.assertEqual(cm.exception.message, "Invalid Project Acronym")

    def test_TC11(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                date, budget)
        self.assertEqual(cm.exception.message, "Invalid Project Acronym")

    def test_TC12(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJECT1234"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                date, budget)
        self.assertEqual(cm.exception.message, "Invalid Project Acronym")

    def test_TC13(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "proj1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                date, budget)
        self.assertEqual(cm.exception.message, "Invalid Project Acronym")

    def test_TC14(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = 1234567890
        department = "HR"
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                date, budget)
        self.assertEqual(cm.exception.message, "Invalid Project Description")

    def test_TC15(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "blueberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                date, budget)
        self.assertEqual(cm.exception.message, "Invalid Project Description")

    def test_TC16(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "competitions developments tests"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                date, budget)
        self.assertEqual(cm.exception.message, "Invalid Project Description")

    def test_TC17(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = 123
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                date, budget)
        self.assertEqual(cm.exception.message, "Invalid Department")

    def test_TC18(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "SALES"
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                date, budget)
        self.assertEqual(cm.exception.message, "Invalid Department")

    def test_TC19(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = 1/1/2025 # Should maybe just change to int
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                date, budget)
        self.assertEqual(cm.exception.message, "Invalid Date")

    def test_TC20(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/31/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                date, budget)
        self.assertEqual(cm.exception.message, "Invalid Date")

    def test_TC21(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "00/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                date, budget)
        self.assertEqual(cm.exception.message, "Invalid Date")

    def test_TC22(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "32/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                date, budget)
        self.assertEqual(cm.exception.message, "Invalid Date")

    def test_TC23(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/00/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                date, budget)
        self.assertEqual(cm.exception.message, "Invalid Date")

    def test_TC24(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/13/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                date, budget)
        self.assertEqual(cm.exception.message, "Invalid Date")

    def test_TC25(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2024"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                date, budget)
        self.assertEqual(cm.exception.message, "Invalid Date")

    def test_TC26(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2028"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                date, budget)
        self.assertEqual(cm.exception.message, "Invalid Date")

    def test_TC27(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/02/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                date, budget)
        self.assertEqual(cm.exception.message, "Invalid Date")

    def test_TC28(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = "50000.00"
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                date, budget)
        self.assertEqual(cm.exception.message, "Invalid Budget")

    def test_TC29(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.0
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                date, budget)
        self.assertEqual(cm.exception.message, "Invalid Budget")

    def test_TC30(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.000
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                date, budget)
        self.assertEqual(cm.exception.message, "Invalid Budget")

    def test_TC31(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 49999.99
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                date, budget)
        self.assertEqual(cm.exception.message, "Invalid Budget")

    def test_TC32(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 1000000.01
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                date, budget)
        self.assertEqual(cm.exception.message, "Invalid Budget")

    def test_TC33(self):
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.01
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                date, budget)
        self.assertEqual(cm.exception.message, "Project with same name for the same CIF already existed in the data file")
