import os
import requests
import json

def jaccard_similarity(x,y):
  # Returns the jaccard similarity between two lists
  intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
  union_cardinality = len(set.union(*[set(x), set(y)]))
  return intersection_cardinality/float(union_cardinality)

# Search and compare
def search(book1, book2):
    # Format strings
    urlValue1 = book1.replace(" ", "_")
    urlValue2 = book2.replace(" ", "_")

    # Uses the Google Books API temporarily. Can update later
    url1 = f"https://www.googleapis.com/books/v1/volumes?q={urlValue1}"
    url2 = f"https://www.googleapis.com/books/v1/volumes?q={urlValue2}"

    # Connect and open both urls
    connection1 = requests.get(url1)
    response1 = connection1.json()

    connection2 = requests.get(url2)
    response2 = connection2.json()

    # For early testing, we'll only take the first value from each response
    firstRes = response1["items"][0]["volumeInfo"]["description"]
    secondRes = response2["items"][0]["volumeInfo"]["description"]

    # Get similarity value of each book's description
    similarity = jaccard_similarity(firstRes, secondRes)

    # Return similarity value
    return similarity

# Temporary lines for comparing data
book1 = input("Enter first book: ")
book2 = input("Enter second book: ")

similarity = search(book1, book2) * 100

print(f"{similarity:.2f}% match")