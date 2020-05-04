from wc_kernel import single_page_proc
from url import generate_search_url_wechat

url = generate_search_url_wechat('动物森友',1,2)
single_page_proc(url)