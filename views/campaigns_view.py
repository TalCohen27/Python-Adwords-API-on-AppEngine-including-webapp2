import os
import webapp2
import get_campaigns
import jinja2
import logging
from googleads import adwords
from handlers.api_handler import APIHandler
import yaml
import json

logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.transport').setLevel(logging.DEBUG)

PAGE_SIZE = 100

class GetAllCampaigns(webapp2.RequestHandler):

    def get(self):

        adwords_client = adwords.AdWordsClient.LoadFromStorage('googleads.yaml')
        path = os.path.join(os.path.dirname(__file__), '../googleads.yaml')
        stream = open(path, 'r')
        authTokens = yaml.load(stream)

        client_customer_id = authTokens.get('adwords').get('client_customer_id')
        client_id = authTokens.get('adwords').get('client_id')
        developer_token = authTokens.get('adwords').get('developer_token')
        client_secret = authTokens.get('adwords').get('client_secret')
        data = []

        try:
            try:
                # Load Client instance.
                handler = APIHandler(client_id,
                                     client_secret,
                                     developer_token)

                campaigns = handler.GetCampaigns(client_customer_id)

                for campaign in campaigns:
                    data.append(campaign.name)

            except Exception, e:
               data.append(str(e))
        finally:
            self.response.headers['Content-Type'] = 'application/json'
            self.response.out.write(json.dumps(data))



