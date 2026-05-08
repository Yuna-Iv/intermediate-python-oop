import unittest
from unittest.mock import patch, MagicMock

# Functions under test
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b

def get_evens(numbers: list) -> list:
    return [n for n in numbers if n % 2 == 0]

def fetch_user(user_id: int) -> dict:
    import urllib.request
    urllib.request.urlopen(f"https://api.example.com/users/{user_id}")
    return {"id": user_id, "name": "Mock User"}

#Class under test
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be > 0")
        self._balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be > 0")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

# Tests
class TestDivide(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(divide(10, 2), 5.0)

    def test_float(self):
        self.assertAlmostEqual(divide(1, 3), 0.3333, places=4)

    def test_negative(self):
        self.assertEqual(divide(-6, 2), -3.0)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0.0)


class TestGetEvens(unittest.TestCase):

    def test_mixed(self):
        self.assertEqual(get_evens([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_all_odd(self):
        self.assertEqual(get_evens([1, 3, 5]), [])

    def test_empty(self):
        self.assertEqual(get_evens([]), [])

    def test_negatives(self):
        self.assertIn(-4, get_evens([-3, -4, -5]))


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Alice", balance=1000.0)

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 1000.0)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500.0)

    def test_withdraw(self):
        self.account.withdraw(200)
        self.assertEqual(self.account.balance, 800.0)

    def test_deposit_negative_raises(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_withdraw_insufficient(self):
        with self.assertRaises(ValueError) as ctx:
            self.account.withdraw(9999)
        self.assertIn("Insufficient funds", str(ctx.exception))

    def test_multiple_ops(self):
        self.account.deposit(200)
        self.account.withdraw(100)
        self.assertEqual(self.account.balance, 1100.0)


class TestWithMock(unittest.TestCase):

    @patch("urllib.request.urlopen")
    def test_fetch_user_calls_api(self, mock_urlopen):
        mock_urlopen.return_value = MagicMock()
        result = fetch_user(1)
        mock_urlopen.assert_called_once()
        self.assertEqual(result["id"], 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
