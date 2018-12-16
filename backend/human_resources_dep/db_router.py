class HumanResourcesDepRouter:

    def db_for_read(self, model, **hints):

        if model._meta.app_label == 'human_resources_dep':
            return 'hrd_db'
        return None

    def db_for_write(self, model, **hints):

        if model._meta.app_label == 'human_resources_dep':
            return 'hrd_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):

        if obj1._meta.app_label == 'human_resources_dep' or \
           obj2._meta.app_label == 'human_resources_dep':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label == 'human_resources_dep':
            return db == 'hrd_db'
        return None
