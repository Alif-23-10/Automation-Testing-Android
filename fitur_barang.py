import time
from telnetlib import EC

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from setup_descap import *

# untuk menunggu element menggunakan wait until
wait = WebDriverWait(driver, 10)

def tambah_barang_default(nama_barang, kode_barang, stok_barang, harga_beli, harga_jual):
    try:
        driver.implicitly_wait(10)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/bars").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lin_manajemen").click()

        driver.implicitly_wait(100)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView").click()
        driver.implicitly_wait(50)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/fab").click()

        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editNamaBarang").send_keys(nama_barang)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editKodeBarang").send_keys(kode_barang)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editJumlah").send_keys(stok_barang)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editHargaBeli").send_keys(harga_beli)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editHargaJual").send_keys(harga_jual)
        simpan_barang = wait.until(EC.visibility_of_element_located((By.ID, "org.owline.kasirpintarpro:id/btnTambahDataBarang")))
        simpan_barang.click()
        time.sleep(2)
        driver.back()
        # time.sleep(2)
        # try:
        #     sukses_tambah_barang = driver.find_elements(By. ID, "org.owline.kasirpintarpro:id/fab")
        #     barang_sudah_ada = driver.find_elements(By. ID, "org.owline.kasirpintarpro:id/btnTambahDataBarang")
        #
        #     if len(sukses_tambah_barang)>0:
        #         # klik button back
        #         back = wait.until(EC.visibility_of_element_located((By.ID, "org.owline.kasirpintarpro:id/iv_back")))
        #         back.click()
        #         status = "sukses"
        #         return status
        #     elif len(barang_sudah_ada)>0:
        #         # klik button back
        #         back = wait.until(EC.visibility_of_element_located((By.ID, "org.owline.kasirpintarpro:id/iv_back")))
        #         back.click()
        #         button_ya = wait.until(EC.visibility_of_element_located((By.ID, "org.owline.kasirpintarpro:id/ya")))
        #         button_ya.click()
        #         # klik button back
        #         back = wait.until(EC.visibility_of_element_located((By.ID, "org.owline.kasirpintarpro:id/iv_back")))
        #         back.click()
        #         status = "sukses"
        #         return status
        #     else:
        #         status = "Case Tambah Barang default Gagal"
        #
        #     return status
        # except Exception as e:
        #     status = "Error: " + str(e)
        status = "sukses"
    except Exception as e:
        status = "Error: " + str(e)
    return status


def tambah_barang_multisatuan(nama_barang, harga_beli, harga_jual, nama_satuan_terkecil, nama_satuan_lain, jumlah_satuan_lain, harga_satuan_lain, kode_barang, stok_barang):
    try:
        time.sleep(2)
        # klik tambah Barang
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/bars").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lin_manajemen").click()
        driver.implicitly_wait(100)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView").click()
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/fab").click()

        # mengisi data barang
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editNamaBarang").send_keys(nama_barang)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/text_itemlist_spinner").click()
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[5]").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editHargaBeli").send_keys(harga_beli)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editHargaJual").send_keys(harga_jual)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/linier_tambah_multisatuan").click()
        driver.implicitly_wait(2)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/satuan_terkecil").send_keys(nama_satuan_terkecil)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/tambah_satuan_terkecil").click()
        driver.implicitly_wait(2)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/tambah_multisatuan").click()
        driver.implicitly_wait(2)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/nama_satuan").send_keys(nama_satuan_lain)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/jumlah").send_keys(jumlah_satuan_lain)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/harga").clear()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/harga").send_keys(harga_satuan_lain)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ya").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/doneCheck").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editKodeBarang").send_keys(kode_barang)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editJumlah").send_keys(stok_barang)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btnTambahDataBarang").click()
        time.sleep(3)
        driver.back()
        status = "sukses"
    except Exception as x:
        status = "gagal menambahkan multisatuan" + str(x)
    return status

def tambah_barang_1Varian(nama_barang, nama_varian_pertama, nama_varian_kedua, nama_varian_ketiga, kode_varian_pertama, stok_varian_pertama, harga_beli_pertama, harga_jual_pertama, kode_varian_kedua, stok_varian_kedua, harga_beli_kedua, harga_jual_kedua, kode_varian_ketiga, stok_varian_ketiga, harga_beli_ketiga, harga_jual_ketiga, kode_barang, harga_beli_induk, harga_jual_induk):
    try:
        # klik tambah Barang
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/bars").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lin_manajemen").click()
        driver.implicitly_wait(100)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView").click()
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/fab").click()

        # mengisi data barang
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editNamaBarang").send_keys(nama_barang)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/spinnerTipeBarang").click()
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[4]").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/linier_tambah_variasi").click()
        driver.implicitly_wait(2)
        driver.find_element(By. ID, "org.owline.kasirpintarpro:id/btn_tambah_v_n1").click()
        driver.find_element(By. ID, "org.owline.kasirpintarpro:id/edittext_v_c1").send_keys(nama_varian_pertama)
        driver.find_element(By. ID, "org.owline.kasirpintarpro:id/txt_child_ok1").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_tambah_v_n1").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edittext_v_c1").send_keys(nama_varian_kedua)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/txt_child_ok1").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_tambah_v_n1").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edittext_v_c1").send_keys(nama_varian_ketiga)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/txt_child_ok1").click()
        driver.find_element(By. ID, "org.owline.kasirpintarpro:id/doneCheck").click()

        # mengisi data varian pertama
        driver.find_element(By. XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText").send_keys(kode_varian_pertama)
        driver.find_element(By. XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.EditText").send_keys(stok_varian_pertama)
        driver.find_element(By. XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText").send_keys(harga_beli_pertama)
        driver.find_element(By. XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.EditText").send_keys(harga_jual_pertama)

        # mengisi data varian kedua
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText").send_keys(kode_varian_kedua)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.EditText").send_keys(stok_varian_kedua)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText").send_keys(harga_beli_kedua)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.EditText").send_keys(harga_jual_kedua)

        # mengisi data varian ketiga
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText").send_keys(kode_varian_ketiga)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.EditText").send_keys(stok_varian_ketiga)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText").send_keys(harga_beli_ketiga)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.EditText").send_keys(harga_jual_ketiga)

        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/doneCheck").click()

        time.sleep(1)
        # Mendefinisikan kordinat yang akan di scroll
        start_x = int(driver.get_window_size()['width'] * 0.5)  # mendapatkan kordinat tengah dari hp
        start_y = int(driver.get_window_size()['height'] * 0.8)  # mendapatkan kordinat tinggi hp dari atas sampe dengan bawah sebanyak 80%
        end_y = int(driver.get_window_size()['height'] * 0.2)  # mendapatkan kordinat tinggi hp dari atas sampe bawah sebanyak 20%

        # Fungsi untuk melakukan scroll
        action = TouchAction(driver)
        action.press(x=start_x, y=start_y).wait(2000).move_to(x=start_x, y=end_y).release().perform()

        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editKodeBarang").send_keys(kode_barang)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editHargaBeli").send_keys(harga_beli_induk)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editHargaJual").send_keys(harga_jual_induk)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btnTambahDataBarang").click()
        time.sleep(2)
        driver.back()
        status = "sukses"
    except Exception as x:
        status = "tambah barang 1 varian gagal" + str(x)
    return status

# def tambah_barang_2Varian(nama_barang, nama_varian_pertama, nama_varian_kedua, nama_varian_ketiga, kode_varian_pertama, stok_varian_pertama, harga_beli_pertama, harga_jual_pertama, kode_varian_kedua, stok_varian_kedua, harga_beli_kedua, harga_jual_kedua, kode_varian_ketiga, stok_varian_ketiga, harga_beli_ketiga, harga_jual_ketiga, kode_barang, harga_beli_induk, harga_jual_induk):
#     try:
#         # klik tambah Barang
#         driver.find_element(By.ID, "org.owline.kasirpintarpro:id/bars").click()
#         driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lin_manajemen").click()
#         driver.implicitly_wait(100)
#         driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView").click()
#
#
#         # mengisi data barang
#         driver.implicitly_wait(5)
#         driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editNamaBarang").send_keys(nama_barang)
#         driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editKodeBarang").send_keys(kode_barang)
#         driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editHargaBeli").send_keys(harga_beli_induk)
#         driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editHargaJual").send_keys(harga_jual_induk)
#
#         driver.find_element(By.ID, "org.owline.kasirpintarpro:id/fab").click()
#
#         # varian 1
#         driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[4]").click()
#         driver.find_element(By.ID, "org.owline.kasirpintarpro:id/linier_tambah_variasi").click()
#         driver.implicitly_wait(2)
#         driver.find_element(By. ID, "org.owline.kasirpintarpro:id/btn_tambah_v_n1").click()
#         driver.find_element(By. ID, "org.owline.kasirpintarpro:id/edittext_v_c1").send_keys(VarianPertama_kesatu)
#         driver.find_element(By. ID, "org.owline.kasirpintarpro:id/txt_child_ok1").click()
#         driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_tambah_v_n1").click()
#         driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edittext_v_c1").send_keys(VarianPertama_kedua)
#         driver.find_element(By.ID, "org.owline.kasirpintarpro:id/txt_child_ok1").click()
#
#         # varian 2
#         driver.find_element(By.ID, "org.owline.kasirpintarpro:id/linear_btn_tambah").click()
#         driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_tambah_v_n2").click()
#         driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edittext_v_c2").send_keys(VarianKedua_pertama)
#         driver.find_element(By.ID, "org.owline.kasirpintarpro:id/txt_child_ok2").click()
#         driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_tambah_v_n2").click()
#         driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edittext_v_c2").send_keys(VarianKedua_kedua)
#         driver.find_element(By.ID, "org.owline.kasirpintarpro:id/txt_child_ok2").click()
#
#         driver.find_element(By. ID, "org.owline.kasirpintarpro:id/doneCheck").click()
#
#         # mengisi data kombinasi varian (ex : Biru XL)
#         driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText").send_keys(kode_varian_pertama)
#         driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.EditText").send_keys(stok_varian_pertama)
#         driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText").send_keys(harga_beli_pertama)
#         driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.EditText").send_keys(harga_jual_pertama)
#
#         # mengisi data kombinasi varian (ex : Biru L)
#         driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText").send_keys(kode_varian_kedua)
#         driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.EditText").send_keys(stok_varian_kedua)
#         driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText").send_keys(harga_beli_kedua)
#         driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.EditText").send_keys(harga_jual_kedua)
#
#         # mengisi data kombinasi varian (ex : Merah XL)
#         driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText").send_keys(kode_varian_ketiga)
#         driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.EditText").send_keys(stok_varian_ketiga)
#         driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText").send_keys(harga_beli_ketiga)
#         driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.EditText").send_keys(harga_jual_ketiga)
#
#         # mengisi data kombinasi varian (ex : Merah L)
#         driver.find_element(By.XPATH, "")
#         driver.find_element(By.XPATH, "")
#         driver.find_element(By.XPATH, "")
#         driver.find_element(By.XPATH, "")
#
#         driver.find_element(By.ID, "org.owline.kasirpintarpro:id/doneCheck").click()
#
#         time.sleep(1)
#         # Mendefinisikan kordinat yang akan di scroll
#         start_x = int(driver.get_window_size()['width'] * 0.5)  # mendapatkan kordinat tengah dari hp
#         start_y = int(driver.get_window_size()['height'] * 0.8)  # mendapatkan kordinat tinggi hp dari atas sampe dengan bawah sebanyak 80%
#         end_y = int(driver.get_window_size()['height'] * 0.2)  # mendapatkan kordinat tinggi hp dari atas sampe bawah sebanyak 20%
#
#         # Fungsi untuk melakukan scroll
#         action = TouchAction(driver)
#         action.press(x=start_x, y=start_y).wait(2000).move_to(x=start_x, y=end_y).release().perform()
#
#
#         driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btnTambahDataBarang").click()
#         time.sleep(2)
#         driver.back()
#         status = "sukses"
#     except Exception as x:
#         status = "tambah barang 1 varian gagal" + str(x)
#     return status

def tambah_barang_TipeHarga(nama_barang, jumlah_barang, kode_barang, harga_beli, harga_jual, nama_tipeharga, harga_tipeharga_pertama, jumlah_stok_tipeharga_kedua, harga_tipeharga_kedua):
    try:
        # klik tambah Barang
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/bars").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lin_manajemen").click()
        driver.implicitly_wait(100)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView").click()
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/fab").click()

        # mengisi data barang
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editNamaBarang").send_keys(nama_barang)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editJumlah").send_keys(jumlah_barang)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editKodeBarang").send_keys(kode_barang)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editHargaBeli").send_keys(harga_beli)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editHargaJual").send_keys(harga_jual)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/text_tampilkan").click()

        # Mendefinisikan kordinat yang akan di scroll
        start_x = int(driver.get_window_size()['width'] * 0.5)  # mendapatkan kordinat tengah dari hp
        start_y = int(driver.get_window_size()[
                          'height'] * 0.8)  # mendapatkan kordinat tinggi hp dari atas sampe dengan bawah sebanyak 80%
        end_y = int(driver.get_window_size()['height'] * 0.2)  # mendapatkan kordinat tinggi hp dari atas sampe bawah sebanyak 20%

        # Fungsi untuk melakukan scroll
        action = TouchAction(driver)
        action.press(x=start_x, y=start_y).wait(2000).move_to(x=start_x, y=end_y).release().perform()
        action.press(x=start_x, y=start_y).wait(2000).move_to(x=start_x, y=end_y).release().perform()

        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/linier_tambah_tipe_harga").click()
        driver.implicitly_wait(2)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edt_nama_tipeharga").send_keys(nama_tipeharga)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_add_tipe_harga").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edt_harga_per_barang").send_keys(harga_tipeharga_pertama)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lanjut").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_add_tipe_harga").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edt_jumlah").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edt_jumlah").send_keys(jumlah_stok_tipeharga_kedua)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edt_harga_per_barang").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edt_harga_per_barang").send_keys(harga_tipeharga_kedua)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lanjut").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/linear_more").click()
        driver.implicitly_wait(10)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btnTambahDataBarang").click()
        time.sleep(2)
        driver.back()
        status = "sukses"
    except Exception as x:
        status = "tambah barang tipe harga gagal" + str(x)
    return status

def tambah_barang_imei(nama_barang, kode_barang, harga_beli, harga_jual, nama_imei_1, nama_imei_2):
    try:
        # klik tambah Barang
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/bars").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lin_manajemen").click()
        driver.implicitly_wait(100)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView").click()
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/fab").click()

        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editNamaBarang").send_keys(nama_barang)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editKodeBarang").send_keys(kode_barang)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editHargaBeli").send_keys(harga_beli)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editHargaJual").send_keys(harga_jual)

        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/spinnerTipeBarang").click()
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[6]").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/linier_tambah_imei").click()

        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/tambah_imei").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edt_barcode").send_keys(nama_imei_1)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/tambahkan").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edt_barcode").send_keys(nama_imei_2)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/tambahkan").click()

        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/doneCheck").click()

        try:
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/kembali").click()
        except:
            driver.back()

        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btnTambahDataBarang").click()
        time.sleep(4)
        driver.back()

        status = "sukses"
    except Exception as x:
        status = "tambah barang imei sukses" + str(x)
    return status

def tambah_barang_addon(nama_barang, kode_barang, stok_barang, harga_beli, harga_jual):
    try:
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/bars").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lin_manajemen").click()

        driver.implicitly_wait(100)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView").click()
        driver.implicitly_wait(50)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/fab").click()

        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editNamaBarang").send_keys(nama_barang)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editKodeBarang").send_keys(kode_barang)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editJumlah").send_keys(stok_barang)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editHargaBeli").send_keys(harga_beli)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editHargaJual").send_keys(harga_jual)

        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/text_itemlist_spinner").click()
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[7]").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btnTambahDataBarang").click()
        time.sleep(4)
        driver.back()
        status = "suksess"
    except Exception as x:
        status = "tambah barang addon sukses" + str(x)
    return status

def tambah_barang_bahan_baku(nama_barang, kode_barang, stok_barang, harga_beli, harga_jual):
    try:
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/bars").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lin_manajemen").click()

        driver.implicitly_wait(100)
        driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView").click()
        driver.implicitly_wait(50)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/fab").click()

        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editNamaBarang").send_keys(nama_barang)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editKodeBarang").send_keys(kode_barang)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editJumlah").send_keys(stok_barang)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editHargaBeli").send_keys(harga_beli)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editHargaJual").send_keys(harga_jual)

        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/text_itemlist_spinner").click()
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[2]").click()

        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/linier_bahan_baku").click()
        time.sleep(2)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/label").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/label").send_keys("anak bahan baku")
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.LinearLayout").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lanjut").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/doneCheck").click()

        driver.implicitly_wait(5)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btnSimpan").click()
        try:
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ya").click()
        except:
            pass

        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btnTambahDataBarang").click()
        time.sleep(2)
        driver.back()
        status = "suksess"
    except Exception as x:
        status = "tambah barang bahan baku sukses" + str(x)
    return status

def tambah_barang_paket(nama_barang, kode_barang, stok_barang, harga_beli, harga_jual):
    try:
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/bars").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lin_manajemen").click()

        driver.implicitly_wait(100)
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView").click()
        driver.implicitly_wait(50)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/fab").click()

        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editNamaBarang").send_keys(nama_barang)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editKodeBarang").send_keys(kode_barang)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editJumlah").send_keys(stok_barang)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editHargaBeli").send_keys(harga_beli)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editHargaJual").send_keys(harga_jual)

        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/text_itemlist_spinner").click()
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[3]").click()

        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/linier_tambah_add_on").click()
        time.sleep(2)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/label").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/label").send_keys("anak bahan baku")
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout/android.widget.LinearLayout").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lanjut").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/doneCheck").click()

        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btnTambahDataBarang").click()
        time.sleep(2)
        driver.back()
        status = "suksess"
    except Exception as x:
        status = "tambah barang paket sukses" + str(x)
    return status

def hapus_barang(nama_barang):
    try:
    # ke halaman barang untuk menghapus barang
        time.sleep(2)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/bars").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lin_manajemen").click()
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView").click()
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText").send_keys(nama_barang)

        longpress_barang = driver.find_element(By. ID, "org.owline.kasirpintarpro:id/linierBarang")
        action = TouchAction(driver)
        action.long_press(longpress_barang, duration=3000).release().perform()


        time.sleep(4)
        icon_hapus = driver.find_elements(By. ID, "org.owline.kasirpintarpro:id/hapus")
        if len(icon_hapus)>0:
            driver.find_element(By. ID, "org.owline.kasirpintarpro:id/hapus").click()
            button_ya = wait.until(EC.visibility_of_element_located((By.ID, "org.owline.kasirpintarpro:id/ya")))
            button_ya.click()
            back = wait.until(EC.visibility_of_element_located((By.ID, "org.owline.kasirpintarpro:id/iv_back")))
            back.click()
            status = "sukses"
        else:
            back = wait.until(EC.visibility_of_element_located((By.ID, "org.owline.kasirpintarpro:id/iv_back")))
            back.click()
            status = "sukses"
            pass
    except:
        pass
        status = "gagal hapus barang"
    return status

