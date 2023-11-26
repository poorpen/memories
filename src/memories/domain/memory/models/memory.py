from datetime import datetime, timezone
from typing import Optional

from memories.domain.memory.value_objects import text_block, media
from memories.domain.memory import exceptions


class Memory:
    def __init__(
        self,
        title: text_block.Title,
        text: text_block.Text,
        photo: media.Photo,
        owner_id: int,
        deleted: Optional[bool] = None,
        create_at: Optional[datetime] = None,
    ):
        self.title = title
        self.text = text
        self.photo = photo
        self.owner_id = owner_id
        self.deleted = deleted or False
        self.create_at = create_at or datetime.now(timezone.utc)

    def update_text_block(
        self,
        title: Optional[text_block.Title] = None,
        text: Optional[text_block.Text] = None,
    ) -> None:
        self._check_deleted()
        if title:
            self.title = title
        if text:
            self.text = text

    def update_media(self, photo: Optional[media.Photo] = None) -> None:
        self._check_deleted()
        if photo:
            self.photo = photo

    def delete(self) -> None:
        self._check_deleted()
        self.deleted = True

    def _check_deleted(self) -> None:
        if self.deleted:
            raise exceptions.MemeryIsDeleted()
