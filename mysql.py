import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
    "Cookie": "ptcz=ed603fb287360f2101fc8dec7dd5459a02d35dc7034dddaae0a334e284432af1; pgv_pvid=5365889883; RK=GTeZ/mg6/6; _clck=102h2hg|1|fuc|0; qq_domain_video_guid_verify=30b4f490eeefb839; _qimei_uuid42=1931e15342c100084d0a04ff7ea3128989cf16f374; _qimei_fingerprint=b8694ad705a59b8e43f025de8db604b5; video_platform=2; video_guid=30b4f490eeefb839; _qimei_q36=; _qimei_h38=f74bac094d0a04ff7ea312890200000a51931e; check_16=e7ef0d7dc4aefcac4edc11ffa7963c1d; pgv_info=ssid=s2498362800",  # Cookie
}

url = "https://pbaccess.video.qq.com/trpc.universal_backend_service.page_server_rpc.PageServer/GetPageData?"

params = {
    'video_appid': '1000005',
    'vplatform': '2',
    'vversion_name': '8.9.10',
    'new_mark_label_enabled': '1'
}

# 请求数据
data ={"page_params":{"channel_id":"100119","filter_params":"sort=75","page_type":"channel_operation","page_id":"channel_list_second_page"},"page_context":{"view_ad_ssp_mg_ctx_version":"1","view_ad_ssp_mgv2_ad_count_send":"0","view_ad_ssp_cards_consumed":"0","view_ad_ssp_mg_ad_count_send":"0","data_src_647bd63b21ef4b64b50fe65201d89c6e_data_version":"","view_ad_ssp_mg_remaining":"0","view_ad_ssp_ctx_version":"1","view_ad_ssp_mgv2_remaining":"0","view_ad_ssp_flush_num":"1","view_ad_ssp_mgv2_ctx_version":"1","sdk_page_ctx":"{\"page_offset\":1,\"page_size\":2,\"used_module_num\":2}","data_src_647bd63b21ef4b64b50fe65201d89c6e_page":"1","view_ad_ssp_remaining":"0","view_ad_ssp_mg_cards_consumed":"0","view_ad_ssp_mg_flush_num":"1","view_ad_ssp_mgv2_flush_num":"1","page_index":"1","view_ad_ssp_ad_count_send":"0","view_ad_ssp_mgv2_cards_consumed":"0"}}
#post请求
response = requests.post(url=url,params=params,headers=headers,data=data)

# 获取json数据
json_data = response.json()
print(json_data)
