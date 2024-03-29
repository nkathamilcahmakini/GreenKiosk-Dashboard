from cart.models import Cart
from inventory.models import Product
from order.models import Order
from payment.models import Payment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from customer.models import Customer
from vendor.models import Vendor
from .serializers import CustomerSerializer, OrderSerializer, PaymentSerializer, ProductSerializer
from .serializers import VendorSerializer

class CustomerListView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
       serializer = CustomerSerializer(data=request.data)
       if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CustomerDetailView(APIView):
    def get(self, request, id, format=None):
        customer = Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
           customer = Customer.objects.get(id=id)
           serializer = CustomerSerializer(customer, data=request.data) 
           if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_200_OK) 
           return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self , request , id, format=None):
        customer = Customer.objects.get(id=id)
        customer.delete()
        return Response("Customer deleted" , status=status.HTTP_204_NO_CONTENT)
    
# class CartListView(APIView):
#     def get(self, request):
#         carts=Cart.objects.all()
#         serializer= CartSerializer(carts,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer=CartSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class CartDetailView(APIView):
#     def get(self,request,id, format=None):
#         cart= self.get_object(id)
#         serializer= CartSerializer(cart)
#         return Response(serializer.data)
    
#     def put(self, request, id, format=None):
#         cart = self.get_object(id)
#         serializer=CartSerializer(cart,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,id, format=None):
#         cart= self.get_object(id)
#         cart.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



class ProductListView(APIView):
    def get(self,request):
        products =Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
def post(self,request):
    serializer= ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
class ProductDetailView(APIView):
    def get(self, request, id, format=None):
        product= self.get_object(id) 
        serializer=ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self,request, id ,format=None):
        product=self.get_object(id)
        serializer=ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id, format=None):
        product= self.get_object(id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  


 
class OrderListView(APIView):
    def get(self,request):
        orders =Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
def post(self,request):
    serializer= OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
class OrderDetailView(APIView):
    def get(self, request, id, format=None):
        order= self.get_object(id) 
        serializer=OrderSerializer(order)
        return Response(serializer.data)
    
    def put(self,request, id ,format=None):
        order=self.get_object(id)
        serializer=OrderSerializer(order,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id, format=None):
        order= self.get_object(id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class PaymentListView(APIView):
    def get(self,request):
        payments =Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)
    
def post(self,request):
    serializer= PaymentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
class PaymentDetailView(APIView):
    def get(self, request, id, format=None):
        payment= self.get_object(id) 
        serializer=PaymentSerializer(payment)
        return Response(serializer.data)
    
    def put(self,request, id ,format=None):
        payment=self.get_object(id)
        serializer=PaymentSerializer(payment,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id, format=None):
        payment= self.get_object(id)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ........................................
# class ShippingListView(APIView):
#     def get(self,request):
#         shippings =Shipping.objects.all()
#         serializer = ShippingSerializer(shippings, many=True)
#         return Response(serializer.data)
    
# def post(self,request):
#     serializer= ShippingSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
# class ShippingDetailView(APIView):
#     def get(self, request, id, format=None):
#         shipping= self.get_object(id) 
#         serializer=ShippingSerializer(shipping)
#         return Response(serializer.data)
    
#     def put(self,request, id ,format=None):
#         shipping=self.get_object(id)
#         serializer=ShippingSerializer(shipping,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,id, format=None):
#         shipping= self.get_object(id)
#         shipping.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
    

class VendorListView(APIView):
    def get(self,request):
        vendors=Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)
    
def post(self,request):
    serializer= VendorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
class VendorDetailView(APIView):
    def get(self, request, id, format=None):
        vendor= self.get_object(id) 
        serializer=VendorSerializer(vendor)
        return Response(serializer.data)
    
    def put(self,request, id ,format=None):
        vendor=self.get_object(id)
        serializer=VendorSerializer(vendor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id, format=None):
        vendor= self.get_object(id)
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class AddToCartView(APIView):
    def post(self, request, formart = None):
        cart_id = request.data ["cart_id"]
        product_id = request.data[product_id] 
        cart = Cart.objects.get(id = cart_id)
        product = Product.objects.get(id = product_id)
        updtaed_cart = cart.add_product(product)
        serializer = CartSerializer(updtaed_cart)
        return Response(serializer.date)

