import unittest
from main import calculate


class KnapSackCase(unittest.TestCase):
    """Tests for the 'calculate' function"""

    def test_none_type(self):
        """ memes or usb_size is None -> TypeError """
        self.assertRaises(TypeError, calculate, None, [])
        self.assertRaises(TypeError, calculate, 3, None)
        self.assertRaises(TypeError, calculate, None, None)

    def test_empty_list(self):
        """ memes or usb_size is 0 -> 0 """
        self.assertEqual(0, calculate(123, []))
        self.assertEqual(0, calculate(0, [1, 2, 3]))
        self.assertEqual(0, calculate(0, 0))

    def test_string_usb_size(self):
        """ usb_size can’t be coverted to int -> TypeError """
        usb_size = "1"
        memes = [
            ("rollsafe.jpg", 205, 6),
            ("sad_pepe_compilation.gif", 410, 10),
            ("yodeling_kid.avi", 605, 12),
        ]
        expected = (22, {"sad_pepe_compilation.gif", "yodeling_kid.avi"})
        self.assertEqual(expected, calculate(usb_size, memes))

    def test_wrong_usb_size(self):
        """ usb_size can’t be coverted to int -> TypeError """
        usb_size = "dummy"
        memes = [
            ("rollsafe.jpg", 205, 6),
            ("sad_pepe_compilation.gif", 410, 10),
            ("yodeling_kid.avi", 605, 12),
        ]
        self.assertRaises(ValueError, calculate, usb_size, memes)

    def test_not_tuple(self):
        """ memes is not a list of tuples -> TypeError """
        usb_size = 1
        memes = [
            ("rollsafe.jpg", 205, 6),
            ["sad_pepe_compilation.gif", 410, 10],
            {"yodeling_kid.avi", 605, 12},
        ]
        self.assertRaises(TypeError, calculate, usb_size, memes)

    def test_wrong_number_of_args(self):
        """ a tuple inside memes doesn’t have 3 args -> ValueError """
        usb_size = 1
        memes = [
            ("rollsafe.jpg", 205),
            ("sad_pepe_compilation.gif", 410, 10, 623),
            ("yodeling_kid.avi"),
        ]
        self.assertRaises(ValueError, calculate, usb_size, memes)

    def test_wrong_label_type(self):
        """ meme name is not string -> TypeError """
        usb_size = 1
        memes = [
            (5235, 205, 6),
            (("sad_pepe_compilation.gif", 292), 410, 10),
            ("yodeling_kid.avi", 605, 12),
        ]
        self.assertRaises(TypeError, calculate, usb_size, memes)

    def test_wrong_size_type(self):
        """ meme size or value is not int -> TypeError """
        usb_size = 1
        memes = [
            ("rollsafe.jpg", 205.62, 6),
            ["sad_pepe_compilation.gif", 410, 10],
            {"yodeling_kid.avi", "abc", 12},
        ]
        self.assertRaises(TypeError, calculate, usb_size, memes)

    def test_wrong_value_type(self):
        """ meme size or value is not int -> TypeError """
        usb_size = 1
        memes = [
            ("rollsafe.jpg", 205, 6.6),
            ("sad_pepe_compilation.gif", 410, "10"),
            ("yodeling_kid.avi", 605, 12),
        ]
        self.assertRaises(TypeError, calculate, usb_size, memes)

    def test_case_1(self):
        """ general case test using given example data by Clearcode """
        usb_size = 1
        memes = [
            ("rollsafe.jpg", 205, 6),
            ("sad_pepe_compilation.gif", 410, 10),
            ("yodeling_kid.avi", 605, 12),
        ]
        expected = (22, {"sad_pepe_compilation.gif", "yodeling_kid.avi"})
        self.assertEqual(expected, calculate(usb_size, memes))

    def test_case_2(self):
        """ another general case test, just to make sure """
        items = [
            ("a", 2 * 1024, 2),
            ("b", 2 * 1024, 4),
            ("c", 4 * 1024, 6),
            ("d", 5 * 1024, 9),
        ]
        max_weight = 8
        expected = (13, {"b", "d"})
        self.assertEqual(expected, calculate(max_weight, items))


if __name__ == "__main__":
    unittest.main()
