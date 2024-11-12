import School.Module_12_Поддержка_цикла_разработки.HomeWork.m12_hw2_.runner_and_tournament as runner
import unittest


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.Usain = runner.Runner('Усэйн', 10)
        self.Andre = runner.Runner('Андрей', 9)
        self.Nick = runner.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        pass
        # for i in cls.all_results.values():
        #     print(i, '\n')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        self.Tournament = runner.Tournament(90, self.Usain, self.Nick)
        self.all_results[1] = self.Tournament.start()
        self.assertTrue(self.all_results[len(self.all_results)][2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        self.Tournament = runner.Tournament(90, self.Andre, self.Nick)
        self.all_results[2] = self.Tournament.start()
        self.assertTrue(self.all_results[len(self.all_results)][2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        self.Tournament = runner.Tournament(90, self.Usain, self.Andre, self.Nick)
        self.all_results[3] = self.Tournament.start()
        self.assertTrue(self.all_results[len(self.all_results)][3] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_4(self):
        self.Tournament = runner.Tournament(2, self.Usain, self.Andre, self.Nick)
        self.all_results[4] = self.Tournament.start()
        self.assertTrue(self.all_results[len(self.all_results)][3] == 'Ник')


if __name__ == '__main__':
    unittest.main()
