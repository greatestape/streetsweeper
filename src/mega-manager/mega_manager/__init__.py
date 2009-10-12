from django.db import models
from django.db.models.query import QuerySet


def make_manager(*manager_classes):
    name_base = ''
    query_set_parent_classes = set()
    for manager_class in manager_classes:
        name_base += manager_class.__name__.rsplit('Manager', 1)[0]
        if hasattr(manager_class, 'query_set_class'):
            query_set_parent_classes.add(manager_class.query_set_class)

    # Each custom query set should be extending QuerySet already,
    # so we shouldn't extend it separately.
    try:
        query_set_parent_classes.remove(QuerySet)
    except KeyError:
        pass

    if len(query_set_parent_classes) > 0:
        query_set_class = type(
                '%sQuerySet' % name_base,
                tuple(query_set_parent_classes),
                {}
                )
    else:
        query_set_class = QuerySet

    class CustomQuerysetParentManager(models.Manager):
        """
        Use this manager as the last in the list of parent classes when
        constructing dynamic manager classes. So long as all the other class's
        get_query_set methods call the super-class, and so long as this is the
        last class in the list of parents, this will ensure that an instance of
        the class in self.query_set_class is what's returned.
        """
        def get_query_set(self):
            return self.query_set_class(self.model)

    manager_class = type(
            '%sManager' % name_base,
            tuple(manager_classes + (CustomQuerysetParentManager,)),
            {'query_set_class': query_set_class}
            )
    return manager_class()
