import time

from contextlib import contextmanager

from apiclient import discovery


class Api(object):

    discovery_url = 'https://sheets.googleapis.com/$discovery/rest?version=v4'

    http = None
    spreadsheet_id = None
    service = None

    queue_actions = None
    queue_values = None

    last_action = None


    def __init__(self, http, spreadsheet_id):
        self.http = http
        self.spreadsheet_id = spreadsheet_id
        self.service = discovery.build('sheets', 'v4', http=self.http, discoveryServiceUrl=self.discovery_url)

        self.queue_actions = []
        self.queue_values = []


    @contextmanager
    def action_set(self):
        yield
        self.flush()


    def add_action(self, name, properties):
        self.queue_actions.append({ name: properties})

    def add_values(self, values):
        self.queue_values.append(values)

    def flush(self):
        # Values first, so that formatting (eg auto-resize) is applied to up-to-date data.
        self._flush_values()
        self._flush_actions()

    def _flush_actions(self):
        if self.queue_actions:
            print("== Execute: %s" % [list(action.keys())[0] for action in self.queue_actions])

            data = {'requests': self.queue_actions}

            self.rate_limit()

            result = self.service.spreadsheets() \
                         .batchUpdate(spreadsheetId=self.spreadsheet_id, body=data) \
                         .execute()

        self.queue_actions = []

    def _flush_values(self):
        if self.queue_values:
            # Sample:
            #   {'data': [{'range': 'r1714 replicas!S2:U2', 'values': [['mgmt', 'sea5r1', 'tuk5r1']], 'majorDimension': 'ROWS'}],
            #    'includeValuesInResponse': False,
            #    'valueInputOption': 'RAW'}
            print("== Data: Updating values... %r" % [len(values) for datum in self.queue_values for values in datum.get('values',[])])

            data = {
                'valueInputOption': 'RAW',
                'data': self.queue_values,
                'includeValuesInResponse': False,
            }

            self.rate_limit()

            result = self.service.spreadsheets().values() \
                         .batchUpdate(spreadsheetId=self.spreadsheet_id, body=data) \
                         .execute()

        self.queue_values = []


    def rate_limit(self):
        # https://developers.google.com/analytics/devguides/config/mgmt/v3/limits-quotas
        # Default: 100 requests per 100 seconds per user
        if self.last_action:
            num_requests = 100
            num_seconds = 100
            min_interval = float(num_seconds) / float(num_requests)
            cur_interval = time.time() - self.last_action
            if cur_interval < min_interval:
                delay = min_interval - cur_interval
                print("== Throttle: %r" % delay)
                time.sleep(delay)

        self.last_action = time.time()

