import unittest
import subprocess


class Test(unittest.TestCase):
    def test(self):
        expected = "ERROR: Port 'port_2' connected to missing end 'endpoint_2'!\n"

        path = "./tests/missing_endpoint/"
        map_chain = f"{path}l_1,[{path}l_2_1,{path}l_2_2]"

        actual = ''
        try:
            actual = subprocess.check_output(['python',
                                              'fpga_port2pin_mapper.py',
                                              'map',
                                              f"{path}connection.yaml",
                                              map_chain,
                                              'tmp.xdc'])
            raise Exception("This subprocess must fail!")
        except Exception as e:
            actual = e.output

        actual = str(actual.decode('utf-8'))
        self.assertEqual(expected, actual)
