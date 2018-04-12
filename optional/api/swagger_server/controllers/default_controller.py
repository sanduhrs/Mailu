import connexion
import six

from swagger_server.models.alias import Alias  # noqa: E501
from swagger_server.models.alternative import Alternative  # noqa: E501
from swagger_server.models.domain import Domain  # noqa: E501
from swagger_server.models.fetch import Fetch  # noqa: E501
from swagger_server.models.manager import Manager  # noqa: E501
from swagger_server.models.relay import Relay  # noqa: E501
from swagger_server.models.token import Token  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def alias_get():  # noqa: E501
    """alias_get

    Returns all aliases from the system that the user has access to # noqa: E501


    :rtype: List[Alias]
    """
    return 'do some magic!'


def alternative_get():  # noqa: E501
    """alternative_get

    Returns all alternatives from the system that the user has access to # noqa: E501


    :rtype: List[Alternative]
    """
    return 'do some magic!'


def domain_get():  # noqa: E501
    """domain_get

    Returns all domains from the system that the user has access to # noqa: E501


    :rtype: List[Domain]
    """
    return 'do some magic!'


def fetch_get():  # noqa: E501
    """fetch_get

    Returns all fetchs from the system that the user has access to # noqa: E501


    :rtype: List[Fetch]
    """
    return 'do some magic!'


def manager_get():  # noqa: E501
    """manager_get

    Returns all managers from the system that the user has access to # noqa: E501


    :rtype: List[Manager]
    """
    return 'do some magic!'


def relay_get():  # noqa: E501
    """relay_get

    Returns all relays from the system that the user has access to # noqa: E501


    :rtype: List[Relay]
    """
    return 'do some magic!'


def token_get():  # noqa: E501
    """token_get

    Returns all tokens from the system that the user has access to # noqa: E501


    :rtype: List[Token]
    """
    return 'do some magic!'


def user_get():  # noqa: E501
    """user_get

    Returns all users from the system that the user has access to # noqa: E501


    :rtype: List[User]
    """
    return 'do some magic!'
