import sys
import traceback
from importlib import import_module

if __name__ == "__main__":
    try:
        module_name = sys.argv[1]
        function_name = sys.argv[2]
        args = sys.argv[3:]
    except BaseException:
        print("Celery task not provided.")
        sys.exit(2)

    try:
        module = import_module(module_name)
        function = module.__getattribute__(function_name)

        print(f"Running task: #{module} #{function} #{args}")
        if callable(function) and "apply_async" in dir(function):
            task = function.apply_async(args=args)
            result = task.wait()
            if isinstance(result, BaseException):
                raise result
            else:
                print(result)
        else:
            print("Function provided is not a callable task.")
            sys.exit(2)
    except BaseException:
        type, value, trace = sys.exc_info()
        traceback.print_exception(type, value, trace)
        sys.exit(1)
    else:
        sys.exit(0)
