"""Testing file for EnterpriseManager"""
import unittest
from uc3m_consulting import EnterpriseManager
from uc3m_consulting import EnterpriseManagementException


class TestEnterpriseManager(unittest.TestCase):
    """Class for testing the EnterpriseManager class"""

    @classmethod
    def setUpClass(cls):
        print("Execute setUpClass Classmethod")

    @classmethod
    def tearDownClass(cls):
        print("Execute tearDownClass Classmethod")

    def setUp(self):
        print("Execute setUp")

    def tearDown(self):
        print("Execute tearDown")

    def test_TC1(self):
        """Valid Test Case 1"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.00
        output = enterprise_manager.register_project(company_cif, project_acronym,
                                                     project_description, department, date, budget)
        self.assertEqual("e59f691d9ac4975dde6e5acfca0f98e8", output)

    def test_TC2(self):
        """Valid Test Case 2"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ12"
        project_description = "competition"
        department = "FINANCE"
        date = "02/02/2026"
        budget = 50000.01
        output = enterprise_manager.register_project(company_cif, project_acronym,
                                                     project_description, department, date, budget)
        self.assertEqual("06bfa76853c4414f4607e8ed6107db6e", output)

    def test_TC3(self):
        """Valid Test Case 3"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJECT12"
        project_description = "competition development tests"
        department = "LEGAL"
        date = "30/11/2027"
        budget = 1000000.00
        output = enterprise_manager.register_project(company_cif, project_acronym,
                                                     project_description, department, date, budget)
        self.assertEqual("6241127df42cb7486858e3c8b46b58c2", output)

    def test_TC4(self):
        """Valid Test Case 4"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJECT123"
        project_description = "competitions development tests"
        department = "LOGISTICS"
        date = "31/12/2025"
        budget = 999999.99
        output = enterprise_manager.register_project(company_cif, project_acronym,
                                                     project_description, department, date, budget)
        self.assertEqual("b21123066aa51951c4887d33c68faf0d", output)

    def test_TC5(self):
        """Invalid Test Case 5 - Company CIF"""
        enterprise_manager = EnterpriseManager()
        company_cif = 123
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Company CIF - Wrong Data Type")

    def test_TC6(self):
        """Invalid Test Case 6 - Company CIF"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818502"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Company CIF")

    def test_TC7(self):
        """Invalid Test Case 7 - Company CIF"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A588185012"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Company CIF - Too Long")

    def test_TC8(self):
        """Invalid Test Case 8 - Company CIF"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A5881850"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Company CIF - Too Short")

    def test_TC9(self):
        """Invalid Test Case 9 - Company CIF"""
        enterprise_manager = EnterpriseManager()
        company_cif = "158818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Company CIF - Wrong Format")

    def test_TC10(self):
        """Invalid Test Case 10 - Project Acronym"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = 10000
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Project Acronym - Wrong Data Type")

    def test_TC11(self):
        """Invalid Test Case 11 - Project Acronym"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Project Acronym - Too Short")

    def test_TC12(self):
        """Invalid Test Case 12 - Project Acronym"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJECT1234"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Project Acronym - Too Long")

    def test_TC13(self):
        """Invalid Test Case 13 - Project Acronym"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "proj1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Project Acronym - Not Valid String")

    def test_TC14(self):
        """Invalid Test Case 14 - Project Description"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = 1234567890
        department = "HR"
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Project Description - Wrong Data Type")

    def test_TC15(self):
        """Invalid Test Case 15 - Project Description"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "blueberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Project Description - Too Short")

    def test_TC16(self):
        """Invalid Test Case 16 - Project Description"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "competitions developments tests"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Project Description - Too Long")

    def test_TC17(self):
        """Invalid Test Case 17 - Department"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = 123
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Department")

    def test_TC18(self):
        """Invalid Test Case 18 - Department"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "SALES"
        date = "01/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Department")

    def test_TC19(self):
        """Invalid Test Case 19 - Date"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = 1/1/2025 # Should maybe just change to int
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Date")

    def test_TC20(self):
        """Invalid Test Case 20 - Date"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/31/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Date")

    def test_TC21(self):
        """Invalid Test Case 21 - Date"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "00/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Date")

    def test_TC22(self):
        """Invalid Test Case 22 - Date"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "32/01/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Date")

    def test_TC23(self):
        """Invalid Test Case 23 - Date"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/00/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Date")

    def test_TC24(self):
        """Invalid Test Case 24 - Date"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/13/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Date")

    def test_TC25(self):
        """Invalid Test Case 25 - Date"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2024"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Date")

    def test_TC26(self):
        """Invalid Test Case 26 - Date"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2028"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Date")

    def test_TC27(self):
        """Invalid Test Case 27 - Date"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/02/2025"
        budget = 50000.00
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Date")

    def test_TC28(self):
        """Invalid Test Case 28 - Budget"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = "50000.00"
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Budget")

    def test_TC29(self):
        """Invalid Test Case 29 - Budget"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.0
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Budget")

    def test_TC30(self):
        """Invalid Test Case 30 - Budget"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.000
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Budget")

    def test_TC31(self):
        """Invalid Test Case 31 - Budget"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 49999.99
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Budget")

    def test_TC32(self):
        """Invalid Test Case 32 - Budget"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 1000000.01
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message, "Invalid Budget")

    def test_TC33(self):
        """Invalid Test Case 33 - Output"""
        enterprise_manager = EnterpriseManager()
        company_cif = "A58818501"
        project_acronym = "PROJ1"
        project_description = "strawberry"
        department = "HR"
        date = "01/01/2025"
        budget = 50000.01
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(company_cif, project_acronym,
                                                project_description, department, date, budget)
        self.assertEqual(cm.exception.message,
                         "Project with same name for the same CIF already existed in the data file")

if __name__ == '__main__':
    unittest.main()
