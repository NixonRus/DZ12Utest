import unittest
from unittest import TestCase
from School.Module_12_Поддержка_цикла_разработки.HomeWork.m12_hw1_Простые_Юнит_Тесты.runner import Runner


class TunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        run = Runner('Ted')
        for i in range(10):
            run.walk()
        return self.assertEqual(run.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        run = Runner('Ted')
        for i in range(10):
            run.run()
        return self.assertEqual(run.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        run1 = Runner('Ted')
        run2 = Runner('Bil')
        for i in range(10):
            run1.run()
            run2.walk()
        return self.assertNotEqual(run1.distance, run2.distance)


if __name__ == '__main__':
    unittest.main()
