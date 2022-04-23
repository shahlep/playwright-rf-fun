from playwright.sync_api import expect


class LandingPage:
    @staticmethod
    def test_url_page_is_working(page):
        # Add 5 tods and check the counts
        items = ['one', 'two', 'three', 'four', 'five']
        for item in items:
            page.click('.new-todo')
            page.fill('.new-todo', item)
            page.locator('.new-todo').press('Enter')
        number = page.locator('.todo-list li').count()
        expect(page.locator('.todo-list li')).to_have_count(number)
