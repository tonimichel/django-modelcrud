__all__ = ['AbstractCrudConf']

class AbstractCrudConf(object):
    """
    This is the abstract crudconf your concrete CrudConf should inherit from.
    A crudconf provides a common interface for the Crud views in order to provide
    appropriate model instance url resolving in the template.
    """

    model = None
    list_display = []
    detail_properties = []
    list_display_detail_link_index = 0

    def __init__(self, instance):
        self.instance = instance

    def get_model_verbose_name(self):
        """
        Returns the model verbose name of the instance.
        """
        return self.instance._meta.verbose_name

    def get_model_verbose_name_plural(self):
        """
        Returns the model verbose name plural.
        """
        return self.instance._meta.verbose_name_plural

    def get_origin_url(self):
        """
        Return the URL that represents the page, this model's dialogs
        can be reached from. E.g. consider Angebote, where Angebote can
        be reached from fg_base_dashboard, this function should return the
        reverse of that URL. It is used in order to provide a back link
        to the originating page.
        """
        return

    def get_origin_title(self):
        """
        Return the Title of the page.
        """
        return 'Dashboard'

    def get_display_name(self):
        """
        Returns the string representation of the object bount to this
        viewinfo object. E.g. get_display_name of an Angebot instance returns
        the human-readable string representation of this angebot.
        The default implementation is to return the instance's __unicode__.
        """
        return str(self.instance)

    def get_list_url(self):
        """
        Returns the reversed URL for the list view.
        """
        return

    def get_create_url(self):
        return

    def get_detail_url(self):
        return

    def get_change_url(self):
        return

    def get_delete_url(self):
        return

    # --------------------------------------------------------------------------

    def _get_field_strings(self, field_list):
        """
        Takes a list of field name strings.
        Returns that original list, or in case the field_list's first entry
        equals '*' all fields of the associated model (self.instance). 
        """
        if len(field_list) and field_list[0] == '*':
            return [field.name for field in self.model._meta.get_fields()]
        else:
            return field_list

    def get_list_display(self):
        """
        Returns a list of strings representing the names of the fields that
        should be displayed in the list view table.
        """
        return self._get_field_strings(self.list_display)


    def get_detail_properties(self):
        """
        Returns a list of strings representing the names of the fields that
        should be displayed in the .
        """
        return self._get_field_strings(self.detail_properties)
