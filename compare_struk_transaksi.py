from selenium.webdriver.common.by import By

from datetime import datetime

from setup_descap import driver
import json

def compare_struk_transaksi_berhasil():
    # declare data JSON yang ingin Anda bandingkan
    json_data = '{"nama_penjual": " Alif kaspin ", "nama_barang1" : "1. Sepatu", "sub_harga_perbarang1" : "  1  x 2,00", "total_harga_perbarang1" : "Rp 2,000", "sub_total_transaksi" : "Rp 2,000", "total_transaksi" : "Rp 2,000", "jenis_pembayaran" : "Charges (Cash)", "total_harga_jenis_pembayaran" : "Rp 2,000", "kembalian" : "Rp 0"}'
    expected_data_struk = json.loads(json_data)

    # Ambil data dari elemen-elemen Android
    element_nama_penjual = driver.find_element(By.ID, "org.owline.kasirpintarpro:id/nama_kasir")
    element_nama_barang = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView")
    element_sub_harga_perbarang1 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]")
    element_total_harga_perbarang1 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[2]")
    element_sub_total_transaksi = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TableRow[5]/android.widget.TextView[2]")
    element_total_transaksi = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TableRow[6]/android.widget.TextView[2]")
    element_jenis_pembayaran = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TableRow[7]/android.widget.TextView[1]")
    element_total_harga_jenis_pembayaran = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TableRow[7]/android.widget.TextView[2]")
    element_kembalian = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TableRow[8]/android.widget.TextView[2]")

    # ambil teks dari element
    struk_nama_penjual = element_nama_penjual.text
    struk_nama_barang = element_nama_barang.text
    struk_sub_harga_perbarang1 = element_sub_harga_perbarang1.text
    struk_total_harga_perbarang1 = element_total_harga_perbarang1.text
    struk_sub_total_transaksi = element_sub_total_transaksi.text
    struk_total_transaksi = element_total_transaksi.text
    struk_jenis_pembayaran = element_jenis_pembayaran.text
    struk_total_harga_jenis_pembayaran = element_total_harga_jenis_pembayaran.text
    struk_kembalian = element_kembalian.text

    print("-------------------------------------")
    print("nama penjual : " + struk_nama_penjual)
    print("nama barang : " + struk_nama_barang)
    print("sub harga perbarang 1 : " + struk_sub_harga_perbarang1)
    print("sub harga perbarang 1 : " + struk_total_harga_perbarang1)
    print("sub total transaksi : " + struk_sub_total_transaksi)
    print("total transaksi : " + struk_total_transaksi)
    print("jenis pembayarannya adalah : " + struk_jenis_pembayaran)
    print("total harga di jenis pembayarannya : " + struk_total_harga_jenis_pembayaran)
    print("kembalian : " + struk_kembalian)

    # Buat objek Python dari data yang diambil dari elemen Android
    android_data = {
        "nama_penjual": struk_nama_penjual,
        "nama_barang1": struk_nama_barang,
        "sub_harga_perbarang1": struk_sub_harga_perbarang1,
        "total_harga_perbarang1": struk_total_harga_perbarang1,
        "sub_total_transaksi": struk_sub_total_transaksi,
        "total_transaksi": struk_total_transaksi,
        "jenis_pembayaran": struk_jenis_pembayaran,
        "total_harga_jenis_pembayaran": struk_total_harga_jenis_pembayaran,
        "kembalian": struk_kembalian
    }

    keterangan_struk = []

    # Bandingkan data dari elemen Android dengan data JSON
    if android_data == expected_data_struk:
        status = "sukses"
    else:
        status = "data struk tidak sesuai"
        if android_data["nama_penjual"] != expected_data_struk["nama_penjual"]:
            print("-------------------------------------")
            print("nama penjual tidak sesuai")
            keterangan_struk.append("nama penjual tidak sesuai")
        if android_data["nama_barang1"] != expected_data_struk["nama_barang1"]:
            print("-------------------------------------")
            print("nama barang 1 tidak sesuai")
            keterangan_struk.append("nama barang 1 tidak sesuai")
        if android_data["sub_harga_perbarang1"] != expected_data_struk["sub_harga_perbarang1"]:
            print("-------------------------------------")
            print("sub harga perbarang1 tidak sesuai")
            keterangan_struk.append("sub harga perbarang1 tidak sesuai")
        if android_data["total_harga_perbarang1"] != expected_data_struk["total_harga_perbarang1"]:
            print("-------------------------------------")
            print("total harga perbarang 1 tidak sesuai")
            keterangan_struk.append("total harga perbarang 1 tidak sesuai")
        if android_data["sub_total_transaksi"] != expected_data_struk["sub_total_transaksi"]:
            print("-------------------------------------")
            print("sub total transaksi tidak sesuai")
            keterangan_struk.append("sub total transaksi tidak sesuai")
        if android_data["total_transaksi"] != expected_data_struk["total_transaksi"]:
            print("-------------------------------------")
            print("total transaksi tidak sesuai")
            keterangan_struk.append("total transaksi tidak sesuai")
        if android_data["jenis_pembayaran"] != expected_data_struk["jenis_pembayaran"]:
            print("-------------------------------------")
            print("jenis pembayaran tidak sesuai")
            keterangan_struk.append("jenis pembayaran tidak sesuai")
        if android_data["total_harga_jenis_pembayaran"] != expected_data_struk["total_harga_jenis_pembayaran"]:
            print("-------------------------------------")
            print("total harga jenis pembayaran tidak sesuai")
            keterangan_struk.append("total harga jenis pembayaran tidak sesuai")
        if android_data["kembalian"] != expected_data_struk["kembalian"]:
            print("-------------------------------------")
            print("kembalian tidak sesuai")
            keterangan_struk.append("kembalian tidak sesuai")

    if status != "sukses":
        # Path (jalur) lengkap menuju folder di mana Anda ingin menyimpan file
        folder_keterangan_struk = "D:\\ALIF\\FIle General\\QA Automation\\AUTOMATION ANDROID\\September 2023"  # Gantilah dengan path yang sesuai

        # Mendapatkan waktu saat ini
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")

        # Nama file untuk menyimpan keterangan struk
        nama_file = f"Laporan struk dari Transaksi Berhasil {timestamp}.txt"

        # Membuka file untuk menulis (mode "w") dengan path lengkap
        with open(f"{folder_keterangan_struk}/{nama_file}", "w") as file:
            for keterangan in keterangan_struk:
                file.write(keterangan + "\n")

    print(" ini nih statusnya " + status)
    driver.back()
    driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btnSelesai").click()
    return status
    # status = str(status)
    # print("ini lo masalahnya" + str(status))


def compare_struk_laporan ():
    # declare data JSON yang ingin Anda bandingkan
    json_data = '{"nama_penjual": " Alif kaspin 1", "nama_barang1" : "1. Sepatu2", "sub_harga_perbarang1" : "  1  x 2,000", "total_harga_perbarang1" : "Rp 2,000", "sub_total_transaksi" : "Rp 2,000", "total_transaksi" : "Rp 2,000", "jenis_pembayaran" : "Charges (Cash)", "total_harga_jenis_pembayaran" : "Rp 12,000", "kembalian" : "Rp 10"}'
    expected_data_struk = json.loads(json_data)

    # Ambil data dari elemen-elemen Android
    element_nama_penjual = driver.find_element(By.ID, "org.owline.kasirpintarpro:id/nama_kasir")
    element_nama_barang = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView")
    element_sub_harga_perbarang1 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]")
    element_total_harga_perbarang1 = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[2]")
    element_sub_total_transaksi = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TableRow[5]/android.widget.TextView[2]")
    element_total_transaksi = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TableRow[6]/android.widget.TextView[2]")
    element_jenis_pembayaran = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TableRow[7]/android.widget.TextView[1]")
    element_total_harga_jenis_pembayaran = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TableRow[7]/android.widget.TextView[2]")
    element_kembalian = driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TableRow[8]/android.widget.TextView[2]")

    # ambil teks dari element
    struk_nama_penjual = element_nama_penjual.text
    struk_nama_barang = element_nama_barang.text
    struk_sub_harga_perbarang1 = element_sub_harga_perbarang1.text
    struk_total_harga_perbarang1 = element_total_harga_perbarang1.text
    struk_sub_total_transaksi = element_sub_total_transaksi.text
    struk_total_transaksi = element_total_transaksi.text
    struk_jenis_pembayaran = element_jenis_pembayaran.text
    struk_total_harga_jenis_pembayaran = element_total_harga_jenis_pembayaran.text
    struk_kembalian = element_kembalian.text

    print("-------------------------------------")
    print("nama penjual : " + struk_nama_penjual)
    print("nama barang : " + struk_nama_barang)
    print("sub harga perbarang 1 : " + struk_sub_harga_perbarang1)
    print("sub harga perbarang 1 : " + struk_total_harga_perbarang1)
    print("sub total transaksi : " + struk_sub_total_transaksi)
    print("total transaksi : " + struk_total_transaksi)
    print("jenis pembayarannya adalah : " + struk_jenis_pembayaran)
    print("total harga di jenis pembayarannya : " + struk_total_harga_jenis_pembayaran)
    print("kembalian : " + struk_kembalian)

    # Buat objek Python dari data yang diambil dari elemen Android
    android_data = {
        "nama_penjual": struk_nama_penjual,
        "nama_barang1": struk_nama_barang,
        "sub_harga_perbarang1": struk_sub_harga_perbarang1,
        "total_harga_perbarang1": struk_total_harga_perbarang1,
        "sub_total_transaksi": struk_sub_total_transaksi,
        "total_transaksi": struk_total_transaksi,
        "jenis_pembayaran": struk_jenis_pembayaran,
        "total_harga_jenis_pembayaran": struk_total_harga_jenis_pembayaran,
        "kembalian": struk_kembalian
    }

    keterangan_struk = []

    # Bandingkan data dari elemen Android dengan data JSON
    if android_data == expected_data_struk:
        status = "sukses"
    else:
        status = "data struk tidak sesuai"
        if android_data["nama_penjual"] != expected_data_struk["nama_penjual"]:
            print("-------------------------------------")
            print("nama penjual tidak sesuai")
            keterangan_struk.append("nama penjual tidak sesuai")
        if android_data["nama_barang1"] != expected_data_struk["nama_barang1"]:
            print("-------------------------------------")
            print("nama barang 1 tidak sesuai")
            keterangan_struk.append("nama barang 1 tidak sesuai")
        if android_data["sub_harga_perbarang1"] != expected_data_struk["sub_harga_perbarang1"]:
            print("-------------------------------------")
            print("sub harga perbarang1 tidak sesuai")
            keterangan_struk.append("sub harga perbarang1 tidak sesuai")
        if android_data["total_harga_perbarang1"] != expected_data_struk["total_harga_perbarang1"]:
            print("-------------------------------------")
            print("total harga perbarang 1 tidak sesuai")
            keterangan_struk.append("total harga perbarang 1 tidak sesuai")
        if android_data["sub_total_transaksi"] != expected_data_struk["sub_total_transaksi"]:
            print("-------------------------------------")
            print("sub total transaksi tidak sesuai")
            keterangan_struk.append("sub total transaksi tidak sesuai")
        if android_data["total_transaksi"] != expected_data_struk["total_transaksi"]:
            print("-------------------------------------")
            print("total transaksi tidak sesuai")
            keterangan_struk.append("total transaksi tidak sesuai")
        if android_data["jenis_pembayaran"] != expected_data_struk["jenis_pembayaran"]:
            print("-------------------------------------")
            print("jenis pembayaran tidak sesuai")
            keterangan_struk.append("jenis pembayaran tidak sesuai")
        if android_data["total_harga_jenis_pembayaran"] != expected_data_struk["total_harga_jenis_pembayaran"]:
            print("-------------------------------------")
            print("total harga jenis pembayaran tidak sesuai")
            keterangan_struk.append("total harga jenis pembayaran tidak sesuai")
        if android_data["kembalian"] != expected_data_struk["kembalian"]:
            print("-------------------------------------")
            print("kembalian tidak sesuai")
            keterangan_struk.append("kembalian tidak sesuai")

    if status != "sukses":
        # Path (jalur) lengkap menuju folder di mana Anda ingin menyimpan file
        folder_keterangan_struk = "D:\\ALIF\\FIle General\\QA Automation\\AUTOMATION ANDROID\\Oktober 2023"  # Gantilah dengan path yang sesuai

        # Mendapatkan waktu saat ini
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")

        # Nama file untuk menyimpan keterangan struk
        nama_file = f"Laporan struk dari Laporan Penjualan {timestamp}.txt"

        # Membuka file untuk menulis (mode "w") dengan path lengkap
        with open(f"{folder_keterangan_struk}/{nama_file}", "w") as file:
            for keterangan in keterangan_struk:
                file.write(keterangan + "\n")


    driver.back()
    driver.back()
    driver.back()

    print(" ini nih statusnya " + status)
    return status
    # status = str(status)
    # print("ini lo masalahnya" + str(status))
