

import datetime
import requests
url = 'https://api.github.com/repos/Zinko17/RestProject/commits'

start = '2021-06-01T00:00:00Z'
end = '2021-06-17T00:00:00Z'

def convertStr(date):
    return datetime.datetime.strptime(date,'%Y-%m-%dT%H:%M:%SZ')


def commits_between(data,start_date,end_date):
    start = convertStr(start_date)
    end = convertStr(end_date)
    for i in data:
        commit_date = convertStr(i['commit']['author']['date'])
        if start<commit_date<end:
            print(i['commit']['message'])

x = requests.get(url).json()
commits_between(x,start,end)


