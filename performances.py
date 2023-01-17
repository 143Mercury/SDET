import requests
import time  # в случае задержки использовать time.sleep(x) - Либо режим неявных ожиданий

url = "https://www.votpusk.ru/"

num_requests = 100

concurrent_requests = 10

responses = []

for i in range(0, num_requests, concurrent_requests):

    session = requests.Session()

    reqs = [session.get(url) for _ in range(concurrent_requests)]

    for req in reqs:
        responses.append(req.text)

# Вывести ответы
for response in responses:
    print(response)
