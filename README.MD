# MQTT Sensor & Timer

###Утилита для отображения показаний с датчика температуры

* Отбражение показаний датчика температуры
* Предупреждение выхода из диапазона значений
* Таймер времени

###Показания датчика

Значения датчика получаются по MQTT протоколу.
Для подписки на топик с данными задайте настройки MQTT сервера. (кнопка <Settings>)
Кнопка <MQTT> запускает получение данных с сервера.
Для включения режима предупреждения установите пороговые значения min и max и дважды кликните на экране значений датчика.
Экран значений станет зеленым, это означает включение режима предупреждения и нахождение данных в заданном диапазоне.
При выходе значения из диапазона цифры станут красными и включится звуковой сигнал.
Для отключения режима предупреждения дважды кликните на экране значений датчика.

###Таймер

Возможны три режима:
* Текущее время (по умолчанию)
* Таймер на заданное время
* таймер обратного отсчета

Для установки таймера на точное время задайте в верхнем поле время синала.
Дважды кликните на экране таймера. Показания времени станут зелеными.

Для установки таймера в режим обратного отсчета задайте в нижнем поле число минут или часов:минут.
Дважды кликните на экране таймера. Показания времени станут зелеными.