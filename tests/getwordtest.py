## Couple of tests for our mdict ##
## Testing Testing Testing, Need more tests but don't have time ##
from click.testing import CliRunner
import unittest
from mdict import mdict


class mdictGetWordTests(unittest.TestCase):
    
    ## Checking if lower case word working ##
    def testGetWordLower(self):
        runner = CliRunner()
        result = runner.invoke(mdict, ['define', '-w', 'exercise'])
        self.assertEqual(result.exit_code, 0)
    ## Checking if upper case word working ## 
    def testGetWordUpper(self):
        runner = CliRunner()
        result = runner.invoke(mdict, ['define', '-w', 'EXERCISE'])
        self.assertEqual(result.exit_code, 0)

if __name__ == '__main__':
    unittest.main()
