# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SasUriResponse(Model):
    """Get SAS URL operation response.

    :param sas_uri: A URL with a SAS token to upload a blob for execution in
     the given workspace.
    :type sas_uri: str
    """

    _attribute_map = {
        'sas_uri': {'key': 'sasUri', 'type': 'str'},
    }

    def __init__(self, *, sas_uri: str=None, **kwargs) -> None:
        super(SasUriResponse, self).__init__(**kwargs)
        self.sas_uri = sas_uri
