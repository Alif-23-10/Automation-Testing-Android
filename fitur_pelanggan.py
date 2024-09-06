import time

from setup_descap import *

def tambah_pelanggan_manual(nama_pelanggan, kode_pelanggan, email_pelanggan, no_hp_pelanggan, alamat_pelanggan):
    try:
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/bars").click()
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lin_manajemen").click()

        # klik menu pelanggan dan supplier
        driver.implicitly_wait(10)
        driver.find_element(By. XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.LinearLayout").click()
        # klik pelanggan
        driver.implicitly_wait(10)
        driver.find_element(By. XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]").click()

        try:
            driver.implicitly_wait(3)
            driver.find_element(By. ID, "org.owline.kasirpintarpro:id/btn_ok").click()
        except:
            pass

        try:
            driver.implicitly_wait(3)
            driver.find_element(By. ID, "com.android.permissioncontroller:id/permission_allow_button").click()
        except:
            pass

        driver.implicitly_wait(5)
        driver.find_element(By. ID, "org.owline.kasirpintarpro:id/btn_manual").click()

        # input form pelanggan
        driver.implicitly_wait(10)
        driver.find_element(By. ID, "org.owline.kasirpintarpro:id/editNamaPanggilan").send_keys(nama_pelanggan)
        driver.find_element(By. ID, "org.owline.kasirpintarpro:id/editKodePelanggan").send_keys(kode_pelanggan)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editEmail").send_keys(email_pelanggan)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editTelepon").send_keys(no_hp_pelanggan)
        driver.find_element(By.ID, "org.owline.kasirpintarpro:id/editAlamat").send_keys(alamat_pelanggan)
        driver.implicitly_wait(4)
        driver.find_element(By. ID, "org.owline.kasirpintarpro:id/btnTambahDataBarang").click()

        # ketika email pelanggan tidak di isi, lalu email akan di generate otomatis lewat pop up ini
        try:
            driver.implicitly_wait(10)
            driver.find_element(By. ID, "org.owline.kasirpintarpro:id/btn_ok").click()
        except:
            pass

        # pop up tambahkan ke kontak
        driver.implicitly_wait(5)
        driver.find_element(By. ID, "org.owline.kasirpintarpro:id/tidak").click()
        time.sleep(2)
        driver.back()
        status = "sukses"
    except:
        pass
        status = "gagal"
    return status