
# Token Based Authentication

How to make user authentication more secure than simple username and password? 

The answer lies in using Jwt token. Token based authentication provide more security layer to your application.

It uses a token (refresh token) that will be validated and through this the user will be authenticated and given authorization.

In this project I have used djangorestframework-simplejwt package to use JWT token.

I have added an extra layer that is I added access token along with refresh token. Access Token has major claims for authorization. 

Access Token has expiry of less time than refresh token. When the access token expires then refresh token (which has more expiration time then AT) will fetch new access token. This way there is another layer of protection.