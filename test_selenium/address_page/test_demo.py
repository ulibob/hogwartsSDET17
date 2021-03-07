from test_selenium.address_page.main_page import MainPage


class TestAddcontact:

    def test_add_contact(self):
        main_page = MainPage()
        contact_page = main_page.goto_address().goto_addcontacts()
        contact_page.add_message()
        contact_page.contact_save()

# main_page.goto_add_contacts()
