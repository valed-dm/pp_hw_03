## ДЗ №3

### Scoring API: выполнено.

Как использовать приложение:

```commandline
 python api.py --help
```

```text
usage: api.py [-h] [-p PORT] [-l LOG]

server port, log file setup

options:
  -h, --help            show this help message and exit
  -p PORT, --port PORT
  -l LOG, --log LOG
```

При запуске можно указать порт и путь к log-файлу.
В противном случае  порт сервера по умолчанию 8080, лог в stdout.

Работа API соответствует ТЗ, тесты пройдены:

[<img src="images/img_01.png" width="1000"/>](images/img_01.png)

Себе на заметку: при валидации нужно учитывать

```code
var = 0
if var: # erroneous result due to falsy value; var is not empty
```
