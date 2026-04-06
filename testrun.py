
import pyautogui
import time
import requests

def fetch_image(filename):
    url = f"https://raw.githubusercontent.com/Nearcy/public-scripts/main/pictures/{filename}"
    img_data = requests.get(url).content
    with open(filename, "wb") as f:
        f.write(img_data)

images = [
    "ss1.png","ss2.png","ss3.png",
    "earntask1.png","earntask2.png","earntask3.png", "earntask11.png", "earntask22.png", "earntask33.png",
    "detect1.png","detect2.png",
    "losestreak.png","earnup.png",
    "mode2.png","mode22.png","open.png","coupon.png","ss_evo.png"
]

for img in images:
    fetch_image(img)

def checker():
    try:
        match1 = pyautogui.locateOnScreen('ss1.png', confidence=0.8)
    except Exception as e:
        print(f"Error saat mencari ss1.png: {e}")
        match1 = None

    if match1:
        try:
            x, y = pyautogui.center(match1)
            pyautogui.click(x, y)
            time.sleep(2)
            pyautogui.moveTo(225, 30, duration=2)
            pyautogui.doubleClick(225, 30)
            time.sleep(1)
            pyautogui.moveTo(15, 188, duration=2)
            pyautogui.doubleClick(15, 188)
            time.sleep(1)
            return True
        except Exception as e:
            print(f"Error saat menjalankan proses match1: {e}")
            return False
    try:
        match2 = pyautogui.locateOnScreen('ss_evo.png', confidence=0.8)
    except Exception as e:
        print(f"Error saat mencari ss2.png: {e}")
        match2 = None

    if match2:
        try:
            x, y = pyautogui.center(match2)
            pyautogui.click(x, y)
            time.sleep(2)
            pyautogui.moveTo(225, 30, duration=2)
            pyautogui.doubleClick(225, 30)
            time.sleep(1)
            pyautogui.moveTo(15, 188, duration=2)
            pyautogui.doubleClick(15, 188)
            time.sleep(1)
            return True
        except Exception as e:
            print(f"Error saat menjalankan proses match2: {e}")
            return False
    try:
        match3 = pyautogui.locateOnScreen('ss3.png', confidence=0.8)
    except Exception as e:
        print(f"Error saat mencari ss3.png: {e}")
        match3 = None

    if match3:
        try:
            x, y = pyautogui.center(match3)
            pyautogui.click(x, y)
            time.sleep(2)
            pyautogui.moveTo(225, 30, duration=2)
            pyautogui.doubleClick(225, 30)
            time.sleep(1)
            pyautogui.moveTo(15, 188, duration=2)
            pyautogui.doubleClick(15, 188)
            time.sleep(1)
            return True
        except Exception as e:
            print(f"Error saat menjalankan proses match3: {e}")
            return False
        
def checker2():
    try:
        match1 = pyautogui.locateOnScreen('earntask1.png', confidence=0.8)
    except Exception as e:
        print(f"Error saat mencari earntask1.png: {e}")
        match1 = None

    if match1:
        try:
            x, y = pyautogui.center(match1)
            pyautogui.click(x, y)
            time.sleep(2)
            pyautogui.moveTo(225, 30, duration=2)
            pyautogui.doubleClick(225, 30)
            time.sleep(1)
            pyautogui.moveTo(15, 188, duration=2)
            pyautogui.doubleClick(15, 188)
            time.sleep(1)
            return True
        except Exception as e:
            print(f"Error saat menjalankan proses match1: {e}")
            return False
            
    try:
        match2 = pyautogui.locateOnScreen('earntask2.png', confidence=0.8)
    except Exception as e:
        print(f"Error saat mencari earntask2.png: {e}")
        match2 = None

    if match2:
        try:
            x, y = pyautogui.center(match2)
            pyautogui.click(x, y)
            time.sleep(2)
            pyautogui.moveTo(225, 30, duration=2)
            pyautogui.doubleClick(225, 30)
            time.sleep(1)
            pyautogui.moveTo(15, 188, duration=2)
            pyautogui.doubleClick(15, 188)
            time.sleep(1)
            return True
        except Exception as e:
            print(f"Error saat menjalankan proses match2: {e}")
            return False

    try:
        match4 = pyautogui.locateOnScreen('earntask11.png', confidence=0.8)
    except Exception as e:
        print(f"Error saat mencari earntask11.png: {e}")
        match4 = None

    if match4:
        try:
            x, y = pyautogui.center(match4)
            pyautogui.click(x, y)
            time.sleep(2)
            pyautogui.moveTo(225, 30, duration=2)
            pyautogui.doubleClick(225, 30)
            time.sleep(1)
            pyautogui.moveTo(15, 188, duration=2)
            pyautogui.doubleClick(15, 188)
            time.sleep(1)
            return True
        except Exception as e:
            print(f"Error saat menjalankan proses match4: {e}")
            return False

    try:
        match3 = pyautogui.locateOnScreen('open.png', confidence=0.8)
    except Exception as e:
        print(f"Error saat mencari open.png: {e}")
        match3 = None

    if match3:
        try:
            x, y = pyautogui.center(match3)
            pyautogui.click(x, y)
            time.sleep(2)
            return True
        except Exception as e:
            print(f"Error saat menjalankan proses match3: {e}")
            return False
        

    print("Tidak ada mode yang cocok.")
    return False      
    
def checker3():
    try:
        match1 = pyautogui.locateOnScreen('earntask2.png', confidence=0.8)
    except Exception as e:
        print(f"Error saat mencari earntask2.png: {e}")
        match1 = None

    if match1:
        try:
            x, y = pyautogui.center(match1)
            pyautogui.click(x, y)
            time.sleep(2)
            pyautogui.moveTo(225, 30, duration=2)
            pyautogui.doubleClick(225, 30)
            time.sleep(1)
            pyautogui.moveTo(15, 188, duration=2)
            pyautogui.doubleClick(15, 188)
            time.sleep(1)
            return True
        except Exception as e:
            print(f"Error saat menjalankan proses match1: {e}")
            return False

    try:
        match2 = pyautogui.locateOnScreen('earntask3.png', confidence=0.8)
    except Exception as e:
        print(f"Error saat mencari earntask3.png: {e}")
        match2 = None

    if match2:
        try:
            x, y = pyautogui.center(match2)
            pyautogui.click(x, y)
            time.sleep(2)
            pyautogui.moveTo(225, 30, duration=2)
            pyautogui.doubleClick(225, 30)
            time.sleep(1)
            pyautogui.moveTo(15, 188, duration=2)
            pyautogui.doubleClick(15, 188)
            time.sleep(1)
            return True
        except Exception as e:
            print(f"Error saat menjalankan proses match2: {e}")
            return False

    try:
        match3 = pyautogui.locateOnScreen('earntask22.png', confidence=0.8)
    except Exception as e:
        print(f"Error saat mencari earntask22.png: {e}")
        match3 = None

    if match3:
        try:
            x, y = pyautogui.center(match3)
            pyautogui.click(x, y)
            time.sleep(2)
            pyautogui.moveTo(225, 30, duration=2)
            pyautogui.doubleClick(225, 30)
            time.sleep(1)
            pyautogui.moveTo(15, 188, duration=2)
            pyautogui.doubleClick(15, 188)
            time.sleep(1)
            return True
        except Exception as e:
            print(f"Error saat menjalankan proses match3: {e}")
            return False

    try:
        match4 = pyautogui.locateOnScreen('earntask33.png', confidence=0.8)
    except Exception as e:
        print(f"Error saat mencari earntask33.png: {e}")
        match4 = None

    if match4:
        try:
            x, y = pyautogui.center(match4)
            pyautogui.click(x, y)
            time.sleep(2)
            pyautogui.moveTo(225, 30, duration=2)
            pyautogui.doubleClick(225, 30)
            time.sleep(1)
            pyautogui.moveTo(15, 188, duration=2)
            pyautogui.doubleClick(15, 188)
            time.sleep(1)
            return True
        except Exception as e:
            print(f"Error saat menjalankan proses match4: {e}")
            return False
        
    print("Tidak ada mode yang cocok.")
    return False       
        
def checker_scroll(max_scroll=3000, step=200):
    current_scroll = 0
    while current_scroll <= max_scroll:
        if checker():
            print(f"Checker berhasil di posisi scroll {current_scroll}")
            # tugas checker sudah dijalankan di dalam fungsi checker()
            # jangan scroll balik ke atas, langsung lanjut ke bawah
            current_scroll += step
            pyautogui.scroll(-step)
            print(f"Lanjut scroll ke bawah {current_scroll}")
            time.sleep(1)
        else:
            current_scroll += step
            print(f"Checker gagal, scroll ke bawah {current_scroll}")
            pyautogui.scroll(-step)
            time.sleep(1)
    print("Checker tidak ditemukan lagi sampai batas scroll.")
    
def checker_scroll2(max_scroll=1800, step=200):
    current_scroll = 0
    while current_scroll <= max_scroll:
        if checker2():
            print(f"Checker berhasil di posisi scroll {current_scroll}")
            # tugas checker sudah dijalankan di dalam fungsi checker()
            # jangan scroll balik ke atas, langsung lanjut ke bawah
            current_scroll += step
            pyautogui.scroll(-step)
            print(f"Lanjut scroll ke bawah {current_scroll}")
            time.sleep(1)
        else:
            current_scroll += step
            print(f"Checker gagal, scroll ke bawah {current_scroll}")
            pyautogui.scroll(-step)
            time.sleep(1)
    print("Checker tidak ditemukan lagi sampai batas scroll.")

def checker_scroll3(max_scroll=3000, step=200):
    current_scroll = 0
    while current_scroll <= max_scroll:
        if checker3():
            print(f"Checker berhasil di posisi scroll {current_scroll}")
            # tugas checker sudah dijalankan di dalam fungsi checker()
            # jangan scroll balik ke atas, langsung lanjut ke bawah
            current_scroll += step
            pyautogui.scroll(-step)
            print(f"Lanjut scroll ke bawah {current_scroll}")
            time.sleep(1)
        else:
            current_scroll += step
            print(f"Checker gagal, scroll ke bawah {current_scroll}")
            pyautogui.scroll(-step)
            time.sleep(1)
    print("Checker tidak ditemukan lagi sampai batas scroll.")
    
def verif1():
    try:
        match = pyautogui.locateOnScreen('detect1.png', confidence=0.8)
        if match:
            x, y = pyautogui.center(match)
            time.sleep(3)
            pyautogui.doubleClick(x, y)
            print(f"Gambar pertama ditemukan di {x}, {y} dan diklik detect1")
            return True
        else:
            print("Gambar tidak ditemukan di layar.")
            return False
    except pyautogui.ImageNotFoundException:
        print("Gambar tidak ditemukan (exception).")
    except Exception as e:
        print(f"Terjadi error: {e}")

def validation1():
    try:
        match = pyautogui.locateOnScreen('losestreak.png', confidence=0.8)
        if match:
            time.sleep(3)
            pyautogui.doubleClick(1824, 372)
            print("Gambar ditemukan dan diklik di (1824, 372).")
            time.sleep(3)
            pyautogui.hotkey('ctrl', 'r')
            time.sleep(5)
            return True
        else:
            print("Gambar tidak ditemukan di layar.")
            return False
    except Exception as e:
        print(f"Terjadi error: {e}")
        return False

def coupon():
    try:
        match = pyautogui.locateOnScreen('coupon.png', confidence=0.8)
        if match:
            x, y = pyautogui.center(match)
            pyautogui.click(x, y)
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'r')
            time.sleep(5)
            return True
        else:
            print("Gambar tidak ditemukan di layar.")
            return False
    except Exception as e:
        print(f"Terjadi error: {e}")
        return False
        
def earnup():
    try:
        match = pyautogui.locateOnScreen('earnup.png', confidence=0.8)
        if match:
            time.sleep(3)
            pyautogui.doubleClick(1815, 453)
            print("Gambar ditemukan dan diklik di (1815, 453).")
            time.sleep(3)
            pyautogui.hotkey('ctrl', 'r')
            time.sleep(5)
            return True
        else:
            print("Gambar tidak ditemukan di layar.")
            return False
    except Exception as e:
        print(f"Terjadi error: {e}")
        return False

def verif2():
    try:
        match = pyautogui.locateOnScreen('detect2.png', confidence=0.8)

        if match:
            x, y = pyautogui.center(match)
            print(f"Gambar pertama ditemukan di {x}, {y} dan diklik detect2")
            return True
        else:
            print("Gambar tidak ditemukan di layar.")
            return False
    except pyautogui.ImageNotFoundException:
        print("Gambar tidak ditemukan (exception).")
    except Exception as e:
        print(f"Terjadi error: {e}")


def move_and_click(start_x, start_y, end_x, end_y, duration=2):
    pyautogui.moveTo(start_x, start_y)
    time.sleep(0.5)
    pyautogui.moveTo(end_x, end_y, duration=duration)
    pyautogui.doubleClick(end_x, end_y)
    print(f"Mouse dipindahkan ke ({end_x},{end_y}) dan double-click dilakukan.")

def modechoose():
    try:
        match1 = pyautogui.locateOnScreen('detect2.png', confidence=0.8)
    except Exception as e:
        print(f"Error saat mencari detect2.png: {e}")
        match1 = None

    if match1:
        try:
            time.sleep(10)
            result = validation1()
            print(f"Hasil validation1: {result}")
            result2 = earnup()
            print(f"Hasil earnup: {result2}")
            result3 = coupon()
            print(f"Hasil earnup: {result3}")
            
            pos = checker_scroll(max_scroll=3000, step=250)
            if pos is not None:
                print(f"Checker ditemukan, lanjut dari posisi scroll {pos}")
            else:
                time.sleep(3)
                pyautogui.hotkey('alt', 'f4')
                
            return True
        except Exception as e:
            print(f"Error saat menjalankan proses match1: {e}")
            return False

    try:
        match2 = pyautogui.locateOnScreen('mode2.png', confidence=0.8)
    except Exception as e:
        print(f"Error saat mencari mode2.png: {e}")
        match2 = None

    if match2:
        try:
            print("Berhasil match2")
            pos1 = checker_scroll2(max_scroll=1800, step=250)
            if pos1 is not None:
                print(f"Checker ditemukan, lanjut dari posisi scroll {pos1}")
            else:
                time.sleep(2)
                pyautogui.moveTo(481, 174, duration=2)
                pyautogui.doubleClick(481, 174)
                time.sleep(1)      
                
            time.sleep(2)
            
            pos2 = checker_scroll3(max_scroll=3000, step=250)
            if pos2 is not None:
                print(f"Checker ditemukan, lanjut dari posisi scroll {pos2}")
            else:
                time.sleep(3)
                pyautogui.hotkey('alt', 'f4')
            
            return True
        except Exception as e:
            print(f"Error saat menjalankan proses match2: {e}")
            return False

    try:
        match3 = pyautogui.locateOnScreen('mode22.png', confidence=0.8)
    except Exception as e:
        print(f"Error saat mencari mode22.png: {e}")
        match3 = None

    if match3:
        try:
            print("Berhasil mode22")
            pos1 = checker_scroll2(max_scroll=1800, step=250)
            if pos1 is not None:
                print(f"Checker ditemukan, lanjut dari posisi scroll {pos1}")
            else:
                time.sleep(2)
                pyautogui.moveTo(481, 174, duration=2)
                pyautogui.doubleClick(481, 174)
                time.sleep(1)      
                
            time.sleep(2)
            
            pos2 = checker_scroll3(max_scroll=3000, step=250)
            if pos2 is not None:
                print(f"Checker ditemukan, lanjut dari posisi scroll {pos2}")
            else:
                time.sleep(3)
                pyautogui.hotkey('alt', 'f4')
            
            return True
        except Exception as e:
            print(f"Error saat menjalankan proses match3: {e}")
            return False
        

    print("Tidak ada mode yang cocok.")
    return False

        
        
def run_sequence():
    start_x, start_y = 100, 100
    for i, coord in enumerate(coordinates, start=1):
        if coord["active"]:
            print(f"Step {i}: koordinat aktif → ({coord['x']},{coord['y']})")
            move_and_click(start_x, start_y, coord["x"], coord["y"], duration=2)
            time.sleep(1)

            while not verif1():
                time.sleep(3)
                pyautogui.hotkey('ctrl', 'r')
                time.sleep(2)
            
            while not modechoose():
                time.sleep(5)
                pyautogui.hotkey('ctrl', 'r')
                time.sleep(2)

        else:
            print(f"Step {i}: koordinat tidak aktif → dilewati.")

# Jalankan
run_sequence()
time.sleep(2)
run_sequence()
