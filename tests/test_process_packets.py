from unittest import TestCase, main
import os
from pathlib import Path
import sys
from datastructure.process_network_packets import main as mainAlgo




class Test(TestCase):
    def test_from_file(self):
        for i in range(1,23):
            p_str = f"{i}".rjust(2,'0')
            p = Path(os.getcwd())/Path('tests')/Path('network_packet_testcases')/p_str
            sys.stdin = open(p, "r")
            responses = [i for i in mainAlgo()]
            p_str +='.a'
            ansF= Path(os.getcwd())/Path('tests')/Path('network_packet_testcases')/p_str
            with open(ansF, 'r') as ans_file:
                ans = [int(i.strip()) for i in ans_file.readlines()]
                self.assertEqual(responses,ans)

    pass

if __name__ == '__main__':
    main()
