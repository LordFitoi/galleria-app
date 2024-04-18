import time, os

from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait_delay = 15 # seconds
username = "[USERNAME HERE]"
password = "[PASSWORD HERE]"


images = [
    os.getcwd()+"/images/image-1.png",
    os.getcwd()+"/images/image-2.png",
    os.getcwd()+"/images/image-3.png",
]

def select(selector):
    print(f"SELECTING: <{selector}>")
    return WebDriverWait(driver, wait_delay).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
    )

def select_no_wait(selector):
    return driver.find_element(by=By.CSS_SELECTOR, value=selector)

# TEST 1: Probar que carga la pagina principal.
driver.get("https://www.flickr.com/")
time.sleep(1)
driver.save_screenshot("./screenshot-1.png")

# TEST 2: Ir a pagina de inicio de sesion.
select("a[href='/signin']").click()
driver.save_screenshot("./screenshot-2.png")

# TEST 3: Iniciar sesion.
select("input#login-email").send_keys(username)
select("button[data-testid='identity-form-submit-button']").click()
driver.save_screenshot("./screenshot-3a.png")

select("input#login-password").send_keys(password)
select("button[data-testid='identity-form-submit-button']").click()
driver.save_screenshot("./screenshot-3b.png")

# TEST 4: Probar la interfaz de subir imagenes y subir imagenes.
select("a[data-track='gnUploadIconMain']").click()
driver.save_screenshot("./screenshot-4.png")

# TEST 5: Probar a subir imagenes.
time.sleep(1)
select_no_wait('input#choose-photos-and-videos').send_keys('\n'.join(images))
driver.save_screenshot("./screenshot-5a.png")
select("input#action-publish").click()
select("input#confirm-publish").click()

time.sleep(10)
driver.save_screenshot("./screenshot-5b.png")

# TEST 6: Verificar que las imagenes se subieron.
driver.get("https://www.flickr.com/")
select(".mobile-nav-toggle").click()
select(".mobile-nav-menu-item:nth-child(7)").click()
driver.save_screenshot("./screenshot-6.png")

# TEST 7: Crear un album.
select(".cameraroll-item-placeholder").click()
driver.save_screenshot("./screenshot-7a.png")

select('.button.dismiss').click()
select(".album-selected-photos").click()
driver.save_screenshot("./screenshot-7b.png")

select(".create-button").click()
select("input.stuff-creation-title").send_keys("My Album")
driver.save_screenshot("./screenshot-7c.png")

select(".button.mini.button-action").click()
select(".button.mini.done-button").click()

# TEST 8: Verificar que el album se creo.
select(".links #albums").click()
driver.save_screenshot("./screenshot-8.png")

# TEST 9: Ir a la pagina de galerias.
select(".links #galleries").click()
driver.save_screenshot("./screenshot-9.png")

#TEST 10: Crear una galeria.
try:
    select(".new-gallery-button").click()
except TimeoutException:
    select(".empty-create-button").click()

select(".stuff-creation-title").send_keys("My Gallery")
driver.save_screenshot("./screenshot-10a.png")

select(".button.mini.button-action").click()
driver.save_screenshot("./screenshot-10b.png")

# TEST 11: Agregar fotos a galeria.
driver.get("https://www.flickr.com/explore")
driver.save_screenshot("./screenshot-11a.png")

select(".photo-list-photo-view").click()
driver.save_screenshot("./screenshot-11b.png")

select(".engagement-item.curate").click()
driver.save_screenshot("./screenshot-11c.png")

select(".selection-item").click()

# TEST 12: Verificar que las fotos se agregaron a la galeria.
select(".mobile-nav-toggle").click()
select(".mobile-nav-menu-item:nth-child(4)").click()
driver.save_screenshot("./screenshot-12a.png")

select(".photo-list-gallery-view").click()
driver.save_screenshot("./screenshot-12b.png")

# TEST 13: Eliminar galeria.
select(".action.edit").click()
driver.save_screenshot("./screenshot-13a.png")
select(".delete-button").click()
driver.save_screenshot("./screenshot-13b.png")
select(".confirm-button").click()

time.sleep(5)

driver.save_screenshot("./screenshot-13c.png")

# TEST 14: Eliminar fotos.
select(".links #cameraroll").click()
select("a[data-track='selectAllClick']").click()
driver.save_screenshot("./screenshot-14a.png")
select('.delete-selected-photos').click()
driver.save_screenshot("./screenshot-14b.png")
select('.confirm.danger').click()
driver.save_screenshot("./screenshot-14c.png")

time.sleep(5)

driver.save_screenshot("./screenshot-14d.png")

driver.quit()