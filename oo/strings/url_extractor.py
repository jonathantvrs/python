class URLExtractor:
    def __init__(self, url):
        self.__url = self.__sanitize_url(url)
        self.__validate_url()

    def __sanitize_url(self, url):
        return url.strip()

    def __validate_url(self):
        if self.__url == '':
            raise ValueError('The url is empty!')

    def get_base_url(self):
        question_mark_index = self.__url.find('?')
        base_url = self.__url[:question_mark_index]

        return base_url

    def get_params_url(self):
        question_mark_index = self.__url.find('?')
        params_url = self.__url[question_mark_index + 1:]

        return params_url

    def get_param_value(self, param_name):
        param_index = self.get_params_url().find(param_name)
        value_index = param_index + len(param_name) + 1
        e_commercial_index = self.get_params_url().find('&', value_index)

        if e_commercial_index == -1:
            value = self.get_params_url()[value_index:]
        else:
            value = self.get_params_url()[value_index:e_commercial_index]

        return value