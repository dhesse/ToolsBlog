import unittest
from collections import defaultdict

class MockDB(object):
    def __init__(self):
        self.objects = []
        self.calls = defaultdict(int)
    def update(self, search, newvlas, upsert):
        self.calls['update'] += 1

class MockMongo(object):
    def __init__(self, dictgen):
        self.d = dictgen
    def __getattr__(self, name):
        return self.d[name]
    def __contains__(self, item):
        return item in self.d

def saveOptions(mongo_client, **opts):
    for k in opts:
        mongo_client.myapp.settings.update(
            {'key': k},
            {'$set': {'value': opts[k]}},
            True)

class SaveOptionsTest(unittest.TestCase):
    def setUp(self):
        self.db = MockMongo(defaultdict(
            lambda: MockMongo(
                defaultdict(lambda: MockDB()))))
    def test_uses_right_collection(self):
        saveOptions(self.db, model='svm')
        self.assertTrue('myapp' in self.db)
    def test_uses_right_db(self):
        saveOptions(self.db, model='svm')
        self.assertTrue('settings' in self.db.myapp)
    def test_calls_update(self):
        saveOptions(self.db, model='svm', S=5)
        self.assertEqual(self.db.myapp.settings.calls['update'], 2)

if __name__ == '__main__':
    unittest.main()
