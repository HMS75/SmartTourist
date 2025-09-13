import hashlib

class MockBlockchain:
    def __init__(self):
        self.issued_ids = set()

    def generate_id(self, tourist_name):
        # hash tourist_name + something unique
        hash_value = hashlib.sha256(tourist_name.encode()).hexdigest()
        self.issued_ids.add(hash_value)
        return hash_value

    def verify(self, hash_value):
        return hash_value in self.issued_ids

# Global blockchain instance
blockchain = MockBlockchain()
