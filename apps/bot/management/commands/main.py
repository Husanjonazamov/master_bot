from django.core.management import BaseCommand

from .bot import bot


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        import apps.bot.management.commands.handlers

        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling()
