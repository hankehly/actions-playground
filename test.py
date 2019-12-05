import unittest

from pydantic import BaseModel, ValidationError


class AddArgs(BaseModel):
    x: int
    y: int


def add(args: AddArgs):
    return args.x + args.y


class ATestCase(unittest.TestCase):
    """
    An example test case
    """

    def test_ok(self):
        act = add(AddArgs(x=1, y=1))
        self.assertEqual(act, 2)

    def test_err(self):
        with self.assertRaises(ValidationError):
            args = AddArgs(x="not an integer", y=1)
            add(args)


if __name__ == "__main__":
    unittest.main()
