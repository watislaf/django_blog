# django_blog
Django project июль 2020. 
Сервер работает до конца лета 2020.

Коротко 
![image](https://user-images.githubusercontent.com/45079123/91281591-f500d200-e790-11ea-98d7-bff2207261a5.png)

Сайт лежит на сервере Яндекс Обалка, подключение по домену gigglingpenguin.me, имеется корпоративная почта. Поддерживается протокол https. На самом сервере установлен nginx и подключение через gunicorn, настроен фаервол и используется база данных postgresql, ошибки сайта остлеживаются через сервис SENTRY, некоторые части сайта переведены на английский и русский. Сайт включает в себя Магазин/блог/чат/добавление постов и их лайкание/мини новостная лента основанная на подписке.
Чат работает на channels и вебсокетах. Так же на сервере сайт упокован в Docker containter.
____

![image](https://user-images.githubusercontent.com/45079123/91281454-c71b8d80-e790-11ea-99c4-5428919fffb7.png)

Регистрация проходит через подтверждение почты или через соцсети, отправка почты по протоколу smtp. 

![image](https://user-images.githubusercontent.com/45079123/91281818-31ccc900-e791-11ea-954b-875ba8cc15c4.png)

Есть возможность восстановить пароль/сменить данные. А так же поставить аватарку.

![image](https://user-images.githubusercontent.com/45079123/91281954-5aed5980-e791-11ea-8ea5-41fa78071a68.png)

Вести свой блог, и оставлять блогам комментарии

![image](https://user-images.githubusercontent.com/45079123/91282014-6f315680-e791-11ea-9769-7ba17a32cb7a.png)

Выставлять фотографии 

![image](https://user-images.githubusercontent.com/45079123/91282090-883a0780-e791-11ea-8a3b-83dc3c388fa7.png)

А так же их лайкать

![image](https://user-images.githubusercontent.com/45079123/91282130-98ea7d80-e791-11ea-9825-55c1e139241f.png)

Видеть всех людей.

![image](https://user-images.githubusercontent.com/45079123/91282204-b61f4c00-e791-11ea-80a6-ad161776ed63.png)

Подписываться на них и узнавать какие фотографии они постили.

![image](https://user-images.githubusercontent.com/45079123/91282254-c7685880-e791-11ea-9d6d-d752f72d2e29.png)

Имеется магазин.

![image](https://user-images.githubusercontent.com/45079123/91282319-dea74600-e791-11ea-8321-b3b148545bff.png)

В котором можно добавлять товары в тележку и оформлять заказ. 

![image](https://user-images.githubusercontent.com/45079123/91282379-ef57bc00-e791-11ea-8dce-9531cc25938c.png)

Система оплаты поддерживается API от paypal. 

![image](https://user-images.githubusercontent.com/45079123/91282446-05fe1300-e792-11ea-9f2c-bef6b958a4e4.png)

Чат на вебсокетах и channels для асинхронной работы

![image](https://user-images.githubusercontent.com/45079123/91286411-182e8000-e797-11ea-8dac-de903bf89e90.png)













# Источники

Книга Django_3_By_Example_Build_powerful_and_reliable_Python_web_applications

https://pythonru.com/primery/blog-na-django-22-rendering-form-v-shablonah -- статьи

https://www.youtube.com/watch?v=WTXPLwrK398&list=PLF-NY6ldwAWrb6nQcPL21XX_-AmivFAYq&index=7 -- видеоролики
