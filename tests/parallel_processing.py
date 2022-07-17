from unittest import TestCase, main
import os
from pathlib import Path
import sys
from datastructure.parallel_processing import main as mainAlgo


class Test(TestCase):
    def test_from_file(self):
        for i in [2, 8]:
            p_str = f"{i}".rjust(2,'0')
            p = Path(os.getcwd())/Path('tests')/Path('parallel_processing_testcases')/p_str
            sys.stdin = open(p, "r")
            responses = [i for i in mainAlgo()]
            p_str +='.a'
            ansF= Path(os.getcwd())/Path('tests')/Path('parallel_processing_testcases')/p_str
            with open(ansF, 'r') as ans_file:
                ans = [(int(i.strip().split()[0]),int(i.strip().split()[1])) for i in ans_file.readlines()]
                # print(list(zip(responses,ans)))
                self.assertEqual(responses,ans)

    pass

if __name__ == '__main__':
    main()
