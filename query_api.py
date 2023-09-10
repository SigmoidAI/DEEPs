import requests
import json

url = "https://api.wisecube.ai/orpheus/graphql"


def get_resources(user_search):
    header = {"Content-Type": "application/json",
             "x-api-key": "bPXtTm8CIU3vYqzYKFtYeaql9kFSgXsT5r47MSw5",
             "Authorization": "Bearer eyJraWQiOiJsXC91aDJkVlcwNURDRUlxejhZcmRPcEt0MDVBditMSGluTmlDMEZ0aUloaz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI2YjcxOTdlNy0wYjljLTQ0NmYtOWY0ZS1jMTg4ZTgyMDk2MTEiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0yLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMl9abHJZZXBkd2giLCJjbGllbnRfaWQiOiIxbWJnYWhwNnAzNmlpMWpjODUxb2xxZmhubSIsIm9yaWdpbl9qdGkiOiI0ZTQ4YzYzNy03MmFhLTQ3NjItOWM1NS02ZGJlMmRmOTBmZjciLCJldmVudF9pZCI6IjE1MjQ2NmQ3LWZjZDQtNDAxYS1iM2IzLWNlZDYxZjA1NGQxMSIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2OTQyNzc2NDEsImV4cCI6MTY5NDM2NDA0MSwiaWF0IjoxNjk0Mjc3NjQxLCJqdGkiOiJmMzgwZDkwOS0xYTExLTRiZjAtYWEyNC1kYWViNzRkMzMxYjIiLCJ1c2VybmFtZSI6IjZiNzE5N2U3LTBiOWMtNDQ2Zi05ZjRlLWMxODhlODIwOTYxMSJ9.XkyNF4K3MQKllcXoRN-8i9E-EBj8Xo376tXfruMFHPX7nhjyP7KXDfaVseCrWyS4Wovotk-YpqwlGRr6GqaLxf_XTH9ezuZ8zhoYn3dNzpE-EWpoOYORM_ELgI1DeNAmyxDUGWyTeLyEOdATbDbElPYtSUY7vzQqx-4Odo6K-uHTKirikMtR8sXjE5Qlf8bxTLCmQ6U3jbKmU8Uq82Y86lBZlmkS_wN3WvNVmN_Q-0uxj1ioNox-OA2f3fAnP_s_hylm021XPSWEv6TGZJPyz8ifkHqnZhn-rLGq_t6Cv4FkXbumzejQahDbTiVt50PhyMa6vtbMykALIUsVsZpgOg"}
    query = '{\"query\":\"query questionAnswer($query: String) {\\n  summaryInsights(engineID: \\"23343\\", searchInput: ' \
            '{query: $query, type: [QA]}) {\\n    data {\\n      __typename\\n      ... on QAInsight {\\n        ' \
            'question\\n        answers {\\n          answer\\n          document {\\n            id\\n            ' \
            'title\\n            abs\\n            source\\n            __typename\\n          }\\n          took\\n      ' \
            '    context\\n          probability\\n          __typename\\n        } \\n        __typename\\n      \\n    ' \
            '}} \\n    __typename\\n  } \\n}\",\"variables\":{\"query\":\"user_input\"}}'.replace("user_input",
                                                                                                  user_search)
    payload = json.loads(query)
    response = requests.post(url, headers=header, json=payload).json()
    resources_list = response["data"]["summaryInsights"][0]["data"]["answers"][0]["document"]
    resource_dict = dict()
    for title in resources_list:
        resource_dict[title["title"]] = [("abs", title["abs"]), ("source", title["source"])]
    five_elements = list(resource_dict.items())[:2]
    return five_elements

