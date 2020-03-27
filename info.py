import i18n

def get_protect_info(lang):
    menu = f'''{i18n.t('_ProtectInfo_', locale=lang)}\n\n {i18n.t('_ReplyForMenu_', locale=lang)}'''
    return menu

def get_travel_info(lang):
    menu = f'''{i18n.t('_TravelAdvice_', locale=lang)}\n\n {i18n.t('_ReplyForMenu_', locale=lang)}'''
    return menu

def get_questions_info(lang):
    menu = f'''{i18n.t('_QuestionsInfo_', locale=lang)}\n\n {i18n.t('_ReplyForMenu_', locale=lang)}'''
    return menu

def get_redirect_msg():
    info = f'''{i18n.t('_RedirectInfo_', locale="en")}\n\n {i18n.t('_RedirectInfo_', locale="sl")}\n\n {i18n.t('_RedirectInfo_', locale="tm")}'''
    return info