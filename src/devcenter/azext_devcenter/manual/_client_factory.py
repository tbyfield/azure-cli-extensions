# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

def cf_devcenter_dataplane(cli_ctx, *_):

    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_devcenter.vendored_sdks.devcenter_dataplane import FidalgoDataplaneClient   

    # Override the client to use DevCenter resource rather than ARM's. The .default scope will be appended by the mgmt service client
    cli_ctx.cloud.endpoints.active_directory_resource_id = 'https://devcenter.azure.com'
    return get_mgmt_service_client(cli_ctx, FidalgoDataplaneClient, subscription_bound=False, base_url_bound=False)


def cf_project_dp(cli_ctx, *_):
    return cf_devcenter_dataplane(cli_ctx).project


def cf_pool_dp(cli_ctx, *_):
    return cf_devcenter_dataplane(cli_ctx).pool


def cf_dev_box_dp(cli_ctx, *_):
    return cf_devcenter_dataplane(cli_ctx).dev_box


def cf_environment_dp(cli_ctx, *_):
    return cf_devcenter_dataplane(cli_ctx).environments


def cf_deployment_dp(cli_ctx, *_):
    return cf_devcenter_dataplane(cli_ctx).deployments


def cf_catalog_item_dp(cli_ctx, *_):
    return cf_devcenter_dataplane(cli_ctx).catalog_item


def cf_environment_type_dp(cli_ctx, *_):
    return cf_devcenter_dataplane(cli_ctx).environment_type