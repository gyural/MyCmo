from data_patch import get_crawl_data

def get_banner_img(page=1):
    data = get_crawl_data(page)
    ad_list = data['list']
    img_list = []
    for idx, ad_info in enumerate(ad_list):
        img_url =ad_info['description']['creative_list'][0]['banner_uri']
        img_txt =ad_info['description']['creative_list'][0]['alternative_text']
        img_list.append([img_url, f'page:{page}-{idx}'])

    return img_list

if __name__ == '__main__':
    print(get_banner_img())