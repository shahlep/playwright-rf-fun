from playwright.sync_api import expect
from PIL import Image
from pixelmatch.contrib.PIL import pixelmatch


class LandingPage:
    @staticmethod
    def url_page_is_working(page):
        # Add 5 todos and check the counts
        items = ['one', 'two', 'three', 'four', 'five']
        for item in items:
            page.click('.new-todo')
            page.fill('.new-todo', item)
            page.locator('.new-todo').press('Enter')
        number = page.locator('.todo-list li').count()
        expect(page.locator('.todo-list li')).to_have_count(number)
        for i in range(1, number + 1):
            page.locator('.todo-list li:nth-of-type(i)')
            page.click('.toggle')
            page.click('.clear-completed')
        number1 = page.locator('.todo-list li').count()
        expect(page.locator('.todo-list li')).to_have_count(number1)

    @staticmethod
    def focus_on_todo_input_field(page):
        expect(page.locator('.new-todo')).to_be_focused()

    @staticmethod
    def clear_input_field_after_add(page):
        page.click('.new-todo')
        page.fill('.new-todo', 'item')
        page.locator('.new-todo').press('Enter')

        expect(page.locator('.new-todo')).to_be_empty()
        page.click('.toggle')
        expect(page.locator('.todo-list li')).to_have_class('completed')
        page.click('.clear-completed')

    @staticmethod
    def to_check_todo_can_be_completed(page):
        page.click('.new-todo')
        page.fill('.new-todo', 'item')
        page.locator('.new-todo').press('Enter')
        page.click('.toggle')
        expect(page.locator('.todo-list li')).to_have_class('completed')
        page.click('.clear-completed')

    @staticmethod
    def clear_all_completed_todos(page):
        page.click('.new-todo')
        page.fill('.new-todo', 'item')
        page.locator('.new-todo').press('Enter')
        page.click('.toggle')

        page.click('.clear-completed')
        number = page.locator('.todo-list li').count()
        expect(page.locator('.todo-list li')).to_have_count(number)

    @staticmethod
    def can_edit_a_todo(page):
        page.click('.new-todo')
        page.fill('.new-todo', 'item')
        page.locator('.new-todo').press('Enter')

        page.dblclick('.todo-list label')

        page.fill('.edit', 'edited item')
        page.locator('.edit').press('Enter')

        expect(page.locator('.todo-list li')).to_have_text('edited item')

        page.click('.toggle')

        page.click('.clear-completed')
        number = page.locator('.todo-list li').count()
        expect(page.locator('.todo-list li')).to_have_count(number)

    @staticmethod
    def count_number_of_todo_left_to_complete(page):

        items = ['one', 'two', 'three', 'four', 'five', 'six']
        for item in items:
            page.click('.new-todo')
            page.fill('.new-todo', item)
            page.locator('.new-todo').press('Enter')

        expect(page.locator('.todo-count')).to_have_text('6 items left')

        number = page.locator('.todo-list li').count()
        expect(page.locator('.todo-list li')).to_have_count(number)
        for i in range(1, number + 1):
            page.locator('.todo-list li:nth-of-type(i)')
            page.click('.toggle')
            page.click('.clear-completed')
        number1 = page.locator('.todo-list li').count()
        expect(page.locator('.todo-list li')).to_have_count(number1)

    @staticmethod
    def page_reload_and_persist(page):

        items = ['one', 'two', 'three', 'four', 'five']
        for item in items:
            page.click('.new-todo')
            page.fill('.new-todo', item)
            page.locator('.new-todo').press('Enter')
        number = page.locator('.todo-list li').count()
        expect(page.locator('.todo-list li')).to_have_count(number)

        page.reload()

        expect(page.locator('.todo-list li')).to_have_count(number)

        for i in range(1, number + 1):
            page.locator('.todo-list li:nth-of-type(i)')
            page.click('.toggle')
            page.click('.clear-completed')
        number1 = page.locator('.todo-list li').count()
        expect(page.locator('.todo-list li')).to_have_count(number1)

    @staticmethod
    def display_only_completed_todos(page):

        page.click('.new-todo')
        page.fill('.new-todo', 'item')
        page.locator('.new-todo').press('Enter')
        page.click('.toggle')

        page.click('.selected')
        number = page.locator('.todo-list li').count()
        expect(page.locator('.todo-list li')).to_have_count(number)

    @staticmethod
    def image_compare(page):
        page.screenshot(path="screenshots/screenshot1.png", full_page=True)
        page.screenshot(path="screenshots/screenshot2.png", full_page=True)
        img_a = Image.open("screenshots/screenshot1.png")
        img_b = Image.open("screenshots/screenshot2.png")
        img_diff = Image.new("RGBA", img_a.size)

        # note how there is no need to specify dimensions
        mismatch = pixelmatch(img_a, img_b, img_diff, includeAA=True)

        img_diff.save("screenshots/diff.png")