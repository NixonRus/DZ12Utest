import unittest
import RunnerTest
import TournamentTest


suite_calk = unittest.TestSuite()

suite_calk.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest.TunnerTest))
suite_calk.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite_calk)
