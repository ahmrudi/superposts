import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import django

HOST = 'http://127.0.0.1:8000'

class TestSuperPosts(unittest.TestCase):
    
    def setUp(self):
        '''setup tests'''
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)
    
    def tearDown(self):
        '''teardown tests'''
        self.browser.quit()
    
    def get(self, url='/'):
        '''liat website'''
        self.browser.get(HOST + url)
    
    def test_website(self):
        '''
        Rudi membuat website keren superposts dengan django versi 1.9 dan python 3.4
        Asih ternyata denger nih, lalu dia lihat web bikinan rudi
        
        Setelah itu dia pergi ke warnet karena gak punya netbook
        lalu liat web superposts bikinan rudi
        
        Asih waktu buka halaman utamanya,
        dia liat judul webnya "Super Posts"
        '''
        self.get()
        self.assertIn("Super Posts", self.browser.title)

        '''
        Dia juga melihat ada heading di atas web tersebut bertuliskan "Super Posts"
        '''
        heading_superposts = self.browser.find_element_by_tag_name("h1").text
        self.assertIn(
            'Super Posts',
            heading_superposts
            )
        '''
        Asih kemudian mengepost untuk pertama kalinya
        '''
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Apa yang anda rasakan?'
            )
        '''
        Dia mengetikkan "Hai! Aku asih.."
        '''
        inputbox.send_keys("Hai! Aku asih..")
        '''
        Ketika dia enter, halaman terupdate dan terdapat tulisan
        "Hai! Aku asih.." dalam list posts
        '''
        inputbox.send_keys(Keys.ENTER)
        list_posts = self.browser.find_element_by_id("id_list_posts")
        

        
if __name__ == "__main__":
    unittest.main()