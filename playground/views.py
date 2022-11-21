# from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.shortcuts import render
from .tasks import notify_customers
# from django.db.models import Q, F, DecimalField
# from django.db.models.aggregates import Count
# from django.db.models.functions import Concat
# from django.db.models import Value, Func, ExpressionWrapper
# from django.contrib.contenttypes.models import ContentType
# from store.models import Product, OrderItem, Customer, Collection
# from tags.models import TaggedItem
# from templated_mail.mail import BaseEmailMessage


def say_hello(request):
    notify_customers.delay('Hello')
    return render(request, 'hello.html', {'name': 'Dana'})
    # try:
    #     message = BaseEmailMessage(
    #         template_name='emails/hello.html',
    #         context={'name': 'Dana'}
    #     )
    #     message.send(['ciobanu.dana.adriana@gmail.com'])
    # except BadHeaderError:
    #     pass

    # collection = Collection()
    # collection_title = 'Video Games'
    # collection.featured_product = Product(pk=1)
    # # collection.featured_product_id = 1
    # collection.save()
    #
    # collection = Collection.objects.create(title='a', featured_product=1)

    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    # products = Product.objects.filter(inventory=F('unit_price'))
    # queryset = Product.objects.order_by('unit_price', '-title').reverse()
    # orders = OrderItem.objects.values('product_id').distinct()  # removes the duplicates
    # orders = OrderItem.objects.select_related('customer').order_by('-placed_at')[:5]
    # orders = OrderItem.objects.select_related('customer').prefetch_related('orderitem_set').order_by('-placed_at')[:5]
    # queryset = Product.objects.only('id', 'title')
    # queryset = Product.objects.defer('description')
    # queryset = Product.objects.select_related('collection').all()
    # queryset = Product.objects.prefetch_related('collection').all()
    # queryset = Product.objects.aggregate(Count('id'))
    # queryset = Product.objects.annotate(discounted_price=discounted_price)
    # queryset = Customer.objects.annotate(is_new=Value(True))
    # queryset = Customer.objects.annotate(full_name=Func(F('first_name'),
    # Value(' '), F('last_name'), function='CONCAT'))
    # queryset = Customer.objects.annotate(full_name=Concat('first_name', Value(' '), 'last_name'))
    # content_type = ContentType.objects.get_for_model(Product)
    # queryset = TaggedItem.objects.select_related('tag').filter(content_type=content_type, object_id=1)


