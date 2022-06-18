# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from knack.arguments import CLIArgumentType
from azure.cli.core.commands.parameters import (
    tags_type,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import (
    get_default_location_from_resource_group,
    validate_file_or_dict
)
from azext_devcenter.action import (
    AddParameters,
    AddGitHub,
    AddImageReference,
    AddSku
)

def load_arguments(self, _):

    from azure.cli.core.commands.parameters import tags_type

    with self.argument_context('devcenter dev project list') as c:
        c.argument('top', type=int, help='The maximum number of resources to return from the operation. Example: '
                   '\'$top=10\'.')
        c.argument('filter_', options_list=['--filter'], type=str, help='An OData $filter clause to apply to the '
                   'operation.')
        c.argument('dev_center', type=str, help='The DevCenter.')
        c.argument('devcenter_dns_suffix', type=str, help='Optional DevCenter DNS suffix')

    with self.argument_context('devcenter dev pool list') as c:
        c.argument('top', type=int, help='The maximum number of resources to return from the operation. Example: '
                   '\'$top=10\'.')
        c.argument('filter_', options_list=['--filter'], type=str, help='An OData $filter clause to apply to the '
                   'operation.')
        c.argument('project_name', type=str, help='The Project upon which to execute operations.')
        c.argument('dev_center', type=str, help='The DevCenter.')
        c.argument('devcenter_dns_suffix', type=str, help='Optional DevCenter DNS suffix')

    with self.argument_context('devcenter dev pool show') as c:
        c.argument('pool_name', options_list=['--name', '-n', '--pool-name'], type=str, help='The name of a pool of '
                   'virtual machines.')
        c.argument('project_name', options_list=['--project-name', '--project'], type=str, help='The Project upon which to execute operations.')
        c.argument('dev_center', type=str, help='The DevCenter.')
        c.argument('devcenter_dns_suffix', type=str, help='Optional DevCenter DNS suffix')

    with self.argument_context('devcenter dev dev-box list') as c:
        c.argument('filter_', options_list=['--filter'], type=str, help='An OData $filter clause to apply to the '
                   'operation.')
        c.argument('top', type=int, help='The maximum number of resources to return from the operation. Example: '
                   '\'$top=10\'.')
        c.argument('project_name', type=str, help='The Project upon which to execute operations.')
        c.argument('user_id', type=str, help='The id of the user. If value is \'me\', the identity is taken from the '
                   'authentication context')
        c.argument('dev_center', type=str, help='The DevCenter.')
        c.argument('devcenter_dns_suffix', type=str, help='Optional DevCenter DNS suffix')

    with self.argument_context('devcenter dev dev-box show') as c:
        c.argument('project_name', type=str, help='The Project upon which to execute operations.')
        c.argument('user_id', type=str, help='The id of the user. If value is \'me\', the identity is taken from the '
                   'authentication context')
        c.argument('dev_box_name', options_list=['--name', '-n', '--dev-box-name'], type=str,
                   help='The name of a virtual machine.')
        c.argument('dev_center', type=str, help='The DevCenter.')
        c.argument('devcenter_dns_suffix', type=str, help='Optional DevCenter DNS suffix')

    with self.argument_context('devcenter dev dev-box create') as c:
        c.argument('project_name', type=str, help='The Project upon which to execute operations.')
        c.argument('user_id', type=str, help='The id of the user. If value is \'me\', the identity is taken from the '
                   'authentication context')
        c.argument('dev_box_name', options_list=['--name', '-n', '--dev-box-name'], type=str,
                   help='The name of a virtual machine.')
        c.argument('pool_name', type=str, help='The name of the virtual machine pool this machine belongs to.')
        c.argument('dev_center', type=str, help='The DevCenter.')
        c.argument('devcenter_dns_suffix', type=str, help='Optional DevCenter DNS suffix')

    with self.argument_context('devcenter dev dev-box delete') as c:
        c.argument('project_name', type=str, help='The Project upon which to execute operations.')
        c.argument('user_id', type=str, help='The id of the user. If value is \'me\', the identity is taken from the '
                   'authentication context')
        c.argument('dev_box_name', options_list=['--name', '-n', '--dev-box-name'], type=str,
                   help='The name of a virtual machine.')
        c.argument('dev_center', type=str, help='The DevCenter.')
        c.argument('devcenter_dns_suffix', type=str, help='Optional DevCenter DNS suffix')

    with self.argument_context('devcenter dev dev-box assign') as c:
        c.argument('project_name', type=str, help='The Project upon which to execute operations.')
        c.argument('user_id', type=str, help='The id of the user. If value is \'me\', the identity is taken from the '
                   'authentication context')
        c.argument('dev_box_name', options_list=['--name', '-n', '--dev-box-name'], type=str,
                   help='The name of a virtual machine.')
        c.argument('new_owner', type=str, help='Identifier of new owner')
        c.argument('dev_center', type=str, help='The DevCenter.')
        c.argument('devcenter_dns_suffix', type=str, help='Optional DevCenter DNS suffix')

    with self.argument_context('devcenter dev dev-box get-remote-connection') as c:
        c.argument('project_name', type=str, help='The Project upon which to execute operations.')
        c.argument('user_id', type=str, help='The id of the user. If value is \'me\', the identity is taken from the '
                   'authentication context')
        c.argument('dev_box_name', options_list=['--name', '-n', '--dev-box-name'], type=str,
                   help='The name of a virtual machine.')
        c.argument('dev_center', type=str, help='The DevCenter.')
        c.argument('devcenter_dns_suffix', type=str, help='Optional DevCenter DNS suffix')

    with self.argument_context('devcenter dev dev-box start') as c:
        c.argument('project_name', type=str, help='The Project upon which to execute operations.')
        c.argument('user_id', type=str, help='The id of the user. If value is \'me\', the identity is taken from the '
                   'authentication context')
        c.argument('dev_box_name', options_list=['--name', '-n', '--dev-box-name'], type=str,
                   help='The name of a virtual machine.')
        c.argument('dev_center', type=str, help='The DevCenter.')
        c.argument('devcenter_dns_suffix', type=str, help='Optional DevCenter DNS suffix')

    with self.argument_context('devcenter dev dev-box stop') as c:
        c.argument('project_name', type=str, help='The Project upon which to execute operations.')
        c.argument('user_id', type=str, help='The id of the user. If value is \'me\', the identity is taken from the '
                   'authentication context')
        c.argument('dev_box_name', options_list=['--name', '-n', '--dev-box-name'], type=str,
                   help='The name of a virtual machine.')
        c.argument('dev_center', type=str, help='The DevCenter.')
        c.argument('devcenter_dns_suffix', type=str, help='Optional DevCenter DNS suffix')

    with self.argument_context('devcenter dev environment list') as c:
        c.argument('dev_center', type=str, help='The DevCenter to operate on.')
        c.argument('devcenter_dns_suffix', type=str, help='The DNS suffix used as the base for all devcenter requests.')
        c.argument('top', type=int, help='The maximum number of resources to return from the operation. Example: '
                   '\'$top=10\'.')
        c.argument('project_name', type=str, help='The Project upon which to execute operations.')
        c.argument('filter_', options_list=['--filter'], type=str, help='An OData $filter clause to apply to the '
                   'operation.')

    with self.argument_context('devcenter dev environment show') as c:
        c.argument('dev_center', type=str, help='The DevCenter to operate on.')
        c.argument('devcenter_dns_suffix', type=str, help='The DNS suffix used as the base for all devcenter requests.')
        c.argument('project_name', type=str, help='The Project upon which to execute operations.')
        c.argument('environment_name', options_list=['--name', '-n', '--environment-name'], type=str, help='The name '
                   'of the environment.')

    with self.argument_context('devcenter dev environment create') as c:
        c.argument('dev_center', type=str, help='The DevCenter to operate on.')
        c.argument('devcenter_dns_suffix', type=str, help='The DNS suffix used as the base for all devcenter requests.')
        c.argument('project_name', type=str, help='The Project upon which to execute operations.')
        c.argument('environment_name', options_list=['--name', '-n', '--environment-name'], type=str, help='The name '
                   'of the environment.')
        c.argument('description', type=str, help='Description of the Environment.')
        c.argument('catalog_item_name', type=str, help='Name of the catalog item.')
        c.argument('deployment_parameters', type=validate_file_or_dict, help='Deployment parameters passed to catalog '
                   'item. Expected value: json-string/json-file/@json-file.')
        c.argument('environment_type', type=str, help='Environment type.')
        c.argument('owner', type=str, help='Identifier of the owner of this Environment.')
        c.argument('tags', tags_type)

    with self.argument_context('devcenter dev environment update') as c:
        c.argument('dev_center', type=str, help='The DevCenter to operate on.')
        c.argument('devcenter_dns_suffix', type=str, help='The DNS suffix used as the base for all devcenter requests.')
        c.argument('project_name', type=str, help='The Project upon which to execute operations.')
        c.argument('environment_name', options_list=['--name', '-n', '--environment-name'], type=str, help='The name '
                   'of the environment.')
        c.argument('description', type=str, help='Description of the Environment.')
        c.argument('catalog_item_name', type=str, help='Name of the catalog item.')
        c.argument('deployment_parameters', type=validate_file_or_dict, help='Deployment parameters passed to catalog '
                   'item. Expected value: json-string/json-file/@json-file.')

    with self.argument_context('devcenter dev environment delete') as c:
        c.argument('dev_center', type=str, help='The DevCenter to operate on.')
        c.argument('devcenter_dns_suffix', type=str, help='The DNS suffix used as the base for all devcenter requests.')
        c.argument('project_name', type=str, help='The Project upon which to execute operations.')
        c.argument('environment_name', options_list=['--name', '-n', '--environment-name'], type=str, help='The name '
                   'of the environment.')

    with self.argument_context('devcenter dev environment deploy') as c:
        c.argument('dev_center', type=str, help='The DevCenter to operate on.')
        c.argument('devcenter_dns_suffix', type=str, help='The DNS suffix used as the base for all devcenter requests.')
        c.argument('project_name', type=str, help='The Project upon which to execute operations.')
        c.argument('environment_name', options_list=['--name', '-n', '--environment-name'], type=str, help='The name '
                   'of the environment.')
        c.argument('parameters', type=validate_file_or_dict, help='Deployment parameters. Expected value: '
                   'json-string/json-file/@json-file.')

    with self.argument_context('devcenter dev deployment list') as c:
        c.argument('dev_center', type=str, help='The DevCenter to operate on.')
        c.argument('devcenter_dns_suffix', type=str, help='The DNS suffix used as the base for all devcenter requests.')
        c.argument('project_name', type=str, help='The Project upon which to execute operations.')
        c.argument('environment_name', type=str, help='The name of the environment.')
        c.argument('top', type=int, help='The maximum number of resources to return from the operation. Example: '
                   '\'$top=10\'.')
        c.argument('filter_', options_list=['--filter'], type=str, help='An OData $filter clause to apply to the '
                   'operation.')

    with self.argument_context('devcenter dev catalog-item list') as c:
        c.argument('dev_center', type=str, help='The DevCenter to operate on.')
        c.argument('devcenter_dns_suffix', type=str, help='The DNS suffix used as the base for all devcenter requests.')
        c.argument('project_name', type=str, help='The Project upon which to execute operations.')
        c.argument('top', type=int, help='The maximum number of resources to return from the operation. Example: '
                   '\'$top=10\'.')
        c.argument('filter_', options_list=['--filter'], type=str, help='An OData $filter clause to apply to the '
                   'operation.')

    with self.argument_context('devcenter dev environment-type list') as c:
        c.argument('dev_center', type=str, help='The DevCenter to operate on.')
        c.argument('devcenter_dns_suffix', type=str, help='The DNS suffix used as the base for all devcenter requests.')
        c.argument('project_name', type=str, help='The Project upon which to execute operations.')
        c.argument('top', type=int, help='The maximum number of resources to return from the operation. Example: '
                   '\'$top=10\'.')

    #control plane
    with self.argument_context('devcenter admin dev-center list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('top', type=int, help='The maximum number of resources to return from the operation. Example: '
                   '\'$top=10\'.')

    with self.argument_context('devcenter admin dev-center show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', options_list=['--name', '-n', '--dev-center-name'], type=str, help='The name of '
                   'the devcenter.', id_part='name')

    with self.argument_context('devcenter admin dev-center create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', options_list=['--name', '-n', '--dev-center-name'], type=str, help='The name of '
                   'the devcenter.')
        c.argument('tags', tags_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('identity_type', arg_type=get_enum_type(['SystemAssigned', 'UserAssigned',
                                                                             'SystemAssigned, UserAssigned', 'None']),
                   help='The type of identity used for the resource. The type \'SystemAssigned, UserAssigned\' '
                   'includes both an implicitly created identity and a user assigned identity. The type \'None\' will '
                   'remove any identities from the resource.', required=False, arg_group='Identity')
        c.argument('user_assigned_identity', type=str, help='The user identity '
                   'associated with the resource. The user identity references will be an ARM resource id '
                   'in the form: \'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microso'
                   'ft.ManagedIdentity/userAssignedIdentities/{identityName}\'. ', arg_group='Identity')

    with self.argument_context('devcenter admin dev-center update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', options_list=['--name', '-n', '--dev-center-name'], type=str, help='The name of '
                   'the devcenter.', id_part='name')
        c.argument('tags', tags_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('identity_type', arg_type=get_enum_type(['SystemAssigned', 'UserAssigned',
                                                                             'SystemAssigned, UserAssigned', 'None']),
                   help='The type of identity used for the resource. The type \'SystemAssigned, UserAssigned\' '
                   'includes both an implicitly created identity and a user assigned identity. The type \'None\' will '
                   'remove any identities from the resource.', required=False, arg_group='Identity')
        c.argument('user_assigned_identities', type=validate_file_or_dict, help='The list of user identities '
                   'associated with the resource. The user identity dictionary key references will be ARM resource ids '
                   'in the form: \'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microso'
                   'ft.ManagedIdentity/userAssignedIdentities/{identityName}\'. Expected value: '
                   'json-string/json-file/@json-file.', arg_group='Identity')

    with self.argument_context('devcenter admin dev-center delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', options_list=['--name', '-n', '--dev-center-name'], type=str, help='The name of '
                   'the devcenter.', id_part='name')

    with self.argument_context('devcenter admin dev-center attach-network') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', options_list=['--name', '-n', '--dev-center-name'], type=str, help='The name of '
                   'the devcenter.', id_part='name')
        c.argument('network_connection_id', type=str, help='Resource id of a Network Settings resource')

    with self.argument_context('devcenter admin dev-center detach-network') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', options_list=['--name', '-n', '--dev-center-name'], type=str, help='The name of '
                   'the devcenter.', id_part='name')
        c.argument('network_connection_id', type=str, help='Resource id of a Network Settings resource')

    with self.argument_context('devcenter admin dev-center wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', options_list=['--name', '-n', '--dev-center-name'], type=str, help='The name of '
                   'the devcenter.', id_part='name')

    with self.argument_context('devcenter admin project list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('top', type=int, help='The maximum number of resources to return from the operation. Example: '
                   '\'$top=10\'.')

    with self.argument_context('devcenter admin project show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', options_list=['--name', '-n', '--project-name'], type=str, help='The name of the '
                   'project.', id_part='name')

    with self.argument_context('devcenter admin project create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', options_list=['--name', '-n', '--project-name'], type=str, help='The name of the '
                   'project.')
        c.argument('tags', tags_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('dev_center_id', type=str, help='Resource Id of an associated DevCenter')
        c.argument('description', type=str, help='Description of the project.')

    with self.argument_context('devcenter admin project update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', options_list=['--name', '-n', '--project-name'], type=str, help='The name of the '
                   'project.', id_part='name')
        c.argument('tags', tags_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('dev_center_id', type=str, help='Resource Id of an associated DevCenter')
        c.argument('description', type=str, help='Description of the project.')

    with self.argument_context('devcenter admin project delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', options_list=['--name', '-n', '--project-name'], type=str, help='The name of the '
                   'project.', id_part='name')

    with self.argument_context('devcenter admin project wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', options_list=['--name', '-n', '--project-name'], type=str, help='The name of the '
                   'project.', id_part='name')

    with self.argument_context('devcenter admin attached-network list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', type=str, help='The name of the project.')
        c.argument('top', type=int, help='The maximum number of resources to return from the operation. Example: '
                   '\'$top=10\'.')
        c.argument('dev_center_name', type=str, help='The name of the devcenter.')

    with self.argument_context('devcenter admin attached-network show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', type=str, help='The name of the project.', id_part='name')
        c.argument('attached_network_connection_name', options_list=['--name', '-n', '--attached-network-connection-name'], type=str, help='The name of the attached NetworkConnection.',
                   id_part='child_name_1')
        c.argument('dev_center_name', type=str, help='The name of the devcenter.', id_part='name')

    with self.argument_context('devcenter admin attached-network create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.')
        c.argument('attached_network_connection_name', options_list=['--name', '-n', '--attached-network-connection-name'], type=str, help='The name of the attached NetworkConnection.')
        c.argument('network_connection_resource_id', type=str, help='The resource ID of the NetworkConnection you want '
                   'to attach.')

    with self.argument_context('devcenter admin attached-network update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.', id_part='name')
        c.argument('attached_network_connection_name', options_list=['--name', '-n', '--attached-network-connection-name'], type=str, help='The name of the attached NetworkConnection.',
                   id_part='child_name_1')
        c.argument('network_connection_resource_id', type=str, help='The resource ID of the NetworkConnection you want '
                   'to attach.')

    with self.argument_context('devcenter admin attached-network delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.', id_part='name')
        c.argument('attached_network_connection_name', options_list=['--name', '-n', '--attached-network-connection-name'], type=str, help='The name of the attached NetworkConnection.',
                   id_part='child_name_1')

    with self.argument_context('devcenter admin attached-network wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', type=str, help='The name of the project.', id_part='name')
        c.argument('attached_network_connection_name', type=str, help='The name of the attached NetworkConnection.',
                   id_part='child_name_1')
        c.argument('dev_center_name', type=str, help='The name of the devcenter.', id_part='name')

    with self.argument_context('devcenter admin environment-type list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', type=str, help='The name of the project.')
        c.argument('top', type=int, help='The maximum number of resources to return from the operation. Example: '
                   '\'$top=10\'.')
        c.argument('dev_center_name', type=str, help='The name of the devcenter.')

    with self.argument_context('devcenter admin environment-type show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.', id_part='name')
        c.argument('environment_type_name', options_list=['--name', '-n', '--environment-type-name'], type=str,
                   help='The name of the environment type.', id_part='child_name_1')

    with self.argument_context('devcenter admin environment-type create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.')
        c.argument('environment_type_name', options_list=['--name', '-n', '--environment-type-name'], type=str,
                   help='The name of the environment type.')
        c.argument('tags', tags_type)
        c.argument('description', type=str, help='Description of the environment type.')

    with self.argument_context('devcenter admin environment-type update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.', id_part='name')
        c.argument('environment_type_name', options_list=['--name', '-n', '--environment-type-name'], type=str,
                   help='The name of the environment type.', id_part='child_name_1')
        c.argument('tags', tags_type)
        c.argument('description', type=str, help='Description of the environment type.')

    with self.argument_context('devcenter admin environment-type delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.', id_part='name')
        c.argument('environment_type_name', options_list=['--name', '-n', '--environment-type-name'], type=str,
                   help='The name of the environment type.', id_part='child_name_1')

    with self.argument_context('devcenter admin environment-type wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.', id_part='name')
        c.argument('environment_type_name', options_list=['--name', '-n', '--environment-type-name'], type=str,
                   help='The name of the environment type.', id_part='child_name_1')

    with self.argument_context('devcenter project-environment-type list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', type=str, help='The name of the project.')
        c.argument('top', type=int, help='The maximum number of resources to return from the operation. Example: '
                   '\'$top=10\'.')

    with self.argument_context('devcenter project-environment-type show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', type=str, help='The name of the project.', id_part='name')
        c.argument('environment_type_name', type=str, help='The name of the environment type.',
                   id_part='child_name_1')

    with self.argument_context('devcenter project-environment-type create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', type=str, help='The name of the project.')
        c.argument('environment_type_name', type=str, help='The name of the environment type.')
        c.argument('tags', tags_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('deployment_target_id', type=str, help='Id of a subscription that the environment type will be '
                   'mapped to. The environment\'s resources will be deployed into this subscription.')
        c.argument('status', arg_type=get_enum_type(['Enabled', 'Disabled']), help='Defines whether this Environment '
                   'Type can be used in this Project.')
        c.argument('creator_role_assignment', type=str, help='The role definition assigned to the environment creator '
                   'on backing resources.')
        c.argument('user_role_assignments', type=validate_file_or_dict, help='Role Assignments created on environment '
                   'backing resources. This is a mapping from a user object ID to an object of role definition IDs. '
                   'Expected value: json-string/json-file/@json-file.')
        c.argument('type_', options_list=['--type'], arg_type=get_enum_type(['None', 'SystemAssigned', 'UserAssigned',
                                                                             'SystemAssigned, UserAssigned']),
                   help='Type of managed service identity (where both SystemAssigned and UserAssigned types are '
                   'allowed).', arg_group='Identity')
        c.argument('user_assigned_identities', type=validate_file_or_dict, help='The set of user assigned identities '
                   'associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids '
                   'in the form: \'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microso'
                   'ft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty '
                   'objects ({}) in requests. Expected value: json-string/json-file/@json-file.',
                   arg_group='Identity')

    with self.argument_context('devcenter project-environment-type update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', type=str, help='The name of the project.', id_part='name')
        c.argument('environment_type_name', type=str, help='The name of the environment type.',
                   id_part='child_name_1')
        c.argument('tags', tags_type)
        c.argument('deployment_target_id', type=str, help='Id of a subscription that the environment type will be '
                   'mapped to. The environment\'s resources will be deployed into this subscription.')
        c.argument('status', arg_type=get_enum_type(['Enabled', 'Disabled']), help='Defines whether this Environment '
                   'Type can be used in this Project.')
        c.argument('creator_role_assignment', type=str, help='The role definition assigned to the environment creator '
                   'on backing resources.')
        c.argument('user_role_assignments', type=validate_file_or_dict, help='Role Assignments created on environment '
                   'backing resources. This is a mapping from a user object ID to an object of role definition IDs. '
                   'Expected value: json-string/json-file/@json-file.')
        c.argument('type_', options_list=['--type'], arg_type=get_enum_type(['None', 'SystemAssigned', 'UserAssigned',
                                                                             'SystemAssigned, UserAssigned']),
                   help='Type of managed service identity (where both SystemAssigned and UserAssigned types are '
                   'allowed).', arg_group='Identity')
        c.argument('user_assigned_identities', type=validate_file_or_dict, help='The set of user assigned identities '
                   'associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids '
                   'in the form: \'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microso'
                   'ft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty '
                   'objects ({}) in requests. Expected value: json-string/json-file/@json-file.',
                   arg_group='Identity')

    with self.argument_context('devcenter project-environment-type delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', type=str, help='The name of the project.', id_part='name')
        c.argument('environment_type_name', type=str, help='The name of the environment type.',
                   id_part='child_name_1')

    with self.argument_context('devcenter admin gallery list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.')
        c.argument('top', type=int, help='The maximum number of resources to return from the operation. Example: '
                   '\'$top=10\'.')

    with self.argument_context('devcenter admin gallery show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.', id_part='name')
        c.argument('gallery_name', options_list=['--name', '-n', '--gallery-name'], type=str, help='The name of the '
                   'gallery.', id_part='child_name_1')

    with self.argument_context('devcenter admin gallery create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.')
        c.argument('gallery_name', options_list=['--name', '-n', '--gallery-name'], type=str, help='The name of the '
                   'gallery.')
        c.argument('gallery_resource_id', type=str, help='The resource ID of the backing Azure Compute Gallery.')

    with self.argument_context('devcenter admin gallery update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.', id_part='name')
        c.argument('gallery_name', options_list=['--name', '-n', '--gallery-name'], type=str, help='The name of the '
                   'gallery.', id_part='child_name_1')
        c.argument('gallery_resource_id', type=str, help='The resource ID of the backing Azure Compute Gallery.')
        c.ignore('body')

    with self.argument_context('devcenter admin gallery delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.', id_part='name')
        c.argument('gallery_name', options_list=['--name', '-n', '--gallery-name'], type=str, help='The name of the '
                   'gallery.', id_part='child_name_1')

    with self.argument_context('devcenter admin gallery wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.', id_part='name')
        c.argument('gallery_name', options_list=['--name', '-n', '--gallery-name'], type=str, help='The name of the '
                   'gallery.', id_part='child_name_1')
                   
    with self.argument_context('devcenter admin image list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.')
        c.argument('gallery_name', type=str, help='The name of the gallery.')
        c.argument('top', type=int, help='The maximum number of resources to return from the operation. Example: '
                   '\'$top=10\'.')

    with self.argument_context('devcenter admin image show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.', id_part='name')
        c.argument('gallery_name', type=str, help='The name of the gallery.', id_part='child_name_1')
        c.argument('image_name', options_list=['--name', '-n', '--image-name'], type=str,
                   help='The name of the image.', id_part='child_name_2')

    with self.argument_context('devcenter admin image-version list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.')
        c.argument('gallery_name', type=str, help='The name of the gallery.')
        c.argument('image_name', type=str, help='The name of the image.')

    with self.argument_context('devcenter admin image-version show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.', id_part='name')
        c.argument('gallery_name', type=str, help='The name of the gallery.', id_part='child_name_1')
        c.argument('image_name', type=str, help='The name of the image.', id_part='child_name_2')
        c.argument('version_name', type=str, help='The version of the image.', id_part='child_name_3')

    with self.argument_context('devcenter admin catalog list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.')
        c.argument('top', type=int, help='The maximum number of resources to return from the operation. Example: '
                   '\'$top=10\'.')

    with self.argument_context('devcenter admin catalog show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.', id_part='name')
        c.argument('catalog_name', options_list=['--name', '-n', '--catalog-name'], type=str, help='The name of the '
                   'Catalog.', id_part='child_name_1')

    with self.argument_context('devcenter admin catalog create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.')
        c.argument('catalog_name', options_list=['--name', '-n', '--catalog-name'], type=str, help='The name of the '
                   'Catalog.')
        c.argument('git_hub', action=AddGitHub, nargs='+', help='Properties for a GitHub catalog type.')
        c.argument('ado_git', action=AddGitHub, nargs='+', help='Properties for an Azure DevOps catalog type.')

    with self.argument_context('devcenter admin catalog update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.', id_part='name')
        c.argument('catalog_name', options_list=['--name', '-n', '--catalog-name'], type=str, help='The name of the '
                   'Catalog.', id_part='child_name_1')
        c.argument('tags', tags_type)
        c.argument('git_hub', action=AddGitHub, nargs='+', help='Properties for a GitHub catalog type.')
        c.argument('ado_git', action=AddGitHub, nargs='+', help='Properties for an Azure DevOps catalog type.')

    with self.argument_context('devcenter admin catalog delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.', id_part='name')
        c.argument('catalog_name', options_list=['--name', '-n', '--catalog-name'], type=str, help='The name of the '
                   'Catalog.', id_part='child_name_1')

    with self.argument_context('devcenter admin catalog sync') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.', id_part='name')
        c.argument('catalog_name', options_list=['--name', '-n', '--catalog-name'], type=str, help='The name of the '
                   'Catalog.', id_part='child_name_1')

    with self.argument_context('devcenter admin catalog wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.', id_part='name')
        c.argument('catalog_name', options_list=['--name', '-n', '--catalog-name'], type=str, help='The name of the '
                   'Catalog.', id_part='child_name_1')

    with self.argument_context('devcenter admin devbox-definition list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.')
        c.argument('top', type=int, help='The maximum number of resources to return from the operation. Example: '
                   '\'$top=10\'.')

    with self.argument_context('devcenter admin devbox-definition show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.', id_part='name')
        c.argument('dev_box_definition_name', options_list=['--name', '-n', '--devbox-definition-name'], type=str,
                   help='The name of the Dev Box definition.', id_part='child_name_1')

    with self.argument_context('devcenter admin devbox-definition create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.')
        c.argument('dev_box_definition_name', options_list=['--name', '-n', '--dev-box-definition-name'], type=str,
                   help='The name of the Dev Box definition.')
        c.argument('tags', tags_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('image_reference', action=AddImageReference, nargs='+', help='Image reference information.')
        c.argument('sku', action=AddSku, nargs='+', help='The SKU for Dev Boxes created using this definition.')
        c.argument('os_storage_type', type=str, help='The storage type used for the Operating System disk of Dev Boxes '
                   'created using this definition.')

    with self.argument_context('devcenter admin devbox-definition update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.', id_part='name')
        c.argument('dev_box_definition_name', options_list=['--name', '-n', '--dev-box-definition-name'], type=str,
                   help='The name of the Dev Box definition.', id_part='child_name_1')
        c.argument('tags', tags_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('image_reference', action=AddImageReference, nargs='+', help='Image reference information.')
        c.argument('sku', action=AddSku, nargs='+', help='The SKU for Dev Boxes created using this definition.')
        c.argument('os_storage_type', type=str, help='The storage type used for the Operating System disk of Dev Boxes '
                   'created using this definition.')

    with self.argument_context('devcenter admin devbox-definition delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.', id_part='name')
        c.argument('dev_box_definition_name', options_list=['--name', '-n', '--devbox-definition-name'], type=str,
                   help='The name of the Dev Box definition.', id_part='child_name_1')

    with self.argument_context('devcenter admin devbox-definition wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.', id_part='name')
        c.argument('dev_box_definition_name', options_list=['--name', '-n', '--devbox-definition-name'], type=str,
                   help='The name of the Dev Box definition.', id_part='child_name_1')

    with self.argument_context('devcenter admin mapping delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('dev_center_name', type=str, help='The name of the devcenter.', id_part='name')
        c.argument('mapping_name', options_list=['--name', '-n', '--mapping-name'], type=str, help='Mapping name.',
                   id_part='child_name_1')

    with self.argument_context('devcenter admin operation-statuses show') as c:
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('operation_id', type=str, help='The ID of an ongoing async operation')

    with self.argument_context('devcenter admin sku list') as c:
        c.argument('top', type=int, help='The maximum number of resources to return from the operation. Example: '
                   '\'$top=10\'.')

    with self.argument_context('devcenter admin pool list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', type=str, help='The name of the project.')
        c.argument('top', type=int, help='The maximum number of resources to return from the operation. Example: '
                   '\'$top=10\'.')

    with self.argument_context('devcenter admin pool show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', type=str, help='The name of the project.', id_part='name')
        c.argument('pool_name', options_list=['--name', '-n', '--pool-name'], type=str, help='Name of the pool.',
                   id_part='child_name_1')

    with self.argument_context('devcenter admin pool create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', type=str, help='The name of the project.')
        c.argument('pool_name', options_list=['--name', '-n', '--pool-name'], type=str, help='Name of the pool.')
        c.argument('tags', tags_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('dev_box_definition_name', options_list=['--devbox-definition-name'], type=str, help='Name of a Dev Box definition in parent Project of this Pool')
        c.argument('network_connection_name', type=str, help='Name of a Network Connection in parent Project of this Pool')
        c.argument('local_administrator', arg_type=get_enum_type(['Disabled', 'Enabled']), help='Indicates whether '
                   'owners of Dev Boxes in this pool are added as local administrators on the Dev Box.')

    with self.argument_context('devcenter admin pool update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', type=str, help='The name of the project.', id_part='name')
        c.argument('pool_name', options_list=['--name', '-n', '--pool-name'], type=str, help='Name of the pool.',
                   id_part='child_name_1')
        c.argument('tags', tags_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('dev_box_definition_name', options_list=['--devbox-definition-name'], type=str, help='Name of a Dev Box definition in parent Project of this Pool')
        c.argument('network_connection_name', type=str, help='Name of a Network Connection in parent Project of this Pool')
        c.argument('local_administrator', arg_type=get_enum_type(['Disabled', 'Enabled']), help='Indicates whether '
                   'owners of Dev Boxes in this pool are added as local administrators on the Dev Box.')

    with self.argument_context('devcenter admin pool delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', type=str, help='The name of the project.', id_part='name')
        c.argument('pool_name', options_list=['--name', '-n', '--pool-name'], type=str, help='Name of the pool.',
                   id_part='child_name_1')

    with self.argument_context('devcenter admin pool wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', type=str, help='The name of the project.', id_part='name')
        c.argument('pool_name', options_list=['--name', '-n', '--pool-name'], type=str, help='Name of the pool.',
                   id_part='child_name_1')

    with self.argument_context('devcenter admin schedule list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', type=str, help='The name of the project.')
        c.argument('pool_name', type=str, help='Name of the pool.')
        c.argument('top', type=int, help='The maximum number of resources to return from the operation. Example: '
                   '\'$top=10\'.')

    with self.argument_context('devcenter admin schedule show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', type=str, help='The name of the project.', id_part='name')
        c.argument('pool_name', type=str, help='Name of the pool.', id_part='child_name_1')
        c.argument('schedule_name', options_list=['--name', '-n', '--schedule-name'], type=str, help='The name of the '
                   'schedule that uniquely identifies it.', id_part='child_name_2')
        c.argument('top', type=int, help='The maximum number of resources to return from the operation. Example: '
                   '\'$top=10\'.')

    with self.argument_context('devcenter admin schedule create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', type=str, help='The name of the project.')
        c.argument('pool_name', type=str, help='Name of the pool.')
        c.argument('schedule_name', options_list=['--name', '-n', '--schedule-name'], type=str, help='The name of the '
                   'schedule that uniquely identifies it.')
        c.argument('top', type=int, help='The maximum number of resources to return from the operation. Example: '
                   '\'$top=10\'.')
        c.argument('time', type=str, help='The target time to trigger the action. The format is HH:MM.')
        c.argument('time_zone', type=str, help='The IANA timezone id at which the schedule should execute.')
        c.argument('state', arg_type=get_enum_type(['Enabled', 'Disabled']), help='Indicates whether or not this '
                   'scheduled task is enabled.')

    with self.argument_context('devcenter admin schedule update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', type=str, help='The name of the project.', id_part='name')
        c.argument('pool_name', type=str, help='Name of the pool.', id_part='child_name_1')
        c.argument('schedule_name', options_list=['--name', '-n', '--schedule-name'], type=str, help='The name of the '
                   'schedule that uniquely identifies it.', id_part='child_name_2')
        c.argument('top', type=int, help='The maximum number of resources to return from the operation. Example: '
                   '\'$top=10\'.')
        c.argument('tags', tags_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('time', type=str, help='The target time to trigger the action. The format is HH:MM.')
        c.argument('time_zone', type=str, help='The IANA timezone id at which the schedule should execute.')
        c.argument('state', arg_type=get_enum_type(['Enabled', 'Disabled']), help='Indicates whether or not this '
                   'scheduled task is enabled.')

    with self.argument_context('devcenter admin schedule delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', type=str, help='The name of the project.', id_part='name')
        c.argument('pool_name', type=str, help='Name of the pool.', id_part='child_name_1')
        c.argument('schedule_name', options_list=['--name', '-n', '--schedule-name'], type=str, help='The name of the '
                   'schedule that uniquely identifies it.', id_part='child_name_2')
        c.argument('top', type=int, help='The maximum number of resources to return from the operation. Example: '
                   '\'$top=10\'.')

    with self.argument_context('devcenter admin schedule wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('project_name', type=str, help='The name of the project.', id_part='name')
        c.argument('pool_name', type=str, help='Name of the pool.', id_part='child_name_1')
        c.argument('schedule_name', options_list=['--name', '-n', '--schedule-name'], type=str, help='The name of the '
                   'schedule that uniquely identifies it.', id_part='child_name_2')
        c.argument('top', type=int, help='The maximum number of resources to return from the operation. Example: '
                   '\'$top=10\'.')

    with self.argument_context('devcenter admin network-connection list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('top', type=int, help='The maximum number of resources to return from the operation. Example: '
                   '\'$top=10\'.')

    with self.argument_context('devcenter admin network-connection show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_setting_name', options_list=['--name', '-n', '--network-connection-name'], type=str,
                   help='Name of the Network Settings that can be applied to a Pool.', id_part='name')

    with self.argument_context('devcenter admin network-connection create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_setting_name', options_list=['--name', '-n', '--network-connection-name'], type=str,
                   help='Name of the Network Settings that can be applied to a Pool.')
        c.argument('tags', tags_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('subnet_id', type=str, help='The subnet to attach Virtual Machines to')
        c.argument('domain_name', type=str, help='Active Directory domain name')
        c.argument('organization_unit', type=str, help='Active Directory domain Organization Unit (OU)')
        c.argument('domain_username', type=str, help='The username of an Active Directory account (user or service '
                   'account) that has permissions to create computer objects in Active Directory. Required format: '
                   'admin@contoso.com.')
        c.argument('domain_password', type=str, help='The password for the account used to join domain')
        c.argument('networking_resource_group_name', type=str, help='The name for the managed resource group where NICs will be '
                   'placed.')
        c.argument('domain_join_type', arg_type=get_enum_type(['HybridAzureADJoin', 'AzureADJoin']), help='AAD Join '
                   'type.')

    with self.argument_context('devcenter admin network-connection update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_setting_name', options_list=['--name', '-n', '--network-connection-name'], type=str,
                   help='Name of the Network Settings that can be applied to a Pool.', id_part='name')
        c.argument('tags', tags_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('subnet_id', type=str, help='The subnet to attach Virtual Machines to')
        c.argument('domain_name', type=str, help='Active Directory domain name')
        c.argument('organization_unit', type=str, help='Active Directory domain Organization Unit (OU)')
        c.argument('domain_username', type=str, help='The username of an Active Directory account (user or service '
                   'account) that has permissions to create computer objects in Active Directory. Required format: '
                   'admin@contoso.com.')
        c.argument('domain_password', type=str, help='The password for the account used to join domain')

    with self.argument_context('devcenter admin network-connection delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_setting_name', options_list=['--name', '-n', '--network-connection-name'], type=str,
                   help='Name of the Network Settings that can be applied to a Pool.', id_part='name')

    with self.argument_context('devcenter admin network-connection show-health-detail') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_setting_name', options_list=['--name', '-n', '--network-connection-name'], type=str,
                   help='Name of the Network Settings that can be applied to a Pool.', id_part='name')

    with self.argument_context('devcenter admin network-connection run-health-check') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_connection_name', options_list=['--name', '-n', '--network-connection-name'], type=str,
                   help='Name of the Network Connection that can be applied to a Pool.', id_part='name')

    with self.argument_context('devcenter admin network-connection wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_setting_name', options_list=['--name', '-n', '--network-connection-name'], type=str,
                   help='Name of the Network Settings that can be applied to a Pool.', id_part='name')
