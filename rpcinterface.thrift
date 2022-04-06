/**
* Микросервис позволяет давать задания на вычисления в очередь celery и 
* отображает параметры хоста: cpu load, memory load и прочее
*/
namespace py prcinterface
/**
* структура результата задачи
*/
struct calcResult {
  /**
  * UUID задачи
  */
  1: str id,
  /**
  * статус выполнения задачи (строка константа)
  */
  2: str status,
  /**
  * время постановки задачи в очередь
  */
  3: str pushtime,
  /**
  * время начала вычисления (опционально)
  */
  4: optional str starttime,
  /**
  * время завершения вычисления (опционально)
  */
  5: optional str stoptime,
  /** 
  * текущий результат (опционально)
  */
  6: optional double result
}

/*
* Исключение в случае не верного id задачи
*/
exception BadTask {
  /**
  * The problem uuid
  */
  1: string       uuid,
  /**
  * Сервисный код
  */
  2: i16          error_code
} 

//Микросервисы
service RPCService {
  /**
  * Запустить вычисление числа Pi с заданной точностью
  * 
  * @param decimal количество цифр после запятой
  * @return UUID задачи в очереди
  */
  str startCalcPi(1: i8 decimal)
  /**
  * Получить результат задачи по UUID
  *
  * @param uuid идентификатор задачи в очереди
  * @return отчет о задаче в очереди 
  * @throws BadTask отсутствие идентификатора задачи
  */
  calcResult getTaskStatus(1: str uuid)
     throws (1: BadTask bt) 
  /**
  * Получить список всех задач
  *
  * @return список всех задач в очереди
  */
  list<calcResult> listTask()
}