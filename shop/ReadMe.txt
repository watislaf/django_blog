Глава7 Стр226 Сделаем свой магазин!
Добавим модель категорий и товаров, добавим их в адмнике. Добавим urls, и get_url via reverse method.
Сделаем по страничке и на ней все разместим. Ничего сложного.

Теперь сделаем свою тележку, для этого будем использовать Django session ( django.contrib.sessions.middleware.SessionMiddleware )

request.session['foo'] = 'bar'
Retrieve a session key as follows:
request.session.get('foo')
Delete a key you previously stored in the session as follows:
del request.session['foo']

• SESSION_COOKIE_AGE: The duration of session cookies in seconds.
The default value is 1209600 (two weeks).
• SESSION_COOKIE_DOMAIN: The domain used for session cookies. Set this to
mydomain.com to enable cross-domain cookies or use None for a standard
domain cookie.
• SESSION_COOKIE_SECURE: A Boolean indicating that the cookie should only
be sent if the connection is an HTTPS connection.
• SESSION_EXPIRE_AT_BROWSER_CLOSE: A Boolean indicating that the session
has to expire when the browser is closed.
• SESSION_SAVE_EVERY_REQUEST: A Boolean that, if True, will save the session
to the database on every request. The session expiration is also updated each
time it's saved.

245 каретка. 18.07
Теперь мы берём, создаём обьект и формочку, view и так далее. Классика. В некоторых местах хитро добавляем формочку,
делаем ей невидимый аргумент, который мы можем указывать скрытно.

    Необходимо изменить состояние каретки на всех страницах. Используем context processor, он уже встроен в installed
apps. Эта штука создаст нам обьект на всех страницах через request.

    После готового заказа, его надо оформить. Сделаем новый проект orders. Этот проект имеет в себе обьект Заказаз и
вещь заказа. Сохраняется через формочку.

263 19.07
    Celery - позволяет делать асинхронные запросы. То есть, отвечать html сразу и всё ещё обробатывать
какую-нибудь часть кода.

269
    Оплата кредиткой. Для этого используем сторонний сервис, такой как Braintree.
    pip install braintree. Уже есть готовая библа для джанго и этой шутки, добавим все необходимые настройки.
получаем токен и обробатываем его в js коде. Вся инструккция по js коду 279


284 20.07
    Собственные действия на админке. orders, admin.py. Добавим создание cvs файла. Добавили функцию, которая получает
    три обьекта, работая с ними вернём ответ.

287
    Создадим свои вьюшки для админки. Там ты просто создаём свою ссылку и так же extand стили админки.
    Так же мы можем сделать редирек, например вместо свойства (290) добавить в админку функцию на перенаправление.

292
    WeasyPrint позволяет сделать Pdf файлики через сайтик. Там мы используем функцию, которая рендерит страницу .html
     используя обьект. Так же мы использовали html - to pdf и прикрепили его к request. Отправим этот pdf по почте.
     Однако у нас проблемы с GTK на винде, поэтому мы идём дальше.

301 - купоны и скидки.
