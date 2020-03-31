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

def get_latest_news(lang):
    news = f'''*{i18n.t('_LatestNewsHeading_', locale=lang)}* \n\n
            {i18n.t('_DeptGovInfoKey_', locale=lang)} - {i18n.t('_DeptGovInfoValue_', locale=lang)} \n
            {i18n.t('_HPBKey_', locale=lang)} - {i18n.t('_HPBValue_', locale=lang)} \n    
            {i18n.t('_EPIDUnitKey_', locale=lang)} - {i18n.t('_EPIDUnitValue_', locale=lang)} \n\n
            {i18n.t('_InternationalNewsHeading_', locale=lang)} \n\n
            {i18n.t('_SituationRepKey_', locale=lang)}: \n
            {i18n.t('_SituationRepValue_', locale=lang)} \n\n
            {i18n.t('_RollUpdateKey_', locale=lang)}: \n
            {i18n.t('_RollUpdateValue_', locale=lang)} \n\n
            {i18n.t('_NewsArticlesKey_', locale=lang)}: \n
            {i18n.t('_NewsArticlesValue_', locale=lang)} \n\n'''
    return news