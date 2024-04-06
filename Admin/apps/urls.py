from django.urls import path
from apps.views import (
    calendar_view,
    filemanager_view,
    chat_view,
    email_view,
    
    apps_ecommerce_products_view,
    apps_ecommerce_products_grid_view,
    apps_ecommerce_products_details_view,
    apps_ecommerce_add_product_view,
    apps_ecommerce_orders_view,
    apps_ecommerce_order_overview_view,
    apps_ecommerce_customers_view,
    apps_ecommerce_cart_view,
    apps_ecommerce_checkout_view,
    apps_ecommerce_sellers_view,
    apps_ecommerce_seller_overview_view,
    
    apps_learning_list,
    apps_learning_grid_view,
    apps_learning_category_view,
    apps_learning_overview_view,
    apps_learning_create_courses_view,
    apps_student_courses_view,
    apps_student_subscriptions_view,
    apps_instructors_list_view,
    apps_instructors_grid_view,
    apps_instructors_overview_view,
    apps_instructors_create_view,
    
    apps_invoices_list_view,
    apps_invoices_overview_view,
    apps_invoices_create_view,
    
    apps_real_estate_list_view,
    apps_real_estate_grid_view,
    apps_real_estate_map_view,
    apps_real_estate_property_overview,
    apps_real_estate_add_properties,
    apps_real_estate_earnings,
    apps_agent_list_view,
    apps_agent_grid_view,
    apps_agent_overview_view,
    apps_agencies_list_view,
    apps_agencies_overview_view,
    
    apps_support_tickets_list_view,
    apps_support_overview_view,
)

app_name = 'apps'

urlpatterns = [
    path('calendar',calendar_view,name="calendar"),
    path('file-manager',filemanager_view,name="file-manager"),
    path('chat',chat_view,name="chat"),
    path('email',email_view,name="email"),
    
    # Ecommerce
    
    path('ecommerce/products',apps_ecommerce_products_view,name="ecommerce.products"),
    path('ecommerce/products-grid',apps_ecommerce_products_grid_view,name="ecommerce.products-grid"),
    path('ecommerce/products-details',apps_ecommerce_products_details_view,name="ecommerce.products-details"),
    path('ecommerce/add-product',apps_ecommerce_add_product_view,name="ecommerce.add_product"),
    path('ecommerce/orders',apps_ecommerce_orders_view,name="ecommerce.orders"),
    path('ecommerce/order-overview',apps_ecommerce_order_overview_view,name="ecommerce.order-overview"),
    path('ecommerce/customers',apps_ecommerce_customers_view,name="ecommerce.customers"),
    path('ecommerce/cart',apps_ecommerce_cart_view,name="ecommerce.cart"),
    path('ecommerce/checkout',apps_ecommerce_checkout_view,name="ecommerce.checkout"),
    path('ecommerce/sellers',apps_ecommerce_sellers_view,name="ecommerce.sellers"),
    path('ecommerce/seller-overview',apps_ecommerce_seller_overview_view,name="ecommerce.seller-overview"),
    
   # Learning
    path('learning/courses/list-view',apps_learning_list,name="learning.courses.list-view"),
    path('learning/courses/grid-view',apps_learning_grid_view,name="learning.courses.grid-view"),
    path('learning/courses/category-view',apps_learning_category_view,name="learning.courses.category-view"),
    path('learning/courses/overview',apps_learning_overview_view,name="learning.courses.overview"),
    path('learning/courses/create-course',apps_learning_create_courses_view,name="learning.courses.create-course"),
    
        # students
    path('learning/students/mycourses',apps_student_courses_view,name="learning.students.mycourses"),
    path('learning/students/subscriptions',apps_student_subscriptions_view,name="learning.students.subscriptions"),
    
    # instructors
    path('learning/instructors/list',apps_instructors_list_view,name="learning.instructors.list"),
    path('learning/instructors/grid',apps_instructors_grid_view,name="learning.instructors.grid"),
    path('learning/instructors/overview',apps_instructors_overview_view,name="learning.instructors.overview"),
    path('learning/instructors/create',apps_instructors_create_view,name="learning.instructors.create"),
   
    # invoices   
    path('invoices/list',apps_invoices_list_view,name="invoices.list"),
    path('invoices/overview',apps_invoices_overview_view,name="invoices.overview"),
    path('invoices/create',apps_invoices_create_view,name="invoices.create"),
    
    # real estate
    path('real-estate/list',apps_real_estate_list_view,name="real_estate.list"),
    path('real-estate/grid',apps_real_estate_grid_view,name="real_estate.grid"),
    path('real-estate/map',apps_real_estate_map_view,name="real_estate.map"),
    path('real-estate/property-overview',apps_real_estate_property_overview,name="real_estate.property-overview"),
    path('real-estate/add-properties',apps_real_estate_add_properties,name="real_estate.add-properties"),
    path('real-estate/earnings',apps_real_estate_earnings,name="real_estate.earnings"),
    
        #  agent
    path('real-estate/agent/list',apps_agent_list_view,name="real_estate.agent.list"),
    path('real-estate/agent/grid',apps_agent_grid_view,name="real_estate.agent.grid"),
    path('real-estate/agent/overview',apps_agent_overview_view,name="real_estate.agent.overview"),
    
        # agencies
    path('real-estate/agencies/list',apps_agencies_list_view,name="real_estate.agencies.list"),
    path('real-estate/agencies/overview',apps_agencies_overview_view,name="real_estate.agencies.overview"),
    
    # support tickets
    path('support-tickets/list',apps_support_tickets_list_view,name="support_tickets.list"),
    path('support-tickets/overview',apps_support_overview_view,name="support_tickets.overview"),
    
]
