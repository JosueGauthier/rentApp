from django.db import models


class Organization(models.Model):
    """

    Define organization model 

    Organisation is an student association in our case that proceed on a specific field (e.g : sewing, work equipment, sound equipment )

    """
    name_organization = models.CharField('Nom', max_length=254)
    image_organization_url = models.TextField('imagelink')

    def __str__(self):
        """
        Return the display name.
        :returns: name attribute
        :rtype: string
        """
        return self.name_organization.capitalize()


class Category(models.Model):
    """

    Define category model 

    A category is a group of product of the same type of one organization
    """
    name_category = models.CharField('Nom', max_length=254)
    image_category_url = models.TextField('imagelink')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return the display name.
        :returns: name attribute
        :rtype: string
        """
        return self.name_category.capitalize()


class Product(models.Model):
    """

    Define product model 

    Product is a the object that a personn wants to borrow. 

    """
    name_product = models.CharField('Nom', max_length=254)
    image_product_url = models.TextField('imagelink')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField('Active', default=True)
    is_removed = models.BooleanField('Removed', default=False)
    qty_total = models.IntegerField('Total quantity', default=1)
    qty_available = models.IntegerField('Available quantity', default=1)
    is_consumable = models.BooleanField('Consumable', default=False)

    def __str__(self):
        """
        Return the display name.
        :returns: name attribute
        :rtype: string
        """
        return self.name_product.capitalize()
