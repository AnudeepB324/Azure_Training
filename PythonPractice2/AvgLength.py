# Calculating Avg Length 

Classics = ['VANILLA', 'CHOCOLATE', 'STRAWBERRY']
Trendy_flavors = ['SALTED CARAMEL', 'MATCHA', 'COOKIES & CREAM']
Kid_Friendly = ['RAINBOW SHERBET', 'BUBBLEGUM', 'COTTON CANDY']
Seasonal_Specials = ['MANGO', 'PINEAPPLE-COCONUT', 'KEY LIME PIE']

#Adding up all the flavours and calculating the Avg length
all_flavors = Classics + Trendy_flavors + Kid_Friendly + Seasonal_Specials
average_length = sum(len(flavor) for flavor in all_flavors) / len(all_flavors)

print(f"\nAverage length of flavor names: {average_length:}")