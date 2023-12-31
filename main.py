import datetime
import time

from dateutil.relativedelta import relativedelta
import weekdays
import http_request


def main():
    start_date = datetime.date.today()
    end_date = start_date + relativedelta(weeks=2)

    dates = weekdays.get_fridays_and_saturdays(start_date, end_date)

    request = http_request.generate_request(dates)

    print(request)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed Time: {:.2f} seconds".format(elapsed_time))
