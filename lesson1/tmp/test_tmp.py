from .main import Main


class TestWait:
    def setup(self):
        main = Main
        main.click_first_link().get_text()
        main.click_first_link().title()
