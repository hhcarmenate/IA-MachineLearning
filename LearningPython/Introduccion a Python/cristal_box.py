import unittest


def es_mayor_de_edad(edad):
    if edad >= 18:
        return True

    return False


class CristalTestTest(unittest.TestCase):

    def test_es_mayor_de_edad(self):
        years = 20

        result = es_mayor_de_edad(years)
        self.assertEqual(result, True)

    def test_es_menor_de_edad(self):
        years = 15

        result = es_mayor_de_edad(years)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
