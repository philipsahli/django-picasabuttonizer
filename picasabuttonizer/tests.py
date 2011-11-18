from django.contrib.auth.models import User
from django.core.files.base import File
from django.db.models.fields.files import FileField

from django.test import TestCase
import zipfile
from django.test.client import Client
from mezzanine.pages.models import Page
import os
from buttonizer import Buttonizer
from models import Button


class ButtonizerTest(TestCase):
    user = None
    button = None
    def setUp(self):
        self.user = User(username="asdf")
        self.user.set_password("asdf")
        self.user.save()

        p = os.path.dirname(os.path.abspath(__file__))

        icon = open(os.path.join(p, "test_files/icon.psd"))
        f_icon = File(icon)

        self.button = Button(
            name="Testbutton",
            user=self.user,
            icon=f_icon,
        )
        self.button.save()

        page = Page(status='2', description="buttonizer", title="Buttonizer")
        page.save()


    def test_button_instance_has_guid(self):
        self.assertTrue(len(self.button.guid)>0)

    def test_create_button(self):
        buttonizer = Buttonizer()
        button = buttonizer.create(
            name="testbutton",
            label="Testseite",
            tooltip="click for upload..",
            psd=self.button.icon,
            guid=self.button.guid,
            hybrid_uploader_url="http://localhost/slideee/picasa"
        )

    def test_create_button_with_model(self):
        buttonizer = Buttonizer()
        name, button = buttonizer.create_for_buttonmodel(self.button)

    def test_get_button_with_client(self):
        c = Client()
        c.login(username='asdf', password='asdf')
        response = c.get("/apps/buttonizer/?get="+self.button.guid)
        self.assertEqual(response.status_code, 200)

    def test_form_saved_and_redirect_authenticated(self):
        c = Client()
        c.login(username='asdf', password='asdf')
        icon = self.button.icon
        response = c.post("/buttonizer/", {
            'name': "testbutton",
            'label': "testbutton",
            'tooltip': "testbutton",
            'hybrid_uploader_url': "http://www.fatrix.ch",
            'icon': icon,
            'icon_name': "testbutton",
            }, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "testbutton", count=1)
        self.button = Button.objects.get(name="testbutton")
        self.assertIsInstance(self.button, Button)

    def test_form_saved_and_redirect_anonymous(self):
        c = Client()
        icon = self.button.icon
        response = c.get("/")
        response = c.post("/buttonizer/", {
            'name': "anonymous_testbutton",
            'label': "testbutton",
            'tooltip': "testbutton",
            'hybrid_uploader_url': "http://www.fatrix.ch",
            'icon': icon,
            'icon_name': "testbutton",
            }, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "anonymous_testbutton", count=1)

    def test_form_edit(self):
        c = Client()
        c.login(username='asdf', password='asdf')
        response = c.post("/buttonizer/?edit="+self.button.guid, {
            'name': "new_anonymous_testbutton",
            'label': "testbutton",
            'tooltip': "testbutton",
            'hybrid_uploader_url': "http://www.fatrix1.ch",
            'icon_name': "testbutton",
            }, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "new_anonymous_testbutton", count=1)

    def test_get_button_with_client_forbidden(self):
        c = Client()
        response = c.get("/buttonizer/?get="+self.button.guid)
        self.assertEqual(response.status_code, 404)

    def test_permission_cannot_add_button(self):
        # TODO: add testmethod to check permission
        pass

    def tearDown(self):
        self.user.delete()
        self.button.delete()
