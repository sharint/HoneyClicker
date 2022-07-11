import requests

cookies = {
    '_gcl_au': '1.1.1914525257.1655871962',
    '_hjSessionUser_3019470': 'eyJpZCI6IjYxNGZkM2QzLTUyNGQtNTM2Mi05YzBmLTMzYmExY2Q4YzNhOSIsImNyZWF0ZWQiOjE2NTU4NzE5NjE5MzgsImV4aXN0aW5nIjp0cnVlfQ==',
    '_gid': 'GA1.2.1846637909.1656961854',
    '_hjIncludedInSessionSample': '1',
    '_hjSession_3019470': 'eyJpZCI6Ijg5OWU2NDE1LTE0MGMtNDEwZC05Y2RlLWJmOGM3YmJlMjZlZSIsImNyZWF0ZWQiOjE2NTcxMDM4MDcxODQsImluU2FtcGxlIjp0cnVlfQ==',
    '_hjIncludedInPageviewSample': '1',
    '_hjAbsoluteSessionInProgress': '0',
    '_ga': 'GA1.2.262697600.1655871963',
    '_dc_gtm_UA-214302361-1': '1',
    '__cf_bm': 'DtXe9xmP5SzgTgcnNKlAbkKcHnWDB2pLnQfEdRGXW5k-1657105898-0-AfVgCXOoc61We66/3qWzrNDXtO5A7/9PAbfwXrfxUCj0N0Ej7YmJV6BpCz5U12sE8ag54JDOkPOxxEHJuReAsbSS2lIFf+UfBb2cvwXeGNt7Z9EIU0fi5Igu9g/W5AaCFw==',
    '_gali': 'unity-canvas-1',
    '_ga_YBK8P76EKN': 'GS1.1.1657103807.42.1.1657105932.60',
}

headers = {
    'authority': 'honeywood.io',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_gcl_au=1.1.1914525257.1655871962; _hjSessionUser_3019470=eyJpZCI6IjYxNGZkM2QzLTUyNGQtNTM2Mi05YzBmLTMzYmExY2Q4YzNhOSIsImNyZWF0ZWQiOjE2NTU4NzE5NjE5MzgsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.1846637909.1656961854; _hjIncludedInSessionSample=1; _hjSession_3019470=eyJpZCI6Ijg5OWU2NDE1LTE0MGMtNDEwZC05Y2RlLWJmOGM3YmJlMjZlZSIsImNyZWF0ZWQiOjE2NTcxMDM4MDcxODQsImluU2FtcGxlIjp0cnVlfQ==; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0; _ga=GA1.2.262697600.1655871963; _dc_gtm_UA-214302361-1=1; __cf_bm=DtXe9xmP5SzgTgcnNKlAbkKcHnWDB2pLnQfEdRGXW5k-1657105898-0-AfVgCXOoc61We66/3qWzrNDXtO5A7/9PAbfwXrfxUCj0N0Ej7YmJV6BpCz5U12sE8ag54JDOkPOxxEHJuReAsbSS2lIFf+UfBb2cvwXeGNt7Z9EIU0fi5Igu9g/W5AaCFw==; _gali=unity-canvas-1; _ga_YBK8P76EKN=GS1.1.1657103807.42.1.1657105932.60',
    'referer': 'https://honeywood.io/game',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

response = requests.get('https://honeywood.io/api/match3/bears1c8cx6hpf6v9u7kcq3wksjnp0cjpnl706vwmle7/stats', cookies=cookies, headers=headers)
print(response.json())
