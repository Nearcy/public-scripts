
import pyautogui
import time
import requests

def fetch_image(filename):
    url = f"https://raw.githubusercontent.com/Nearcy/public-scripts/main/pictures/{filename}"
    img_data = requests.get(url).content
    with open(filename, "wb") as f:
        f.write(img_data)

images = [
    "claim_1_1.png","claim_1_2.png","claim_2_1.png","claim_2_2.png","claim_2_3.png","coupon.png"
]

for img in images:
    fetch_image(img)

def checker_1_1():
    try:
        match1 = pyautogui.locateOnScreen('claim_1_1.png', confidence=0.8)
    except Exception as e:
        print(f"Error saat mencari ss1.png: {e}")
        match1 = None

    if match1:
        try:
            x, y = pyautogui.center(match1)
            time.sleep(1)
            return True
        except Exception as e:
            print(f"Error saat menjalankan proses match1: {e}")
            return False
            
def checker_1_2():
    try:
        match1 = pyautogui.locateOnScreen('claim_1_2.png', confidence=0.8)
    except Exception as e:
        print(f"Error saat mencari ss1.png: {e}")
        match1 = None

    if match1:
        try:
            x, y = pyautogui.center(match1)
            pyautogui.doubleClick(x, y)
            time.sleep(2)
            return True
        except Exception as e:
            print(f"Error saat menjalankan proses match1: {e}")
            return False
            
def checker2():
    try:
        match1 = pyautogui.locateOnScreen('claim_2_1.png', confidence=0.8)
    except Exception as e:
        print(f"Error saat mencari earntask1.png: {e}")
        match1 = None

    if match1:
        try:
            x, y = pyautogui.center(match1)
            pyautogui.doubleClick(x, y)
            time.sleep(2)
            return True
        except Exception as e:
            print(f"Error saat menjalankan proses match1: {e}")
            return False

    
        

    print("Tidak ada mode yang cocok.")
    return False      
    
def checker3():
    try:
        match1 = pyautogui.locateOnScreen('claim_2_2.png', confidence=0.8)
    except Exception as e:
        print(f"Error saat mencari open.png: {e}")
        match1 = None

    if match1:
        try:
            x, y = pyautogui.center(match1)
            pyautogui.doubleClick(x, y)
            time.sleep(2)
            return True
        except Exception as e:
            print(f"Error saat menjalankan proses match1: {e}")
            return False
            
    try:
        match2 = pyautogui.locateOnScreen('claim_2_3.png', confidence=0.8)
    except Exception as e:
        print(f"Error saat mencari open.png: {e}")
        match2 = None

    if match2:
        try:
            x, y = pyautogui.center(match2)
            time.sleep(2)
            return True
        except Exception as e:
            print(f"Error saat menjalankan proses match2: {e}")
            return False
    print("Tidak ada mode yang cocok.")
    return False       
    
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
            print("Berhasil match1_1")
            if checker_1_1():
                print("Checker_1_1 berhasil")
                if checker_1_2():
                    print("Checker_1_2 berhasil")
                    pyautogui.hotkey('alt', 'f4') 
                else:
                    print("Checker_1_1 tidak ditemukan")
                    pyautogui.hotkey('alt', 'f4') 
            else:
                print("ulang sampai ditemukan")
                
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
            if checker2():
                print("Checker2 berhasil dijalankan.")
                if checker3():
                    print("Checker3 berhasil dijalankan dan proses selesai")
                    pyautogui.hotkey('alt', 'f4') 
                else:
                    print("ulang sampai ditemukan")
            else:
                print("ulang sampai ditemukan")
            
            return True
        except Exception as e:
            print(f"Error saat menjalankan proses match2: {e}")
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
