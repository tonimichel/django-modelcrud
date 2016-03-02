
__all__ = ['register']



def register(crudconf_class):
    """
    Registers the crudconf_class on the associated model.
    After register was called, the model's crudconf can be accessed
    via modelinstance.crudconf.
    """

    def get_crudconf(model_instance):
        return crudconf_class(model_instance)

    setattr(crudconf_class.model, 'crudconf', property(get_crudconf))
