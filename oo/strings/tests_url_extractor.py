from url_extractor import URLExtractor


url = URLExtractor('https://google.com/search?q=python&sId=1233423123')

print(url.get_base_url())
print(url.get_params_url())
print(url.get_param_value('q'))
print(url.get_param_value('sId'))