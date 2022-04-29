import urllib.request
from certificates import ssl_expiry_datetime
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.picker import MDThemePicker
from kivymd.uix.screen import Screen
from kivy.core.window import Window
from kivy.lang import Builder
from helpers import screen_helper
from kivy.uix.screenmanager import ScreenManager
from emailverfication import email_ver
from sql import search_data, profile_data
from local_app_data import save_theme, load_theme, load_primary, load_accent, check_status, set_status, get_profile
from api_code import testAPI
from domain_info import domain_info
from ratingTest import ratingData, inputRating, outputRating
from scratch_2 import preview

Window.size = (360, 600)


class BootScreen(Screen):
    pass


class HomeScreen(Screen):
    pass


class SearchScreen(Screen):
    pass


class SettingsScreen(Screen):
    f = 0
    path0 = "themes"
    path1 = "classic_theme"
    path3 = "setting.png"


class FaqsScreen(Screen):
    pass


class FeedbackScreen(Screen):
    pass


class ProfileScreen1(Screen):
    no = 0


class ProfileScreen2(Screen):
    pass


class ReportUrlScreen(Screen):
    pass


class SearchScreen2(Screen):
    pass


class SearchScreen3(Screen):
    pass


class SearchScreen4(Screen):
    pass


class SearchScreen5(Screen):
    pass


# global sm
# sm = ScreenManager()
# sm.add_widget(BootScreen(name='boot'))
# sm.add_widget(HomeScreen(name='home'))
# sm.add_widget(SearchScreen(name='profile'))
# sm.add_widget(SettingsScreen(name='settings'))
# sm.add_widget(FaqsScreen(name='faqs'))
# sm.add_widget(FeedbackScreen(name='feedback'))
# sm.add_widget(ProfileScreen1(name='profile1'))
# sm.add_widget(ProfileScreen2(name='profile2'))
# sm.add_widget(ReportUrlScreen(name='report'))


class Demo(MDApp):
    picker = None
    valid = 0

    # global sm
    sm = ScreenManager()
    sm.add_widget(BootScreen(name='boot'))
    sm.add_widget(HomeScreen(name='home'))
    sm.add_widget(SearchScreen(name='profile'))
    sm.add_widget(SettingsScreen(name='settings'))
    sm.add_widget(FaqsScreen(name='faqs'))
    sm.add_widget(FeedbackScreen(name='feedback'))
    sm.add_widget(ProfileScreen1(name='profile1'))
    sm.add_widget(ProfileScreen2(name='profile2'))
    sm.add_widget(ReportUrlScreen(name='report'))
    sm.add_widget(SearchScreen2(name='search2'))
    sm.add_widget(SearchScreen3(name='search3'))
    sm.add_widget(SearchScreen4(name='search4'))
    sm.add_widget(SearchScreen5(name='search5'))

    def build(self):

        self.theme_cls.theme_style = load_theme()
        self.theme_cls.primary_palette = load_primary()
        self.theme_cls.accent_palette = load_accent()
        # Image(source="22.png")
        screen = Builder.load_string(screen_helper)
        # urL = MDTextField(text='Enter url', pos_hint={'center_x': 0.5, 'center_y': 0.6}, size_hint={})
        # btn1 = MDRectangleFlatButton(text='Search', pos_hint={'center_x': 0.8, 'center_y': 0.5}, size_hint=(0.045, 0.05))
        # btn2 = MDFloatingActionButton(icon='plus', pos_hint={'center_x': 0.9, 'center_y': 0.1})
        # url = Builder.load_string(url_helper)
        # screen.add_widget(url)
        # screen.add_widget(btn1)
        # screen.add_widget(btn2)
        return screen

    # def on_start(self):
    #     print(1)
    #     Clock.schedule_once(self.change_screen, 10)

    def change_screen(self, *args):
        print(2)
        self.sm.current = 'home'
        print(3)

    def go_back(self, screen_name):
        self.root.current = screen_name

    def show_themepicker(self):
        self.picker = MDThemePicker()
        self.picker.open()

    def store_theme(self, f):
        if f == 1:
            save_theme(self.picker.theme_cls.theme_style, self.picker.theme_cls.primary_palette,
                       self.picker.theme_cls.accent_palette)
            self.toast_text(8)
        else:
            self.toast_text(9)

    def theme_pack(self, path):
        path0 = "themes"
        path1 = "\classic_theme"

        if path == "":
            return

    def get_url(self):
        self.Link = self.root.get_screen('home').ids.link.text
        users = search_data(self, self.Link)
        # print(users)
        user = None
        for user in users:
            pass
        self.root.get_screen('search').ids.label1.text = self.Link

        if user == None:
            self.root.get_screen('search').ids.label2.text = "Database Scan Complete : URL Not Found"
        else:
            self.root.get_screen('search').ids.label2.text = "Database Scan Complete : URL Listed as Malicious"

    def register(self):
        strng1 = self.root.get_screen('profile1').ids.name.text
        strng2 = self.root.get_screen('profile1').ids.mail.text
        if self.valid == 0:
            self.toast_text(5)
        elif len(strng1) == 0:
            self.toast_text(6)
        else:
            self.root.current = 'profile2'
            profile_data(self)
            set_status(1, strng2, strng1)
            self.root.get_screen('profile2').ids.username.text = self.root.get_screen('profile1').ids.name.text
            self.root.get_screen('profile2').ids.emailid.text = self.root.get_screen('profile1').ids.mail.text
            # self.eemail= self.root.get_screen('profile2').ids.emailid.text
            self.toast_text(7)

    def get_mail(self):
        no = 0
        strng = self.root.get_screen('profile1').ids.mail.text
        if strng.endswith("gmail.com"):
            no = email_ver(strng)
            self.toast_text(1)
        else:
            self.toast_text(2)
        return no

    def toast_text(self, p):
        if p == 0:
            toast("Sending Otp...!")
        elif p == 1:
            toast("OTP Sent...!")
        elif p == 2:
            toast("Couldn't send OTP. Please Enter a valid Gmail ID...!")
        elif p == 3:
            toast("OTP Verification Successful...!")
        elif p == 4:
            toast("Invalid OTP.Verification Unsuccessful...!")
        elif p == 5:
            toast("First Verify your gmail id using OTP...!")
        elif p == 6:
            toast("Please Enter your name...!")
        elif p == 7:
            toast("Successfully Registered...!")
        elif p == 8:
            toast("Changes Saved...!")
        elif p == 9:
            toast("Theme already saved...!")
        elif p == 10:
            toast("Rating Exists... Insert a different URL")
        elif p==11:
            toast("File Downloaded")

    def validate_otp(self, no):
        if no == self.root.get_screen('profile1').ids.otp.text:
            self.toast_text(3)
            self.valid = 1
        else:
            self.toast_text(4)
            self.valid = 0

    def profile_status(self, s):
        strng = ""
        strng1 = ""
        if s == 0:
            status = check_status()
            if status == 0:
                self.root.current = 'profile1'
            else:
                self.root.get_screen('profile2').ids.emailid.text = get_profile(0)
                self.root.get_screen('profile2').ids.username.text = get_profile(1)
                self.root.current = 'profile2'
        elif s == 2:
            set_status(0, strng, strng1)

    def float(self):
        if check_status() == 0:
            self.root.current = 'profile1'
        else:
            self.root.current = 'report'

    def get_api(self):
        value = testAPI(self.root.get_screen('home').ids.link.text)
        self.root.get_screen('search2').ids.label3.text = value

    def get_domain_info(self):
        # print(type(domain_info()))
        print(self.root.get_screen('home').ids.link.text)
        inf = domain_info(self.root.get_screen('home').ids.link.text)
        print(type(inf))
        print(1)
        self.root.get_screen('search3').ids.label4.text = inf  # domain_info(self.root.get_screen('home').ids.link.text)

    def rating_input(self):
        self.rurl = self.root.get_screen('report').ids.rurl.text
        self.value = self.root.get_screen('report').ids.slide.value
        self.ff = inputRating(self.rurl).rateURL(self.value, get_profile(0))
        print(self.rurl)
        print(self.value)
        if self.ff == False:
            self.toast_text(10)

    def rating_output(self):
        # self.avg_rat = outputRating(self.Link).getRating()
        self.root.get_screen('search').ids.label6.text = str(outputRating(self.Link).getRating())


    def image_preview(self):
        print(self.Link)
        imgg = self.Link
        self.img = preview(imgg)
        # self.img = "https://api.screenshotmachine.com/?key=4ba519&url=cricbuzz.com&dimension=480x800&device=phone&cacheLimit=0&delay=200&zoom=100"
        # print(self.img)
        # print(type(self.img))
        # SearchScreen5().var(self.Link)
        self.downld_ss(self.img)

    def downld_ss(self, url):
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        filename = 'screen_shot.png'
        image_url = url
        # image_url = "https://api.screenshotmachine.com/?key=4ba519&url=cricbuzz.com&dimension=480x800&device=phone&cacheLimit=0&delay=200&zoom=100"
        # image_url = "https://api.screenshotmachine.com/?key=4ba519&url=gcq.ac.in&dimension=480x800&device=phone&cacheLimit=0&delay=200&zoom=100"
        urllib.request.urlretrieve(image_url, filename)
        self.root.get_screen('search5').ids.ss.reload()

    def downld_dinfo(self):
        f = open(self.Link+"_domain_info.txt", "w+")
        f.write(domain_info(self.Link))
        f.close()
        self.toast_text(11)

    def ssl(self):
        self.ssl_info=ssl_expiry_datetime(self.Link)
        self.root.get_screen('search4').ids.label5.text=self.ssl_info

Demo().run()
