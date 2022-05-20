class LandingPageElements:
    def __init__(self, page):
        self.todo_list = page.locator(".todo-list li")
        self.url = "https://demo.playwright.dev/todomvc/#/"
