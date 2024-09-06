import time
import json
from telnetlib import EC
from compare_struk_transaksi import *

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from setup_descap import driver

def transaksi_normal(nama_barang, ubah_harga_sementara, ubah_diskon_perbarang, diskon_pertransaksi, pajak_pertransaksi, catatan_pertransaksi):
    global status
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
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/act_search_product").send_keys(nama_barang)
        except:
            status = "terjadi masalah ketika membuka klik pencarian di halaman transaksi"
            print("--------------------------------------------")
            print(status)
            return

        try:
            # pilih barang "sesuai dengan excel"
            actions = TouchAction(driver)
            actions.long_press(driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout")).release().perform()
        except:
            status = "terjadi masalah ketika memilih barang di transaksi penjualan dengan cara longpress"
            print("--------------------------------------------")
            print(status)
            return

        try:
            # klik checkbox ubah harga sementara
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/checkBox2").click()
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_harga").click()
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_harga").clear()
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_harga").send_keys(ubah_harga_sementara)
        except Exception as x:
            status = "terjadi masalah ketika merubah harga sementara pada pop up" + str(x)
            print("--------------------------------------------")
            print(status)
            return

        try:
            # ubah diskon perbarang
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/checkBox3").click()
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_diskon").click()
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_diskon").clear()
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_diskon").send_keys(ubah_diskon_perbarang)
        except Exception as x:
            status = "Terjadi masalah ketika merubah diskon perbarang pada pop up: " + str(x)
            print("--------------------------------------------")
            print(status)
            return

        # Tutup pop up barang
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lanjut").click()

        # Lanjut ke halaman keranjang
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/tv_count_cart").click()

        # # Menambahkan Biaya Ongkir
        # driver.find_element(By.ID, "org.owline.kasirpintarpro:id/linear_add_biaya").click()
        # driver.implicitly_wait(100)
        # driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_modul_ongkir").click()
        # driver.implicitly_wait(100)
        # driver.find_element(By.XPATH, ("//android.widget.TextView[@text='Pilih Provinsi']")).click()
        # driver.implicitly_wait(100)
        # driver.find_element(By.XPATH, ("//android.widget.TextView[@text='Bali']")).click()
        # driver.implicitly_wait(100)
        # driver.find_element(By.ID, "org.owline.kasirpintarpro:id/spinner_pengiriman").click()
        # driver.implicitly_wait(100)
        # driver.find_element(By.XPATH, ("//android.widget.TextView[@text='JNE']")).click()
        # time.sleep(3)
        # driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_ok").click()

        try:
            # Lanjut ke halaman Pembayaran dengan klik Bayar
            driver.implicitly_wait(10)
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/linear_bayar").click()

            # Input Diskon di halaman Pembayaran
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/linearDiskon").click()
            driver.implicitly_wait(10)
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edit_diskon").click()
            driver.back()
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edit_diskon").clear()
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edit_diskon").send_keys(diskon_pertransaksi)
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/tombol_diskon").click()

            # Input Pajak di halaman Pembayaran
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/linearPajak").click()
            driver.implicitly_wait(10)
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/rb_tax_manual").click()
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/et_tax").clear()
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/et_tax").send_keys(pajak_pertransaksi)
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/tombol_pajak").click()

            # input pembayaran dengan papan uang -> dengan uang pas
            driver.find_element(By. ID, "org.owline.kasirpintarpro:id/iv_btn_quick").click()
            driver.find_element(By.XPATH, ("//android.widget.TextView[@text='Uang Pas']")).click()

            # input Catatan Pertransaksi
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/linearKeterangan").click()
            driver.implicitly_wait(10)
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/isi").click()
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/isi").send_keys(catatan_pertransaksi)
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ya").click()

            # klik centang untuk menyelesaikan pembayaran
            driver.implicitly_wait(10)
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/linearProses").click()
        except Exception as x:
            status = "terjadi masalah ketika melakukan pembayaran" + str(x)
            print("--------------------------------------------")
            print(status)
            return

        # kondisi ketika muncul pop up pilih printer ketika kondisi tidak konek dengan printer
        try:
            driver.implicitly_wait(2)
            driver.find_element(By. ID, "org.owline.kasirpintarpro:id/ya").is_displayed()
            driver.back()
        except :
            pass


        # klik print struk
        # driver.find_element(By. ID, "org.owline.kasirpintarpro:id/linearCetak").click()

        # time.sleep(3)
        # klik cetak pesanan
        # driver.find_element(By. ID, "org.owline.kasirpintarpro:id/linearCetakPesanan").click()

        time.sleep(2)

        # klik lihat struk
        try:
            driver.implicitly_wait(10)
            driver.find_element(By.XPATH, ("//android.widget.TextView[@text='More']")).click()
        except:
            driver.find_element(By.XPATH, ("//android.widget.TextView[@text='Lainnya']")).click()

        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/linearDetailStruk").click()

        # Menunggu menampilkan struk
        driver.implicitly_wait(10)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/nama_toko").is_displayed()

        time.sleep(1)
        driver.back()
        time.sleep(1)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btnSelesai").click()
        status = "sukses"

    except Exception as e:
        status = f"Terjadi kesalahan: {str(e)}"
        print("--------------------------------------------")
        print(status)

    # keterangan_struk = ', '.join(keterangan_struk)
    # print(";".join(keterangan_struk))
    return status

