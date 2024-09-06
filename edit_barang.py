import re
import time
from telnetlib import EC

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from setup_descap import *

def edit_barang_default(nama_barang, nama_barang_default_edit, stok_barang_edit, harga_jual_edit):
    global status

    try:
        print("pertama" + nama_barang_default_edit)
        driver.implicitly_wait(5)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/bars").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lin_manajemen").click()
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView").click()
        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText").send_keys(nama_barang)

        driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]").click()
        driver.implicitly_wait(2)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/fab_edit").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editNamaBarang").clear()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editNamaBarang").send_keys(nama_barang_default_edit)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editJumlah").clear()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editJumlah").send_keys(stok_barang_edit)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editHargaJual").clear()
        print("debug 01")
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editHargaJual").send_keys(harga_jual_edit)
        print("debug 02")
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btnTambahDataBarang").click()
        print("debug 03")
        time.sleep(4)
        nama_barang_default = driver.find_element(By.ID, "org.owline.kasirpintarpro:id/tvNama")
        default = nama_barang_default.text
        print("debug 04")
        stok_barang_default = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[5]/android.widget.TextView[3]")
        stok_barang_default_text = stok_barang_default.text
        int_angka_stok = str(int(re.sub(r'\D', '', stok_barang_default_text)))
        angka_stok = str(int_angka_stok)
        print("debug 05")
        harga_jual_default = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[3]")
        harga_jual_text = harga_jual_default.text
        int_angka_harga_jual = str(int(re.sub(r'\D', '', harga_jual_text)))
        angka_harga_jual = str(int_angka_harga_jual)

        print("ini statusnya" + status)
        print("-------------------------------")
        print("1. " + str(nama_barang_default_edit))
        print("2. " + str(stok_barang_edit))
        print("3. " + str(harga_jual_edit))
        print("-------------------------------")
        print(default)
        print(angka_stok)
        print(angka_harga_jual)

        ekspektasi_data= {
            "nama barang edit" : str(nama_barang_default_edit),
            "stok barang edit" : str(stok_barang_edit),
            "harga jual edit" : str(harga_jual_edit)
        }
        actual_data= {
            "nama barang edit" : default,
            "stok barang edit" : angka_stok,
            "angka harga jual" : angka_harga_jual
        }

        if ekspektasi_data == actual_data:
            status = "sukses"
        else:
            status = "terdapat data hasil edit yang tidak sesuai"

        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.back()
        return status
    except Exception as e:
        status = f"eror edit barang default : {str(e)}"
        return status

def edit_barang_multisatuan(nama_barang, nama_barang_multisatuan_edit, stok_barang_edit, harga_jual_edit, nama_satuan_edit, jumlah_satuan_edit, harga_satuan_edit):
    global status
    try:
        try:
            driver.implicitly_wait(5)
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/bars").click()
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lin_manajemen").click()
            driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView").click()
            driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText").send_keys(nama_barang)

            driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]").click()
            driver.implicitly_wait(2)
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/fab_edit").click()
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editNamaBarang").clear()
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editNamaBarang").send_keys(nama_barang_multisatuan_edit)
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editJumlah").clear()
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editJumlah").send_keys(stok_barang_edit)
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editHargaJual").clear()
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editHargaJual").send_keys(harga_jual_edit)

            driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView").click()
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/tambah_multisatuan").click()
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/nama_satuan").send_keys(nama_satuan_edit)
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/jumlah").send_keys(jumlah_satuan_edit)
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/harga").send_keys(harga_satuan_edit)
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ya").click()
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/doneCheck").click()
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btnTambahDataBarang").click()
        except Exception as e:
            status = f"gagal edit barang multisatuan : {str(e)}"

        try:
            print("debug")
            time.sleep(5)
            nama_barang_multisatuan = driver.find_element(By.ID, "org.owline.kasirpintarpro:id/tvNama")
            multisatuan = nama_barang_multisatuan.text

            stok_barang_multisatuan = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[5]/android.widget.TextView[3]")
            stok_barang_multisatuan_text = stok_barang_multisatuan.text
            angka_stok = str(int(re.sub(r'\D', '', stok_barang_multisatuan_text)))

            harga_jual_multisatuan = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[3]")
            harga_jual_text = harga_jual_multisatuan.text
            angka_harga_jual = str(int(re.sub(r'\D', '', harga_jual_text)))

            nama_satuan = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[5]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.TextView[1]")
            nama_satuan_text = nama_satuan.text

            jumlah_satuan = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[5]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.TextView[2]")
            jumlah_satuan_text = jumlah_satuan.text

            harga_satuan = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[5]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.TextView[3]")
            harga_satuan_text = harga_satuan.text
            angka_harga_satuan = str(int(re.sub(r'\D', '', harga_satuan_text)))

            print("Ekspektasi Data")
            print("1. - " + str(nama_barang_multisatuan_edit))
            print("2. - " + str(harga_jual_edit))
            print("3. - " + str(stok_barang_edit))
            print("4. - " + str(nama_satuan_edit))
            print("5. - " + str(jumlah_satuan_edit))
            print("6. - " + str(harga_satuan_edit))
            print("----------------------------")
            print("Actual Data")
            print("1. " + multisatuan)
            print("2. " + angka_harga_jual)
            print("3. " + angka_stok)
            print("4. " + nama_satuan_text)
            print("5. " + jumlah_satuan_text)
            print("6. " + angka_harga_satuan)
            print("----------------------------")

            ekspektasi_data= {
                "nama barang edit" : str(nama_barang_multisatuan_edit),
                "harga jual edit" : str(harga_jual_edit),
                "stok barang edit" : str(stok_barang_edit),
                "nama satuan edit" : str(nama_satuan_edit),
                "jumlah satuan edit" : str(jumlah_satuan_edit),
                "harga satuan edit" : str(harga_satuan_edit)
            }
            hasil_edit = {
                "nama barang edit" : multisatuan,
                "harga jual edit" : angka_harga_jual,
                "stok barang edit" : angka_stok,
                "nama satuan edit" : nama_satuan_text,
                "jumlah satuan edit" : jumlah_satuan_text,
                "harga satuan edit" : angka_harga_satuan
            }

            if ekspektasi_data == hasil_edit:
                status = "sukses"
            else:
                status = "terdapat data hasil edit yang tidak sesuai"

            time.sleep(2)
            driver.back()
            time.sleep(1)
            driver.back()

            print("status edit barang multisatuan: " + status)

            return status
        except Exception as e:
            status = f"tidak bisa mendefinisikan hasil edit barang : {str(e)}"
            return status
    except Exception as e:
        status = f"eror edit barang Multisatuan: {str(e)}"
        return status

def edit_barang_imei(nama_barang, nama_barang_imei_edit, harga_jual_imei_edit, barcode_imei_edit):
    global status
    try:
        try:
            driver.implicitly_wait(5)
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/bars").click()
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lin_manajemen").click()
            driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView").click()
            driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText").send_keys(nama_barang)

            driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]").click()
            driver.implicitly_wait(2)
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/fab_edit").click()
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editNamaBarang").clear()
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editNamaBarang").send_keys(nama_barang_imei_edit)
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editHargaJual").clear()
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editHargaJual").send_keys(harga_jual_imei_edit)

            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/linier_tambah_imei").click()

            # edit data data imei ke1
            driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ScrollView/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView").click()
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/edt_barcode").send_keys(barcode_imei_edit)
            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/doneCheck").click()

            time.sleep(1)
            driver.back()

            driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btnTambahDataBarang").click()

        except:
            status = "gagal edit barang imei"

        try:
            # Menunggu setelah edit barang
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "org.owline.kasirpintarpro:id/tvNama"))
            )
            nama_imei = driver.find_element(By.ID, "org.owline.kasirpintarpro:id/tvNama")
            nama_imei_text = nama_imei.text

            harga_jual_imei = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[3]")
            harga_jual_text = harga_jual_imei.text
            angka_harga_jual_imei = str(int(re.sub(r'\D', '', harga_jual_text)))

            print(nama_imei_text)
            print(angka_harga_jual_imei)

            ekspektasi_data = {
                "nama barang": nama_barang_imei_edit,
                "harga jual imei": str(harga_jual_imei_edit)
            }

            hasil_edit = {
                "nama barang": nama_imei_text,
                "harga jual imei": angka_harga_jual_imei
            }
            time.sleep(3)
            driver.back()
            time.sleep(2)
            driver.back()

            if ekspektasi_data == hasil_edit:
                status = "sukses"
            else:
                status = "terdapat data hasil edit yang tidak sesuai"

        except:
            status = "tidak bisa mendefinisikan edit barang"

        return status
    except:
        status = "edit barang imei eror"
    return status