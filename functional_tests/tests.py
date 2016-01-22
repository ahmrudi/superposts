from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class TestSuperPosts(LiveServerTestCase):
    
    def setUp(self):
        '''setup tests'''
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)
    
    def tearDown(self):
        '''teardown tests'''
        self.browser.quit()
    
    def get(self, url='/'):
        '''liat website'''
        self.browser.get(self.live_server_url + url)

    def check_for_now_in_list_table(self, row_text):
        posts = self.browser.find_element_by_id('id_list_posts')
        rows = posts.find_elements_by_tag_name('div')
        self.assertIn(row_text, [row.text for row in rows])
    
    def test_website(self):

        '''
        Rudi membuat website keren superposts dengan django versi 1.9 dan python 3.4.
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
            'Apa yang kamu rasakan?'
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
        asih_post_url = self.browser.current_url
        self.assertRegex(asih_post_url, '/posts/.+')
        self.check_for_now_in_list_table("Hai! Aku asih..")

        '''
        Asih posting lagi apa yang dia rasakan, sepertinya lagi galau dia.
        '''
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Bosen neh, gak ada yang ngajak jalan :)')
        inputbox.send_keys(Keys.ENTER)

        '''
        Halaman terupdate lagi, dan dia melihat semua apa yang telah diposting
        '''
        list_posts = self.browser.find_element_by_id('id_list_posts')
        rows = list_posts.find_elements_by_tag_name('div')
        self.check_for_now_in_list_table("Hai! Aku asih..")
        self.check_for_now_in_list_table("Bosen neh, gak ada yang ngajak jalan :)")
        
        '''
        kemudian asih keluar dari website karena disuruh pulang ke rumah karena
        mau masak ikan asin
        '''
        self.browser.quit()
        self.browser = webdriver.Firefox()

        '''
        Hari berikutnya
        '''

        '''
        Asih cerita sama petot tentang website superposts bikinan rudi
        lalu petot pun tertarik mengunjunginya
        '''

        '''
        Petot pergi website dan melihat judul "Super Posts"
        '''
        self.get()
        self.assertEqual("Super Posts", self.browser.title)

        '''
        Lalu petot posting apa yang dia rasakan kala itu
        '''
        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys("Asih lagi ngapain ya hari ini???")
        inputbox.send_keys(Keys.ENTER)

        '''
        Petot pun melihat kegalauan dia lewat tulisan yang dia bikin
        '''
        petot_post_url = self.browser.current_url
        self.assertRegex(petot_post_url, '/posts/.+')
        self.check_for_now_in_list_table("Asih lagi ngapain ya hari ini???")

        '''
        Petot mencari postingan asih yang telah lalu karena dia penasaran
        '''
        self.assertNotEqual(petot_post_url, asih_post_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Hai! Aku asih..', page_text)
        self.assertIn('Asih lagi ngapain ya hari ini???', page_text)


        
if __name__ == "__main__":
    unittest.main()