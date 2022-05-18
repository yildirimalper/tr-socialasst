# wbdata_collection.py script was run and Turkish economic data was thrived from World Bank Database in June 2021

import wbdata
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt

# Scraping Data using WB API for "Average Per Capita Transfer - All Social Assistance"
turkey = [i['id'] for i in wbdata.get_country(country_id=("TUR"))]
assistance = {"per_sa_allsa.avt_pop_tot": "Avg per Capita Transfer", 
              "per_sa_allsa.avt_q1_tot": "1st quintile",
              "per_sa_allsa.avt_q2_tot": "2nd quantile",
              "per_sa_allsa.avt_q3_tot": "3rd quantile",
              "per_sa_allsa.avt_q4_tot": "4th quantile",
              "per_sa_allsa.avt_q5_tot": "5th quantile"
             }

social_asst = wbdata.get_dataframe(assistance, country=turkey, convert_date=True)
social_asst.dropna(inplace=True)

# Line Plot Visualization for "Average Per Capita Transfer - All Social Assistance"
ax = social_asst.plot(figsize=(10,6), xlabel="Years", ylabel="Average Per Capita Transfer", title="Average Per Capita Transfer - All Social Assistance")
plt.legend()
plt.savefig("avgpercaptransfer.png")
plt.show()

# ------------------------------------------------------------------------------------

# Scraping Data for "Coverage (%) - All Social Assistance"
turkey = [i['id'] for i in wbdata.get_country(country_id=("TUR"))]
cvrg_asst = {"per_sa_allsa.cov_pop_preT_tot": "All Social Assistance", 
             "per_sa_allsa.cov_pop_rur": "Rural Areas",
             "per_sa_allsa.cov_pop_urb": "Urban Areas"
            }

cvrg_asst_df = wbdata.get_dataframe(cvrg_asst, country=turkey, convert_date=True)
cvrg_asst_df.dropna(inplace=True)

# Line Plot Visualization for "Coverage (%) - All Social Assistance"
ax = cvrg_asst_df.plot(figsize=(10,6), xlabel="Years", ylabel="Coverage (%)", title="Coverage (%) - All Social Assistance")
plt.legend()
plt.savefig("cvrg_asst.png")
plt.show()

# ------------------------------------------------------------------------------------

# Scraping Data for "Coverage of Social Pensions"
turkey = [i['id'] for i in wbdata.get_country(country_id=("TUR"))]
pensions = {"per_sa_sp.cov_pop_tot": "Coverage (%) - Social Pensions", 
            "per_sa_sp.adq_q1_tot": "1st quintile",
            "per_sa_sp.adq_q2_tot": "2nd quantile",
            "per_sa_sp.adq_q3_tot": "3rd quantile",
            "per_sa_sp.adq_q4_tot": "4th quantile",
            "per_sa_sp.adq_q5_tot": "5th quantile"
            }

pension_df = wbdata.get_dataframe(assistance, country=turkey, convert_date=True)
pension_df.dropna(inplace=True)

# Line Plot Visualization for "Coverage of Social Pensions"
ax = pension_df.plot(figsize=(10,6), xlabel="Years", ylabel="Coverage (%)", title="Coverage of Social Pensions (%)")
plt.legend()
plt.savefig("pensioncoverage.png")
plt.show()