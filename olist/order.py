import pandas as pd
import numpy as np
from olist.utils import haversine_distance
from olist.data import Olist


class Order:
    '''
    DataFrames containing all orders as index,
    and various properties of these orders as columns
    '''
    def __init__(self):
        # Assign an attribute ".data" to all new instances of Order
        self.data = Olist().get_data()

    def get_wait_time(self, is_delivered=True):
        """
        Returns a DataFrame with:
        [order_id, wait_time, expected_wait_time, delay_vs_expected, order_status]
        and filters out non-delivered orders unless specified
        """
        orders = self.data['orders'].copy()
        
        if is_delivered:
            orders = orders[orders['order_status'] == 'delivered'].copy()
            
        orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
        orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
        orders['order_estimated_delivery_date'] = pd.to_datetime(orders['order_estimated_delivery_date'])
        
        orders['wait_time'] = (orders['order_delivered_customer_date'] - orders['order_purchase_timestamp']) / np.timedelta64(24, 'h')
        orders['expected_wait_time'] = (orders['order_estimated_delivery_date'] - orders['order_purchase_timestamp']) / np.timedelta64(24, 'h')
        orders['delay_vs_expected'] = (orders['wait_time'] - orders['expected_wait_time']).clip(lower=0.0)
        
        return orders[['order_id', 'wait_time', 'expected_wait_time', 'delay_vs_expected', 'order_status']]

    def get_review_score(self):
        """
        Returns a DataFrame with:
        order_id, dim_is_five_star, dim_is_one_star, review_score
        """
        reviews = self.data['order_reviews'].copy()
        
        reviews['dim_is_five_star'] = np.where(reviews['review_score'] == 5, 1, 0)
        reviews['dim_is_one_star'] = np.where(reviews['review_score'] == 1, 1, 0)
        
        return reviews[['order_id', 'dim_is_five_star', 'dim_is_one_star', 'review_score']]

    def get_number_items(self):
        """
        Returns a DataFrame with:
        order_id, number_of_items
        """
        number_items = self.data['order_items'].copy()
        number_of_items = number_items['order_id'].value_counts().reset_index(name='number_of_items')
        
        return number_of_items

    def get_number_sellers(self):
        """
        Returns a DataFrame with:
        order_id, number_of_sellers
        """
        sellers = self.data['order_items'].copy()
        number_of_sellers = sellers.groupby('order_id')['seller_id'].nunique().reset_index(name='number_of_sellers')
        
        return number_of_sellers

    def get_price_and_freight(self):
        """
        Returns a DataFrame with:
        order_id, price, freight_value
        """
        price_and_freight = self.data['order_items'].copy()
        price_and_freight_orders = price_and_freight.groupby('order_id')[['price', 'freight_value']].sum().reset_index()
        
        return price_and_freight_orders

    # Optional
    def get_distance_seller_customer(self):
        """
        Returns a DataFrame with:
        order_id, distance_seller_customer
        """

        data = self.data
        orders = data['orders']
        order_items = data['order_items']
        sellers = data['sellers']
        customers = data['customers']

        geo = data['geolocation']
        geo = geo.groupby('geolocation_zip_code_prefix', as_index=False).first()

        df = order_items.merge(sellers, on='seller_id')\
                        .merge(orders, on='order_id')\
                        .merge(customers, on='customer_id')

        df = df.merge(geo[['geolocation_zip_code_prefix', 'geolocation_lat', 'geolocation_lng']],
                      left_on='customer_zip_code_prefix',
                      right_on='geolocation_zip_code_prefix')

        df = df.merge(geo[['geolocation_zip_code_prefix', 'geolocation_lat', 'geolocation_lng']],
                      left_on='seller_zip_code_prefix',
                      right_on='geolocation_zip_code_prefix',
                      suffixes=('_customer', '_seller'))

        df['distance_seller_customer'] = df.apply(
            lambda row: haversine_distance(
                row['geolocation_lng_seller'],
                row['geolocation_lat_seller'],
                row['geolocation_lng_customer'],
                row['geolocation_lat_customer']
            ), axis=1)

        return df.groupby('order_id', as_index=False)['distance_seller_customer'].mean()

    def get_training_data(self,
                          is_delivered=True,
                          with_distance_seller_customer=False):
        """
        Returns a clean DataFrame (without NaN), with the all following columns:
        ['order_id', 'wait_time', 'expected_wait_time', 'delay_vs_expected',
        'order_status', 'dim_is_five_star', 'dim_is_one_star', 'review_score',
        'number_of_items', 'number_of_sellers', 'price', 'freight_value',
        'distance_seller_customer']
        """
        training_data = self.get_wait_time(is_delivered=is_delivered)
        training_data = training_data.merge(self.get_review_score(), on='order_id') \
                                     .merge(self.get_number_items(), on='order_id') \
                                     .merge(self.get_number_sellers(), on='order_id') \
                                     .merge(self.get_price_and_freight(), on='order_id')

        if with_distance_seller_customer:
            training_data = training_data.merge(self.get_distance_seller_customer(), on='order_id')

        training_data = training_data.dropna()
        
        return training_data