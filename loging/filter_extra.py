import logging


# Определяем свой фильтр, наследуюясь от класса Filter библиотеки logging
class EvenLogFilter(logging.Filter):
    def filter(self, record):
        return not record.i % 2


# Инициализируем логгер
logger = logging.getLogger(__name__)

# Создаем хэндлер, который будет направлять логи в stderr
stderr_handler = logging.StreamHandler()

# Подключаем фильтр к хэндлеру
stderr_handler.addFilter(EvenLogFilter())

# Подключаем хэндлер к логгеру
logger.addHandler(stderr_handler)

for i in range(1, 5):
    logger.warning('Важно! Это лог с предупреждением! %d', i, extra={'i': i})
