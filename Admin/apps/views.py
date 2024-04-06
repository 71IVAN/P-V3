from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class AppsView(LoginRequiredMixin,TemplateView):
    pass

# calendar
calendar_view = AppsView.as_view(template_name = "apps/apps-calendar.html")

# filemanager
filemanager_view = AppsView.as_view(template_name = "apps/apps-file-manager.html")

# chat
chat_view = AppsView.as_view(template_name = "apps/apps-chat.html")

# email
email_view = AppsView.as_view(template_name = "apps/apps-email.html")

# Ecommerce
apps_ecommerce_products_view = AppsView.as_view(template_name = "apps/ecommerce/apps-ecommerce-products.html")
apps_ecommerce_products_grid_view = AppsView.as_view(template_name = "apps/ecommerce/apps-ecommerce-products-grid.html")
apps_ecommerce_products_details_view = AppsView.as_view(template_name = "apps/ecommerce/apps-ecommerce-product-details.html")
apps_ecommerce_add_product_view = AppsView.as_view(template_name = "apps/ecommerce/apps-ecommerce-add-product.html")
apps_ecommerce_orders_view = AppsView.as_view(template_name = "apps/ecommerce/apps-ecommerce-orders.html")
apps_ecommerce_order_overview_view = AppsView.as_view(template_name = "apps/ecommerce/apps-ecommerce-order-overview.html")
apps_ecommerce_customers_view = AppsView.as_view(template_name = "apps/ecommerce/apps-ecommerce-customers.html")
apps_ecommerce_cart_view = AppsView.as_view(template_name = "apps/ecommerce/apps-ecommerce-cart.html")
apps_ecommerce_checkout_view = AppsView.as_view(template_name = "apps/ecommerce/apps-ecommerce-checkout.html")
apps_ecommerce_sellers_view = AppsView.as_view(template_name = "apps/ecommerce/apps-ecommerce-sellers.html")
apps_ecommerce_seller_overview_view = AppsView.as_view(template_name = "apps/ecommerce/apps-ecommerce-seller-overview.html")

# Learning

    # courses
apps_learning_list = AppsView.as_view(template_name = "apps/learning/courses/apps-learning-list.html")
apps_learning_grid_view = AppsView.as_view(template_name = "apps/learning/courses/apps-learning-grid.html")
apps_learning_category_view = AppsView.as_view(template_name = "apps/learning/courses/apps-learning-category.html")
apps_learning_overview_view = AppsView.as_view(template_name = "apps/learning/courses/apps-learning-overview.html")
apps_learning_create_courses_view = AppsView.as_view(template_name = "apps/learning/courses/apps-learning-create.html")


    # students
apps_student_courses_view = AppsView.as_view(template_name = "apps/learning/students/apps-student-courses.html")
apps_student_subscriptions_view = AppsView.as_view(template_name = "apps/learning/students/apps-student-subscriptions.html")

    # instructors
apps_instructors_list_view = AppsView.as_view(template_name = "apps/learning/instructors/apps-instructors-list.html")
apps_instructors_grid_view = AppsView.as_view(template_name = "apps/learning/instructors/apps-instructors-grid.html")
apps_instructors_overview_view = AppsView.as_view(template_name = "apps/learning/instructors/apps-instructors-overview.html")
apps_instructors_create_view = AppsView.as_view(template_name = "apps/learning/instructors/apps-instructors-create.html")

# invoices
apps_invoices_list_view = AppsView.as_view(template_name = "apps/invoices/apps-invoices-list.html")
apps_invoices_overview_view = AppsView.as_view(template_name = "apps/invoices/apps-invoices-overview.html")
apps_invoices_create_view = AppsView.as_view(template_name = "apps/invoices/apps-invoices-create.html")


# real esate
apps_real_estate_list_view = AppsView.as_view(template_name = "apps/real-estate/apps-real-estate-list.html")
apps_real_estate_grid_view = AppsView.as_view(template_name = "apps/real-estate/apps-real-estate-grid.html")
apps_real_estate_map_view = AppsView.as_view(template_name = "apps/real-estate/apps-real-estate-map.html")
apps_real_estate_property_overview = AppsView.as_view(template_name = "apps/real-estate/apps-real-estate-property-overview.html")
apps_real_estate_add_properties = AppsView.as_view(template_name = "apps/real-estate/apps-real-estate-add-properties.html")
apps_real_estate_earnings = AppsView.as_view(template_name = "apps/real-estate/apps-real-estate-earnings.html")

    # agent
apps_agent_list_view = AppsView.as_view(template_name = "apps/real-estate/agent/apps-real-estate-agent-list.html")
apps_agent_grid_view = AppsView.as_view(template_name = "apps/real-estate/agent/apps-real-estate-agent-grid.html")
apps_agent_overview_view = AppsView.as_view(template_name = "apps/real-estate/agent/apps-real-estate-agent-overview.html")
    
    # agencies
apps_agencies_list_view = AppsView.as_view(template_name = "apps/real-estate/agencies/apps-real-estate-agencies-list.html")
apps_agencies_overview_view = AppsView.as_view(template_name = "apps/real-estate/agencies/apps-real-estate-agencies-overview.html")

# support-tickets
apps_support_tickets_list_view = AppsView.as_view(template_name = "apps/support-tickets/apps-tickets-list.html")
apps_support_overview_view = AppsView.as_view(template_name = "apps/support-tickets/apps-tickets-overview.html")

