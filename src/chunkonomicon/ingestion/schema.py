from enum import Enum
from dataclasses import dataclass, field

class BlockType(str, Enum):
    DIALOGUE = "dialogue"
    VOCAB_LIST = "vocab_list"
    GRAMMAR_POINT = "grammar_point"
    EXERCISE = "exercise"
    CULTURAL_NOTE = "cultural_note"

@dataclass
class LessonBlock:
    lesson_number: int
    block_type: BlockType
    heading: str
    content: str
    metadata: dict = field(default_factory=dict)
