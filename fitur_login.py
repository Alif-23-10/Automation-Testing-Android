import time
# import mysql.connector
from telnetlib import EC

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from setup_descap import *

# untuk menunggu element menggunakan wait until
wait = WebDriverWait(driver, 10)

def login_function(email, password):
    try:
        # klik button Login
        time.sleep(2)
        button_login = wait.until(EC.visibility_of_element_located((By.ID, "org.owline.kasirpintarpro:id/tv_login")))
        button_login.click()
        # input data
        time.sleep(2)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edt_email").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edt_email").send_keys(email)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edt_password").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edt_password").send_keys(password)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_login").click()
    except:
        status = "login gagal"
        return status

    try:
        time.sleep(2)
        email_tidak_terdaftar = driver.find_elements(By. ID, "org.owline.kasirpintarpro:id/btn_OK")
        popup_getdevice = driver.find_elements(By.ID, "org.owline.kasirpintarpro:id/btn_ok")
        popup_terpakai_device_lain = driver.find_elements(By.ID, "org.owline.kasirpintarpro:id/ya")

        time.sleep(1)
        # jika muncul pop up email tidak terdaftar
        if len(email_tidak_terdaftar) > 0:
            # Lakukan langkah ketika email tidak terdaftar
            klik_OK = wait.until(EC.visibility_of_element_located((By.ID, "org.owline.kasirpintarpro:id/btn_OK")))
            klik_OK.click()
            driver.back()
            status = "sukses"
            return status
        # jika muncul pop up get device atau pop up terpakai device lain
        elif len(popup_getdevice) > 0 or len(popup_terpakai_device_lain) > 0:
            # Lakukan langkah ketika login berhasil

            # pop up get devices
            try:
                driver.implicitly_wait(10)
                klik_ya = wait.until(EC.visibility_of_element_located((By.ID, "org.owline.kasirpintarpro:id/ya")))
                klik_ya.click()
            except:
                pass

            # pop up Notifikasi permission get tipe device
            try:
                driver.implicitly_wait(10)
                klik_ok = wait.until(EC.visibility_of_element_located((By.ID, "org.owline.kasirpintarpro:id/btn_ok")))
                klik_ok.click()
            except:
                pass

            # Pop Up Permisson Android 12 keatas
            try:
                driver.implicitly_wait(3)
                driver.find_element(By.ID, "com.android.permissioncontroller:id/permission_allow_button").click()
            except:
                pass

            # Pilih Bulan
            try:
                driver.implicitly_wait(10)
                driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]").click()
            except:
                pass

            # Pop Up Permisson Android 12 keatas
            try:
                driver.implicitly_wait(10)
                driver.find_element(By.ID, "com.android.permissioncontroller:id/permission_allow_button").click()
            except:
                pass

            # apabila terdapat pop up update
            try:
                driver.implicitly_wait(2)
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ya").click()
            except:
                pass

            # Permission android 12 keatas
            try:
                driver.implicitly_wait(10)
                driver.find_element(By.ID, "com.android.permissioncontroller:id/permission_allow_button").click()
            except:
                pass

            try:
                # menunggu halaman manajemen nampil
                # bars = wait.until(EC.visibility_of_element_located((By.ID, "org.owline.kasirpintarpro:id/bars")))
                time.sleep(2)
                manajemen = driver.find_elements(By.ID, "org.owline.kasirpintarpro:id/bars")
                if len(manajemen)>0:
                    # SCROL UNTUK BUKA HALAMAN NOTIFIKASI
                    # time.sleep(2)
                    # Mendefinisikan kordinat yang akan di scroll
                    kordinat_tengah = int(
                        driver.get_window_size()['width'] * 0.5)  # mendapatkan kordinat tengah dari hp
                    kordinat_atas = int(
                        driver.get_window_size()['height'] * 0.01)  # mendapatkan kordinat atas sebanyak 1%
                    kordinat_bawah = int(
                        driver.get_window_size()['height'] * 0.95)  # mendapatkan kordinat bawah sebanyak 95%
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

            except:
                status = "Tidak bisa scroll untuk clear notifikasi"
                return status

            status = "sukses"
            return status
        else:
            status = "case login gagal"
            return status
    except Exception as e:
        status = "Error: " + str(e)
        return status







