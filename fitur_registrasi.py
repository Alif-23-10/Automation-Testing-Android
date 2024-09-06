import time
import re
from telnetlib import EC

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from setup_descap import *

def registrasi():
    try:
        print("lololoo")
        time.sleep(2)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_register").click()
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "com.google.android.gms:id/main_title").is_displayed()
        driver.back()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edt_username").send_keys("baru dari alif")
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edt_email").send_keys("aliftesting01@yopmail.com")
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edt_password").send_keys("alif2310")
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edt_phone").send_keys("82229062087")

        # Mendefinisikan kordinat yang akan di scroll
        kordinat_tengah = int(driver.get_window_size()['width'] * 0.5)  # mendapatkan kordinat tengah dari hp
        kordinat_atas = int(driver.get_window_size()['height'] * 0.01)  # mendapatkan kordinat atas sebanyak 1%
        kordinat_bawah = int(driver.get_window_size()['height'] * 0.95)  # mendapatkan kordinat bawah sebanyak 95%
        # Fungsi untuk melakukan scroll
        action = TouchAction(driver)
        action.press(x=kordinat_tengah, y=kordinat_atas).wait(2000).move_to(x=kordinat_tengah, y=kordinat_bawah).release().perform()
        driver.implicitly_wait(2)

        try:
            # klik CLEAR NOTIFIKASI EMULATOR
            # driver.find_element(By. ID, "com.android.systemui:id/dismiss_text").click()

            # Klik CLEAR NOTIFIKASI Real Device
            driver.find_element(By.ID, "com.android.systemui:id/clear_all_port").click()
        except:
            driver.back()

        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_register").click()

        try:
            driver.find_element(By. ID, "org.owline.kasirpintarpro:id/linear_wa").click()
        except:
            pass

        time.sleep(5)

        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/tv_menu").is_displayed()

        # Mendefinisikan kordinat yang akan di scroll
        kordinat_tengah = int(driver.get_window_size()['width'] * 0.5)  # mendapatkan kordinat tengah dari hp
        kordinat_atas = int( driver.get_window_size()['height'] * 0.01)  # mendapatkan kordinat atas sebanyak 1%
        kordinat_bawah = int(driver.get_window_size()['height'] * 0.95)  # mendapatkan kordinat bawah sebanyak 95%
        # Fungsi untuk melakukan scroll
        action = TouchAction(driver)
        action.press(x=kordinat_tengah, y=kordinat_atas).wait(2000).move_to(x=kordinat_tengah, y=kordinat_bawah).release().perform()
        driver.implicitly_wait(2)



        get_text_otp = driver.find_element(By.ID, "android:id/message_text")
        # otp_text = "Assalamu'alaikum, kode verifikasi aplikasi Kasir Pintar: 584141. Ini hanya untuk verifikasi, pastikan kode ini tetap aman."
        otp_text = get_text_otp.text
        angka_otp = re.compile(r'\b\d+\b')
        hasil_otp = angka_otp.findall(otp_text)
        angka = hasil_otp[0] if hasil_otp else None
        print(hasil_otp)
    #     print(otp_text)
        otp_1 = angka[0]
        otp_2 = angka[1]
        otp_3 = angka[2]
        otp_4 = angka[3]
        otp_5 = angka[4]
        otp_6 = angka[5]
    #
        print(otp_1)
        print(otp_2)
        print(otp_3)
        print(otp_4)
        print(otp_5)
        print(otp_6)
    #
        driver.back()

        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edt_otp_1").send_keys(otp_1)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edt_otp_2").send_keys(otp_2)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edt_otp_3").send_keys(otp_3)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edt_otp_4").send_keys(otp_4)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edt_otp_5").send_keys(otp_5)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edt_otp_6").send_keys(otp_6)
        time.sleep(1)

        driver.find_element(By. ID, "org.owline.kasirpintarpro:id/btn_verif").click()

        status = "sukses"

    except:
        status = "gagal regis"

    return status

def isi_data_toko():
    try:
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.Spinner/android.widget.TextView").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[2]").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edt_nama_toko").send_keys("Toko Alif")
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.Spinner/android.widget.LinearLayout").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.Spinner/android.widget.LinearLayout").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView").click()
        time.sleep(2)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edt_alamat_lengkap").send_keys("Alamat Surabaya")
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_simpan").click()
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ya").click()
        status = "sukses"
    except:
        status = "isi data toko gagal"
    return status

def onboarding():
    try:
        driver.implicitly_wait(10)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_start_guide").click()
        driver.implicitly_wait(2)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_continue").click()

        driver.implicitly_wait(5)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/tvManajemenOK").click()
        driver.implicitly_wait(2)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/tvLaporanOK").click()
        driver.implicitly_wait(2)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/tvSettingOK").click()
        driver.implicitly_wait(2)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/tvOlshopOK").click()
        driver.implicitly_wait(2)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/tvManajemenOK").click()
        driver.implicitly_wait(2)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btnTambah").click()
        driver.implicitly_wait(2)

        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/tilNamaBarang").send_keys("Barang Contoh")
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edtStok").send_keys("10")
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edtKode").send_keys("BarangContoh")
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edtHargaBeli").send_keys("1000")
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edtHargaJual").send_keys("2000")
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btnTambahBarang").click()

        driver.implicitly_wait(5)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/tvTransaksiOK").click()
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView").click()
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lin_lanjut").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/linearBottom").click()

        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout[4]/android.widget.FrameLayout/android.widget.LinearLayout").click()
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout").click()
        driver.implicitly_wait(2)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/linearSend").click()
        time.sleep(4)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_finish").click()
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_cancel").click()

        status = "sukses"
    except:
        status = "gagal onboarding"
    return status

