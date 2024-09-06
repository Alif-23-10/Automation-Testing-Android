import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from setup_descap import *

def seting_printer_bluetooth():
    try:
        # 3baris untuk membuka sidebar
        driver.implicitly_wait(20)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/bars").click()

        # Klik pengaturan di sidebar
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lin_pengaturan").click()

        # KLik Printer dan Struk di menu Pengaturan
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.LinearLayout").click()

        # Klik Pengaturan printer
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout").click()

        #Klik button tambah di Struk Transaksi
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.LinearLayout/android.widget.LinearLayout[2]").click()

        #Apabila muncul permission Lokasi (persyaratan untuk mengakses bluetooth)
        try:
            driver.implicitly_wait(3)
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_ok").click()
            driver.find_element(By.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
        except:
            pass

        driver.implicitly_wait(20)
        # Pilih printer dengan nama "Bluetooth Printer"
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.RadioButton").click()
        # Klik button set
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_set").click()


        #klik button simpan
        driver.implicitly_wait(4)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_save").click()

        # back ke halaman utama pengaturan
        driver.implicitly_wait(3)
        driver.back()
        time.sleep(2)
        driver.back()



        # driver.implicitly_wait(1)
        # driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_set").click()
        #
        # driver.implicitly_wait(5)
        # # Mendefinisikan kordinat yang akan di scroll
        # start_x = int(driver.get_window_size()['width'] * 0.5)  # mendapatkan kordinat tengah dari hp
        # start_y = int(driver.get_window_size()['height'] * 0.8)  # mendapatkan kordinat tinggi hp dari atas sampe dengan bawah sebanyak 80%
        # end_y = int(driver.get_window_size()['height'] * 0.2)  # mendapatkan kordinat tinggi hp dari atas sampe bawah sebanyak 20%
        #
        # # Fungsi untuk melakukan scroll
        # action = TouchAction(driver)
        # action.press(x=start_x, y=start_y).wait(2000).move_to(x=start_x, y=end_y).release().perform()
        # action.press(x=start_x, y=start_y).wait(2000).move_to(x=start_x, y=end_y).release().perform()
        #
        #
        # driver.implicitly_wait(10)
        # driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edit_printer_bluetooth").click()
        #
        # driver.implicitly_wait(10)
        # driver.find_element(By.XPATH, "//android.widget.TextView[@text='BlueTooth Printer']").click()
        # # driver.find_element(By.XPATH, "//android.widget.TextView[@text='RPP02N']").click()
        #
        # driver.implicitly_wait(10)
        # driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_preview").click()
        #
        # driver.implicitly_wait(10)
        # driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_test_cetak").click()
        # time.sleep(3)
        #
        # driver.implicitly_wait(10)
        # driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_simpan_preview").click()
        status = "sukses"
    except Exception as x:
        status = "Seting printer gagal" + str(x)
    return status

