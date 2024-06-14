import unittest
class TestProgrammer(unittest.TestCase):
    def setUp(self):
        self.prog = Programmer('Valeria', 'Junior')

    def test_work(self):
        self.assertEqual(Programmer.work(self.prog, 50), 1000)

    def test_str(self):
        with self.assertRaises(TypeError):
            Programmer.work('unsupported operand type(s) for +=: int and str')


    def test_info(self):
        self.assertEqual(Programmer.info(self.prog), f'Valeria:отработано 0 ч. оклад составляет:0 тгр.')

    # # Place your tests here

if __name__ == '__main__':
    unittest.main()

