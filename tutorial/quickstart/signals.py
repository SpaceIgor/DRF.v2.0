from django.db.models.signals import pre_save, pre_delete
from models import Post, Comment
from django.dispatch import receiver
import re
from profanity_filter import ProfanityFilter


@receiver(pre_save, sender=Post)
def delete_spec_symbol(sender, instance, **kwargs):
    """ This func  delete spec_symbol in model Post for title
     title == post_text """

    instance.post_text = re.sub(r'[^A-Za-zА-Яа-я0-9!?-]', ' ', instance.post_text)


@receiver(pre_save, sender=Comment)
def correct_comment(sender, instance, **kwargs):
    """ This func checks comment on bad world for EN language
    For Multilingual analysis using:
    pf = ProfanityFilter(languages=['ru', 'en'])
    """
    pf = ProfanityFilter()

    instance.text = pf.censor(instance.text)


@receiver(pre_delete, sender=Comment)
def cancel_comment(sender, instance, **kwargs):
    """This signal prohibits the deletion of the comment"""

    if instance:
        raise TypeError(f"Don't delete comment: {instance.text} for post: {instance.post_text}")













