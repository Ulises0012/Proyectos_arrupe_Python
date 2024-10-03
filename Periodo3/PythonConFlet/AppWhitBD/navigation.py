from flet import Page

def navigate_to_login(page: Page):
    page.clean()
    from login import Login_page
    Login_page(page)

def navigate_to_register(page: Page):
    page.clean()
    from register import Register_page
    Register_page(page)

def navigate_to_welcome(page: Page):
    page.clean()
    from welcome import Welcome
    Welcome(page)
