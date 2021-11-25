from homescreen import hs
from searchscreen import shs
from settingsscreen import ss
from faqsscreen import fs
from feedbackscreen import fes
from profilescreen1 import ps1
from profilescreen2 import ps2
from ReportUrlScreen import rus

screen_helper = """

ScreenManager:
    HomeScreen:
    SearchScreen:
    SettingsScreen:
    FaqsScreen:
    FeedbackScreen:
    ProfileScreen1: 
    ProfileScreen2:
    ReportUrlScreen:


""" + ss + shs + fes + fs + ps1 + ps2 + hs + rus
