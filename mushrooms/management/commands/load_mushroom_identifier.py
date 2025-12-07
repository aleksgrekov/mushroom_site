from django.core.management.base import BaseCommand
from mushrooms.models import (
    Mushroom, Lookalike, Characteristic, 
    CharacteristicOption, MushroomCharacteristic
)

class Command(BaseCommand):
    help = 'Load mushroom data for identifier (without deleting existing data)'
    
    def handle(self, *args, **options):
        self.stdout.write("🔄 Начинаем загрузку данных для определителя...")
        
        # НЕ удаляем старые данные!
        self.create_characteristics()
        self.create_mushrooms()
        self.create_lookalikes()
        
        self.stdout.write(self.style.SUCCESS("✅ Данные для определителя успешно загружены!"))
    
    def create_characteristics(self):
        self.stdout.write("📝 Создаем характеристики...")
        
        characteristics_data = [
            {
                'name': 'cap_shape',
                'question': 'Какая форма шляпки?',
                'order': 1,
                'options': [
                    ('umbrella', 'Зонтиковидная (с бугорком)'),
                    ('convex', 'Выпуклая'),
                    ('flat', 'Плоская'),
                    ('funnel', 'Воронковидная'),
                    ('bell', 'Колокольчатая'),
                ]
            },
            {
                'name': 'cap_color', 
                'question': 'Какой цвет шляпки?',
                'order': 2,
                'options': [
                    ('brown_scaly', 'Коричневая с чешуйками'),
                    ('white', 'Белая'),
                    ('orange', 'Оранжевая'),
                    ('yellow', 'Желтая'),
                    ('red_brown', 'Красно-коричневая'),
                    ('pink_zones', 'Розовая с концентрическими зонами'),
                ]
            },
            {
                'name': 'gills_color',
                'question': 'Какой цвет пластинок?',
                'order': 3,
                'options': [
                    ('white', 'Белые'),
                    ('cream', 'Кремовые'),
                    ('yellow', 'Желтые'),
                    ('pink', 'Розовые'),
                    ('green', 'Зеленоватые'),
                    ('orange', 'Оранжевые'),
                ]
            },
            {
                'name': 'stem_ring',
                'question': 'Есть ли кольцо на ножке?',
                'order': 4,
                'options': [
                    ('movable', 'Есть, подвижное'),
                    ('fixed', 'Есть, неподвижное'),
                    ('none', 'Нет'),
                ]
            },
            {
                'name': 'milk',
                'question': 'Есть ли млечный сок?',
                'order': 5,
                'options': [
                    ('orange', 'Оранжевый, не едкий'),
                    ('white_burning', 'Белый, едкий'),
                    ('white_yellowing', 'Белый, желтеет на воздухе'),
                    ('none', 'Нет млечного сока'),
                ]
            },
            {
                'name': 'habitat',
                'question': 'Где растет гриб?',
                'order': 6,
                'options': [
                    ('meadow', 'Луга, открытые пространства'),
                    ('coniferous', 'Хвойные леса'),
                    ('deciduous', 'Лиственные леса'),
                    ('birch', 'Под березами'),
                    ('mixed', 'Смешанные леса'),
                    ('wood', 'На древесине'),
                ]
            }
        ]
        
        for char_data in characteristics_data:
            char, created = Characteristic.objects.get_or_create(
                name=char_data['name'],
                defaults={
                    'question': char_data['question'],
                    'order': char_data['order']
                }
            )
            for opt_value, opt_desc in char_data['options']:
                CharacteristicOption.objects.get_or_create(
                    characteristic=char,
                    value=opt_value,
                    defaults={'description': opt_desc}
                )
            
            if created:
                self.stdout.write(f"   Создана характеристика: {char_data['name']}")
    
    def create_mushrooms(self):
        self.stdout.write("🍄 Проверяем грибы для определителя...")
        
        mushrooms_data = [
            {
                'russian_name': 'Зонтик пестрый',
                'latin_name': 'Macrolepiota procera',
                'mushroom_type': 'lamellar',
                'edibility': 'edible',
                'description': '''Крупный съедобный гриб с характерной шляпкой-зонтиком.
Шляпка: до 30-40 см, покрыта коричневыми чешуйками, с темным бугорком в центре.
Ножка: высокая, с подвижным кольцом.
Пластинки: белые, свободные.
Растет: на лугах, опушках, в светлых лесах.''',
                'habitat': 'Луга, опушки, светлые леса',
                'season': 'Июль-октябрь',
                'key_characteristics': 'Крупный размер, коричневые чешуйки на шляпке, подвижное кольцо',
            },
            {
                'russian_name': 'Хлорофиллум свинцовошлаковый', 
                'latin_name': 'Chlorophyllum molybdites',
                'mushroom_type': 'lamellar',
                'edibility': 'poisonous',
                'description': '''Опасный двойник зонтика. При употреблении вызывает сильное отравление.
Шляпка: беловатая с розоватыми чешуйками.
Пластинки: с возрастом становятся зеленоватыми.
Ножка: с неподвижным кольцом.''',
                'habitat': 'Луга, парки, сады',
                'season': 'Лето-осень',
                'key_characteristics': 'Зеленеющие пластинки, неподвижное кольцо',
            },
            # Добавьте остальные грибы по аналогии...
        ]
        
        for data in mushrooms_data:
            mushroom, created = Mushroom.objects.get_or_create(
                russian_name=data['russian_name'],
                defaults=data
            )
            if created:
                self.stdout.write(f"   Создан гриб: {data['russian_name']}")
            else:
                self.stdout.write(f"   Гриб уже существует: {data['russian_name']}")
    
    def create_lookalikes(self):
        self.stdout.write("⚠️ Создаем связи двойников...")
        
        lookalikes_data = [
            {
                'main': 'Зонтик пестрый',
                'lookalike': 'Хлорофиллум свинцовошлаковый',
                'danger_level': 'high',
                'differences': '''1. Пластинки: у зонтика всегда белые, у хлорофиллума с возрастом зеленеют
2. Кольцо: у зонтика подвижное, у хлорофиллума - нет''',
                'visual_differences': '''Зонтик: коричневые чешуйки, высокий стройный вид
Хлорофиллум: более приземистый, чешуйки розоватые''',
            },
            # Добавьте остальные связи...
        ]
        
        for data in lookalikes_data:
            try:
                main_mushroom = Mushroom.objects.get(russian_name=data['main'])
                lookalike_mushroom = Mushroom.objects.get(russian_name=data['lookalike'])
                
                Lookalike.objects.get_or_create(
                    mushroom=main_mushroom,
                    lookalike=lookalike_mushroom,
                    defaults={
                        'danger_level': data['danger_level'],
                        'differences': data['differences'],
                        'visual_differences': data['visual_differences'],
                    }
                )
                self.stdout.write(f"   Создана связь: {data['main']} → {data['lookalike']}")
            except Mushroom.DoesNotExist as e:
                self.stdout.write(self.style.WARNING(f"   Пропущена связь: {e}"))