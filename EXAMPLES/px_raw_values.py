import openpyxl as px

def main():
    wb = px.load_workbook('../DATA/presidents.xlsx')
    ws = wb['US Presidents']  # get active sheet
    headers = next(ws.values)   # read first row from iterator
    for row in ws.values:  # loop over rows in iterator
        print(row[:5])   # print first 5 elements of row tuple


if __name__ == '__main__':
    main()
