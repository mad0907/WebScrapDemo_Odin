import http.client

conn = http.client.HTTPSConnection("sunglasshut.in")

payload = ""

headers = {
    'authority': "sunglasshut.in",
    'accept': "application/json, text/plain, */*",
    'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",
    'authorization': "Bearer NjJlYjM3NTM1Zjk2NzkyOWRhY2EwM2UzOkZLX0dnVll3NA==",
    'cookie': "anonymous_id=16d23fa88def47ebafa159c1481a1df5; old_browser_anonymous_id=16d23fa88def47ebafa159c1481a1df5; _gid=GA1.2.679412433.1674355697; _fbp=fb.1.1674355697482.1225472316; _gcl_au=1.1.463804555.1674355698; _ga=GA1.1.2146349363.1674355697; _ga_CG4JSGT7NH=GS1.1.1674355696.1.1.1674355750.0.0.0",
    'referer': "https://sunglasshut.in/collection/versace-sunglasses-for-women?sort_on=latest",
    'sec-ch-ua': "^\^Not_A",
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': "^\^Windows^^",
    'sec-fetch-dest': "empty",
    'sec-fetch-mode': "cors",
    'sec-fetch-site': "same-origin",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    'x-fp-date': "20230122T024921Z",
    'x-fp-sdk-version': "0.1.34",
    'x-fp-signature': "v1.1:768ee3007824c6ece0abc60861eef94d585d4b0905d7b593ac215468fc74b7d9"
    }

conn.request("GET", "/ext/algolia/application/api/v1.0/collections/versace-sunglasses-for-women/items?page_id=%5E%25%5E2A&page_size=12&sort_on=latest", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))