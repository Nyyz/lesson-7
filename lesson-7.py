def func(func1):
  def wrapper(*args):
        res = tuple(
            {
                 "тип": type(arg),
                 "елемент": arg,
                }
            for arg in args if arg == int or str
        )
        return func1(res)
  return wrapper

@func
def func3(f):
    print(f)
func3(1,"hello",2,"hello",3,"hello")