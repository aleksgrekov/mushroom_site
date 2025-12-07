# mushrooms/management/commands/fix_quiz_answers.py
from django.core.management.base import BaseCommand
from mushrooms.models import QuizQuestion, QuizAnswer

class Command(BaseCommand):
    help = 'Fix quiz answers - ensure each question has correct answers'
    
    def handle(self, *args, **options):
        self.stdout.write("🔧 Проверка и исправление ответов в квизах...")
        
        questions = QuizQuestion.objects.all()
        fixed_count = 0
        
        for question in questions:
            correct_answers = question.answers.filter(is_correct=True)
            
            if correct_answers.count() == 0:
                self.stdout.write(
                    self.style.WARNING(f'❌ Вопрос "{question.question_text[:50]}..." не имеет правильных ответов!')
                )
                # Назначаем первый ответ как правильный
                first_answer = question.answers.first()
                if first_answer:
                    first_answer.is_correct = True
                    first_answer.save()
                    fixed_count += 1
                    self.stdout.write(
                        self.style.SUCCESS(f'✅ Назначен правильный ответ: "{first_answer.answer_text}"')
                    )
            
            elif correct_answers.count() > 1 and question.question_type == 'single':
                self.stdout.write(
                    self.style.WARNING(f'⚠️ Вопрос с одиночным выбором имеет несколько правильных ответов: "{question.question_text[:50]}..."')
                )
        
        self.stdout.write(self.style.SUCCESS(f'✅ Исправлено {fixed_count} вопросов'))