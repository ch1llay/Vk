import requests


class Vk:
    def __init__(self, token):
        self.base_url = f"https://api.vk.com/method/%s?v=5.131&access_token={token}"
        self.user_id = self.method("users.get")["response"][0]["id"]

    def method(self, method_name, **params) -> dict:
        return requests.get(self.base_url % method_name, params=params).json()

    def get_all_groups(self, **kwargs) -> list:
        return self.method("groups.get", user_id=self.user_id, **kwargs)["response"]["items"]
