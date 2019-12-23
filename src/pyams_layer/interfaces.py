#
# Copyright (c) 2015-2019 Thierry Florac <tflorac AT ulthar.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""PyAMS_layer.interfaces module

"""

from pyramid.interfaces import IRequest
from zope.configuration.fields import GlobalInterface
from zope.interface import Interface
from zope.schema import TextLine


__docformat__ = 'restructuredtext'


PYAMS_BASE_SKIN_NAME = 'PyAMS base skin'


class IBaseLayer(IRequest):
    """Base layer interface"""


class IFormLayer(Interface):
    """Custom layer for forms management"""


class IPyAMSLayer(IBaseLayer, IFormLayer):
    """PyAMS default layer"""


class IPyAMSUserLayer(IPyAMSLayer):
    """PyAMS custom user layer

    This layer is the base for all custom skins.
    Any component should provide a look and feel for this layer.
    """


class ISkin(Interface):
    """Skin interface

    Skins are registered as utilities implementing this interface
    and defining request layer as attribute.
    """

    label = TextLine(title="Skin name")

    layer = GlobalInterface(title="Request layer",
                            description="This interface will be used to tag request layer",
                            required=True)
