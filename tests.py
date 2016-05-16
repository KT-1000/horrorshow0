from server import app

import unittest


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        """ See if index route returns html and responds with OK status. """
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
