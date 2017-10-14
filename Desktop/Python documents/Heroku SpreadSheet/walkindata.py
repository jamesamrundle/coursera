import openpyxl, os
from openpyxl import load_workbook

os.chdir('/home/jamesrundle/anaconda3/envs/invdata')

wb = load_workbook('./drwalkin.xlsx')

sheet = wb.get_sheet_by_name('Sheet1')
