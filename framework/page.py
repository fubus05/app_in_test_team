class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_component(self, by, value):
        return self.driver.find_element(by=by, value=value)

