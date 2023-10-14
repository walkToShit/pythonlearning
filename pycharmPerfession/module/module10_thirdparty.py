import requests

response = requests.get(
    'https://ai.deepshare.net/detail/v_5fa11a8de4b01f764d8871bd/3?from=p_5e3ccc2937a30_YeCUNZHT&type=6')

print((response.content.decode('utf-8')))
print((response.text))  # 此种方式看文本  会有乱码 或者是二进制流
