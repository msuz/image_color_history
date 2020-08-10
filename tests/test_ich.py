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

        data_0 = [
            [[118, 123, 118], [124, 118, 255]],
            [[255, 146, 126], [118, 255, 118]]
        ]
        self.assertEqual(self.ich.image_data[0].tolist(), data_0)

        data_1 = [
            [[255, 255, 255], [112, 255, 255]],
            [[255, 255, 112], [255, 148, 255]]
        ]
        self.assertEqual(self.ich.image_data[1].tolist(), data_1)


    def test_get_pixcel_bgr_list(self):
        self.ich.load_image_data("./tests/test_image/*.png")
        a = self.ich.get_pixcel_bgr_list(0, 1)
        self.assertEqual(a[0].tolist(), [124, 118, 255])
        self.assertEqual(a[1].tolist(), [112, 255, 255])
        a_t  = a.T
        self.assertEqual(a_t[0].tolist(), [124, 112])
        self.assertEqual(a_t[1].tolist(), [118, 255])
        self.assertEqual(a_t[2].tolist(), [255, 255])

        a = self.ich.get_pixcel_bgr_list(1, 1)
        self.assertEqual(a[0].tolist(), [118, 255, 118])
        self.assertEqual(a[1].tolist(), [255, 148, 255])

if __name__ == '__main__':
    unittest.main()