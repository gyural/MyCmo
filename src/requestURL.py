def getURL(page=1):
    return ("https://api.whatads.co.kr/public/monitoring/display-ads"
             "?ad_type_code=DA&media_code=ALL&business_category_code=ALL&device_type_code=ALL&ad_product_cost=ALL"
             f"&page_num={page}&use_paging=true&row_num=20")

