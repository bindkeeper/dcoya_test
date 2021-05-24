

from rest_framework_jwt.settings import api_settings
import logging

logger = logging.getLogger(__name__)


def create_jwt_and_save_jwt(user):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(user)
    logger.info(payload["exp"])
    token = jwt_encode_handler(payload)
    user.jwt = token
    user.jwt_expiration = (payload["exp"])
    user.save()
    return token
