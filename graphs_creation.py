import pandas as pd
from pytrends.request import TrendReq
import plotly.express as px

pytrends = TrendReq(hl='en-US', tz=360)


def get_relevant_statistics(interest_words_list):
    pytrends.build_payload(interest_words_list, cat=0, timeframe='today 5-y')
    time_data = pytrends.interest_over_time()
    time_data = time_data.reset_index()
    fig = px.line(time_data, x="date", y=interest_words_list, title='The relevance of the searched topic in last 5 years')
    return fig


def get_related_queries(interest_words_list):
    pytrends.build_payload(interest_words_list, cat=0, timeframe='today 5-y')
    related_data = pytrends.related_queries()
    related_data_for_term = {}
    for term in interest_words_list:
        related_data_for_term[term] = related_data[term]['top']
    return related_data
