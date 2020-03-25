from repositories.disease_data_repository import DiseaseDataRepository
import i18n


class Stats:
    def __init__(self, cache):
        self.cache = cache

    def get_numbers(self, lang):
        data_repository = DiseaseDataRepository(cache= self.cache)
        data = data_repository.get_disease_data()
        stats = f"""*{i18n.t('_SriLanka_', locale=lang)}* \n\n{data['sl_new']} {i18n.t('_NewCases_', locale=lang)}\n{data['sl_confirmed']} {i18n.t('_Confirmed_', locale=lang)} \n{data['sl_hospitals']} {i18n.t('_Suspects_', locale=lang)}\n\n{data['sl_recovered']} {i18n.t('_Recovered_', locale=lang)}\n{data['sl_new_deaths']} {i18n.t('_NewDeaths_', locale=lang)}\n{data['sl_deaths']} {i18n.t('_Deaths_', locale=lang)} \n\n{i18n.t('_LatestNewsLocal_', locale=lang)} www.news.lk \n\n\n *{i18n.t('_Globally_', locale=lang)}* \n\n {data['global_new_cases']} {i18n.t('_NewCases_', locale=lang)}\n {data['global_confirmed']} {i18n.t('_Confirmed_', locale=lang)}\n\n {data['global_recovered']} {i18n.t('_Recovered_', locale=lang)} \n {data['global_new_deaths']} {i18n.t('_NewDeaths_', locale=lang)} \n {data['global_deaths']} {i18n.t('_Deaths_', locale=lang)}  \n\n{i18n.t('_LatestNewsGlobal_', locale=lang)} www.who.int  \n"""
        return stats
