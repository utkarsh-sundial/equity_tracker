import pandas as pd
import yfinance as yf

# resources:
# 1. https://analyticsindiamag.com/hands-on-guide-to-using-yfinance-api-in-python/

company_name = yf.Ticker('PFE')
a = company_name.info

company_info = pd.DataFrame(company_name.info.items(), columns = ['parameter', 'value'])

# function to get historical OHCL
company_historical_data = company_name.history(start = '2015-01-01', end = '2021-07-17')

# function to get info on dividends and splits
company_actions = company_name.actions

# function to get company sustainability (not very relevant)
company_sustainability = company_name.sustainability

# function to fetch recommendations
company_recommendations = company_name.recommendations

# function to know about the company's earnings and revenue
company_calendar = company_name.calendar

