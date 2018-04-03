import time
from googleads.errors import GoogleAdsError
from googleads.oauth2 import GoogleRefreshTokenClient
from googleads import adwords
from demo import VERSION

class APIHandler(object):
      """Handler for the AdWords API using the Ads Python Client Libraries."""

      # The user-agent sent in requests from this demo.
      _USER_AGENT = 'AppEngine Googleads Demo v%s' % VERSION

      def __init__(self, client_id, client_secret, refresh_token):

        credentials = GoogleRefreshTokenClient(client_id, client_secret,
                                               refresh_token)
        self.client = adwords.AdWordsClient.LoadFromStorage('googleads.yaml')

      def GetCampaigns(self, client_customer_id):
            """Returns a client account's Campaigns that haven't been removed.
            Args:
              client_customer_id: str Client Customer Id used to retrieve Campaigns.
            Returns:
              list List of Campaign data objects.
            """
            self.client.SetClientCustomerId(client_customer_id)
            # A somewhat hackish workaround for "The read operation timed out" error,
            # which could be triggered on AppEngine's end if the request is too large
            # and is taking too long.
            max_tries = 3
            today = time.strftime('%Y%m%d', time.localtime())
            for i in xrange(1, max_tries + 1):
                try:
                    selector = {
                        'fields': ['Id', 'Name', 'Status', 'BudgetId', 'Amount'],
                        'predicates': [
                            {
                                'field': 'Status',
                                'operator': 'NOT_EQUALS',
                                'values': ['REMOVED']
                            }
                        ],
                        'dateRange': {
                            'min': today,
                            'max': today
                        }
                    }
                    campaigns = self.client.GetService('CampaignService').get(selector)
                    if int(campaigns['totalNumEntries']) > 0:
                        return campaigns['entries']
                    else:
                        return None
                except Exception, e:
                    if i == max_tries:
                        raise GoogleAdsError(e)
                    continue
