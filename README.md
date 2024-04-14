# Terms
1.Хост - ip адрес сервера(-ов) которые являются главными в данной системе, на них происходят основные операции: сохранение файлов, процесс оптимизации.

2.Нода - ip адрес сервера(-ов) которые являеются зависимыми от хоста, принимают команды для выполнения и после процесса моделирования с них собирается результаты и отправляются на хост.

# Use
Для использования данного продукта необходимо сделать следущее:

1.Установить Gitbash или аналог, для взаимодействия с bash'ом.

2.Установить anaconda/miniconda.

3.Запустить скрипт для установки основных зависимостей и создания окружения.
```bash
sh env_deploy/gitbash.sh
```
После выполнения данного скрипта, конфиг в файле .bash_profile будет полностью перезаписан, если вам нужно дозаписать новые строки, то измените в файле `gitbash.sh` строки с >> на >. `В строку 15 вставить путь к папке с скриптами`

4.Выполнить команду `pip install -r requirements.txt`

5.Запустить на нодах сервер
- `sh node.sh` для запуска в фоне
- `python run_worker.py` для запуска в обычном режиме

6.На хосте запустить `python main.py --epoch n`, где n - количество запусков моделирования.

7.В конечном результате будет получено n\*k моделей, где n - количество итераций, k количество машин.
 
# Struct
Структура проекта:

 1.`autogui.py` файл отвечающий за взаимодействие с интерфейом tNavigator'а.
 
 Необходимо заменить пути к вашим файлам 
 - `строка 9 - путь к tnavigator'у`
 - `строка 26 - путь к папке с данными`
 - `строка 52 - изменить имя ПК`
 - `строка 63 - путь к папке с продуктом`*
 
 2.`create_graph.py` файл отвечающий за построение графиков по дебиту нефти.
 
 3.`file_client.py` файл отвечающий за отправку файлов с результатами моделирования на хост, а так же отправку файла с параметрами для моделирования на ноды.
 
 - Если ip адрес переданный в функцию находится в списке хостов, тогда происходит отправка с ноды на хост результата моделирования.
 - Если ip адрес переданный в функцию находится в списке нод, тогда происходит отправка с хоста на ноды сгенерированных файлов для последующего моделирования
 - Передача файлов происходит при помощи протокола TCP и только в бинарном формате

4.`file_server.py` файл отвечающий за организацию сервера и ожидания подключений с целью отправки файла.

5.`optimizer.py` файл отвечающий за перебор 4 параметров(по функции Кори)

6.`run_worker.py` файл отвечает за поднятие сервера, необходимого для работы скриптов.(работает в виде службы  см. п9)

7.`send_to_workers.py` файл отвечает за отправление команды с хостов на ноды, для запуска основного сценария(`main.py`)

8.`settings.py` файл с конфигурациями

- `port` порт через который будет происходить взаимодействие в локальной сети
- `hosts` список состоящий из ip адресов пк, являющихся главными компьютерами( >1 пк не тестировалось)
- `workers` список состоящий из ip адресов пк, являющихся зависимыми(нодами)*

9.`node.sh` файл отвечающий за поднятие сервера в фоновом режиме.
