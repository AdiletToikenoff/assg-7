from abc import ABC, abstractmethod

# Document storage interface
class DocumentStorage(ABC):
    @abstractmethod
    def upload_document(self, document):
        pass

    @abstractmethod
    def download_document(self, document_id):
        pass

    @abstractmethod
    def edit_document(self, document_id, content):
        pass

    @abstractmethod
    def search_documents(self, query):
        pass

# Document class
class Document:
    def __init__(self, document_id, content):
        self.document_id = document_id
        self.content = content

# Proxy for document storage
class DocumentStorageProxy(DocumentStorage):
    def __init__(self, document_storage, user):
        self.document_storage = document_storage
        self.user = user

    def upload_document(self, document):
        if self.user.has_permission("upload"):
            self.document_storage.upload_document(document)
        else:
            print("You don't have permission to upload documents.")

    def download_document(self, document_id):
        if self.user.has_permission("download"):
            return self.document_storage.download_document(document_id)
        else:
            print("You don't have permission to download documents.")

    def edit_document(self, document_id, content):
        if self.user.has_permission("edit"):
            self.document_storage.edit_document(document_id, content)
        else:
            print("You don't have permission to edit documents.")

    def search_documents(self, query):
        if self.user.has_permission("search"):
            return self.document_storage.search_documents(query)
        else:
            print("You don't have permission to search documents.")

# User class
class User:
    def __init__(self, username, permissions):
        self.username = username
        self.permissions = permissions

    def has_permission(self, permission):
        return permission in self.permissions

# Example usage
if __name__ == "__main__":
    # Create a user
    user = User("Alice", ["upload", "download", "edit", "search"])

    # Create a document storage proxy
    document_storage_proxy = DocumentStorageProxy(DocumentStorage(), user)

    # Upload a document
    document = Document(1, "Sample document content")
    document_storage_proxy.upload_document(document)

    # Download a document
    document_content = document_storage_proxy.download_document(1)
    print(document_content)

    # Edit a document
    document_storage_proxy.edit_document(1, "Edited document content")

    # Search documents
    documents = document_storage_proxy.search_documents("sample")
    print(documents)
