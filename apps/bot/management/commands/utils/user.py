from apps.bot.models import User as BUser


class User:

    @staticmethod
    def get_user(user_id):
        try:
            return BUser.objects.get(user_id=user_id)
        except:
            return None
