from glob import glob
import cv2

class ImageColorHistory:
    def __init__(self):
        self.image_path = "./"
        self.image_files = []
        self.image_data = []

    def load_image_data(self, path):
        self.image_path = path

        self.image_files = sorted(glob(self.image_path))

        for image_file in self.image_files:
            image_data = cv2.imread(image_file).tolist()
            self.image_data.append(image_data)

    def get_image_history(self, x, y):
        return list(map(lambda d: d[x][y], self.image_data))

if __name__ == '__main__':
    print(ImageColorHistory().image_path)