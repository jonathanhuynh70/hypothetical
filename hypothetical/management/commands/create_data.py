from django.core.management.base import BaseCommand, CommandError
from hypothetical.models import Question, User, Comments, Choice, Vote 
from datetime import datetime
import random

class Command(BaseCommand):
    help = "Creates dummy data for the hypothetical models"

    def handle(self, *args, **options):
        jonathan = User.objects.create(name="Jonathan Huynh")
        for _ in range(6):
            Question.objects.create(author=jonathan, question_text="What is life?")
        
        for _ in range(15):
            questions = Question.objects.all()
            random_nm = random.randint(0, len(questions)-1)
            Choice.objects.create(question=questions[random_nm], choice_text="To go on dates with my gf", author=jonathan)
            Comments.objects.create(question=questions[random_nm], comment_text="What a girl, sigh...", author=jonathan)
        