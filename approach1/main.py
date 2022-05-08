from bangla import BanglaCalender

def main():
    obj = BanglaCalender("%d-%m-%Y")
    obj.set_date("13-04-2022")
    # obj.set_date("16-12-2022")
    # obj.set_date("17-10-2022")
    # obj.get_bangla_month()
    print(obj.getBanglaDate())

    
if __name__ == '__main__':
    main()