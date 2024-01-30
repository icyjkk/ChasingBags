import requests
import time

if __name__ == "__main__":

    while True:
        cookies = {
            '__dcfduid': 'f94db8a28aa111eea1b296f93731ed84',
            '__sdcfduid': 'f94db8a28aa111eea1b296f93731ed8409edc4a503b32e4ad0d28d61d9935108551a8ad29258179194a527bed0d9b115',
            '_ga_XXP2R74F46': 'GS1.2.1704139559.1.0.1704139559.0.0.0',
            '_ga': 'GA1.1.1342412728.1702897833',
            '_ga_YL03HBJY7E': 'GS1.1.1705623550.2.0.1705624139.0.0.0',
            '__cfruid': 'dec63482cf73855ddfab92353afe96d76743736d-1706535383',
            '_cfuvid': 'l5Ci26U73znMczS7PO044GD5QztlRbJHZ5k7oAV96Mo-1706535383911-0-604800000',
            'cf_clearance': 'o5QfcP0HOi8vTr2hxi8CTTCCmbccLjVDMrs_qqdrvMk-1706535384-1-AU3MzW9m9hXTlOJSCS4hGH/fop+50J526AjFDVi4DZaSA97vIaS24D6IdNuRXiVocFjRC2/r1S42Dd53Ryd3sm4=',
            'locale': 'es-ES',
            'OptanonConsent': 'isIABGlobal=false&datestamp=Mon+Jan+29+2024+14%3A53%3A19+GMT%2B0100+(hora+est%C3%A1ndar+de+Europa+central)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0',
        }

        headers = {
            'authority': 'discord.com',
            'accept': '*/*',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'authorization': 'NDgxNjAyNjAzODU2NDI5MDc2.GhGYoM.T5CwibNn-LQ6Exp42lzNNzsK_YcVPUcMGOxSi8',
            # 'cookie': '__dcfduid=f94db8a28aa111eea1b296f93731ed84; __sdcfduid=f94db8a28aa111eea1b296f93731ed8409edc4a503b32e4ad0d28d61d9935108551a8ad29258179194a527bed0d9b115; _ga_XXP2R74F46=GS1.2.1704139559.1.0.1704139559.0.0.0; _ga=GA1.1.1342412728.1702897833; _ga_YL03HBJY7E=GS1.1.1705623550.2.0.1705624139.0.0.0; __cfruid=dec63482cf73855ddfab92353afe96d76743736d-1706535383; _cfuvid=l5Ci26U73znMczS7PO044GD5QztlRbJHZ5k7oAV96Mo-1706535383911-0-604800000; cf_clearance=o5QfcP0HOi8vTr2hxi8CTTCCmbccLjVDMrs_qqdrvMk-1706535384-1-AU3MzW9m9hXTlOJSCS4hGH/fop+50J526AjFDVi4DZaSA97vIaS24D6IdNuRXiVocFjRC2/r1S42Dd53Ryd3sm4=; locale=es-ES; OptanonConsent=isIABGlobal=false&datestamp=Mon+Jan+29+2024+14%3A53%3A19+GMT%2B0100+(hora+est%C3%A1ndar+de+Europa+central)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0',
            'referer': 'https://discord.com/channels/1178718307000528976/1178718307453505638',
            'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'es-ES',
            'x-discord-timezone': 'Europe/Madrid',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVzLUVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTIxLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3QuY28vZDBMR3FBZUhMdyIsInJlZmVycmluZ19kb21haW4iOiJ0LmNvIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50Ijoid3d3Lmdvb2dsZS5jb20iLCJzZWFyY2hfZW5naW5lX2N1cnJlbnQiOiJnb29nbGUiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyNjE5NzMsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
        }

        params = {
            'limit': '1',
        }

        response = requests.get(
            'https://discord.com/api/v9/channels/1191855182959628359/messages',
            params=params,
            cookies=cookies,
            headers=headers,
        )

        print(response.text)

        if '38143' in response.text:
            print("true")
            requests.post('https://discord.com/api/webhooks/1191856297226801223/zLqo9gAq7GK8dNZgLaIC5WFA6jstGeDF7SQyw1vugDpmfJtwPmSfF2buiVdQF4cbPxYJ', headers={'Content-Type': 'application/json'}, json={"content": "@here"})

        time.sleep(1)
