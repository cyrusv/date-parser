### Plain text calendar creation

To install:

```pip install requirements.txt```

To run the server:

```python promise.py```

To unit-test the server:

```python test.py```

To run a client:

```python client.py "every weekday"```
Note, this just does a GET request on localhost:5000 with GET form data `q: every weekday`



####Assignment:
Create an API for transforming natural language recurring date expressions into
the equivalent calendar format.
The API should accept recurring meeting time expressions in at least three formats:

1. "every weekday"
2. "every weekday at 5pm"
3. "every week on Monday and Wednesday at 5pm"
4. "every week on Monday and Wednesday at 5pm until 6/1"

And it should return either:
* the expression converted to a RRULE or RRULESET (see the iCalendar RFC),
embedded in a plain-text (i/v)calendar format
* an expanded, plain-text list of event start times in some human readable
format (e.g. "2015-03-26 18:00:00"), one per line, subject to some reasonable limit

Additional details for the API
* when provided, event start times will always be in the form "at <time-format>”
* similarly, end dates for the recurrence will be in the form "until <date-format>".
* when an "at" time is provided, it is at the end of string, unless an "until" is included, which would then conclude the expression.
* the start for the recurrence can be assumed to be the date of submission or the clock time of the first event, where provided
* timezones can be ignored or fixed to an arbitrary selection

Solutions & Scoping:
* To get a sense of the scope of work and what libraries would be appropriate,
 please don't expect to spend more than 3 hours at this.
* Please use any open-source libraries that you wish but do not call
external APIs that you have not created.
* Please provide your documented code for the service & a small sample
client, along with instructions for installing and running them locally in a Linux/Mac OS X environment
- an IP-based service API and client. The protocol is up to you, just explain how it works
- any combination of open source libraries you want to use to meet the requirements is fine. Again, just don’t use a commercial or external API. I should be able to setup and run your solution on a box with only local loop networking.

Not required but interesting:
* Extend the API to also accept a RRULE/RRULESET expression and return that rule expressed in natural language
