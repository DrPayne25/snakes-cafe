def opening():
  menu = """
  **************************************
  **    Welcome to the Snakes Cafe!   **
  **    Please see our menu below.    **
  **
  ** To quit at any time, type "quit" **
  **************************************

  Appetizers
  ----------
  Wings
  Cookies
  Spring Rolls

  Entrees
  -------
  Salmon
  Steak
  Meat Tornado
  A Literal Garden

  Desserts
  --------
  Ice Cream
  Cake
  Pie

  Drinks
  ------
  Coffee
  Tea
  Unicorn Tears

  ***********************************
  ** What would you like to order? **
  ***********************************
  """
  print(menu)

menu_items = [
  {
    "section": "Appetizers",
    "items": [
      "Wings",
      "Cookies",
      "Spring Rolls",
    ],
  },
    {
    "section": "Entrees",
    "items": [
      "Wings",
      "Cookies",
      "Spring Rolls",
    ],
  },
  {
    "section": "Deserts",
    "items": [
      "Ice Cream",
      "Cake",
      "Pie",
    ],
  },
  {
    "section": "Drinks",
    "items": [
      "Coffee",
      "Tea",
      "Unicorn Tears",
    ],
  },
]



if __name__ == "__main__":
  opening()
  order_question  = ""
  count = 0
  order = []
  while order_question != "quit":
    order_question = input("> ")
    order.append(order_question)
    count = order.count(order_question)
    if order_question == "quit": 
      break
    elif count <= 1:
      response = f'** 1 order of {order_question} has been added to your meal **'
      print(response)
    elif count > 1:
      response = f'** {count} orders of {order_question} have been added to your meal **'
      print(response)
  #print(order_question)

