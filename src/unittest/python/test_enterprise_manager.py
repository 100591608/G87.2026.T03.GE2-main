"""Testing file for EnterpriseManager"""
from unittest import TestCase
from uc3m_consulting import EnterpriseManager


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
        project_description = "competition development test"
        department = "LEGAL"
        date = "30/11/2027"
        budget = 1000000
        output = enterprise_manager.register_project(company_cif, project_acronym, project_description, department,
                                                     date, budget)
        self.assertEqual("96749da7fd992e68b7c87fa8831a7001", output)

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
        self.fail()

    def test_TC6(self):
        self.fail()

    def test_TC7(self):
        self.fail()

    def test_TC8(self):
        self.fail()

    def test_TC9(self):
        self.fail()

    def test_TC10(self):
        self.fail()

    def test_TC11(self):
        self.fail()

    def test_TC12(self):
        self.fail()

    def test_TC13(self):
        self.fail()

    def test_TC14(self):
        self.fail()

    def test_TC15(self):
        self.fail()

    def test_TC16(self):
        self.fail()

    def test_TC17(self):
        self.fail()

    def test_TC18(self):
        self.fail()

    def test_TC19(self):
        self.fail()

    def test_TC20(self):
        self.fail()

    def test_TC21(self):
        self.fail()

    def test_TC22(self):
        self.fail()

    def test_TC23(self):
        self.fail()

    def test_TC24(self):
        self.fail()

    def test_TC25(self):
        self.fail()

    def test_TC26(self):
        self.fail()

    def test_TC27(self):
        self.fail()

    def test_TC28(self):
        self.fail()

    def test_TC29(self):
        self.fail()

    def test_TC30(self):
        self.fail()

    def test_TC31(self):
        self.fail()

    def test_TC32(self):
        self.fail()

    def test_TC33(self):
        self.fail()
