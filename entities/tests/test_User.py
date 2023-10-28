from unittest import TestCase

from entities.User import User

user = User("name", "age", "type")


class TestUser(TestCase):
    def test_name(self):
        self.assertEquals(user.name, "name")
        user.name = "set_name"
        self.assertEquals(user.name, "set_name")

    def test_age(self):
        self.assertEquals(user.age, "age")
        user.age = "set_age"
        self.assertEquals(user.age, "set_age")

    def test_type(self):
        self.assertEquals(user.type, "type")
        user.type = "set_type"
        self.assertEquals(user.type, "set_type")
