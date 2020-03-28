
import i18n

def get_welcome_menu():
    menu = f'''Hi 🙂, \n\n{i18n.t('_Welcome_', locale="en")} \n\n{i18n.t('_Welcome_', locale="sl")}  \n\n{i18n.t('_Welcome_', locale="tm")} \n\n{i18n.t('_LangSelection_', locale="en")} \n{i18n.t('_LangSelection_', locale="sl")} \n{i18n.t('_LangSelection_', locale="tm")} '''
    return menu

def get_main_menu(lang):
    menu = i18n.t('_MainMenu_', locale=lang)
    return menu