import numpy as np
import pandas as pd

data_2013 = pd.read_excel("./oesm13nat/national_M2013_dl.xls")
data_2019 = pd.read_excel("./oesm19nat/national_M2019_dl.xlsx")

total_employment_2013 = 116310000
total_employment_2019 = 130600000

probability99 = ["41-9041", "23-2093", "51-6051", "15-2091", "13-2053", "49-9064", "43-5011", "13-2082", "51-9151", "43-4141", "25-4031", "43-9021"]
probability98 = probability99 + ["51-2093", "43-9041", "43-4011", "43-4151", "13-2072", "13-1032", "27-2023", "43-3071", "51-9194", "51-9111", "43-3061", "43-5071", "51-4035", "13-2041", "41-2022", "13-1031", "53-3031", "27-4013", "43-6012", "43-3031", "51-9061", "41-9012"] #TODO
probability95 = probability98 + [] #TODO

#for total_employment, employment_data in zip([total_employment_2013, total_employment_2019], [data_2013, data_2019]):
emp_sum = 0
for code in probability98:
    row = data_2013.loc[data_2013['OCC_CODE'] == code]
    emp_sum += list(row.to_dict()['TOT_EMP'].values())[0]

print(emp_sum / total_employment_2013)

emp_sum = 0
for code in probability98:
    row = data_2019.loc[data_2019['occ_code'] == code]
    if row.empty:
        emp_sum += 0
        print("Occupation not found: " + code)
    else:
        emp_sum += list(row.to_dict()['tot_emp'].values())[0]

print(emp_sum / total_employment_2019)