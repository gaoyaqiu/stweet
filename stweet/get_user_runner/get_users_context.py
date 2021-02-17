"""Domain TweetsByIdsContext class."""

from dataclasses import dataclass, field
from typing import Optional, List, Tuple


@dataclass
class GetUsersContext:
    """Domain TweetsByIdsContext class."""

    scrapped_count: int = 0
    usernames_with_error: List[Tuple[str, Exception]] = field(default_factory=list)

    def add_one_scrapped_user(self):
        """Method raise counter of all scrapped tweets."""
        self.scrapped_count += 1

    def add_user_with_scrap_error(self, username: str, exception: Exception):
        """Method add user with raised exception."""
        self.usernames_with_error.append((username, exception))
