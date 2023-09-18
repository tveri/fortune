from api.schemas import ShowUser


class UserDAL:
    async def get_user_list_by_group_name(self, group_name) -> list[ShowUser]:
        l = [{'full_name': 'Курочкин Иван'}, {'full_name': 'Батакова Екатерина'}, {'full_name': 'Титов Владимир'}, {'full_name': 'Шабанов Иван'}, {'full_name': 'Хохулин Александр'}, {'full_name': 'Хохулин Виктор'}, {'full_name': 'Суслов Андрей'}, {'full_name': 'Юрченко Иван'}, {'full_name': 'Козикова Александра'}, {'full_name': 'Корсаков Кирилл'}]
        return l