from django.db import models

# Create your models here.
class Faq(models.Model):
    question = models.TextField(verbose_name='질문')
    QUES_CATEGORY = (
        (1, '일반'),
        (2, '계정'),
        (3, '기타'),
    )
    ques_category = models.IntegerField(choices=QUES_CATEGORY)
    answer = models.TextField( verbose_name='답변')
    writer = models.CharField(max_length=7, null=True, blank=True, verbose_name='작성자')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='작성일')
    last_updater = models.CharField(max_length=7, null=True, blank=True, verbose_name='최종 수정자')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='최종 수정일')