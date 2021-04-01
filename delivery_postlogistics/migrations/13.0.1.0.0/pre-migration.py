# Copyright 2013-2016 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from openupgradelib import openupgrade  # pylint: disable=W7936


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.update_module_names(
        env.cr,
        [("delivery_carrier_label_postlogistics", "delivery_postlogistics")],
        merge_modules=True,
    )

    # Model renaming
    # delivery.carrier.template.otion => postlogistics.delivery.carrier.template.option
    rename_model_list = [
        (
            "delivery.carrier.template.option",
            "postlogistics.delivery.carrier.template.option",
        )
    ]
    openupgrade.rename_models(env.cr, rename_model_list)

    # Delete obsolete model
    env.cr.execute(
        """
        DELETE FROM ir_model_fields
        WHERE model_id IN
        (SELECT id FROM ir_model WHERE model = 'postlogistics.auth');
    """
    )

    # Remove obsolete view
    openupgrade.delete_records_safely_by_xml_id(
        env, ["delivery_postlogistics.view_postlogistics_auth_form"]
    )
