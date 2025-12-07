from django.core.management.base import BaseCommand
from mushrooms.models import Mushroom, Characteristic, CharacteristicOption, MushroomCharacteristic

class Command(BaseCommand):
    help = 'Create mushroom-characteristic relationships'
    
    def handle(self, *args, **options):
        self.stdout.write("🔗 Создаем связи грибов с характеристиками...")
        
        # Очищаем старые связи
        MushroomCharacteristic.objects.all().delete()
        
        # Словарь характеристик для быстрого доступа
        chars = {
            'cap_shape': Characteristic.objects.get(name='cap_shape'),
            'cap_color': Characteristic.objects.get(name='cap_color'),
            'gills_color': Characteristic.objects.get(name='gills_color'),
            'stem_ring': Characteristic.objects.get(name='stem_ring'),
            'milk': Characteristic.objects.get(name='milk'),
            'habitat': Characteristic.objects.get(name='habitat'),
        }
        
        # Данные для связей: гриб -> характеристики
        mushroom_characteristics = {
            'Зонтик пестрый': {
                'cap_shape': 'umbrella',
                'cap_color': 'brown_scaly', 
                'gills_color': 'white',
                'stem_ring': 'movable',
                'milk': 'none',
                'habitat': 'meadow'
            },
            'Хлорофиллум свинцовошлаковый': {
                'cap_shape': 'umbrella',
                'cap_color': 'white',
                'gills_color': 'green', 
                'stem_ring': 'fixed',
                'milk': 'none',
                'habitat': 'meadow'
            },
            'Рыжик настоящий': {
                'cap_shape': 'funnel',
                'cap_color': 'orange',
                'gills_color': 'orange',
                'stem_ring': 'none',
                'milk': 'orange',
                'habitat': 'coniferous'
            },
            'Млечник жгуче-едкий': {
                'cap_shape': 'convex', 
                'cap_color': 'white',
                'gills_color': 'white',
                'stem_ring': 'none',
                'milk': 'white_burning',
                'habitat': 'deciduous'
            },
            'Опёнок осенний': {
                'cap_shape': 'convex',
                'cap_color': 'red_brown',
                'gills_color': 'white',
                'stem_ring': 'fixed', 
                'milk': 'none',
                'habitat': 'wood'
            },
            'Ложноопёнок серно-желтый': {
                'cap_shape': 'bell',
                'cap_color': 'yellow',
                'gills_color': 'green',
                'stem_ring': 'none',
                'milk': 'none',
                'habitat': 'wood'
            },
            'Лисичка обыкновенная': {
                'cap_shape': 'funnel',
                'cap_color': 'yellow', 
                'gills_color': 'yellow',
                'stem_ring': 'none',
                'milk': 'none',
                'habitat': 'mixed'
            },
            'Ложная лисичка': {
                'cap_shape': 'convex',
                'cap_color': 'orange',
                'gills_color': 'orange',
                'stem_ring': 'none',
                'milk': 'none', 
                'habitat': 'wood'
            },
            'Подберёзовик': {
                'cap_shape': 'convex',
                'cap_color': 'brown_scaly',
                'gills_color': 'white',
                'stem_ring': 'none',
                'milk': 'none',
                'habitat': 'birch'
            },
            'Желчный гриб': {
                'cap_shape': 'convex',
                'cap_color': 'brown_scaly', 
                'gills_color': 'pink',
                'stem_ring': 'none',
                'milk': 'none',
                'habitat': 'coniferous'
            },
            'Груздь настоящий': {
                'cap_shape': 'funnel',
                'cap_color': 'white',
                'gills_color': 'white',
                'stem_ring': 'none',
                'milk': 'white_yellowing',
                'habitat': 'birch'
            },
            'Волнушка розовая': {
                'cap_shape': 'funnel',
                'cap_color': 'pink_zones',
                'gills_color': 'pink', 
                'stem_ring': 'none',
                'milk': 'white_burning',
                'habitat': 'birch'
            }
        }
        
        created_count = 0
        for mushroom_name, char_data in mushroom_characteristics.items():
            try:
                mushroom = Mushroom.objects.get(russian_name=mushroom_name)
                
                for char_name, option_value in char_data.items():
                    characteristic = chars[char_name]
                    try:
                        option = CharacteristicOption.objects.get(
                            characteristic=characteristic,
                            value=option_value
                        )
                        
                        MushroomCharacteristic.objects.create(
                            mushroom=mushroom,
                            characteristic=characteristic,
                            option=option
                        )
                        created_count += 1
                        
                    except CharacteristicOption.DoesNotExist:
                        self.stdout.write(
                            self.style.WARNING(f"   Опция не найдена: {char_name}={option_value}")
                        )
                
                self.stdout.write(f"   Созданы связи для: {mushroom_name}")
                
            except Mushroom.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(f"   Гриб не найден: {mushroom_name}")
                )
        
        self.stdout.write(
            self.style.SUCCESS(f"✅ Создано {created_count} связей гриб-характеристика!")
        )