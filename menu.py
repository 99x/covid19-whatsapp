
def get_welcome_menu():
    menu = '''
    *WELCOME TO COVID-19 DATA BOT (by UNDP and 99X)*
    
    * You can get information regarding COVID-19 outbreak in Sri Lanka
    * ශ්‍රී ලංකාවේ වර්තමාන COVID-19 වෛරසය පැතිරීම පිළිබඳ තොරතුරු මෙතැනින් ලබා ගත හැකිය
    * இலங்கையில் COVID-19 தொற்றுநோய் பரவல் குறித்த தகவல்களை இங்கே பெறலாம்

    1. Provide data in English
    2. සිංහල භාෂාවෙන් දත්ත දෙන්න 
    3. தகவல்களைத் தமிழில் கொடுங்கள்
    
    --
        '''
    return menu

def get_english_menu():
    menu = '''
    *Enter the menu number for the information you require. *\n
    4. Latest numbers
    5. Related news
    6. Graph data
    '''
    return menu

def get_sinhala_menu():
    menu = '''
    *ඔබට අවශ්‍ය තොරතුරු වල මෙනු අංකය ඇතුළත් කරන්න. *\n
    7. අලුත්ම සංක්‍යා 
    8. නවතම පුවත් 
    9. ප්‍රස්ථාර දත්ත
    '''
    return menu

def get_tamil_menu():
    menu = '''
    *உங்களுக்குத் தேவையான தகவலின் எண்ணை உள்ளிடவும். *\n
    10. பாதிக்கப்பட்டோர் என்னிக்கைகள்
    11. நோய் பற்றிய புதிய செய்திகள்
    12. வரைபடங்கள்
    '''
    return menu