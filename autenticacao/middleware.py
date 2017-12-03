def autenticacao_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("\n\n\nREQUEST")
        print(request)

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        print("\n\n\nRESPONSE")
        print(request)


        return response

    return middleware
