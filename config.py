import os
import ProxyCloud

BOT_TOKEN =  os.environ.get('bot_token','5867281966:AAEfBMW4rj8J1g5e8AvqM2RVIVouHD0iYqU')
API_ID =  os.environ.get('api_id','12569968')
API_HASH = os.environ.get('api_hash','2d5b54d8745cab19f3bf12cfd77c4897')
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('killerj00','geoge0x0').split(';')
PROXY = ProxyCloud.parse(os.environ.get('proxy_enc','proxy socks5://KFDDKDYEJIJFGFYDJEGKGJYEIJIIRDGELGGJKG'))

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')
