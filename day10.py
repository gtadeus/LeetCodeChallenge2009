import unittest
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        nr_of_bulls = 0
        nr_of_cows = 0

        i = 0
        while i < len(secret):
            val = secret[i]
            if val == guess[i]:
                nr_of_bulls += 1
                secret = secret[:i] + secret[(i+1):]
                guess = guess[:i] + guess[(i+1):]
                i-=1
            i += 1

        for i, val in enumerate(guess):
            nr_of_hits = 0
            position = secret.find(val)
            if position != -1:
                secret = secret[:position] + secret[(position+1):]
                nr_of_cows += 1

        return str(nr_of_bulls)+"A"+str(nr_of_cows)+"B"


class TestDay10(unittest.TestCase):

    S = Solution()
    test_inp = [
        {"secret" : "1807", "guess" : "7810"},
        {"secret" : "1123", "guess" : "0111"},
        {"secret" : "11", "guess" : "10"},
        {"secret" : "11", "guess" : "01"},
        {"secret" : "11", "guess" : "11"},
        {"secret" : "1122", "guess" : "2211"},
    ]
    test_result = [
        "1A3B",
        "1A1B",
        "1A0B",
        "1A0B",
        "2A0B",
        "0A4B",
    ]

    def test_solution(self):
        for i, val in enumerate(self.test_inp):
            
            try:
                self.assertEqual(self.test_result[i], self.S.getHint(val["secret"], val["guess"]))
            except:
                print("test case nr. ", i+1, " failed")
                raise AssertionError
if __name__ == "__main__":
    unittest.main()

