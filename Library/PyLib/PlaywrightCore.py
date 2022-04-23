from playwright.sync_api import sync_playwright


class PlaywrightCore:
    browser = None
    context = None
    page = None
    pwSync = None

    @staticmethod
    def launch_browser(browser_name):
        print("Browser : " + browser_name)
        PlaywrightCore.pwSync = sync_playwright().start()
        if browser_name.lower() == "Chromium":
            PlaywrightCore.browser = PlaywrightCore.pwSync.chromium.launch(headless=False)

    @staticmethod
    def close_browser():
        PlaywrightCore.browser.close()
        PlaywrightCore.pwSync.stop()
