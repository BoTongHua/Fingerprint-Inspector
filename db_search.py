from pymongo import MongoClient


def search(fingerprint):
    """
    A method searches for registered criminal person whose fingerprint matches with the imported one.

    example fingerprint: "2__M_index_finger.BMP"
    """
    client = MongoClient("localhost", 27017)
    db = client.criminal_record
    suspects = db.suspects

    for person in suspects.find({"fingerprint": fingerprint}):
        return person
