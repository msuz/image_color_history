import unittest
from classes.ich import ImageColorHistory

class ImageColorHistoryTestCase(unittest.TestCase):
    def setUp(self):
        self.ich = ImageColorHistory()

    def test_default_values(self):
        self.assertEqual(self.ich.image_path, "./")
        self.assertEqual(self.ich.image_files, [])
        self.assertEqual(self.ich.image_data, [])

    def test_load_image_data(self):
        path = "./tests/test_image/*.png"

        self.ich.load_image_data(path)
        self.assertEqual(self.ich.image_path, path)

        files = [
            "./tests/test_image/1.png",
            "./tests/test_image/2.png"
        ]
        self.assertEqual(self.ich.image_files, files)

        data = [
            [
                [[118, 123, 118], [124, 118, 255]],
                [[255, 146, 126], [118, 255, 118]]
            ],
            [
                [[255, 255, 255], [112, 255, 255]],
                [[255, 255, 112], [255, 148, 255]]
            ]
        ]
        self.assertEqual(self.ich.image_data, data)

    def test_get_image_history(self):
        self.ich.load_image_data("./tests/test_image/*.png")
        a = self.ich.get_image_history(0, 1)
        b = [[124, 118, 255], [112, 255, 255]]
        self.assertEqual(a, b)
        a = self.ich.get_image_history(1, 1)
        b = [[118, 255, 118], [255, 148, 255]]
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()