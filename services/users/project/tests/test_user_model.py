# services/users/project/tests/test_user_model.py


import unittest

from project import db
from project.api.models import User
from project.tests.base import BaseTestCase
from sqlalchemy.exc import IntegrityError


class TestUserModel(BaseTestCase):

    def test_add_user(self):
        user = User(
                username='justatest',
                email='test@test.com',
                password="greaterthaneight"
        )
        db.session.add(user)
        db.session.commit()
        self.assertTrue(user.id)
        self.assertEqual(user.username, 'justatest')
        self.assertEqual(user.email, 'test@test.com')
        self.assertTrue(user.active)

    def test_add_user_duplicate_username(self):
        user = User(
                username='justatest',
                email='test@test.com',
                password="greaterthaneight"
        )
        db.session.add(user)
        db.session.commit()
        duplicate_user = User(
                username='justatest',
                email='test@test2.com',
                password="greaterthaneight"

        )
        db.session.add(duplicate_user)
        with self.assertRaises(IntegrityError):
            db.session.commit()

    def test_add_user_duplicate_email(self):
        user = User(
                username='justatest',
                email='test@test.com',
                password="greaterthaneight"
        )
        db.session.add(user)
        db.session.commit()
        duplicate_user = User(
                username='justanothertest',
                email='test@test.com',
                password="greaterthaneight"
        )
        db.session.add(duplicate_user)
        with self.assertRaises(IntegrityError):
            db.session.commit()

    def test_to_json(self):
        user = User(
                username='justatest',
                email='test@test.com',
                password="greaterthaneight"
        )
        db.session.add(user)
        db.session.commit()
        self.assertTrue(isinstance(user.to_json(), dict))


if __name__ == '__main__':
    unittest.main()
