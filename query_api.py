import requests
import json

url = "https://api.wisecube.ai/orpheus/graphql"


def get_resources(user_search):
    header = {"Content-Type": "application/json",
             "x-api-key": "bPXtTm8CIU3vYqzYKFtYeaql9kFSgXsT5r47MSw5",
             "Authorization": "Bearer eyJraWQiOiJsXC91aDJkVlcwNURDRUlxejhZcmRPcEt0MDVBditMSGluTmlDMEZ0aUloaz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIzMDY0YzM1My03ODFmLTQ0OGEtYTIyZS02OTE1YjkxNmY4OGMiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0yLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMl9abHJZZXBkd2giLCJjbGllbnRfaWQiOiIxbWJnYWhwNnAzNmlpMWpjODUxb2xxZmhubSIsIm9yaWdpbl9qdGkiOiI4ZmJhNzkzMC0yMGZhLTQyYTMtYTMxNS0zNzkzOWRmZmFhNWQiLCJldmVudF9pZCI6ImE3MzJlYTM4LWFlNWQtNGFkYy1iNDUzLTlkY2I2NTAzZTdkZSIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2OTQyODcyNTQsImV4cCI6MTY5NDM3MzY1NCwiaWF0IjoxNjk0Mjg3MjU0LCJqdGkiOiJkYjNmYTljNC1hMWMxLTQ1OTctOTkxNS0yNGIyOGU3YzkyMTAiLCJ1c2VybmFtZSI6IjMwNjRjMzUzLTc4MWYtNDQ4YS1hMjJlLTY5MTViOTE2Zjg4YyJ9.GpkfeM02lPy00JQUOEza-6egjHqgTyFzan6gUwfkHnSRTYjHWIc6vQCOXGTqh1Ec8odcW1QgTqJxJBL-jgX-FqC4qG46VhpcA7nJXgZYX8dcwIhDDxi6WfBpJFz5F6aybQ4Oh9ZoWr-BtonNt51ecUNrxbdiLc6Q4gG-63R8m14AmkqTRnQD-mCYKn7gC8W3G7BCioEzt4tsxMbdUWr6_XICrFu9MtAS8afQiKH7g7rWSrcQbfviE4VYtM1NdeTDcx9O4lQMkt-YBze7qKorFG_wU2Z4w3jFfAmijLCXhxN8hsyW58lyumFaJxIdLEJ5mRV6H0sfH1eoLPEQ0el63Q"}
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
    sources = [resources_list[i]["source"] for i in range(0, len(resources_list) - 1)]
    return sources

