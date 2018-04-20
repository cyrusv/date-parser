import datetime
from flask import Flask, request

from icalendar import Calendar
from recurrent import RecurringEvent

app = Flask(__name__)


def get_rrule(human_string):
    r = RecurringEvent(now_date=datetime.datetime.now())
    return r.parse(human_string)


@app.route('/', methods=['GET'])
def parse_rrule():
    human_string = request.form['q']
    cal = Calendar()
    cal['RRULE'] = get_rrule(human_string)
    return cal.to_ical()


if __name__ == '__main__':
    app.run()
