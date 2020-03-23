from repositories.disease_data_repository import DiseaseDataRepository
import i18n


class Stats:
    def __init__(self, cache):
        self.cache = cache

    def get_stats(self, lang):
        i18n.set('locale', lang)
        data_repository = DiseaseDataRepository(cache= self.cache)
        data = data_repository.get_disease_data()
        stats = f"""*{i18n.t('_SriLanka_')}* \n{data['sl_new']} {i18n.t('_NewCases_')}\n{data['sl_confirmed']} {i18n.t('_Confirmed_')} \n{data['sl_deaths']} {i18n.t('_Deaths_')}\n{data['sl_hospitals']} {i18n.t('_Suspects_')}\n{data['sl_recovered']} {i18n.t('_Recovered_')} \n\n{i18n.t('_LatestNewsLocal_')} www.news.lk \n \n *{i18n.t('_Globally_')}* \n {data['global_confirmed']} {i18n.t('_Confirmed_')} \n {data['global_deaths']} {i18n.t('_Deaths_')}  \n\n{i18n.t('_LatestNewsGlobal_')} www.who.int  \n{i18n.t('_InternationalBreifings_')}  www.who.int/press-briefings \n"""
        return stats
