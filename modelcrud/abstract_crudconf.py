

__all__ = ['AbstractCrudConf']

class AbstractCrudConf(object):

    model = None
    list_display = []
    detail_properties = []

    def __init__(self, instance):
        self.instance = instance

    def get_model_verbose_name(self):
        return self.instance._meta.verbose_name

    def get_model_verbose_name_plural(self):
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

    def get_display_name(self):
        """
        Returns the string representation of the object bount to this
        viewinfo object. E.g. get_display_name of an Angebot instance returns
        the human-readable string representation of this angebot.
        The default implementation is to return the instance's __unicode__.
        """
        return str(self.instance)

    def get_list_url(self):
        return

    def get_create_url(self):
        return

    def get_detail_url(self):
        return

    def get_change_url(self):
        return

    def get_delete_url(self):
        return



    # ------------

    def get_list_display(self):
        if len(self.list_display) and self.list_display[0] == '*':
            return [field.name for field in self.model._meta.get_fields()]
        else:
            return self.list_display
