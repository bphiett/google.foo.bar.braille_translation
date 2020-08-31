import unittest

def solution(s):

    capitalize = '000001'
    
    translate = {'t': '011110', 'h': '110010', 'e': '100010', ' ': '000000', 'q': '111110', 'u': '101001', 'i': '010100', 'c': '100100', 'k': '101000', 'b': '110000', 'r': '111010', 'o': '101010', 'w': '010111', 'n': '101110', 'f': '110100', 'x': '101101', 'j': '010110', 'm': '101100', 'p': '111100', 's': '011100', 'v': '111001', 't': '011110', 'l': '111000', 'a': '100000', 'z': '101011', 'y': '101111', 'd': '100110', 'g': '110110'}

    
    translation = ''
    
    for i in range(len(s)):
        if s[i].isupper():
            translation = translation + capitalize + translate[s[i].lower()]
        else:
            translation = translation + translate[s[i]]

    return translation


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution('code'), '100100101010100110100010')
        self.assertEqual(solution('Braille'), '000001110000111010100000010100111000111000100010')
        self.assertEqual(solution('The quick brown fox jumps over the lazy dog'), '000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110')

if __name__ == '__main__':
    unittest.main()
