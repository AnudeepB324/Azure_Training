Classics = ['VANILLA', 'CHOCOLATE', 'STRAWBERRY']
Trendy_flavors = ['SALTED CARAMEL', 'MATCHA', 'COOKIES & CREAM']
Kid_Friendly = ['RAINBOW SHERBET', 'BUBBLEGUM', 'COTTON CANDY']
Seasonal_Specials = ['MANGO', 'PINEAPPLE-COCONUT', 'KEY LIME PIE']

#Adding all flavors into a single list
all_flavors = Classics + Trendy_flavors + Kid_Friendly + Seasonal_Specials

#Using sort for sorting all the flovors
all_flavors.sort()
print("Sorted ice cream flavors:")
for flavor in all_flavors:
    print(flavor)