import re
import time
from telnetlib import EC

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from setup_descap import *
def transaksi_campur(isBarisTerakhir, nama_barang, tipe_barang, jumlah_stok, ubah_harga_sementara, ubah_diskon_perbarang):
    # print(isBarisTerakhir)
    # print(tipe_barang)
    try:
        # 3baris untuk membuka sidebar
        driver.implicitly_wait(50)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/bars").click()
        # Menu transaksi Penjualan di sidebar
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lin_transaksi").click()

        # apabila belum baris terakhir
        if not isBarisTerakhir:
            if tipe_barang == "default" or "paket" :
                # klik pencarian
                driver.implicitly_wait(10)
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_search").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/act_search_product").send_keys(nama_barang)
                # pilih barang "sesuai dengan excel"
                actions = TouchAction(driver)
                actions.long_press(driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout")).release().perform()
                # input stok barang
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/jumlahBarang").send_keys(jumlah_stok)
                # klik checkbox ubah harga sementara
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/checkBox2").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_harga").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_harga").clear()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_harga").send_keys(ubah_harga_sementara)
                # ubah diskon perbarang
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/checkBox3").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_diskon").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_diskon").clear()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_diskon").send_keys(ubah_diskon_perbarang)
                # Tutup pop up barang
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lanjut").click()
                # clear pencarian
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_cancel_form_search").click()
            elif tipe_barang == "imei":
                # klik pencarian
                driver.implicitly_wait(10)
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_search").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/act_search_product").send_keys(nama_barang)
                driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout").click()
                # pilih imei
                time.sleep(2)
                print("ini eror")

                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "org.owline.kasirpintarpro:id/tvNama"))
                )

                driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.ScrollView/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]").click()
                # ubah harga
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lblUbahHarga").click()
                # ubah harga sementara
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/cbUbahHarga").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edtUbahHarga").clear()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edtUbahHarga").send_keys(ubah_harga_sementara)
                # ubah diskon perbarang
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/cbDiskon").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edtDiskon").clear()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edtDiskon").send_keys(ubah_diskon_perbarang)
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ya").click()
                # clear pencarian
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_cancel_form_search").click()
            elif tipe_barang == "addon":
                # klik pencarian
                driver.implicitly_wait(10)
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_search").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/act_search_product").send_keys(nama_barang)
                driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout").click()
                # longpress memiliih
                actions = TouchAction(driver)
                actions.long_press(driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout")).release().perform()
                # input stok barang
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/jumlahBarang").send_keys(jumlah_stok)
                # klik checkbox ubah harga sementara
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/checkBox2").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_harga").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_harga").clear()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_harga").send_keys(ubah_harga_sementara)
                # ubah diskon perbarang
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/checkBox3").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_diskon").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_diskon").clear()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_diskon").send_keys(ubah_diskon_perbarang)
                # menambahkan addon
                time.sleep(2)
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/add_on").click()
                time.sleep(2)
                driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[2]/android.view.ViewGroup[1]/android.widget.CheckBox").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_confirm").click()
                time.sleep(2)
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_save_add_on").click()
                time.sleep(2)
                # clear pencarian
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_cancel_form_search").click()
            elif tipe_barang == "varian":
                # klik pencarian
                driver.implicitly_wait(10)
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_search").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/act_search_product").send_keys(nama_barang)
                driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout").click()
                # klik barang
                driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout").click()
                # pilih varian
                driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]").click()
                # input stok
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edtJumlahBarang").send_keys(jumlah_stok)
                # klik checkbox ubah harga sementara
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/cekUbahHarga").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_harga").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_harga").clear()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_harga").send_keys(ubah_harga_sementara)
                # ubah diskon perbarang
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/checkBox3").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_diskon").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_diskon").clear()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/cekUbahDiskon").send_keys(ubah_diskon_perbarang)
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lanjut")
                time.sleep(2)
                # clear pencarian
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_cancel_form_search").click()


        else:
            if tipe_barang == "default":
                pass
            elif tipe_barang == "imei":
                pass
            elif tipe_barang == "paket":
                # klik pencarian
                driver.implicitly_wait(10)
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_search").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/act_search_product").send_keys(nama_barang)
                # pilih barang "sesuai dengan excel"
                actions = TouchAction(driver)
                actions.long_press(driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout")).release().perform()
                # input stok barang
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/jumlahBarang").send_keys(jumlah_stok)
                # klik checkbox ubah harga sementara
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/checkBox2").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_harga").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_harga").clear()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_harga").send_keys(ubah_harga_sementara)
                # ubah diskon perbarang
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/checkBox3").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_diskon").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_diskon").clear()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_diskon").send_keys(ubah_diskon_perbarang)
                # Tutup pop up barang
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lanjut").click()
                # clear pencarian
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_cancel_form_search").click()
                time.sleep(2)
                # Lanjut ke halaman keranjang
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/tv_count_cart").click()
                # Lanjut ke halaman Pembayaran dengan klik Bayar
                driver.implicitly_wait(10)
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/linear_bayar").click()
                # input pembayaran dengan papan uang -> dengan uang pas
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/iv_btn_quick").click()
                driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/linearProses").click()
                # kondisi ketika muncul pop up pilih printer ketika kondisi tidak konek dengan printer
                try:
                    driver.implicitly_wait(2)
                    driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ya").is_displayed()
                    driver.back()
                except:
                    pass
                time.sleep(2)
                # klik lihat struk
                try:
                    driver.implicitly_wait(10)
                    driver.find_element(By.XPATH, ("//android.widget.TextView[@text='More']")).click()
                except:
                    driver.find_element(By.XPATH, ("//android.widget.TextView[@text='Lainnya']")).click()
                # Menunggu menampilkan struk
                driver.implicitly_wait(10)
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/nama_toko").is_displayed()
                driver.back()
                time.sleep(2)
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btnSelesai").click()

            elif tipe_barang == "addon":
                pass
            elif tipe_barang == "varian":
                # klik pencarian
                driver.implicitly_wait(10)
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_search").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/act_search_product").send_keys(nama_barang)
                driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout").click()
                # klik barang
                driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout").click()
                # pilih varian
                driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]").click()
                # input stok
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edtJumlahBarang").send_keys(jumlah_stok)
                # klik checkbox ubah harga sementara
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/cekUbahHarga").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_harga").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_harga").clear()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_harga").send_keys(ubah_harga_sementara)
                # ubah diskon perbarang
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/checkBox3").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_diskon").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ubah_diskon").clear()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/cekUbahDiskon").send_keys(ubah_diskon_perbarang)
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lanjut")
                time.sleep(2)
                # clear pencarian
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_cancel_form_search").click()

                time.sleep(2)
                # Lanjut ke halaman keranjang
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/tv_count_cart").click()
                # Lanjut ke halaman Pembayaran dengan klik Bayar
                driver.implicitly_wait(10)
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/linear_bayar").click()
                # input pembayaran dengan papan uang -> dengan uang pas
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/iv_btn_quick").click()
                driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout").click()
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/linearProses").click()
                # kondisi ketika muncul pop up pilih printer ketika kondisi tidak konek dengan printer
                try:
                    driver.implicitly_wait(2)
                    driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ya").is_displayed()
                    driver.back()
                except:
                    pass
                time.sleep(2)
                # klik lihat struk
                try:
                    driver.implicitly_wait(10)
                    driver.find_element(By.XPATH, ("//android.widget.TextView[@text='More']")).click()
                except:
                    driver.find_element(By.XPATH, ("//android.widget.TextView[@text='Lainnya']")).click()
                # Menunggu menampilkan struk
                driver.implicitly_wait(10)
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/nama_toko").is_displayed()
                driver.back()
                time.sleep(2)
                driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btnSelesai").click()
        status = "sukses"
    except:
        status = "gagal transaksi"
    return status