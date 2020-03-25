
import i18n

def get_welcome_menu():
    menu = '''
    Hi, \n\n This is an automated service to help you with any COVID-19 related questions you have. Kindly follow the instructions below. \n\n COVID-19 සම්බන්ධයෙන් ඇති ප්‍රශ්න සඳහා පිළිතුරු සැපයීමට මෙම ස්වයංක්‍රීය සේවාව ක්‍රියාත්මක කර ඇත. කරුණාකර පහත උපදෙස් අනුගමනය කරන්න.\n\n இது COVID-19 தொடர்பான உங்களின் கேள்விகளுக்கு உதவுவதற்கான தானியங்கி சேவையாகும். தயவுசெய்து கீழேயுள்ள வழிமுறைகளைப் பின்பற்றவும்.\n\n1. In English \n2. සිංහල භාෂාවෙන්\n3. தமிழ் மொழியிலிருந்து\n\nEnter the menu number:\nමෙනු අංකය ඇතුළත් කරන්න:\nமெனு எண்ணை உள்ளிடவும்:
    '''
    return menu

def get_main_menu(lang):
    menu = i18n.t('_MainMenu_', locale=lang)
    return menu