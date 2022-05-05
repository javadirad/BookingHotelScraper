import unittest

import data
import htmlParser

class TestAddition(unittest.TestCase):
    def setUp(self):
        self.hotelInfo = data.HotelInfo()
    
    def tearDown(self):
        pass
    # def test_pars_html_Correct(self):
    #     html = ""
    #     htmlParser.HtmlParser(html,self.hotelInfo)
    #     self.assertIsNotNone(self.hotelInfo)
    def test_pars_html_None(self):
        html = None
        self.failUnlessRaises(ValueError, htmlParser.HtmlParser, html,self.hotelInfo)  
    def test_pars_html_Empty(self):
        html = ""
        self.failUnlessRaises(ValueError, htmlParser.HtmlParser, html,self.hotelInfo)  
if __name__ == '__main__':
    unittest.main()