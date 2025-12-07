from django.core.management.base import BaseCommand
from mushrooms.models import Quiz, QuizQuestion, QuizAnswer

class Command(BaseCommand):
    help = 'Load quiz data with questions and answers'
    
    def handle(self, *args, **options):
        self.stdout.write("🍄 Загрузка данных для квиза...")
        
        # Удаляем старые квизы (все уровни)
        Quiz.objects.all().delete()
        
        # Создаем только 3 квиза
        basic_quiz = Quiz.objects.create(
            name="Базовый уровень",
            level="basic",
            description='Простые вопросы по общей микологии. Идеально для учеников 7 класса.',
            questions_count=16
        )
        
        advanced_quiz = Quiz.objects.create(
            name="Продвинутый уровень", 
            level="advanced",
            description='Вопросы для опытных грибников. Требует хороших знаний микологии.',
            questions_count=11
        )
        
        expert_quiz = Quiz.objects.create(
            name="Эксперт",
            level="expert", 
            description='Сложные вопросы для экспертов в области микологии. Требует глубоких знаний.',
            questions_count=17
        )
        
        # Очищаем старые вопросы
        QuizQuestion.objects.all().delete()
        
        # =========================================================================
        # ВОПРОСЫ ДЛЯ БАЗОВОГО УРОВНЯ (16 вопросов)
        # =========================================================================
        
        # Вопрос 1
        q1 = QuizQuestion.objects.create(
            quiz=basic_quiz,
            question_text="Грибы объединены в систематическую группу:",
            order=1
        )
        QuizAnswer.objects.create(question=q1, answer_text="род", is_correct=False)
        QuizAnswer.objects.create(question=q1, answer_text="отдел", is_correct=False)
        QuizAnswer.objects.create(question=q1, answer_text="царство", is_correct=True)
        QuizAnswer.objects.create(question=q1, answer_text="семейство", is_correct=False)
        
        # Вопрос 2
        q2 = QuizQuestion.objects.create(
            quiz=basic_quiz,
            question_text="По способу питания грибы:",
            order=2
        )
        QuizAnswer.objects.create(question=q2, answer_text="автотрофы", is_correct=False)
        QuizAnswer.objects.create(question=q2, answer_text="гетеротрофы", is_correct=True)
        QuizAnswer.objects.create(question=q2, answer_text="фототрофы", is_correct=False)
        QuizAnswer.objects.create(question=q2, answer_text="хемотрофы", is_correct=False)
        
        # Вопрос 3
        q3 = QuizQuestion.objects.create(
            quiz=basic_quiz,
            question_text="Тело грибов образовано:",
            order=3
        )
        QuizAnswer.objects.create(question=q3, answer_text="корнями", is_correct=False)
        QuizAnswer.objects.create(question=q3, answer_text="побегом", is_correct=False)
        QuizAnswer.objects.create(question=q3, answer_text="мицелием", is_correct=True)
        QuizAnswer.objects.create(question=q3, answer_text="системой органов", is_correct=False)
        
        # Вопрос 4
        q4 = QuizQuestion.objects.create(
            quiz=basic_quiz,
            question_text="Грибы размножаются бесполым путем с помощью:",
            order=4
        )
        QuizAnswer.objects.create(question=q4, answer_text="гамет", is_correct=False)
        QuizAnswer.objects.create(question=q4, answer_text="семян", is_correct=False)
        QuizAnswer.objects.create(question=q4, answer_text="спермиев", is_correct=False)
        QuizAnswer.objects.create(question=q4, answer_text="спор", is_correct=True)
        
        # Вопрос 5
        q5 = QuizQuestion.objects.create(
            quiz=basic_quiz,
            question_text="В круговороте веществ грибы являются:",
            order=5
        )
        QuizAnswer.objects.create(question=q5, answer_text="производителями органических веществ", is_correct=False)
        QuizAnswer.objects.create(question=q5, answer_text="фотосинтезирующими организмами", is_correct=False)
        QuizAnswer.objects.create(question=q5, answer_text="разрушителями органических веществ", is_correct=True)
        QuizAnswer.objects.create(question=q5, answer_text="растительноядными организмами", is_correct=False)
        
        # Вопрос 6
        q6 = QuizQuestion.objects.create(
            quiz=basic_quiz,
            question_text="В клетках грибов запасное вещество:",
            order=6
        )
        QuizAnswer.objects.create(question=q6, answer_text="хитин", is_correct=False)
        QuizAnswer.objects.create(question=q6, answer_text="гликоген", is_correct=True)
        QuizAnswer.objects.create(question=q6, answer_text="крахмал", is_correct=False)
        QuizAnswer.objects.create(question=q6, answer_text="хлорофилл", is_correct=False)
        
        # Вопрос 7
        q7 = QuizQuestion.objects.create(
            quiz=basic_quiz,
            question_text="Тело дрожжей состоит из:",
            order=7
        )
        QuizAnswer.objects.create(question=q7, answer_text="пенька и шляпки", is_correct=False)
        QuizAnswer.objects.create(question=q7, answer_text="мицелия", is_correct=False)
        QuizAnswer.objects.create(question=q7, answer_text="одной клетки", is_correct=True)
        QuizAnswer.objects.create(question=q7, answer_text="грибницы", is_correct=False)
        
        # Вопрос 8
        q8 = QuizQuestion.objects.create(
            quiz=basic_quiz,
            question_text="Плесень на хлебе образуют:",
            order=8
        )
        QuizAnswer.objects.create(question=q8, answer_text="пеницилл", is_correct=True)
        QuizAnswer.objects.create(question=q8, answer_text="бактерии", is_correct=False)
        QuizAnswer.objects.create(question=q8, answer_text="дрожжи", is_correct=False)
        QuizAnswer.objects.create(question=q8, answer_text="трутовики", is_correct=False)
        
        # Вопрос 9
        q9 = QuizQuestion.objects.create(
            quiz=basic_quiz,
            question_text="Грибы изучает наука:",
            order=9
        )
        QuizAnswer.objects.create(question=q9, answer_text="зоология", is_correct=False)
        QuizAnswer.objects.create(question=q9, answer_text="ботаника", is_correct=False)
        QuizAnswer.objects.create(question=q9, answer_text="микробиология", is_correct=False)
        QuizAnswer.objects.create(question=q9, answer_text="микология", is_correct=True)
        
        # Вопрос 10
        q10 = QuizQuestion.objects.create(
            quiz=basic_quiz,
            question_text="В клетках грибов отсутствует:",
            order=10
        )
        QuizAnswer.objects.create(question=q10, answer_text="ядро", is_correct=False)
        QuizAnswer.objects.create(question=q10, answer_text="цитоплазма", is_correct=False)
        QuizAnswer.objects.create(question=q10, answer_text="хлоропласты", is_correct=True)
        QuizAnswer.objects.create(question=q10, answer_text="наружная мембрана", is_correct=False)
        
        # Вопрос 11
        q11 = QuizQuestion.objects.create(
            quiz=basic_quiz,
            question_text="Дрожжи размножаются путем:",
            order=11
        )
        QuizAnswer.objects.create(question=q11, answer_text="половым", is_correct=False)
        QuizAnswer.objects.create(question=q11, answer_text="спорами", is_correct=False)
        QuizAnswer.objects.create(question=q11, answer_text="почкованием", is_correct=True)
        QuizAnswer.objects.create(question=q11, answer_text="делением пополам", is_correct=False)
        
        # Вопрос 12
        q12 = QuizQuestion.objects.create(
            quiz=basic_quiz,
            question_text="Нити грибницы и корня растения образуют:",
            order=12
        )
        QuizAnswer.objects.create(question=q12, answer_text="тело гриба", is_correct=False)
        QuizAnswer.objects.create(question=q12, answer_text="микоризу", is_correct=True)
        QuizAnswer.objects.create(question=q12, answer_text="побег", is_correct=False)
        QuizAnswer.objects.create(question=q12, answer_text="мицелий", is_correct=False)
        
        # Вопрос 13
        q13 = QuizQuestion.objects.create(
            quiz=basic_quiz,
            question_text="Гриб спорынья питается как:",
            order=13
        )
        QuizAnswer.objects.create(question=q13, answer_text="фототроф", is_correct=False)
        QuizAnswer.objects.create(question=q13, answer_text="симбионт", is_correct=False)
        QuizAnswer.objects.create(question=q13, answer_text="паразит", is_correct=True)
        QuizAnswer.objects.create(question=q13, answer_text="хищник", is_correct=False)
        
        # Вопрос 14
        q14 = QuizQuestion.objects.create(
            quiz=basic_quiz,
            question_text="Из какого гриба получают антибиотики:",
            order=14
        )
        QuizAnswer.objects.create(question=q14, answer_text="пеницилл", is_correct=True)
        QuizAnswer.objects.create(question=q14, answer_text="спорынья", is_correct=False)
        QuizAnswer.objects.create(question=q14, answer_text="мукор", is_correct=False)
        QuizAnswer.objects.create(question=q14, answer_text="дрожжи", is_correct=False)
        
        # Вопрос 15
        q15 = QuizQuestion.objects.create(
            quiz=basic_quiz,
            question_text="По способу питания грибы не являются:",
            order=15
        )
        QuizAnswer.objects.create(question=q15, answer_text="сапрофитами", is_correct=False)
        QuizAnswer.objects.create(question=q15, answer_text="симбионтами", is_correct=False)
        QuizAnswer.objects.create(question=q15, answer_text="автотрофами", is_correct=True)
        QuizAnswer.objects.create(question=q15, answer_text="паразитами", is_correct=False)
        
        # Вопрос 16
        q16 = QuizQuestion.objects.create(
            quiz=basic_quiz,
            question_text="В состав клеточной стенки грибов входит:",
            order=16
        )
        QuizAnswer.objects.create(question=q16, answer_text="гликоген", is_correct=False)
        QuizAnswer.objects.create(question=q16, answer_text="хитин", is_correct=True)
        QuizAnswer.objects.create(question=q16, answer_text="крахмал", is_correct=False)
        QuizAnswer.objects.create(question=q16, answer_text="хлорофилл", is_correct=False)
        
        # =========================================================================
        # ВОПРОСЫ ДЛЯ ПРОДВИНУТОГО УРОВНЯ (11 вопросов)
        # =========================================================================
        
        # Вопрос 1 - множественный выбор
        q17 = QuizQuestion.objects.create(
            quiz=advanced_quiz,
            question_text="Выберите три верных утверждения. Грибы размножаются:",
            order=1,
            question_type='multiple'
        )
        QuizAnswer.objects.create(question=q17, answer_text="Спорами", is_correct=True)
        QuizAnswer.objects.create(question=q17, answer_text="Семенами", is_correct=False)
        QuizAnswer.objects.create(question=q17, answer_text="Корнями", is_correct=False)
        QuizAnswer.objects.create(question=q17, answer_text="Почкованием", is_correct=True)
        QuizAnswer.objects.create(question=q17, answer_text="Частями мицелия", is_correct=True)
        QuizAnswer.objects.create(question=q17, answer_text="Делением пополам", is_correct=False)
        
        # Вопрос 2 - множественный выбор
        q18 = QuizQuestion.objects.create(
            quiz=advanced_quiz,
            question_text="Выберите отрицательные роли грибов в жизни человека (два верных ответа):",
            order=2,
            question_type='multiple'
        )
        QuizAnswer.objects.create(question=q18, answer_text="Вызывают болезни растений (фитофтороз, мучнистая роса)", is_correct=True)
        QuizAnswer.objects.create(question=q18, answer_text="Порча продуктов питания (плесень)", is_correct=True)
        QuizAnswer.objects.create(question=q18, answer_text="Производство антибиотиков (пенициллин)", is_correct=False)
        QuizAnswer.objects.create(question=q18, answer_text="Использование в пищевой промышленности (дрожжи, сыры с плесенью)", is_correct=False)
        QuizAnswer.objects.create(question=q18, answer_text="Вызывают грибковые заболевания у человека и животных (микозы)", is_correct=True)
        
        # Вопрос 3 - множественный выбор
        q19 = QuizQuestion.objects.create(
            quiz=advanced_quiz,
            question_text="Выберите три верных утверждения. Ведут паразитический образ жизни:",
            order=3,
            question_type='multiple'
        )
        QuizAnswer.objects.create(question=q19, answer_text="Фитофтора", is_correct=True)
        QuizAnswer.objects.create(question=q19, answer_text="Мукор", is_correct=False)
        QuizAnswer.objects.create(question=q19, answer_text="Трутовик", is_correct=True)
        QuizAnswer.objects.create(question=q19, answer_text="Дрожжи", is_correct=False)
        QuizAnswer.objects.create(question=q19, answer_text="Спорынья", is_correct=True)
        QuizAnswer.objects.create(question=q19, answer_text="Подосиновик", is_correct=False)
        
        # Вопрос 4 - множественный выбор
        q20 = QuizQuestion.objects.create(
            quiz=advanced_quiz,
            question_text="Выберите положительные роли грибов в жизни человека (два верных ответа):",
            order=4,
            question_type='multiple'
        )
        QuizAnswer.objects.create(question=q20, answer_text="Участвуют в круговороте веществ, разлагая органические остатки", is_correct=True)
        QuizAnswer.objects.create(question=q20, answer_text="Используются для получения ферментов и органических кислот", is_correct=True)
        QuizAnswer.objects.create(question=q20, answer_text="Вызывают аллергические реакции", is_correct=False)
        QuizAnswer.objects.create(question=q20, answer_text="Разрушают древесину (домовые грибы)", is_correct=False)
        QuizAnswer.objects.create(question=q20, answer_text="Используются в биотехнологиях для получения белков и витаминов", is_correct=True)
        
        # Вопрос 5 - одиночный выбор из 10 вариантов
        q21 = QuizQuestion.objects.create(
            quiz=advanced_quiz,
            question_text="Выберите верное утверждение:",
            order=5
        )
        QuizAnswer.objects.create(question=q21, answer_text="Шляпочные грибы содержат пигмент.", is_correct=False)
        QuizAnswer.objects.create(question=q21, answer_text="Клетки грибов содержат запасное вещество – гликоген.", is_correct=True)
        QuizAnswer.objects.create(question=q21, answer_text="Грибница, или мицелий, состоит из тонких ветвящихся нитей – гиф.", is_correct=False)
        QuizAnswer.objects.create(question=q21, answer_text="Одноклеточные грибы – дрожжи", is_correct=False)
        QuizAnswer.objects.create(question=q21, answer_text="Грибы размножаются спорами и вегетативно.", is_correct=False)
        QuizAnswer.objects.create(question=q21, answer_text="Споры грибов образуются в спорангиях, которые образуются на гифах.", is_correct=False)
        QuizAnswer.objects.create(question=q21, answer_text="Род Мукор относится к классу Хитридиомицетов.", is_correct=False)
        QuizAnswer.objects.create(question=q21, answer_text="Сыроежки относятся к классу Аскомицеты.", is_correct=False)
        QuizAnswer.objects.create(question=q21, answer_text="Дрожжи относятся к классу Несовершенные грибы.", is_correct=False)
        QuizAnswer.objects.create(question=q21, answer_text="Подосиновик и подберезовик относятся к классу Базидиомицетов.", is_correct=False)
        
        # Вопрос 6
        q22 = QuizQuestion.objects.create(
            quiz=advanced_quiz,
            question_text="Как называются грибы, мирно уживающиеся с различными видами растений?",
            order=6
        )
        QuizAnswer.objects.create(question=q22, answer_text="паразиты", is_correct=False)
        QuizAnswer.objects.create(question=q22, answer_text="сапрофиты", is_correct=False)
        QuizAnswer.objects.create(question=q22, answer_text="симбионты", is_correct=True)
        QuizAnswer.objects.create(question=q22, answer_text="хищники", is_correct=False)
        
        # Вопрос 7
        q23 = QuizQuestion.objects.create(
            quiz=advanced_quiz,
            question_text="К каким лишайникам относится ягель?",
            order=7
        )
        QuizAnswer.objects.create(question=q23, answer_text="к кустистым", is_correct=True)
        QuizAnswer.objects.create(question=q23, answer_text="к накипным", is_correct=False)
        QuizAnswer.objects.create(question=q23, answer_text="к листоватым", is_correct=False)
        QuizAnswer.objects.create(question=q23, answer_text="к простым", is_correct=False)
        
        # Вопрос 8
        q24 = QuizQuestion.objects.create(
            quiz=advanced_quiz,
            question_text="Как называются нити, из которых состоит мицелий грибов?",
            order=8
        )
        QuizAnswer.objects.create(question=q24, answer_text="Сапры", is_correct=False)
        QuizAnswer.objects.create(question=q24, answer_text="Хемы", is_correct=False)
        QuizAnswer.objects.create(question=q24, answer_text="Симбионты", is_correct=False)
        QuizAnswer.objects.create(question=q24, answer_text="Гифы", is_correct=True)
        
        # Вопрос 9
        q25 = QuizQuestion.objects.create(
            quiz=advanced_quiz,
            question_text="Сморчки и строчки близки по систематическому положению к грибам:",
            order=9
        )
        QuizAnswer.objects.create(question=q25, answer_text="шляпочным", is_correct=False)
        QuizAnswer.objects.create(question=q25, answer_text="пенициллу", is_correct=False)
        QuizAnswer.objects.create(question=q25, answer_text="дрожжам", is_correct=False)
        QuizAnswer.objects.create(question=q25, answer_text="мукору", is_correct=True)
        
        # Вопрос 10
        q26 = QuizQuestion.objects.create(
            quiz=advanced_quiz,
            question_text="Тело пекарских дрожжей состоит из:",
            order=10
        )
        QuizAnswer.objects.create(question=q26, answer_text="шляпки и ножки", is_correct=False)
        QuizAnswer.objects.create(question=q26, answer_text="тканей", is_correct=False)
        QuizAnswer.objects.create(question=q26, answer_text="одной клетки", is_correct=True)
        QuizAnswer.objects.create(question=q26, answer_text="почвенной грибницы", is_correct=False)
        
        # Вопрос 11
        q27 = QuizQuestion.objects.create(
            quiz=advanced_quiz,
            question_text="Признаком грибов, сближающим их с царством растений, является:",
            order=11
        )
        QuizAnswer.objects.create(question=q27, answer_text="гетеротрофный способ питания", is_correct=False)
        QuizAnswer.objects.create(question=q27, answer_text="верхушечный рост мицелия гриба", is_correct=True)
        QuizAnswer.objects.create(question=q27, answer_text="наличие мочевины в качестве промежуточного продукта метаболизма", is_correct=False)
        QuizAnswer.objects.create(question=q27, answer_text="наличие хитина в клеточных стенках", is_correct=False)
        
        # =========================================================================
        # ВОПРОСЫ ДЛЯ УРОВНЯ ЭКСПЕРТ (17 вопросов)
        # =========================================================================
        
        # Вопрос 1
        q28 = QuizQuestion.objects.create(
            quiz=expert_quiz,
            question_text="Какого способа добывания пищи среди грибов не встречается?",
            order=1
        )
        QuizAnswer.objects.create(question=q28, answer_text="сапрофиты", is_correct=False)
        QuizAnswer.objects.create(question=q28, answer_text="паразиты", is_correct=False)
        QuizAnswer.objects.create(question=q28, answer_text="хищные", is_correct=False)
        QuizAnswer.objects.create(question=q28, answer_text="фотосинтезирующие", is_correct=True)
        
        # Вопрос 2
        q29 = QuizQuestion.objects.create(
            quiz=expert_quiz,
            question_text="К грибам паразитам относят:",
            order=2
        )
        QuizAnswer.objects.create(question=q29, answer_text="мухомор и бледная поганка", is_correct=False)
        QuizAnswer.objects.create(question=q29, answer_text="мукор и пеницилл", is_correct=False)
        QuizAnswer.objects.create(question=q29, answer_text="гриб трутовик и головня", is_correct=True)
        QuizAnswer.objects.create(question=q29, answer_text="шампиньоны и вешенки", is_correct=False)
        
        # Вопрос 3
        q30 = QuizQuestion.objects.create(
            quiz=expert_quiz,
            question_text="Грибы не могут размножаться:",
            order=3
        )
        QuizAnswer.objects.create(question=q30, answer_text="семенами", is_correct=True)
        QuizAnswer.objects.create(question=q30, answer_text="спорами", is_correct=False)
        QuizAnswer.objects.create(question=q30, answer_text="вегетативно", is_correct=False)
        QuizAnswer.objects.create(question=q30, answer_text="половым путем", is_correct=False)
        
        # Вопрос 4
        q31 = QuizQuestion.objects.create(
            quiz=expert_quiz,
            question_text="Прочность клеточной оболочки грибам придает:",
            order=4
        )
        QuizAnswer.objects.create(question=q31, answer_text="пектин", is_correct=False)
        QuizAnswer.objects.create(question=q31, answer_text="хитин", is_correct=True)
        QuizAnswer.objects.create(question=q31, answer_text="целлюлоза", is_correct=False)
        QuizAnswer.objects.create(question=q31, answer_text="гликоген", is_correct=False)
        
        # Вопрос 5
        q32 = QuizQuestion.objects.create(
            quiz=expert_quiz,
            question_text="Дрожжи размножаются:",
            order=5
        )
        QuizAnswer.objects.create(question=q32, answer_text="только делением", is_correct=False)
        QuizAnswer.objects.create(question=q32, answer_text="только почкованием", is_correct=False)
        QuizAnswer.objects.create(question=q32, answer_text="делением и почкованием", is_correct=True)
        
        # Вопрос 6
        q33 = QuizQuestion.objects.create(
            quiz=expert_quiz,
            question_text="Какой гриб поражает злаковые культуры и может вызвать отравление человека, попадая в муку?",
            order=6
        )
        QuizAnswer.objects.create(question=q33, answer_text="фитофтора", is_correct=False)
        QuizAnswer.objects.create(question=q33, answer_text="пеницилл", is_correct=False)
        QuizAnswer.objects.create(question=q33, answer_text="спорынья", is_correct=True)
        QuizAnswer.objects.create(question=q33, answer_text="дрожжи", is_correct=False)
        
        # Вопрос 7
        q34 = QuizQuestion.objects.create(
            quiz=expert_quiz,
            question_text="Гриб фитофтора поражает у картофеля:",
            order=7
        )
        QuizAnswer.objects.create(question=q34, answer_text="только листья", is_correct=False)
        QuizAnswer.objects.create(question=q34, answer_text="листья и стебли", is_correct=False)
        QuizAnswer.objects.create(question=q34, answer_text="все растение, в том числе и клубни", is_correct=True)
        
        # Вопрос 8
        q35 = QuizQuestion.objects.create(
            quiz=expert_quiz,
            question_text="Плодовое тело шляпочного гриба образовано:",
            order=8
        )
        QuizAnswer.objects.create(question=q35, answer_text="шляпкой и мицелием", is_correct=False)
        QuizAnswer.objects.create(question=q35, answer_text="ножкой и мицелием", is_correct=False)
        QuizAnswer.objects.create(question=q35, answer_text="шляпкой и ножкой", is_correct=True)
        QuizAnswer.objects.create(question=q35, answer_text="микоризой и спорангием", is_correct=False)
        
        # Вопрос 9
        q36 = QuizQuestion.objects.create(
            quiz=expert_quiz,
            question_text="Грибы неспособны к фотосинтезу, потому что:",
            order=9
        )
        QuizAnswer.objects.create(question=q36, answer_text="они живут в почве", is_correct=False)
        QuizAnswer.objects.create(question=q36, answer_text="не имеют хлорофилла", is_correct=True)
        QuizAnswer.objects.create(question=q36, answer_text="паразитируют на других живых организмах", is_correct=False)
        QuizAnswer.objects.create(question=q36, answer_text="имеют небольшие размеры", is_correct=False)
        
        # Вопрос 10 - множественный выбор
        q37 = QuizQuestion.objects.create(
            quiz=expert_quiz,
            question_text="Ногтевая пластинка при онихомикозе:",
            order=10,
            question_type='multiple'
        )
        QuizAnswer.objects.create(question=q37, answer_text="имеет вид наперстка", is_correct=False)
        QuizAnswer.objects.create(question=q37, answer_text="имеет вид выпуклого стекла", is_correct=False)
        QuizAnswer.objects.create(question=q37, answer_text="имеет вид вогнутого стекла", is_correct=False)
        QuizAnswer.objects.create(question=q37, answer_text="гипертрофируется", is_correct=True)
        QuizAnswer.objects.create(question=q37, answer_text="не изменяется", is_correct=False)
        
        # Вопрос 11 - множественный выбор
        q38 = QuizQuestion.objects.create(
            quiz=expert_quiz,
            question_text="Для общей терапии микозов используются:",
            order=11,
            question_type='multiple'
        )
        QuizAnswer.objects.create(question=q38, answer_text="микосептин", is_correct=False)
        QuizAnswer.objects.create(question=q38, answer_text="циклоспарин", is_correct=False)
        QuizAnswer.objects.create(question=q38, answer_text="пенициллин", is_correct=False)
        QuizAnswer.objects.create(question=q38, answer_text="кетоконазол", is_correct=True)
        QuizAnswer.objects.create(question=q38, answer_text="анилиновые красители", is_correct=False)
        
        # Вопрос 12 - множественный выбор
        q39 = QuizQuestion.objects.create(
            quiz=expert_quiz,
            question_text="Белая кандида является нормальной частью флоры:",
            order=12,
            question_type='multiple'
        )
        QuizAnswer.objects.create(question=q39, answer_text="рта", is_correct=True)
        QuizAnswer.objects.create(question=q39, answer_text="волос", is_correct=False)
        QuizAnswer.objects.create(question=q39, answer_text="потовых желез", is_correct=False)
        QuizAnswer.objects.create(question=q39, answer_text="ногтей", is_correct=False)
        QuizAnswer.objects.create(question=q39, answer_text="сальных желез", is_correct=False)
        
        # Вопрос 13 - множественный выбор
        q40 = QuizQuestion.objects.create(
            quiz=expert_quiz,
            question_text="Укажите факторы патогенности грибов:",
            order=13,
            question_type='multiple'
        )
        QuizAnswer.objects.create(question=q40, answer_text="Хитин", is_correct=False)
        QuizAnswer.objects.create(question=q40, answer_text="Целлюлоза", is_correct=False)
        QuizAnswer.objects.create(question=q40, answer_text="Гликолипопротеины", is_correct=True)
        QuizAnswer.objects.create(question=q40, answer_text="Ферменты", is_correct=True)
        
        # Вопрос 14
        q41 = QuizQuestion.objects.create(
            quiz=expert_quiz,
            question_text="На какой среде определяется тип филаментации грибов рода Candida?",
            order=14
        )
        QuizAnswer.objects.create(question=q41, answer_text="Мясопептонный агар", is_correct=False)
        QuizAnswer.objects.create(question=q41, answer_text="Сабуро", is_correct=False)
        QuizAnswer.objects.create(question=q41, answer_text="Сусло", is_correct=False)
        QuizAnswer.objects.create(question=q41, answer_text="Рисовый агар", is_correct=True)
        QuizAnswer.objects.create(question=q41, answer_text="Чапека", is_correct=False)
        
        # Вопрос 15
        q42 = QuizQuestion.objects.create(
            quiz=expert_quiz,
            question_text="При какой температуре растет Candida dubliniensis?",
            order=15
        )
        QuizAnswer.objects.create(question=q42, answer_text="Только при 42°С", is_correct=False)
        QuizAnswer.objects.create(question=q42, answer_text="Только при 37°С", is_correct=False)
        QuizAnswer.objects.create(question=q42, answer_text="Только при 37°С и ниже", is_correct=True)
        QuizAnswer.objects.create(question=q42, answer_text="В диапазоне 37-42 °C", is_correct=False)
        
        # Вопрос 16
        q43 = QuizQuestion.objects.create(
            quiz=expert_quiz,
            question_text="Обнаружение чего является критерием диагностики генитального кандидоза?",
            order=16
        )
        QuizAnswer.objects.create(question=q43, answer_text="Дрожжевых клеток", is_correct=False)
        QuizAnswer.objects.create(question=q43, answer_text="Дрожжевых почкующихся клеток", is_correct=False)
        QuizAnswer.objects.create(question=q43, answer_text="Псевдомицелия", is_correct=True)
        
        # Вопрос 17
        q44 = QuizQuestion.objects.create(
            quiz=expert_quiz,
            question_text="Выявление типов роста (филаметации) у грибов рода Candida используется для:",
            order=17
        )
        QuizAnswer.objects.create(question=q44, answer_text="Определения вида", is_correct=True)
        QuizAnswer.objects.create(question=q44, answer_text="Определения родовой принадлежности", is_correct=False)
        QuizAnswer.objects.create(question=q44, answer_text="Дифференциации кандидоза от носительства", is_correct=False)
        
        self.stdout.write(self.style.SUCCESS('✅ Данные для квиза успешно загружены!'))
        self.stdout.write(f'✅ Базовый уровень: {basic_quiz.questions.count()} вопросов')
        self.stdout.write(f'✅ Продвинутый уровень: {advanced_quiz.questions.count()} вопросов') 
        self.stdout.write(f'✅ Уровень эксперт: {expert_quiz.questions.count()} вопросов')
        self.stdout.write('\n🎮 Квиз готов к использованию!')