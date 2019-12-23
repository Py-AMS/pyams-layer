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

"""PyAMS_*** module

"""
from pyams_layer.interfaces import ISkin, PYAMS_BASE_SKIN_NAME, IPyAMSLayer
from pyams_utils.registry import utility_config


__docformat__ = 'restructuredtext'

from pyams_layer import _


@utility_config(name=PYAMS_BASE_SKIN_NAME, provides=ISkin)
class PyAMSSkin(object):
    """PyAMS base skin"""

    label = _("PyAMS base skin")
    layer = IPyAMSLayer
