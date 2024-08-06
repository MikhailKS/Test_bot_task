from backend.models.models import MessagesModel


def list_serial(collections) -> list:
    """
    :param collections: input collection object from database
    :return: list of collections elements
    """
    return [MessagesModel.from_mongo(collection) for collection in collections]