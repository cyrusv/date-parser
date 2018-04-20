import unittest

import promise
from promise import get_rrule


class FlaskRouteTestCase(unittest.TestCase):

    def setUp(self):
        promise.app.testing = True
        self.app = promise.app.test_client()

    def test_nlp(self):
        self.assertEqual(
            get_rrule('every weekday'),
            'RRULE:BYDAY=MO,TU,WE,TH,FR;INTERVAL=1;FREQ=WEEKLY'
        )

        self.assertEqual(
            get_rrule('every weekend'),
            'RRULE:BYDAY=SA,SU;INTERVAL=1;FREQ=WEEKLY'
        )

        self.assertEqual(
            get_rrule('every weekday at 5pm'),
            'RRULE:BYMINUTE=0;BYDAY=MO,TU,WE,TH,FR;'
            'BYHOUR=17;FREQ=WEEKLY;INTERVAL=1'
        )

        self.assertEqual(
            get_rrule('every week on Monday and Wednesday at 5pm'),
            'RRULE:BYMINUTE=0;BYDAY=MO,WE;BYHOUR=17;FREQ=WEEKLY;INTERVAL=1'
        )

        self.assertEqual(
            get_rrule('every week on Monday and Wednesday at 5pm until 6/1'),
            'RRULE:BYDAY=MO,WE;BYMINUTE=0;INTERVAL=1;'
            'FREQ=WEEKLY;BYHOUR=17;UNTIL=20180601'
        )

        self.assertRaises(ValueError, get_rrule('Potato'))

    def test_route(self):
        rv = self.app.get('/', data=dict(
            q='every monday',
        ))
        self.assertEqual(
            rv.data,
            'BEGIN:VCALENDAR\r\nRRULE:RRULE:BYDAY=MO\\;'
            'INTERVAL=1\\;FREQ=WEEKLY\r\nEND:VCALENDAR\r\n'
        )


if __name__ == '__main__':
    unittest.main()
