# DevOpsII-RestAPIs
! "number" = put number

Postman:
1. GET
- Put http://127.0.0.1:5000/item inside the url box to see the list of items
- Put http://127.0.0.1:5000/item/"number" to see the specific item

2. POST
1) Put http://127.0.0.1:5000/item inside the url box. 
2) Next click on "body" 
3) Then click on "raw" 
4) Finally put {"name": "product name", "price": "number", "instock": "number"} in the blank
! Recommended to choose JSON in "body"
- To check the result, go back to "GET" and choose 1) to see all items on the list

3. PUT
1) Put http://127.0.0.1:5000/item/"number" inside the url box to update specific item
2) Next click on "body" 
3) Then click on "raw" 
4) Finally put {"name": "product name", "price": "number", "instock": "number"} in the blank
! Recommended to choose JSON in "body"
- To check the result, go back to "GET" and choose 1) again

4. DELETE
- Put http://127.0.0.1:5000/item/"number" to delete the specific item
- To check the result, go back to "GET" and choose 1) again
