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

    @staticmethod
    def open_application():
        PlaywrightCore.context = PlaywrightCore.browser.new_context()
        PlaywrightCore.page = PlaywrightCore.context.new_page()
        PlaywrightCore.page.goto('https://demo.playwright.dev/todomvc/#/')

    @staticmethod
    def close_application():
        PlaywrightCore.page.close()
        PlaywrightCore.context.close()

    @staticmethod
    def get_page_object():
        return PlaywrightCore.page

    @staticmethod
    def take_screenshot():
        return PlaywrightCore.page.screenshot(path="page.png")
