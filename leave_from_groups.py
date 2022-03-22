"""
выход из всех сообществ и групп, в которых вы не являетесь кем-либо, кроме участника
"""
from Vk import Vk

if __name__ == "__main__":
    token = ""
    vk = Vk(token)
    admins_id = vk.get_all_groups(filter="admin, editor, moder, events, advertiser")
    all_groups_id = vk.get_all_groups()
    [all_groups_id.remove(_id) for _id in admins_id]
    [vk.method("groups.leave", group_id=group_id) for group_id in all_groups_id]
