from playwright.sync_api import sync_playwright, APIRequestContext


class PlaywrightCore:
    browser = None
    context = None
    page = None
    pwSync = None
    pwRequest = None

    @staticmethod
    def launch_browser(browser_name):
        print("Browser : " + browser_name)
        PlaywrightCore.pwSync = sync_playwright().start()
        if browser_name.lower() == "chromium":
            PlaywrightCore.browser = PlaywrightCore.pwSync.chromium.launch(
                headless=True
            )
        elif browser_name.lower() == "firefox":
            PlaywrightCore.browser = PlaywrightCore.pwSync.firefox.launch(headless=True)
        else:
            PlaywrightCore.browser = PlaywrightCore.pwSync.webkit.launch(headless=True)
        PlaywrightCore.context = PlaywrightCore.browser.new_context()
        PlaywrightCore.context.tracing.start(
            screenshots=True, snapshots=True, sources=True
        )

        PlaywrightCore.pwRequest = PlaywrightCore.pwSync.request.new_context()

    @staticmethod
    def close_browser():
        PlaywrightCore.context.tracing.stop(path="trace.zip")
        PlaywrightCore.context.close()
        PlaywrightCore.browser.close()
        PlaywrightCore.pwSync.stop()

    @staticmethod
    def open_application():
        PlaywrightCore.page = PlaywrightCore.context.new_page()
        PlaywrightCore.page.goto("https://demo.playwright.dev/todomvc/#/")

    @staticmethod
    def close_application():
        PlaywrightCore.page.close()

    @staticmethod
    def get_page_object():
        return PlaywrightCore.page

    @staticmethod
    def take_screenshot():
        return PlaywrightCore.page.screenshot(path="page.png")

    @staticmethod
    def open_sauce_application():
        PlaywrightCore.page = PlaywrightCore.context.new_page()
        PlaywrightCore.page.goto("https://www.saucedemo.com/")

    @staticmethod
    def close_sauce_application():
        PlaywrightCore.page.close()
