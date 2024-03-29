import time

from colorama import Back, Fore, Style
from PIL import Image
import io
from seleniumbase import get_driver

URL = "https://business-monitor.ch/"
CF_TITLE = "Just a moment"
TRY_COUNT = 5
HEADLESS = True


def color_message(type: str, msg: str):
    match type:
        case "ERROR":
            color = Fore.RED
        case "INFO":
            color = Fore.BLUE
        case "SUCCESS":
            color = Back.GREEN
        case _:
            color = Fore.WHITE

    print(f"[{color + type + Style.RESET_ALL}] {msg}")


def fix_cf_just_moment(url: str, driver):
    # Fix CF `Just moment...` loading
    try_number = 0
    bypass = False

    while try_number < TRY_COUNT:
        color_message("INFO", f"Try bypass CF - {try_number+1}")
        
        driver.uc_open_with_reconnect(URL, 3)

        if CF_TITLE not in driver.title:
            color_message("SUCCESS", "Bypass CF")
            bypass = True
            break

        try_number += 1

    if not bypass:
        color_message("ERROR", "Can't bypass CF")
        raise Exception("CF not bypass")


def run_site():
    driver = get_driver("chrome", headless=HEADLESS, undetectable=True)

    fix_cf_just_moment(URL, driver)

    screenshot_as_png = driver.get_screenshot_as_png()
    driver.quit()

    image = Image.open(io.BytesIO(screenshot_as_png))
    image.show()


if __name__ == "__main__":
    run_site()

    time.sleep(1)
