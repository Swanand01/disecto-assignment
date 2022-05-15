
# Backend Assignment

Develop an application that generates invoices in fairly simple format. Format
for reference can be found at the end of this task. The application must facilitate
the following API(s):

a. GET: get the list of available items with details such as (name, price,
description).

b. POST: to send the list of items to buy with corresponding quantities.

c. PUT: to update the list of items in the purchase list.

d. GET: get the invoice for the purchase in pdf format as per the above
format but with all the necessary details filled dynamically.


## API Reference

#### Register

```http
  POST /auth/registration/
```
Registers a new user

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`| `string` | **Required**. Username            |
| `email`   | `string` | **Required**. Email               |
| `password1`| `string` | **Required**. Password           |
| `password2`| `string` | **Required**. Password again     |


#### Login

```http
  POST /auth/login/
```
User login

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`| `string` | **Required**. Username            |
| `password`| `string` | **Required**. Password            |


#### Get all products

```http
  GET /get-all-products/
```
Returns JSON Response containing all products.

#### Get order

```http
  GET /get-order/{order_id}
```
Gets Order from order_id.
    Returns JSON Response containing name, quantity of all OrderProducts in that order.

#### New Order
```http
  POST /create-new-order/
```
Creates a new Order with the OrderProducts sent in the request.

Sample request body:
```json
{
    "products": [
        {
            "name": "Red Tshirt",
            "quantity": 2
        },
        {
            "name": "IPhone 11",
            "quantity": 1
        }
    ]
}
```

#### Update Order
```http
  POST /update-order/{order_id}
```
Update an Order.
    Gets the Order from order_id, and updates its OrderProducts with the ones sent in the request.

Sample request body:
```json
{
    "products": [
        {
            "name": "IPhone XR",
            "quantity": 1
        },
        {
            "name": "IPhone 11",
            "quantity": 1
        }
    ]
}
```

#### Place Order

```http
  GET /place-order/{order_id}
```
Changes Order status to placed.
## Invoice Generation

```http
  GET /generate-invoice/{order_id}
```

To generate an invoice, visit the above path.
## Live

The web application is deployed [here](https://disecto-backend-assignment.herokuapp.com/). 


## Testing

To test the API endpoints, import the Postman Collection.
Login or register, and use Bearer token as auth where necessary.


### Further documentation

Model and view documentation can be found in models.py and views.py.
