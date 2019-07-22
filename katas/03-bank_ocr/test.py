# To run this file, go to superior folder and from terminal
# python -m 03-bank_ocr.test
# replace "gabriel" with your file name

import unittest
from os.path import join, dirname, abspath
from . import gabriel as kata

TEST_DATA_PATH = join(dirname(abspath(__file__)), "test_cases")


class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_case_00(self):
        file_path = join(TEST_DATA_PATH, "test_case_00.txt")
        self.assertEqual(kata.read_file(file_path), "000000000")

    def test_case_01(self):
        file_path = join(TEST_DATA_PATH, "test_case_01.txt")
        self.assertEqual(kata.read_file(file_path), "111111111")

    def test_case_02(self):
        file_path = join(TEST_DATA_PATH, "test_case_02.txt")
        self.assertEqual(kata.read_file(file_path), "222222222")

    def test_case_03(self):
        file_path = join(TEST_DATA_PATH, "test_case_03.txt")
        self.assertEqual(kata.read_file(file_path), "333333333")

    def test_case_04(self):
        file_path = join(TEST_DATA_PATH, "test_case_04.txt")
        self.assertEqual(kata.read_file(file_path), "444444444")

    def test_case_05(self):
        file_path = join(TEST_DATA_PATH, "test_case_05.txt")
        self.assertEqual(kata.read_file(file_path), "555555555")

    def test_case_06(self):
        file_path = join(TEST_DATA_PATH, "test_case_06.txt")
        self.assertEqual(kata.read_file(file_path), "666666666")

    def test_case_07(self):
        file_path = join(TEST_DATA_PATH, "test_case_07.txt")
        self.assertEqual(kata.read_file(file_path), "777777777")

    def test_case_08(self):
        file_path = join(TEST_DATA_PATH, "test_case_08.txt")
        self.assertEqual(kata.read_file(file_path), "888888888")

    def test_case_09(self):
        file_path = join(TEST_DATA_PATH, "test_case_09.txt")
        self.assertEqual(kata.read_file(file_path), "999999999")

    def test_case_10(self):
        file_path = join(TEST_DATA_PATH, "test_case_10.txt")
        self.assertEqual(kata.read_file(file_path), "123456789")

    def test_valid_account_number(self):
        self.assertEqual(kata.validate_account_number("457508000"), True)

    def test_invalid_account_number(self):
        self.assertEqual(kata.validate_account_number("664371495"), False)

    def test_case_11(self):
        file_path = join(TEST_DATA_PATH, "test_case_11.txt")
        self.assertEqual(kata.get_status(file_path), "000000051")

    def test_case_12(self):
        file_path = join(TEST_DATA_PATH, "test_case_12.txt")
        self.assertEqual(kata.get_status(file_path), "49006771? ILL")

    def test_case_13(self):
        file_path = join(TEST_DATA_PATH, "test_case_13.txt")
        self.assertEqual(kata.get_status(file_path), "1234?678? ILL")

    def test_case_14(self):
        file_path = join(TEST_DATA_PATH, "test_case_14.txt")
        self.assertEqual(kata.get_possibles(file_path), "711111111")

    def test_case_15(self):
        file_path = join(TEST_DATA_PATH, "test_case_15.txt")
        self.assertEqual(kata.get_possibles(file_path), "777777177")

    def test_case_16(self):
        file_path = join(TEST_DATA_PATH, "test_case_16.txt")
        self.assertEqual(kata.get_possibles(file_path), "200800000")

    def test_case_17(self):
        file_path = join(TEST_DATA_PATH, "test_case_17.txt")
        self.assertEqual(kata.get_possibles(file_path), "333393333")

    def test_case_18(self):
        file_path = join(TEST_DATA_PATH, "test_case_18.txt")
        self.assertEqual(kata.get_possibles(file_path), "888888888 AMB ['888886888', '888888880', '888888988']")

    def test_case_19(self):
        file_path = join(TEST_DATA_PATH, "test_case_19.txt")
        self.assertEqual(kata.get_possibles(file_path), "555555555 AMB ['555655555', '559555555']")

    def test_case_20(self):
        file_path = join(TEST_DATA_PATH, "test_case_20.txt")
        self.assertEqual(kata.get_possibles(file_path), "666666666 AMB ['666566666', '686666666']")

    def test_case_21(self):
        file_path = join(TEST_DATA_PATH, "test_case_21.txt")
        self.assertEqual(kata.get_possibles(file_path), "999999999 AMB ['899999999', '993999999', '999959999']")

    def test_case_22(self):
        file_path = join(TEST_DATA_PATH, "test_case_22.txt")
        self.assertEqual(kata.get_possibles(file_path), "490067715 AMB ['490067115', '490067719', '490867715']")

    def test_case_23(self):
        file_path = join(TEST_DATA_PATH, "test_case_23.txt")
        self.assertEqual(kata.get_possibles(file_path), "123456789")

    def test_case_24(self):
        file_path = join(TEST_DATA_PATH, "test_case_24.txt")
        self.assertEqual(kata.get_possibles(file_path), "000000051")

    def test_case_25(self):
        file_path = join(TEST_DATA_PATH, "test_case_25.txt")
        self.assertEqual(kata.get_possibles(file_path), "490867715")


if __name__ == '__main__':
    unittest.main()
