#библиотеки, которые загружаем из вне
import telebot
TOKEN = '6659031789:AAFGvbid5bXThMZCgTP25WEppdKIvAp90Po'


from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('QA.png', 'rb')
	bot.send_photo(message.chat.id, sti)
    #клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Операторы SQL")
	item2 = types.KeyboardButton("Операторы Linux")
	item3 = types.KeyboardButton("Операторы Git")
	item4 = types.KeyboardButton("Структура багрепорта")
	item5 = types.KeyboardButton("Типы данных Json")
	markup.add(item1, item2, item3, item4)
	bot.send_message(message.chat.id, "Привет тебе от помощника Джека , {0.first_name}!".format(message.from_user, bot.get_me()),
    parse_mode='html', reply_markup=markup)
    #назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':

		if message.text == 'Операторы SQL':
			foto = open("sql.png", "rb")
			bot.send_photo(message.chat.id, foto)
			bot.send_message(message.chat.id, 
            '''*SELECT* - _Какой столбик вывести_,

    *FROM* - _Из какой таблички вывести_ 

*JOIN* - _Какую табличку добавляем_

    *ON*- _Название столбика из одной таблицы_

*WHERE* - _Какой столбик известен из текста вопроса = его 
                   значение (AND-и OR-или)_

    *ORDER BY* - _Столбец по которому сортировать_

*LIMIT*- _Число, ограничение выборки (правило хорошего тона,
                чтобы не повесить БД)_

    *UPDATE* - _Название таблицы_

*SET* - _Какой столбик меняем = новое значение_

			            *Агрегатные функции*
*COUNT()* - _Количество_

    *MIN()* - _Минимальное значение_

*MAX()* - _Максимальное значение_

    *AVG()* - _Среднее значение_

*SUM()* - _Сумма_

			            *Виды JOIN*
*INNER JOIN* - _Вернет данные у которых есть пара_

     *LEFT JOIN* - _Вернет данные у которых есть пара и данные 
	                          без пары из левой таблицы_

*RIGHT JOIN* - _Выдает данные, у которых есть пара и данные без 
                          пары из правой таблицы_

    *FULL JOIN* - _Выдает данные у которых ,как есть пара так и нет 
	                         пары_

*CROSS JOIN* - _Выдает комбинацию каждой строки в 1 таблице со 
                          всеми записями во 2 таблице_

    *★* - _Выводит все_ ''', parse_mode="Markdown")




		elif message.text == 'Операторы Linux':
			foto = open("Linux.png", "rb")
			bot.send_photo(message.chat.id, foto)
			bot.send_message(message.chat.id, 
'''*pwd* - _Показать текущее местоположение (папку)_

    *cd* - _Сменить папку (change direktory)_

*cd ..* - _Вернуться на уровень выше_

    *ls* - _Просмотр содержимого папки_

    *mkdir* - _Создать новую папку_

*mv* - _Переместить или переименовать файл_

    *cp* - _Копировать файл_

*touch* - _Создать файл_

    *rm* - _Удаление файла_

*rmdir* - _Удаление папки_

    *cat* - _Предосмотр содержимого_

*grep* - _Фильтр_

    *tail* - _Выведи последние N строк_

*head* - _Выведи первые N строк_

    *vim nano* - _Открыть или редактировать текстовый файл_

                *УПРАВЛЕНИЕ в vim*:
*i* - _Активировать режим редактора (появится внизу надпись INSERT)_

*esc* - _Закончить режим редактора (исчезнет внизу надпись INSERT)_

*esc + :wq + enter* - _Выйти и сохранить (при вводе этой команды она будет видна внизу терминала)_

*esc + :q! + enter* - _Выйти без сохранений (при вводе этой команды она будет видна внизу терминала)_

''', parse_mode="Markdown")



		elif message.text == 'Операторы Git':
			foto = open("Git.png", "rb")
			bot.send_photo(message.chat.id, foto)
			bot.send_message(message.chat.id, 
'''*git init* - _Сделать из любой папки git папку_

	*git clone* - _Скачать на компьютер репозиторий_

*git branch* - _Показать в какой ты сейчас ветке_ 

    *git pull* - _Скачать обновления с репозитория_

*git checkout -b* - _Переключиться на новую ветку_

	*git add* - _Добавить в текущий коммит новые файлы или папки которых раннее не было_

*git commit -m* - _Создать коммит (сохранить текущее состояние)_

	*git push* - _Запушить (отправить) твои изменения в репозиторий_

*git status* - _Узнать в какой ветке ты сейчас находишься_ 

	*git log* - _Показывает какие файлы ты изменил_

*git merge master* - _Влить в мою ветку , ветку мастер_

	*git reset -hard* - _Отменить коммит_

		Как запушить изменения:
*ctrl+s* - _Сохранить изменения в IDE (редакторе кода)_

	*git add .* - _Выполнить_

*git commit -m* - _"Название нового коммита"_

	*git push* - _Выполнить_
	
''', parse_mode="Markdown")



		elif message.text == 'Структура багрепорта':
			foto = open("Bug.png", "rb")
			bot.send_photo(message.chat.id, foto)
			bot.send_message(message.chat.id, 
'''*1.~Summary (Заголовок)* - [bug] [web] [прод] - Заголовок. Что , где и при каких условиях?

*2.~Description (описание)* - пример, нет картинок у новостей на сайте на главной

*3.~Шаги воспроизведения(глаголы в инфинитиве)* - 1.Открыть сайт 2.Обновить страницу и т.д.

*4.~Текущий результат* - Можно описать словами , желательно еще скриншотом или скринкастом

*5.~Ожидаемый результат* - Можно словами или скриншот (или ссылка на макет)

*6.~Окружение* - 1.Билд(это версия приложения, сайта или бекенда,если знаем). 2.Только ios или android или на обеих платформах. 3. Браузер (какой, какая версия)

*7.~Тестовые устройства* - Например(Макбук16, андроид 10 ксиоми экр. 6 дюймов)

*8.~Ручка(чаще для баг репорта на бекенд)* - Курл запроса

*9.~Аналитика* - Если бы я у вас работал то прикрепил бы ссылку на яндекс метрику с количеством пользователей, которых зааффектила проблема

*10.~Документация* - Если бы я у вас работал то прикрепил бы ссылку на документацию по фиче 

*11.~Логи(Кибана) или (Сентри)* - Если бы я у вас работал то прикрепил ссылку на логи из Кибаны или Сентри

*12.~Slack или Дискорд (ссылка на тренд)* - Если бы я у вас работал , то прикрепил ссылку обсуждения этого бага в Slack

*13.~Priority(приориретет)* - Минор, Нормал ,Блокер 

*14.~Severity (Серьезность)* - Блокер, Критикал, Нормал, Минор, Тривиал

*15.~Followers (наблюдатели)* - Босс, Менеджер

*16.~Assignee (ответственный)* - На кого назначим
			
			''', parse_mode="Markdown")
			
		else:
			bot.send_message(message.chat.id,'Я не знаю что на это ответить')



bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods
