import io
import sys
import time

from colorama import Back, Fore, Style
from PIL import Image
from seleniumbase import get_driver

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

        driver.uc_open_with_reconnect(url, 3)

        if CF_TITLE not in driver.title:
            color_message("SUCCESS", "Bypass CF")
            bypass = True
            break

        try_number += 1

    if not bypass:
        color_message("ERROR", "Can't bypass CF")
        raise Exception("CF not bypass")


def run_site(url: str):
    driver = get_driver("chrome", headless=HEADLESS, undetectable=True)

    fix_cf_just_moment(url, driver)

    screenshot_as_png = driver.get_screenshot_as_png()
    driver.quit()

    image = Image.open(io.BytesIO(screenshot_as_png))
    image.show()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].startswith("http"):
        run_site(sys.argv[1])
        time.sleep(1)
    else:
        print("URL not provided. Please specify a URL as the first argument.")
        sys.exit(1)
