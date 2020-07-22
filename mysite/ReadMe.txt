 314 стр  20.14
internationalization and localization
internationalization - позиция по времени
Localization - язык
Сначала мы делаем makemessages который собирает все строчки в файл
и уже внутри  этого файла мы их переводим на разные языки.
• makemessages: This runs over the source tree to find all strings marked
for translation and creates or updates the .po message files in the locale
directory. A single .po file is created for each language.
• compilemessages: This compiles the existing .po message files to .mo files
that are used to retrieve translations.

Нам нужен gettext чтобы создавать и редачить. -_-
Добавим в настройки языки и теперь мы все моменты кода можем выделять в функцию для первода.
Создадим папку locale/en,ru в них будут .po и .mo файлы

После сделаем вот так django-admin makemessages --all
• msgid: The translation string as it appears in the source code.
• msgstr: The language translation, which is empty by default. This is where
you have to enter the actual translation for the given string

322 22.07
Внутри мы можем вбить перевод вместо "" и он будет юзаться.
Забив команду django-admin compilemessages. Папка locale может быть не только в главном, но и в дочерних проетках.
Так например добавим locale в папку blog и все пеерводы будут переходить туда.

Так же легко переводятся поля формочек.

Для перевода html юзаем {% blocktrans %}Hello {{ name }}!{% endblocktrans %}

Помимо этого есть интферфейс
pip install django-rosetta==0.9.3
Который позволяет редачить .po файлы. 328 стр. Так же доступна утилита parler для перевода обьектов в django.
Установка языка будет по url /en/
