import unittest

from main import configApplication, readHtmlFile

class TestAddition(unittest.TestCase):
    def setUp(self):
        self.logger = configApplication()
    
    def tearDown(self):
        pass
    def test_read_html_Correct(self):
        htmlFilePath = "Input/Kempinski Hotel Bristol Berlin, Germany - Booking.com.html"
        html = readHtmlFile(htmlFilePath,self.logger)
        self.assertIsNotNone(html)
    def test_read_html_InCorrect(self):
        htmlFilePath = "badfile.html"
        html = readHtmlFile(htmlFilePath,self.logger)
        self.assertFalse(html)
    def test_read_html_Empty(self):
        htmlFilePath = ""
        html = readHtmlFile(htmlFilePath,self.logger)
        self.assertFalse(html)        
if __name__ == '__main__':
    unittest.main()