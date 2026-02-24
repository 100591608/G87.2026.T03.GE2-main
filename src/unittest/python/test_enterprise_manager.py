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
        expected_output = ""
        self.assertEqual(output, expected_output)

    def test_TC2(self):
        self.fail()

    def test_TC3(self):
        self.fail()

    def test_TC4(self):
        self.fail()

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
