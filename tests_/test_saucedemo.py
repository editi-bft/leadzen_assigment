import pytest

from POM.saucedemo import SauceDemoLogin

def test_login(_drivers):
    login_obj = SauceDemoLogin(_drivers)
    login_obj.username()
    login_obj.password()
    login_obj.login_button()
    login_obj.verify_login()





