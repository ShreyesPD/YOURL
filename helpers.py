from homescreen import hs
from searchscreen import shs, shs2, shs3, shs4, shs5
from settingsscreen import ss
from faqsscreen import fs
from feedbackscreen import fes
from profilescreen1 import ps1
from profilescreen2 import ps2
from ReportUrlScreen import rus
from homescreen import bs

screen_helper = """

ScreenManager:
    BootScreen:
    HomeScreen:
    SearchScreen:
    SearchScreen2:
    SearchScreen3:
    SearchScreen4:
    SearchScreen5:
    SettingsScreen:
    FaqsScreen:
    FeedbackScreen:
    ProfileScreen1: 
    ProfileScreen2:
    ReportUrlScreen:



""" + ss + shs + fes + fs + ps1 + ps2 + hs + rus + bs + shs2 + shs3 + shs4 + shs5
