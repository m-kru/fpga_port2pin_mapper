import unittest
import subprocess


class Test(unittest.TestCase):
    def test(self):
        expected = "ERROR: Terminal endpoint 'endpoint_1', connected to pin 'A1' is not mapped to any port!\n"

        path = "./tests/unconnected_terminal/"
        map_chain = f"{path}l_1,[{path}l_2_1,[{path}l_2_2]"

        actual = ''
        try:
            actual = subprocess.check_output(['python',
                                              'fpga_port2pin_mapper.py',
                                              f"{path}connection.yaml",
                                              map_chain,
                                              'tmp.xdc'])
            raise Exception("This subprocess must fail!")
        except Exception as e:
            actual = e.output

        actual = str(actual.decode('utf-8'))
        self.assertEqual(expected, actual)