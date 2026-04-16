import pandas as pd

crash = pd.read_excel('dataset/nsw_road_crash_data_2020-2024_crash.xlsx')
tu = pd.read_excel('dataset/nsw_road_crash_data_2020-2024_traffic_unit.xlsx')

merged = pd.merge(tu, crash, on='Crash ID', how='left')

merged.to_excel('dataset/nsw_road_crash_merged.xlsx', index=False)
print('Done:', merged.shape)
