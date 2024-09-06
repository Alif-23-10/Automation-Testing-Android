import time
from telnetlib import EC

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from setup_descap import *

def tambah_pesanan():
    try:
        # 3baris untuk membuka sidebar
        time.sleep(3)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/bars").click()

        try:
            # Menu transaksi Penjualan di sidebar
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lin_transaksi").click()
        except:
            status = "terjadi masalah ketika membuka menu transaksi penjualan"
            print("--------------------------------------------")
            print(status)
            return

        try:
            # klik pencarian
            driver.implicitly_wait(10)
            driver.find_element(By.ID,"org.owline.kasirpintarpro:id/btn_search").click()
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/act_search_product").send_keys("add onn")
        except:
            status = "terjadi masalah ketika membuka klik pencarian di halaman transaksi"
            print("--------------------------------------------")
            print(status)
            return
        
        for i in range(10):
            try:
                driver.implicitly_wait(5)
                driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout").click()
            except:
                status = "terjadi masalah ketika memilih barang di halaman transaksi"
                print("--------------------------------------------")
                print(status)
                return

            try:
                driver.implicitly_wait(10)
                # Lanjut ke halaman keranjang
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/tv_count_cart").click()
            except:
                status = "terjadi masalah ketika ingin melanjutkan ke keranjang"
                print("--------------------------------------------")
                print(status)
                return

            try:
                driver.implicitly_wait(10)
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/linear_pesanan").click()
            except:
                status = "terjadi masalah ketika klik button pesan di keranjang"
                print("--------------------------------------------")
                print(status)
                return

            try:
                driver.implicitly_wait(10)
                looping_nama_pesanan = i + 1
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/isi").send_keys("pesanan " + str(looping_nama_pesanan))
            except:
                status = "terjadi masalah ketika input nomor pesanan"
                print("--------------------------------------------")
                print(status)
                return

            try:
                driver.implicitly_wait(10)
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ll_save").click()
            except:
                status = "terjadi masalah ketika simpan pesanan"
                print("--------------------------------------------")
                print(status)
                return

            try:
                button_checkout = driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ll_checkout")
                if button_checkout:
                    driver.back()
                status = "sukses"
                return status
            except:
                status = "terjadi masalah ketika back ke halaman transaksi penjualan"
                print("--------------------------------------------")
                print(status)
                return
    except Exception as e:
        status = f"Terjadi kesalahan: {str(e)}"
        print("--------------------------------------------")
        print(status)
    return

