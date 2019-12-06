import unittest

from pydantic import BaseModel, ValidationError


class AddArgs(BaseModel):
    x: int
    y: int


def subtract(args: AddArgs):
    return args.x - args.y


class App2TestCase(unittest.TestCase):
    """
    An example test case
    """

    def test_ok(self):
        act = subtract(AddArgs(x=2, y=1))
        self.assertEqual(act, 1)

    def test_err(self):
        with self.assertRaises(ValidationError):
            args = AddArgs(x="not an integer", y=1)
            subtract(args)


if __name__ == "__main__":
    unittest.main()
