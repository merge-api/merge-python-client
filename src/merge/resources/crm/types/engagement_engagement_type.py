# This file was auto-generated by Fern from our API Definition.

import typing

from .activity_type_enum import ActivityTypeEnum
from .engagement_type import EngagementType
from .engagement_type_activity_type import EngagementTypeActivityType
from .field_format_enum import FieldFormatEnum
from .field_type_enum import FieldTypeEnum
from .item_format_enum import ItemFormatEnum
from .item_schema import ItemSchema
from .item_type_enum import ItemTypeEnum
from .remote_field import RemoteField
from .remote_field_class import RemoteFieldClass
from .remote_field_class_field_choices_item import RemoteFieldClassFieldChoicesItem
from .remote_field_class_field_format import RemoteFieldClassFieldFormat
from .remote_field_class_field_type import RemoteFieldClassFieldType
from .remote_field_remote_field_class import RemoteFieldRemoteFieldClass

EngagementEngagementType = typing.Union[str, EngagementType]
