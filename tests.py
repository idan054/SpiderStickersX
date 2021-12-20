from woocommerce import API

wcapi = API(
    url="http://www.spider3d.co.il/", # Your store URL
    consumer_key="ck_790bd6e48f79861f3fb04e2162950b8797f061d9", # Your consumer key
    consumer_secret="cs_12a78e53e6e8bd3a26e64761e0ef6002b5413129", # Your consumer secret
    wp_api=True, # Enable the WP REST API integration
    version="wc/v3" # WooCommerce WP REST API version
)

print(wcapi.query_string_auth)