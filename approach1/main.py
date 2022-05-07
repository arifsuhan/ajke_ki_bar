from bangla import BanglaCalender

def main():
    obj = BanglaCalender("%d-%m-%Y")
    obj.set_date("15-05-2022")
    # obj.get_bangla_month()
    print(obj.getBanglaDate())

    
if __name__ == '__main__':
    main()