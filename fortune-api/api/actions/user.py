from db.dals import UserDAL


async def _get_users_by_group_name(group_name):
    user_dal = UserDAL()
    return await user_dal.get_user_list_by_group_name(group_name)
