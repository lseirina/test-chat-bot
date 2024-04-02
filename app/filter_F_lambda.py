"""Simple filters for bot."""
from aiogram import F

# Filter for photo.
F.photo
lambda message: message.photo

# filterfor voice.
F.voice
lambda message: message.voice

# filter for a few different types.
F.content_type.in_({
    ContentType.PHOTO,
    ContentTyep.VOICE,
    ContenType.VIDEO
})
lambda message: message.content_type in {
    ContentType.PHOTO,
    ContentType.VIDEO,
    ContentType.VOICE
}

# filter for exect test maych.
F.text = 'Hello'
lambda message: message.text == 'Hello'

# filter for text start with...
F.text.startwith('bot')
lambda message: message.text.startwith('bot')

#  filter for text does not start with...
~F.text.startwith('bot')
lambda message: not message.text.startwith('bot')

# filter allows updates from a user with ID = 173901673
F.from_user.id = 173901673
lambda message: message.from_user.id == 173901673
# filter allows updates from a list users with IDs.
F.from_user.id.in_({193905674, 173901673, 144941561})
lambda message: message.from_user.id in {193905674, 173901673, 144941561}