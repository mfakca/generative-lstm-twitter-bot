# Kütüphanelerin import edilmesi.
from selenium import webdriver
import time
import urllib.request
import os
from selenium.webdriver.common.keys import Keys
import generate
import time



# 100 defa yapar. Temsili bir sayı.
for i in range(100):
	
	# Chrome driver (Ben chromium kullandım.)
	driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
	
	
	# Giriş yapılan site.
	driver.get('https://twitter.com/login');


	time.sleep(1) # Let the user actually see something!

	# Nereye yazacağına erişiyor.
	user_id = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input")

	# Kullanıcı adını gönderiyor.
	user_id.send_keys('xxx')


	# Şifre textbox'u
	user_pwd = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input")

	# Şifreyi gönderiyor.
	user_pwd.send_keys('xxx')

	user_pwd.submit()
	# Bekleme süresi
	time.sleep(5) # Let the user actually see something!


	# Click message
	time.sleep(2)


	# Soldaki mesaj ikonuna tıklar
	tweet = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[4]/div").click()
	time.sleep(2)


	# En üstteki mesaja tıklar
	driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div[2]/section/div/div/div[1]/div/div").click()


	time.sleep(2)

	# Textbox					
	text_box = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div/aside/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div/div")
	time.sleep(2)

	for i in range(100):
									
		try:								
			son_yazilan = driver.find_element_by_xpath(f"/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div/div/div/div/div/div/div[{i}]/div/div[1]/div/div[2]/div/div/span")
		except:
			continue

		
		
	# Son yazılan mesaj üzerinden bir metin yazar.
	text_box.send_keys(generate.predict(son_yazilan.text))

	
	# Mesajı gönderir.
	text_box.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div/aside/div[2]/div[3]").click()
	
	# 15 dakika bekler.
	time.sleep(15*60)


