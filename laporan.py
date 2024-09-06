from selenium.webdriver.common.by import By
from setup_descap import driver
from compare_struk_transaksi import *
import json

def laporan_sesuai_transaksi():
    try:
        # 3baris untuk membuka sidebar
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/bars").click()

        # membuka menu laporan Transaksi Penjualan
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lin_laporan").click()

        # close pop up news yang ada di halaman laporan jika muncul
        try:
            driver.implicitly_wait(5)
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/close_news").click()
        except:
            pass

        # klik menu laporan transaksi penjualan
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[4]/android.widget.LinearLayout").click()

        # klik report transaksi perhari
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout").click()

        # declare data JSON List Laporan untuk dibandingkan
        json_data = '{"pendapatan": "Rp 2,000", "keuntungan" : "Rp 1,000"}'
        expected_data_list_laporan = json.loads(json_data)

        # Ambil data dari elemen-elemen Android
        element_pendapatan = driver.find_element(By.ID, "org.owline.kasirpintarpro:id/total_keseluruhan")
        element_keuntungan = driver.find_element(By.ID, "org.owline.kasirpintarpro:id/keuntungan")

        # ambil teks dari element
        list_pendapatan = element_pendapatan.text
        list_keuntungan = element_keuntungan.text

        print("--------------------------------------------")
        print("pendapatan di list laporan : " + list_pendapatan)
        print("keuntungan di list laporan : " + list_keuntungan)

        # Buat objek Python dari data yang diambil dari elemen Android
        android_data = {
            "pendapatan": list_pendapatan,
            "keuntungan": list_keuntungan
        }

        keterangan_list_laporan = []
        # Bandingkan data dari elemen Android dengan data JSON
        if android_data == expected_data_list_laporan:
            status = "sukses"

        else:
            status = "Keuntungan atau Pendapatan ada yang tidak sesuai di list laporan"

        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout").click()

    except Exception as x:
        status = "gagal mengakses laporan" + str(x)
    return status

