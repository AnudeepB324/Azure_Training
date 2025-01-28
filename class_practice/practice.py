# function summarize_items with args and kwargs
def summarize_items(name, *args, **kwargs):
    print(f"Name: {name}")
    print(f"Total number of items: {len(args)}")
    return kwargs

result = summarize_items(
    "Anu",
    "Yesh", "Adi",
    location="pointe",
    type="Apartment"
)

print(result)
