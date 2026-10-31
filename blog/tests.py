from django.test import TestCase
from django.urls import reverse
from .models import AboutMeModel,LinksModel
# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        self.about=AboutMeModel.objects.create(text="Salom, men Islomjonman")
        self.links=LinksModel.objects.create(telegram='https://t.me/islomnurmukhammadov', github='https://github.com/islomnurmukhammadov', linkedin='https://www.linkedin.com/in/islomnurmukhammadov/')

    def test_home_status(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)

        response_name=self.client.get(reverse('home'))
        self.assertEqual(response_name.status_code,200)

    def test_home_templates(self):
        response=self.client.get(reverse('home'))
        self.assertTemplateUsed(response,'home.html')
        self.assertTemplateUsed(response,'base.html')

    def test_single_model(self):
        AboutMeModel.objects.create(text='Yangilangan matn')
        self.assertEqual(AboutMeModel.objects.count(),1)
        self.assertEqual(AboutMeModel.load().text,"Yangilangan matn")

    def test_home_content(self):
        response=self.client.get(reverse('home'))
        self.assertContains(response,'https://github.com/islomnurmukhammadov')