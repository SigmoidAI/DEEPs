import requests
import json

url = "https://api.wisecube.ai/orpheus/graphql"


def get_resources(user_search):
    header = {"Content-Type": "application/json",
             "x-api-key": "{access_key}",
             "Authorization": "Bearer {access_token}"}
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
    return resource_dict

