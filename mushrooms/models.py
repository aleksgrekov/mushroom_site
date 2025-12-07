from django.db import models

class Mushroom(models.Model):
    MUSHROOM_TYPES = [
        ('tubular', 'Трубчатые'),
        ('lamellar', 'Пластинчатые'),
        ('other', 'Другие'),
    ]
    
    EDIBILITY_CHOICES = [
        ('edible', '🍄 Съедобный'),
        ('conditionally_edible', '⚠️ Условно-съедобный'),
        ('poisonous', '☠️ Ядовитый'),
        ('deadly', '💀 Смертельно ядовитый'),
        ('inedible', '🚫 Несъедобный'),
    ]

    russian_name = models.CharField(max_length=200, verbose_name="Русское название")
    latin_name = models.CharField(max_length=200, verbose_name="Латинское название")
    mushroom_type = models.CharField(max_length=20, choices=MUSHROOM_TYPES, verbose_name="Тип гриба")
    edibility = models.CharField(max_length=30, choices=EDIBILITY_CHOICES, verbose_name="Съедобность")
    description = models.TextField(verbose_name="Описание")
    habitat = models.TextField(verbose_name="Место обитания")
    season = models.CharField(max_length=100, verbose_name="Сезон")
    distribution = models.TextField(blank=True, verbose_name="Распространение")
    photo = models.ImageField(upload_to='mushrooms/', blank=True, null=True, verbose_name="Фото")

    # Новые поля для определителя
    key_characteristics = models.TextField(blank=True, verbose_name="Ключевые характеристики")
    warning = models.TextField(blank=True, verbose_name="Предупреждение")
    cooking_tips = models.TextField(blank=True, verbose_name="Советы по приготовлению")

    def get_edibility_color(self):
        colors = {
            'edible': 'success',
            'conditionally_edible': 'warning', 
            'poisonous': 'danger',
            'deadly': 'dark',
            'inedible': 'secondary',
        }
        return colors.get(self.edibility, 'secondary')
    
    def __str__(self):
        return self.russian_name

    class Meta:
        verbose_name = "Гриб"
        verbose_name_plural = "Грибы"
        ordering = ['russian_name']


class Lookalike(models.Model):
    DANGER_LEVELS = [
        ('low', '🟡 Низкая опасность'),
        ('medium', '🟠 Средняя опасность'),
        ('high', '🔴 Высокая опасность'),
        ('deadly', '💀 Смертельно опасен'),
    ]
    
    mushroom = models.ForeignKey(
        Mushroom, 
        on_delete=models.CASCADE, 
        related_name='main_mushroom_lookalikes',
        verbose_name="Основной гриб"
    )
    lookalike = models.ForeignKey(
        Mushroom, 
        on_delete=models.CASCADE, 
        related_name='appears_as_lookalike',
        verbose_name="Гриб-двойник"
    )
    danger_level = models.CharField(
        max_length=20, 
        choices=DANGER_LEVELS, 
        verbose_name="Уровень опасности"
    )
    differences = models.TextField(verbose_name="Ключевые отличия")
    visual_differences = models.TextField(verbose_name="Визуальные отличия")
    warning = models.TextField(blank=True, verbose_name="Особое предупреждение")

    class Meta:
        verbose_name = "Двойник гриба"
        verbose_name_plural = "Двойники грибов"
        unique_together = ['mushroom', 'lookalike']

    def __str__(self):
        return f"{self.mushroom.russian_name} → {self.lookalike.russian_name}"


class Characteristic(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название характеристики")
    question = models.TextField(verbose_name="Вопрос для пользователя")
    order = models.IntegerField(default=0, verbose_name="Порядок в определителе")
    is_important = models.BooleanField(default=False, verbose_name="Важная характеристика")
    
    class Meta:
        verbose_name = "Характеристика"
        verbose_name_plural = "Характеристики"
        ordering = ['order']

    def __str__(self):
        return self.name


class CharacteristicOption(models.Model):
    characteristic = models.ForeignKey(
        Characteristic, 
        on_delete=models.CASCADE,
        verbose_name="Характеристика"
    )
    value = models.CharField(max_length=100, verbose_name="Значение")
    description = models.TextField(verbose_name="Описание для пользователя")
    
    class Meta:
        verbose_name = "Вариант характеристики"
        verbose_name_plural = "Варианты характеристик"
        ordering = ['characteristic__order', 'id']

    def __str__(self):
        return f"{self.characteristic.name}: {self.value}"


class MushroomCharacteristic(models.Model):
    mushroom = models.ForeignKey(
        Mushroom, 
        on_delete=models.CASCADE,
        verbose_name="Гриб"
    )
    characteristic = models.ForeignKey(
        Characteristic, 
        on_delete=models.CASCADE,
        verbose_name="Характеристика"
    )
    option = models.ForeignKey(
        CharacteristicOption, 
        on_delete=models.CASCADE,
        verbose_name="Выбранный вариант"
    )
    
    class Meta:
        verbose_name = "Характеристика гриба"
        verbose_name_plural = "Характеристики грибов"
        unique_together = ['mushroom', 'characteristic']

    def __str__(self):
        return f"{self.mushroom.russian_name} - {self.characteristic.name}: {self.option.value}"


# Существующие модели Quiz оставляем без изменений, но добавляем verbose_name
class Quiz(models.Model):
    LEVEL_CHOICES = [
        ('basic', 'Базовый'),
        ('advanced', 'Продвинутый'), 
        ('expert', 'Эксперт'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Название квиза")
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, verbose_name="Уровень сложности")
    description = models.TextField(verbose_name="Описание")
    questions_count = models.PositiveIntegerField(default=20, verbose_name="Количество вопросов")
    
    def __str__(self):
        return f"{self.name} ({self.get_level_display()})"
    
    class Meta:
        verbose_name = "Квиз"
        verbose_name_plural = "Квизы"


class QuizQuestion(models.Model):
    QUESTION_TYPE_CHOICES = [
        ('single', 'Одиночный выбор'),
        ('multiple', 'Множественный выбор'),
    ]
    
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions', verbose_name="Квиз")
    question_text = models.TextField(verbose_name="Текст вопроса")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")
    question_type = models.CharField(
        max_length=10, 
        choices=QUESTION_TYPE_CHOICES, 
        default='single',
        verbose_name="Тип вопроса"
    )
    
    class Meta:
        ordering = ['order']
        verbose_name = "Вопрос квиза"
        verbose_name_plural = "Вопросы квиза"
    
    def __str__(self):
        return f"Вопрос {self.order}: {self.question_text[:50]}..."


class QuizAnswer(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, related_name='answers', verbose_name="Вопрос")
    answer_text = models.CharField(max_length=300, verbose_name="Текст ответа")
    is_correct = models.BooleanField(default=False, verbose_name="Правильный ответ")
    
    def __str__(self):
        return f"{self.answer_text} ({'✓' if self.is_correct else '✗'})"
    
    class Meta:
        verbose_name = "Ответ квиза"
        verbose_name_plural = "Ответы квиза"


class QuizResult(models.Model):
    """Модель для сохранения результатов прохождения квизов"""
    user_name = models.CharField(max_length=100, verbose_name="Имя пользователя")
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name="Квиз")
    score = models.PositiveIntegerField(verbose_name="Количество баллов")
    correct_answers = models.PositiveIntegerField(verbose_name="Правильные ответы")
    wrong_answers = models.PositiveIntegerField(verbose_name="Неправильные ответы")
    total_questions = models.PositiveIntegerField(verbose_name="Всего вопросов")
    percentage = models.PositiveIntegerField(verbose_name="Процент правильных ответов")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата прохождения")
    
    class Meta:
        verbose_name = "Результат квиза"
        verbose_name_plural = "Результаты квизов"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user_name} - {self.quiz.name} ({self.percentage}%)"
    
    def get_performance_level(self):
        """Определяет уровень результата"""
        if self.percentage >= 90:
            return "Отлично"
        elif self.percentage >= 70:
            return "Хорошо"
        elif self.percentage >= 50:
            return "Удовлетворительно"
        else:
            return "Нужно подучить"
    
    def get_detailed_results(self):
        """Получить детальные результаты с вопросами и ответами"""
        return self.user_answers.select_related('question').prefetch_related('selected_answers', 'question__answers')
    
    def get_question_stats(self):
        """Статистика по вопросам"""
        total = self.user_answers.count()
        correct = self.user_answers.filter(is_correct=True).count()
        return {
            'total': total,
            'correct': correct,
            'incorrect': total - correct,
            'percentage': int((correct / total) * 100) if total > 0 else 0
        }


class UserAnswer(models.Model):
    """Модель для хранения ответов пользователя на вопросы"""
    quiz_result = models.ForeignKey(QuizResult, on_delete=models.CASCADE, related_name='user_answers')
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    selected_answers = models.ManyToManyField(QuizAnswer)
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Ответ пользователя"
        verbose_name_plural = "Ответы пользователей"
    
    def __str__(self):
        return f"{self.quiz_result.user_name} - {self.question} - {'✓' if self.is_correct else '✗'}"
    
    def get_correct_answers(self):
        """Получить правильные ответы на этот вопрос"""
        return self.question.answers.filter(is_correct=True)
    
    def get_selected_answers_text(self):
        """Текст выбранных ответов"""
        return ", ".join([answer.answer_text for answer in self.selected_answers.all()])
    
    def get_correct_answers_text(self):
        """Текст правильных ответов"""
        return ", ".join([answer.answer_text for answer in self.get_correct_answers()])