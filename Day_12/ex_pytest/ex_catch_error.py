import pytest


# funkcja podnosi tylko błąd
def func():
    raise Exception('lets see if this works')


# testowanie przechwycenia błędu musi odbywać się za pomocą wyrażenia 'with'
def test_error():
    with pytest.raises(Exception):
        func()


# testowany błąd można sprawdzić - np. co do wiadomości
def test_error_2():
    with pytest.raises(Exception) as exc:
        func()
        assert exc.message == 'lets see if this works'
