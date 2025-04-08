from typing import Optional, List
from pydantic import BaseModel, Field


class Person(BaseModel):
  """Information about a person."""

  # ^ Doc-string for the entity Person.
  # This doc-string is sent to the LLM as the description of the schema Person,
  # and it can help to improve extraction results.

  # Note that:
  # 1. Each field is an `optional` -- this allows the model to decline to extract it!
  # 2. Each field has a `description` -- this description is used by the LLM.
  # Having a good description can help improve extraction results.
  name: Optional[str] = Field(default=None, description="The name of the person")
  hair_color: Optional[str] = Field(
    default=None, description="The color of the person's hair if known"
  )
  height_in_meters: Optional[str] = Field(
    default=None, description="Height measured in meters. The height must have only 2 decimal point."
  )
  total_children: Optional[str] = Field(
    default=None,
    description="The number of children the person has."
  )
  children: Optional[List[str]] = Field(
    default=None,
    description="The name of person's children."
  )
  mother: Optional[str] = Field(
    default=None,
    description="The person's mother name."
  )


class People(BaseModel):
  """Extracted data about people."""

  # Creates a model so that we can extract multiple entities.
  people: List[Person]
