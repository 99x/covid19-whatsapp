
import i18n

def get_welcome_menu():
    menu = "Hi, \n\nThis is an automated service provided by UNDP and 99X Technology to help you with any COVID-19 related questions you have. Kindly follow the instructions below. \n\n COVID-19 සම්බන්ධයෙන් ඇති ප්‍රශ්න සඳහා පිළිතුරු සැපයීමට මෙම ස්වයංක්‍රීය සේවාව UNDP සහ 99X Technology ආයතන මගින් ක්‍රියාත්මක කර ඇත. කරුණාකර පහත උපදෙස් අනුගමනය කරන්න.\n\n இது COVID-19 தொடர்பில் உங்களிடம் உள்ள கேள்விகளுக்கு உதவி வழங்க UNDP மற்றும் 99X Technology யினால் வழங்கப்பட்ட தானியங்கி சேவையாகும். தயவுசெய்து கீழேயுள்ள வழிமுறைகளைப் பின்பற்றவும்.\n\n1️⃣ Please type  1  for English \n2️⃣ සිංහල භාෂාව සඳහා අංක 2 යොදන්න\n3️⃣ தமிழில் தொடர்வதற்கு இலக்கம் 3யை அழுத்தவும்\n\nEnter the menu number:\nමෙනු අංකය ඇතුළත් කරන්න:\nமெனு எண்ணை உள்ளிடவும்:"
    return menu

def get_main_menu(lang):
    menu = i18n.t('_MainMenu_', locale=lang)
    return menu