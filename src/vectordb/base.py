from abc import ABC, abstractmethod
from typing import List, Optional
from langchain.vectorstores import VectorStore
from langchain.schema.embeddings import Embeddings


class BaseVectorDB(ABC):
	@abstractmethod
	def __init__(self, user_id: str, embedder: Optional[Embeddings] = None):
		"""
		"""

	@abstractmethod
	def get_user_client(
			self,
			user_id: str,
			embedder: Optional[Embeddings] = None  # use this embedder if not None or use global embedder
		) -> Optional[VectorStore]:
		"""
		Creates and returns the langchain vectordb client object for the given user_id.

		Args
		----
		user_id: str
			User ID for which to create the client object.
		embedder: Optional[Embeddings]
			Embeddings object to use for embedding documents.

		Returns
		-------
		Optional[VectorStore]
			Client object for the VectorDB or None if error occurs.
		"""

	@abstractmethod
	def setup_schema(self, user_id: str) -> None:
		"""
		Sets up the schema for the VectorDB

		Args
		----
		user_id: str
			User ID for which to setup the schema.

		Returns
		-------
		None
		"""

	@abstractmethod
	def delete_sources(self, user_id: str, source_names: List[str]) -> bool:
		"""
		Deletes all sources with the given names.

		Args
		----
		user_id: str
			User ID for which to delete the sources.
		source_names: List[str]
			List of source names to delete.

		Returns
		-------
		bool
			True if deletion is successful,
			False otherwise
		"""
