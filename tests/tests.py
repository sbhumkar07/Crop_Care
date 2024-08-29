import unittest
from new_core_app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        # Set up a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        result = self.app.get('/home')
        self.assertEqual(result.status_code, 200)

    def test_checkup_status_code(self):
        result = self.app.get('/checkup')
        self.assertEqual(result.status_code, 200)

    def test_post_request_no_image(self):
        result = self.app.post('/', data={})
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Feeding blank image won\'t work. Please enter an input image to continue.', result.data)


    def test_post_request_with_image(self):
        with open(r'G:\Clg - Final Year Project\Clg3_Final_Year Web app\test_images\Corn\healthy-1.jpg', 'rb') as img:
            data = {
                'type': 'corn',
                'img': (img, 'healthy-1.jpg')
            }
            result = self.app.post('/', data=data, content_type='multipart/form-data')
            self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()
