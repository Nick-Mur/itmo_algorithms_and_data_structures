### Задание №4: Прошитый ассоциативный массив   
## Вариант 14   
 
## Задание   
Реализовать ассоциативный массив с поддержкой следующих операций:   
- Добавление или обновление значения по ключу (`put x y`).   
- Получение значения по ключу (`get x`) или <none>, если ключ отсутствует.   
- Получение значения по предыдущему ключу (`prev x`) или <none>.   
- Получение значения по следующему ключу (`next x`) или <none>.   
- Удаление ключа (`delete x`).   
 
Ассоциативный массив должен поддерживать эффективное выполнение операций над ключами, упорядоченными по возрастанию.   
 
## Input / Output   
 
| Input                       | Output              |   
|------------------------------|---------------------|   
| put x 10 \n get x            | 10                 |   
| put y 20 \n next x           | 20                 |   
| put z 30 \n prev z           | 20                 |   
| delete y \n get y            | <none>           |   
 
## Ограничения по времени и памяти   
 
- Ограничение по времени: 1 сек.   
- Ограничение по памяти: 64 МБ.   
 
## Запуск проекта   
 
1. Клонируйте репозиторий:   
   
bash   
   git clone https://github.com/username/repository-name.git   
   
   
 
2. Перейдите в папку с проектом:   
   
bash   
   cd repository-name/lab6/task4   
   
   
 
3. Запустите программу:   
   
bash   
   python src/main.py   
   
   
 
4. Для запуска тестов выполните:   
   
bash   
   pytest tests/   
   
   
 
--- 