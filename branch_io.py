import requests
import json
import logging, traceback, sys
log = logging.getLogger("django")
##
# Generate branch.io deeplink
# @params: param_1 <integer> <any number you want to send as custom object>
# @params: param_2 <string> <any string you want to send as custom object>
##
def create_deep_link(param_1, param_2):
    try:
        headers = {
            "Content-Type": "application/json",
        }
        
        data = """{"branch_key": "key_live_XXXXXXXXXXXXXXXX",
                "channel": "Abhishek",
                "feature": "promotion",
                "campaign": "referral",
                "stage": "new user",
                "data": {
                        "$canonical_identifier": "content/123",
                        "$og_title": "Title from Deep Link(to show on sharing url)",
                        "$og_description": "Description from Deep Link(to show on sharing url).",
                        "$og_image_url": "http://lorempixel.com/400/400/",
                        "$desktop_url": "http://yoursiteurl.com",
                        "custom_object": { "param_1": """ + str(param_1) + """, "param_2": \""""+ param_2 +"""\" }
                }
            }"""
        
        response = requests.request("POST",'https://api2.branch.io/v1/url', headers=headers, data=data)
        if type(response.text) == str:
            response = json.loads(response.text)
        

        if response.get('error', None):
            #{"error":{"code":400,"message":"Invalid JSON"}}
            #print(response.get('error'))
            log.error('Referral | Branch.io generate deeplink log#1', exc_info=True, extra={'response': response})
            return False, ""

        if response.get('url', None):
            # success
            return True, response.get('url')
        else:
            log.error('Referral | Branch.io generate deeplink log#2', exc_info=True, extra={'response': response})
            return False, ""
    except Exception as e:
        #print(e)
        log.error('Referral | exception log#3', exc_info=True, extra={'exception': e})
        return False, ""
