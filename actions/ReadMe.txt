Стр 198 16 07

Создадим отслеживание действий на сайте, прямо как у FaceBook. Для этого создадим новый проект.

Мы хотели бы в действиях отслеживать user X bookmarked image Y or user X is now following user Y
То может быть любой моделью. Для достижения этого фунцкцронала воспольщуемся contenttypes framework. Оно уже
влключено в наш проект, так как используется auth.

>>> from django.contrib.contenttypes.models import ContentType
>>> image_type = ContentType.objects.get(app_label='images',
model='image')
>>> image_type
<ContentType: images | image>

Теперь в моделе у нас есть обьект с обьеденённым полем, описсывающим действия. Так же добавим функцию для
изи создания обьектов.
Добавим их в dash_board. Так же есть метод
(one to one)select_related -> который делает выборку из обьектов достаточно бустро.
Тоже самое, то Many to Manu prefetch_related.

    211 стр. В джанго есть незаменимые сигналы.
pre_save and post_save are sent before or after calling the save() method
    of a model
• pre_delete and post_delete are sent before or after calling the delete()
    method of a model or QuerySet
• m2m_changed is sent when a ManyToManyField on a model is changed

Сделаем сигнал и в apps пропишем инклуд по ready чтобы подключить эти сигналы.

215 redis

    Редис эт быстрая датабаза, которая позволяет хранить разыне данные. На винду ставить её западлу.