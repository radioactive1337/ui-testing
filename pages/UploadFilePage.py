from .BasePage import BasePage
from selenium.webdriver.common.by import By


class UploadFilePageLocators:
    FILE_INPUT = (By.XPATH, "//input[@id='file']")
    FILE_RES = (By.XPATH, "//div[@id='error']")


class UploadFilePage(BasePage):
    def input_file(self, file):
        self.fill_input(UploadFilePageLocators.FILE_INPUT, file)

    def file_is_uploaded(self):
        return "File Successfully Uploaded" in self.get_element(UploadFilePageLocators.FILE_RES).text
