from .page import Page


class LoginPage(Page):
    def click_allow_button_if_present(self, by, value):
        elements = self.driver.find_elements(by=by, value=value)
        if len(elements) > 0:
            allow_button = elements[0]
            allow_button.click()
            return True
        else:
            return False
