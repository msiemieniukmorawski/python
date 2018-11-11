import io
from contextlib import redirect_stdout

def get_print_output(tested_func, *args):

    memory_buffer = io.StringIO()

    with redirect_stdout(memory_buffer):

        tested_func(*args)

        return memory_buffer.getvalue()

