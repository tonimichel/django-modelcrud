
__all__ = ['register']



def register(crudconf_class):

    def get_crudconf(model_instance):
        return crudconf_class(model_instance)

    setattr(crudconf_class.model, 'crudconf', property(get_crudconf))
